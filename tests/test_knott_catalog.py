"""Comprehensive verification suite for the GEOMETOR Knott Mathematical Catalog."""

from __future__ import annotations

import html
import json
import math
import re
from pathlib import Path

import pytest
import sympy as sp
from geometor.knott.catalog import (
    CATALOG_ITEMS,
    COLLECTIONS,
    KNOTT_COPYRIGHT,
    get_catalog_item,
    verify_all_catalog_items,
)
from geometor.knott.constants import (
    PHI,
    PSI,
    SQRT5,
    assert_no_floats,
    assert_zero,
    floor_linear_phi,
    geometor_to_knott_radicals,
    knott_to_geometor,
    phi,
    verify_notation_bijection,
)
from geometor.knott.flat_geometry import GeometricCatalogResult
from geometor.knott.golden_string import (
    beatty_pair,
    from_zeckendorf,
    golden_string_beatty_word,
    golden_string_generations,
    recursive_fib_additions,
    stolarsky_entry,
    to_zeckendorf,
    wythoff_entry,
    wythoff_locate,
    zeckendorf_summands,
)
from geometor.knott.identities import (
    fibonacci_pythagorean_triple,
    fibonomial,
    golden_angle_invariants,
    verify_cassini,
    verify_classical_identities,
    verify_fibonacci_arctan_step,
    verify_fibonacci_pi_telescoping,
)
from geometor.knott.phigits import (
    all_phigit_forms,
    from_phigits,
    phi_continued_fraction_convergents,
    phi_power_linearization,
    phibonacci_brick_invariants,
    to_maximal_phigits,
    to_phigits,
)
from geometor.knott.solid_geometry import (
    dodecahedron_vertices_3d,
    find_five_cubes_in_dodecahedron,
    icosahedron_vertices_3d,
)
from geometor.knott.trigonometry import (
    gauss_seventeen_gon_cosine,
    pentagonal_trig_table,
    three_degree_lattice,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
_G_ROLE_RE = re.compile(r":g:`([^`]+)`")
_EQ_ROLE_RE = re.compile(r":eq:`([^`]+)`")
_SVG_DATAREF_RE = re.compile(r'\bdata-ref="([^"]+)"')


@pytest.fixture(scope="module")
def verified_results() -> dict[str, GeometricCatalogResult]:
    """Execute and cache all 22 catalog item models once per test session."""
    return verify_all_catalog_items()


def test_notation_bijection_and_floors() -> None:
    """Verify exact Knott (PHI, phi) <-> SymPy GoldenRatio bijection and integer Beatty floors."""
    bijection = verify_notation_bijection()
    assert len(bijection) == 5
    s_phi_big = sp.Symbol("Phi", positive=True)
    s_phi_small = sp.Symbol("phi", positive=True)
    sym_expr = 3 * s_phi_big**2 - 2 * s_phi_small
    as_gr = knott_to_geometor(sym_expr)
    assert as_gr.has(sp.GoldenRatio)
    round_trip = geometor_to_knott_radicals(as_gr)
    assert_zero((3 * PHI**2 - 2 * phi) - round_trip)
    assert_zero(PHI + PSI - 1)
    assert_zero(PHI - PSI - SQRT5)

    for a_val in range(-5, 6):
        for b_val in range(-8, 9):
            exact_fl = floor_linear_phi(a_val, b_val)
            if b_val == 0:
                assert exact_fl == a_val
            else:
                diff = sp.sympify(a_val) + sp.sympify(b_val) * PHI - exact_fl
                assert float(diff.evalf(30)) > 0.0
                assert float(diff.evalf(30)) < 1.0


def test_all_twenty_two_catalog_models_exact(
    verified_results: dict[str, GeometricCatalogResult],
) -> None:
    """Confirm all 22 catalog items build non-empty exact models with zero Float atoms."""
    assert len(COLLECTIONS) == 6
    assert len(CATALOG_ITEMS) == 22
    assert len(verified_results) == 22

    for spec in CATALOG_ITEMS:
        assert get_catalog_item(spec.canonical_id) == spec
        res = verified_results[spec.canonical_id]
        assert len(res.model) >= 10
        assert len(res.invariants) >= 4
        assert_no_floats(res.model)
        assert_no_floats(res.invariants)


def test_pentagonal_and_three_degree_trigonometry() -> None:
    """Verify exact pentagonal radicals, all 29 multiples of 3 degrees, and cos(pi/17)."""
    pent = pentagonal_trig_table()
    assert set(pent.keys()) == {18, 36, 54, 72}
    assert_zero(pent[36].cos - PHI / 2)
    assert_zero(pent[18].sin - phi / 2)

    lattice = three_degree_lattice()
    assert len(lattice) == 29
    assert list(lattice.keys()) == [3 * k for k in range(1, 30)]
    for deg, entry in lattice.items():
        assert entry.degrees == deg
        assert_no_floats(entry.sin)
        assert_no_floats(entry.cos)
        assert_no_floats(entry.spread)

    cos_17 = gauss_seventeen_gon_cosine()
    assert_no_floats(cos_17)
    assert abs(float(cos_17.evalf(25)) - math.cos(math.pi / 17.0)) < 1e-15


def test_three_dimensional_solids_and_five_cubes() -> None:
    """Verify 12 icosahedron vertices, 20 dodecahedron vertices, and 5 inscribed cubes."""
    ico = icosahedron_vertices_3d()
    dod = dodecahedron_vertices_3d()
    assert len(ico) == 12
    assert len(dod) == 20
    cubes = find_five_cubes_in_dodecahedron()
    assert len(cubes) == 5
    for cube in cubes:
        assert len(cube) == 8


def test_phi_powers_convergents_and_bergman_phigits() -> None:
    """Verify integer-power linearization, CF convergents, and Bergman's base-Phi phigits."""
    for exp_n in range(-10, 11):
        big_lin, neg_small_lin = phi_power_linearization(exp_n)
        assert_zero(PHI**exp_n - big_lin)
        assert_zero((-phi) ** exp_n - neg_small_lin)

    brick = phibonacci_brick_invariants()
    assert brick["volume"] == 1
    assert brick["space_diagonal"] == 2
    assert_zero(brick["surface_area"] - 4 * PHI)

    convs = phi_continued_fraction_convergents(10)
    assert len(convs) == 10
    assert convs[0].value == sp.Rational(1, 1)
    assert convs[4].value == sp.Rational(8, 5)

    for num in range(1, 25):
        min_p = to_phigits(num)
        max_p = to_maximal_phigits(num)
        assert "11" not in min_p.replace(".", "")
        assert "00" not in max_p.replace(".", "")
        assert not max_p.replace(".", "").endswith("011")
        assert from_phigits(min_p) == num
        assert from_phigits(max_p) == num

    # Every Fibonacci number F_k (k = 2..8: 1, 2, 3, 5, 8, 13, 21) has exactly F_k phigit forms:
    for k_idx in range(2, 9):
        fib_val = int(sp.fibonacci(k_idx))
        forms = all_phigit_forms(fib_val)
        assert len(forms) == fib_val
        for f_str in forms:
            assert from_phigits(f_str) == fib_val

    # Even-indexed Lucas numbers L_{2k} achieve local minima of 2k + 1 forms (L_4 = 7 -> 5, L_6 = 18 -> 7):
    assert len(all_phigit_forms(3)) == 3
    assert len(all_phigit_forms(7)) == 5
    assert len(all_phigit_forms(18)) == 7


def test_golden_string_zeckendorf_wythoff_and_stolarsky() -> None:
    """Verify Sturmian Golden String, Zeckendorf base, and Wythoff/Stolarsky bijections."""
    gens = golden_string_generations(8)
    s8 = gens[-1]
    assert len(s8) == int(sp.fibonacci(9)) == 34
    beatty_w = golden_string_beatty_word(len(s8))
    assert s8 == beatty_w
    # Truncating final two symbols of S_n (n >= 4) leaves an exact central Sturmian palindrome:
    for word in gens[3:]:
        core = word[:-2]
        assert core == core[::-1]

    assert recursive_fib_additions(1) == 0
    assert recursive_fib_additions(10) == int(sp.fibonacci(11)) - 1 == 88

    # Zeckendorf canonical round-trip & non-consecutiveness:
    for num in range(1, 121):
        summands = zeckendorf_summands(num)
        assert sum(summands) == num
        assert summands[-1] >= 1
        assert summands == sorted(summands, reverse=True)
        z_bits = to_zeckendorf(num)
        assert "11" not in z_bits
        assert from_zeckendorf(z_bits) == num

    # Beatty complementary partition of 1..80:
    seen_beatty: set[int] = set()
    for idx in range(1, 60):
        a_n, b_n = beatty_pair(idx)
        assert b_n - a_n == idx
        assert a_n not in seen_beatty
        assert b_n not in seen_beatty
        seen_beatty.add(a_n)
        seen_beatty.add(b_n)
    for m_val in range(1, 81):
        assert m_val in seen_beatty

    # Wythoff bijection:
    for target in range(1, 101):
        r_idx, c_idx = wythoff_locate(target)
        assert wythoff_entry(r_idx, c_idx) == target

    # Stolarsky array Fibonacci row recurrence & distinctness:
    stol_seen: set[int] = set()
    for r_idx in range(8):
        row_vals = [stolarsky_entry(r_idx, c_idx) for c_idx in range(8)]
        for c_idx in range(2, 8):
            assert row_vals[c_idx] == row_vals[c_idx - 1] + row_vals[c_idx - 2]
        for val in row_vals:
            assert val not in stol_seen
            stol_seen.add(val)


def test_identities_pythagorean_cassini_fibonomials_and_pi() -> None:
    """Verify Fibonacci Pythagorean triples, Cassini, Fibonomials, and arctan pi series."""
    for idx in range(1, 10):
        rec = fibonacci_pythagorean_triple(idx)
        assert rec.leg_a**2 + rec.leg_b**2 == rec.hypotenuse_c**2
        assert rec.gcd_factor == (2 if idx % 3 == 0 else 1)
        assert rec.hypotenuse_c == int(sp.fibonacci(2 * idx + 3))
        assert verify_cassini(idx) == ((-1) ** idx)

    assert fibonomial(5, 2) == 15
    assert fibonomial(6, 2) == 40
    assert fibonomial(6, 3) == 60
    invs = verify_classical_identities()
    assert invs["fibonomial_6_3"] == 60

    for step_k in range(1, 7):
        tan_val = verify_fibonacci_arctan_step(step_k)
        assert tan_val == sp.Rational(1, int(sp.fibonacci(2 * step_k)))
    rem = verify_fibonacci_pi_telescoping(6)
    assert rem == sp.atan(sp.Rational(1, int(sp.fibonacci(14))))

    ga = golden_angle_invariants()
    assert_zero(ga["minor_turn_fraction"] - phi**2)


def test_manifest_and_codex_svg_rst_parity() -> None:
    """Verify catalog_manifest.json completeness and 100% RST :g:/:eq: <-> SVG data-ref parity."""
    manifest_file = REPO_ROOT / "resources" / "catalog_manifest.json"
    assert manifest_file.is_file()
    payload = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert payload["kind"] == "mathematical-catalog"
    assert payload["curated_source"]["copyright"] == KNOTT_COPYRIGHT
    assert len(payload["collections"]) == 6
    assert len(payload["items"]) == 22

    for item_entry in payload["items"]:
        url = item_entry["knott_source_url"]
        assert url.startswith("https://r-knott.surrey.ac.uk/")
        assert "#" in url
        svg_path = REPO_ROOT / "docsrc" / item_entry["svg_path"]
        rst_path = REPO_ROOT / "docsrc" / item_entry["doc_path"]
        assert svg_path.is_file(), f"Missing SVG: {svg_path}"
        assert rst_path.is_file(), f"Missing RST: {rst_path}"

        svg_text = svg_path.read_text(encoding="utf-8")
        rst_text = rst_path.read_text(encoding="utf-8")
        assert 'class="euclid-graphic"' in svg_text
        assert KNOTT_COPYRIGHT in rst_text

        svg_refs = {html.unescape(m.group(1)) for m in _SVG_DATAREF_RE.finditer(svg_text)}
        g_matches = list(_G_ROLE_RE.finditer(rst_text))
        assert len(g_matches) >= 3, f"Expected interactive :g: roles in {rst_path}"

        for match in g_matches:
            raw = match.group(1).strip()
            target_part = re.match(r"^.+?\s+<(.+)>$", raw)
            target_str = target_part.group(1).strip() if target_part else raw
            for sub in target_str.split(";"):
                token = sub.strip()
                if not token:
                    continue
                ref_id = token.split(":", 1)[1].strip() if ":" in token else token
                assert ref_id in svg_refs, f"Missing :g: ref {ref_id!r} in {svg_path}"

        for match in _EQ_ROLE_RE.finditer(rst_text):
            raw = match.group(1).strip()
            spec_match = re.match(r"^[^<>]+?\s+<(.+)>$", raw)
            spec_str = spec_match.group(1).strip() if spec_match else raw
            for lhs_rhs in spec_str.split("="):
                token = lhs_rhs.strip()
                if not token:
                    continue
                ref_id = token.split(":", 1)[1].strip() if ":" in token else token
                assert ref_id in svg_refs, f"Missing :eq: ref {ref_id!r} in {svg_path}"
