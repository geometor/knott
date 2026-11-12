r"""Collection 4: Algebraic Powers of :math:`\Phi`, Continued Fractions & Base-:math:`\Phi` "Phigits" (`KNOTT-4.1` – `KNOTT-4.3`).

Catalogs Fibonacci power linearizations, Donald Seitz's Phibonacci brick, extremal
continued fraction convergents :math:`F_{n+1}/F_n`, Hurwitz's :math:`\sqrt{5}` bound,
and George Bergman's (1957) base-:math:`\Phi` ("phigit") numeral system curated by
Dr. Ron Knott on ``propsOfPhi.html``, ``phigits.html``, and ``cfINTRO.html``.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.knott.constants import (
    PHI,
    SQRT5,
    assert_no_floats,
    assert_zero,
    floor_linear_phi,
    phi,
    polygon_signed_area,
    simplify_exact,
)
from geometor.knott.flat_geometry import GeometricCatalogResult


@dataclass(frozen=True)
class ConvergentEntry:
    r"""Exact rational Fibonacci convergent to :math:`\Phi = [1; 1, 1, \dots]`."""

    index: int
    numerator: int
    denominator: int
    value: sp.Rational
    signed_error: sp.Expr
    hurwitz_scaled_error: sp.Expr


def phi_power_linearization(n: int) -> tuple[sp.Expr, sp.Expr]:
    r"""Verify :math:`\Phi^n = F_n \Phi + F_{n-1}` and :math:`(-\phi)^n = F_{n+1} - F_n \Phi`.

    Args:
        n: Any positive, zero, or negative integer exponent.

    Returns:
        Tuple ``(F_n * PHI + F_{n-1}, F_{n+1} - F_n * PHI)`` verified equal to
        :math:`(\Phi^n, (-\phi)^n)`.
    """
    fn = sp.fibonacci(n)
    fn_prev = sp.fibonacci(n - 1)
    fn_next = sp.fibonacci(n + 1)

    big_linear = simplify_exact(fn * PHI + fn_prev)
    neg_small_linear = simplify_exact(fn_next - fn * PHI)
    alt_small_linear = simplify_exact(fn_prev - fn * phi)

    assert_zero(PHI**n - big_linear, f"PHI^{n} == F_{n}*PHI + F_{n-1}")
    assert_zero((-phi) ** n - neg_small_linear, f"(-phi)^{n} == F_{n+1} - F_{n}*PHI")
    assert_zero((-phi) ** n - alt_small_linear, f"(-phi)^{n} == F_{n-1} - F_{n}*phi")
    return big_linear, neg_small_linear


def phibonacci_brick_invariants() -> dict[str, sp.Expr]:
    r"""Verify Donald Seitz's :math:`(1, \phi, \Phi)` Phibonacci brick invariants.

    Cataloged on ``propsOfPhi.html#phiBrick``: a rectangular box of edges
    :math:`(1, \phi, \Phi)` has unit volume ``1``, surface area :math:`4\Phi`,
    and rational space diagonal ``2`` (quadrance ``4``).

    Returns:
        Dictionary of verified exact brick invariants.
    """
    edges = (sp.Integer(1), phi, PHI)
    volume = simplify_exact(edges[0] * edges[1] * edges[2])
    surface_area = simplify_exact(
        2 * (edges[0] * edges[1] + edges[1] * edges[2] + edges[2] * edges[0])
    )
    diag_quadrance = simplify_exact(edges[0] ** 2 + edges[1] ** 2 + edges[2] ** 2)

    assert_zero(volume - 1, "Phibonacci brick volume == 1")
    assert_zero(surface_area - 4 * PHI, "Phibonacci brick surface area == 4*PHI")
    assert_zero(diag_quadrance - 4, "Phibonacci brick space diagonal == 2")
    return {
        "volume": volume,
        "surface_area": surface_area,
        "space_diagonal_quadrance": diag_quadrance,
        "space_diagonal": sp.sqrt(diag_quadrance),
    }


def construct_phi_powers_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-4.1`: Geometric area linearization of :math:`\Phi^2 = \Phi + 1` and :math:`(\phi + \phi^2)^2 = 1`.

    Partitions the :math:`\Phi \times \Phi` square ``AEFD`` along ``x = 1`` and ``y = 1``
    into unit square ``ABCD`` (area ``1``), two golden gnomons ``BEGC`` and ``DCJH``
    (each area :math:`\phi`), and corner square ``CGFJ`` (area :math:`\phi^2`), proving
    :math:`\Phi^2 = 1 + 2\phi + \phi^2 = 1 + \phi + 1 = \Phi + 1`, while simultaneously
    verifying :math:`\Phi^n = F_n \Phi + F_{n-1}` for :math:`n \in [-6, 8]` and the
    Phibonacci brick invariants.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-4.1``.
    """
    for exp_n in range(-6, 9):
        phi_power_linearization(exp_n)
    brick = phibonacci_brick_invariants()

    model = Model("knott-4-1", logger=False, auto_intersect=False)
    pt_a = model.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_b = model.given_point(sp.Integer(1), sp.Integer(0), ID="B")
    pt_e = model.given_point(PHI, sp.Integer(0), ID="E", classes=["golden"])
    pt_d = model.set_point(sp.Integer(0), sp.Integer(1), ID="D", classes=["given"])
    pt_c = model.set_point(sp.Integer(1), sp.Integer(1), ID="C", classes=["given"])
    pt_g = model.set_point(PHI, sp.Integer(1), ID="G", classes=["golden"])
    pt_h = model.set_point(sp.Integer(0), PHI, ID="H", classes=["golden"])
    pt_j = model.set_point(sp.Integer(1), PHI, ID="J", classes=["golden"])
    pt_f = model.set_point(PHI, PHI, ID="F", classes=["golden"])

    # Also subdivide unit square ABCD at x = phi, y = phi to show 1 = phi^2 + 2*phi^3 + phi^4:
    pt_p = model.set_point(phi, sp.Integer(0), ID="P", classes=["golden"])
    pt_q = model.set_point(phi, phi, ID="Q", classes=["golden"])
    pt_r = model.set_point(sp.Integer(0), phi, ID="R", classes=["golden"])

    model.set_polygon([pt_a, pt_e, pt_f, pt_h], classes=["golden"])
    model.set_polygon([pt_a, pt_b, pt_c, pt_d], classes=["given"])
    model.set_polygon([pt_c, pt_g, pt_f, pt_j], classes=["golden"])
    model.set_polygon([pt_a, pt_p, pt_q, pt_r], classes=["golden"])

    model.set_segment(pt_b, pt_j)
    model.set_segment(pt_d, pt_g)
    model.set_segment(pt_p, pt_q, classes=["golden"])
    model.set_segment(pt_r, pt_q, classes=["golden"])
    model.set_segment(pt_a, pt_f, classes=["golden"])

    area_total = polygon_signed_area([pt_a, pt_e, pt_f, pt_h])
    area_unit = polygon_signed_area([pt_a, pt_b, pt_c, pt_d])
    area_wing_1 = polygon_signed_area([pt_b, pt_e, pt_g, pt_c])
    area_wing_2 = polygon_signed_area([pt_d, pt_c, pt_j, pt_h])
    area_corner = polygon_signed_area([pt_c, pt_g, pt_f, pt_j])
    area_sub = polygon_signed_area([pt_a, pt_p, pt_q, pt_r])

    assert_zero(area_total - (PHI + 1), "Area(AEFH) == PHI + 1")
    assert_zero(
        area_total - (area_unit + area_wing_1 + area_wing_2 + area_corner),
        "Square partition sums to PHI^2",
    )
    assert_zero(area_sub - phi**2, "Inner golden square area == phi^2")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-4.1",
        model=model,
        invariants={
            "PHI_squared": area_total,
            "PHI_to_5": phi_power_linearization(5)[0],
            "phi_to_4": simplify_exact(phi**4),
            "brick_volume": brick["volume"],
            "brick_surface_area": brick["surface_area"],
            "brick_space_diagonal": brick["space_diagonal"],
        },
    )


def phi_continued_fraction_convergents(count: int = 8) -> list[ConvergentEntry]:
    r"""Generate exact Fibonacci convergents :math:`c_k = F_{k+1} / F_k` to :math:`\Phi = [1; 1, 1, \dots]`.

    Verifies for each :math:`k = 1\dots \text{count}` that
    :math:`F_{k+1}/F_k - \Phi = (-\phi)^k / F_k` and
    :math:`F_k \phi^k = (1 - (-1)^k \phi^{2k}) / \sqrt{5}`.

    Args:
        count: Number of convergents to generate (:math:`\ge 1`).

    Returns:
        List of verified :class:`ConvergentEntry` records.
    """
    entries: list[ConvergentEntry] = []
    for k in range(1, count + 1):
        fk = int(sp.fibonacci(k))
        fk1 = int(sp.fibonacci(k + 1))
        rat = sp.Rational(fk1, fk)
        err = simplify_exact(rat - PHI)
        expected_err = simplify_exact(((-phi) ** k) / fk)
        assert_zero(err - expected_err, f"c_{k} - PHI == (-phi)^{k} / F_{k}")

        hurwitz_term = simplify_exact(fk * (phi**k))
        expected_hurwitz = simplify_exact((1 - ((-1) ** k) * (phi ** (2 * k))) / SQRT5)
        assert_zero(hurwitz_term - expected_hurwitz, f"Hurwitz error identity at k={k}")

        entries.append(
            ConvergentEntry(
                index=k,
                numerator=fk1,
                denominator=fk,
                value=rat,
                signed_error=err,
                hurwitz_scaled_error=hurwitz_term,
            )
        )
    return entries


def construct_convergents_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-4.2`: Fibonacci convergent lattice points straddling ray :math:`y = \Phi x`.

    Plots origin ``O`` and the exact golden slope ray ``[O P]`` (:math:`P = (5, 5\Phi)`)
    alongside Fibonacci lattice points ``C1(1,1)``, ``C2(1,2)``, ``C3(2,3)``, ``C4(3,5)``,
    and ``C5(5,8)``. Consecutive convergent triangles ``O C_k C_{k+1}`` have exact unit
    cassini area :math:`1/2` (parallelogram area ``1``) and alternate strictly below/above
    the golden ray.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-4.2``.
    """
    convergents = phi_continued_fraction_convergents(8)

    # Also verify Lucas odd-power pure periodic continued fraction root:
    # Phi^(2m+1) satisfies x = L_{2m+1} + 1/x => x^2 - L_{2m+1}*x - 1 == 0
    for m_idx in (0, 1, 2):
        odd_k = 2 * m_idx + 1
        lucas_val = sp.lucas(odd_k)
        p_val = PHI**odd_k
        assert_zero(p_val**2 - lucas_val * p_val - 1, f"Phi^{odd_k} = [{lucas_val}; ...]")

    model = Model("knott-4-2", logger=False, auto_intersect=False)
    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    pt_p = model.set_point(sp.Integer(5), 5 * PHI, ID="P", classes=["golden"])
    model.set_segment(pt_o, pt_p, classes=["golden"])

    c_pts: list[spg.Point] = []
    for entry in convergents[:5]:
        pt_c = model.set_point(
            sp.Integer(entry.denominator),
            sp.Integer(entry.numerator),
            ID=f"C{entry.index}",
            classes=["given"] if entry.index % 2 == 1 else ["golden"],
        )
        c_pts.append(pt_c)
        model.set_segment(pt_o, pt_c)

    for idx in range(len(c_pts) - 1):
        tri_area = abs(polygon_signed_area([pt_o, c_pts[idx], c_pts[idx + 1]]))
        assert_zero(tri_area - sp.Rational(1, 2), f"Area(O C_{idx+1} C_{idx+2}) == 1/2")
        model.set_polygon([pt_o, c_pts[idx], c_pts[idx + 1]])

    # Nested radical identity: sqrt(1 + PHI) == PHI
    assert_zero(sp.sqrt(1 + PHI) - PHI, "sqrt(1 + PHI) == PHI")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-4.2",
        model=model,
        invariants={
            "c5_value": convergents[4].value,
            "c6_value": convergents[5].value,
            "c7_value": convergents[6].value,
            "c8_value": convergents[7].value,
            "hurwitz_constant": 1 / SQRT5,
            "cassini_triangle_area": sp.Rational(1, 2),
        },
    )


def _zphi_geq(a1: int, b1: int, a2: int, b2: int) -> bool:
    r"""Return ``True`` iff :math:`a_1 + b_1 \Phi \ge a_2 + b_2 \Phi` in exact :math:`\mathbb{Z}[\Phi]`."""
    da = a1 - a2
    db = b1 - b2
    # da + db * (1 + sqrt(5))/2 >= 0  <=>  2*da + db + db*sqrt(5) >= 0
    lhs = 2 * da + db
    if db == 0:
        return lhs >= 0
    if db > 0:
        if lhs >= 0:
            return True
        return (-lhs) * (-lhs) <= 5 * db * db
    # db < 0: need lhs >= (-db)*sqrt(5) > 0
    if lhs <= 0:
        return False
    return lhs * lhs >= 5 * db * db


def _format_exponents_as_phigits(exps: frozenset[int]) -> str:
    r"""Format a finite exponent set ``E`` into a base-:math:`\Phi` string (e.g., ``'100.01'``)."""
    if not exps:
        return "0"
    hi = max(max(exps), 0)
    lo = min(min(exps), 0)
    int_digits = "".join("1" if k in exps else "0" for k in range(hi, -1, -1))
    if lo == 0:
        return int_digits
    frac_digits = "".join("1" if k in exps else "0" for k in range(-1, lo - 1, -1))
    return f"{int_digits}.{frac_digits}"


def _parse_phigits_to_exponents(phigit_str: str) -> list[tuple[int, int]]:
    r"""Parse a base-:math:`\Phi` numeral string into ``[(exponent, digit_int), ...]``."""
    cleaned = phigit_str.strip()
    if "." in cleaned:
        int_part, frac_part = cleaned.split(".", 1)
    else:
        int_part, frac_part = cleaned, ""
    pairs: list[tuple[int, int]] = []
    n_int = len(int_part)
    for idx, ch in enumerate(int_part):
        if ch not in "01":
            raise ValueError(f"Invalid phigit character {ch!r} in {phigit_str!r}")
        if ch == "1":
            pairs.append((n_int - 1 - idx, 1))
    for idx, ch in enumerate(frac_part):
        if ch not in "01":
            raise ValueError(f"Invalid phigit character {ch!r} in {phigit_str!r}")
        if ch == "1":
            pairs.append((-(idx + 1), 1))
    return pairs


def to_phigits_exponents(a: int, b: int = 0) -> frozenset[int]:
    r"""Compute the unique canonical (minimal, ``11``-free) base-:math:`\Phi` exponents of :math:`a + b\Phi > 0`.

    Executes Bergman's greedy algorithm purely inside :math:`\mathbb{Z}[\Phi]` using
    :math:`\Phi^k = F_{k-1} + F_k \Phi` and exact integer quadratic comparisons.

    Args:
        a: Integer constant part of :math:`a + b\Phi`.
        b: Integer :math:`\Phi`-coefficient of :math:`a + b\Phi`.

    Returns:
        Frozenset of integer exponents :math:`k` whose canonical digit is ``1``.

    Raises:
        ValueError: If :math:`a + b\Phi < 0`.
    """
    if a == 0 and b == 0:
        return frozenset()
    if not _zphi_geq(a, b, 0, 0):
        raise ValueError(f"Base-Phi greedy encoder requires non-negative input, got {a} + {b}*PHI")

    rem_a, rem_b = a, b
    exps: set[int] = set()

    # Find initial upper exponent bound k_hi with Phi^k_hi <= rem < Phi^(k_hi + 1):
    k_cur = 0
    while _zphi_geq(rem_a, rem_b, int(sp.fibonacci(k_cur)), int(sp.fibonacci(k_cur + 1))):
        k_cur += 1
    while not _zphi_geq(rem_a, rem_b, int(sp.fibonacci(k_cur - 1)), int(sp.fibonacci(k_cur))):
        k_cur -= 1

    steps = 0
    while not (rem_a == 0 and rem_b == 0):
        steps += 1
        if steps > 512:  # pragma: no cover
            raise RuntimeError("Exceeded phigit termination bound")
        p_a = int(sp.fibonacci(k_cur - 1))
        p_b = int(sp.fibonacci(k_cur))
        if _zphi_geq(rem_a, rem_b, p_a, p_b):
            exps.add(k_cur)
            rem_a -= p_a
            rem_b -= p_b
            k_cur -= 2
        else:
            k_cur -= 1

    # Verify non-adjacency (no k and k-1 simultaneously in exps):
    for exp_k in exps:
        if (exp_k - 1) in exps:  # pragma: no cover
            raise AssertionError(f"Adjacent 11 detected in canonical phigits: {exps}")
    return frozenset(exps)


def to_phigits(n: int) -> str:
    r"""Encode non-negative integer ``n`` into its unique minimal base-:math:`\Phi` string.

    Examples:
        ``to_phigits(1) == '1'``, ``to_phigits(2) == '10.01'``,
        ``to_phigits(3) == '100.01'``, ``to_phigits(4) == '101.01'``.

    Args:
        n: Non-negative integer to encode.

    Returns:
        Canonical non-adjacent base-:math:`\Phi` numeral string.
    """
    if n < 0:
        raise ValueError(f"Expected n >= 0, got {n}")
    if n == 0:
        return "0"
    return _format_exponents_as_phigits(to_phigits_exponents(n, 0))


def from_phigits(phigit_str: str) -> sp.Expr:
    r"""Decode any finite base-:math:`\Phi` string into an exact SymPy expression in :math:`\mathbb{Z}[\Phi]`.

    Args:
        phigit_str: Finite base-:math:`\Phi` numeral string containing ``0``, ``1``, and optional ``.``.

    Returns:
        Exact simplified SymPy expression (reducing to ``sp.Integer(n)`` for integer inputs).
    """
    pairs = _parse_phigits_to_exponents(phigit_str)
    total_a = 0
    total_b = 0
    for exp_k, digit in pairs:
        if digit:
            total_a += int(sp.fibonacci(exp_k - 1))
            total_b += int(sp.fibonacci(exp_k))
    return simplify_exact(sp.Integer(total_a) + sp.Integer(total_b) * PHI)


def all_phigit_forms(n: int) -> list[str]:
    r"""Enumerate all finite base-:math:`\Phi` representations of ``n`` not ending in ``011``.

    Implements Dr. Ron Knott's finite expansion closure (``phigits.html#expandall``):
    starting from the minimal representation :func:`to_phigits`, applies all sequences of:

    1. Interior ``100 -> 011`` (:math:`k \to \{k-1, k-2\}` for :math:`k > \min(E)`);
    2. Tail ``101 -> 01111`` (:math:`\{m+2, m\} \to \{m+1, m, m-1, m-2\}` at :math:`m = \min(E)`).

    For every Fibonacci number :math:`F_k` (:math:`k \ge 2`), ``len(all_phigit_forms(F_k)) == F_k``.

    Args:
        n: Positive integer (:math:`n \ge 1`).

    Returns:
        Deterministically sorted list of valid finite base-:math:`\Phi` strings for ``n``.
    """
    if n < 1:
        raise ValueError(f"Expected positive integer n >= 1, got {n}")
    start = to_phigits_exponents(n, 0)
    visited: set[frozenset[int]] = {start}
    queue: deque[frozenset[int]] = deque([start])

    while queue:
        curr = queue.popleft()
        m_min = min(curr)
        # Rule 1: interior 100 -> 011 (for k > m_min with k-1, k-2 absent)
        for k_exp in curr:
            if k_exp > m_min and (k_exp - 1) not in curr and (k_exp - 2) not in curr:
                nxt = frozenset((curr - {k_exp}) | {k_exp - 1, k_exp - 2})
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        # Rule 2: tail 101 -> 01111 at m_min
        if (m_min + 1) not in curr and (m_min + 2) in curr:
            nxt_tail = frozenset((curr - {m_min + 2}) | {m_min + 1, m_min - 1, m_min - 2})
            if nxt_tail not in visited:
                visited.add(nxt_tail)
                queue.append(nxt_tail)

    # Sort from highest leading power / fewest 1s (minimal first, maximal last):
    ordered = sorted(
        visited,
        key=lambda s: (len(s), -max(s), sorted(s, reverse=True)),
    )
    forms = [_format_exponents_as_phigits(s) for s in ordered]
    for f_str in forms:
        assert_zero(from_phigits(f_str) - n, f"Decoded phigit {f_str} == {n}")
    return forms


def to_maximal_phigits(n: int) -> str:
    r"""Return Dr. Ron Knott's unique maximal base-:math:`\Phi` representation of ``n`` (most ``1`` digits, no ``00`` pairs).

    Args:
        n: Positive integer (:math:`n \ge 1`).

    Returns:
        Maximal finite base-:math:`\Phi` string not ending in ``011``.
    """
    forms = all_phigit_forms(n)
    return max(forms, key=lambda s: (s.count("1"), -len(s)))


def construct_phigit_scale_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-4.3`: Geometric phigit Decomposition of integers ``1..6`` over :math:`\Phi^k`.

    Builds an exact geometric bar-and-power decomposition diagram in ``geometor.model``:
    horizontal reference ticks at powers :math:`\Phi^{-2} = \phi^2`, :math:`\Phi^{-1} = \phi`,
    :math:`\Phi^0 = 1`, :math:`\Phi^1 = \Phi`, :math:`\Phi^2 = \Phi + 1`, and
    :math:`\Phi^3 = 2\Phi + 1`, paired with stacked horizontal segments proving
    :math:`2 = \Phi^1 + \Phi^{-2}`, :math:`3 = \Phi^2 + \Phi^{-2}`, and
    :math:`4 = \Phi^2 + \Phi^0 + \Phi^{-2}`. Also verifies Bergman uniqueness and
    Knott's Fibonacci fixed-point theorem ``#all_phigit_forms(F_k) == F_k`` for :math:`k = 2..8`.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-4.3``.
    """
    # Verify round-trip encoding/decoding for 1..30 and Fibonacci self-counts F_2..F_8:
    for val in range(1, 31):
        p_str = to_phigits(val)
        assert_zero(from_phigits(p_str) - val, f"from_phigits(to_phigits({val})) == {val}")

    for k_fib in range(2, 9):
        fn = int(sp.fibonacci(k_fib))
        forms = all_phigit_forms(fn)
        if len(forms) != fn:  # pragma: no cover
            raise AssertionError(f"Expected {fn} phigit forms for F_{k_fib}={fn}, got {len(forms)}")

    # Verify even Lucas two-phigit theorem: L_{2k} = Phi^(2k) + Phi^(-2k)
    for k_even in (1, 2, 3):
        ln = int(sp.lucas(2 * k_even))
        expected_str = "1" + ("0" * (2 * k_even)) + "." + ("0" * (2 * k_even - 1)) + "1"
        if to_phigits(ln) != expected_str:  # pragma: no cover
            raise AssertionError(f"Lucas L_{2*k_even}={ln} expected {expected_str}, got {to_phigits(ln)}")

    model = Model("knott-4-3", logger=False, auto_intersect=False)

    # Bottom axis (y = 0): exact powers of Phi from Phi^-2 up to Phi^3
    p_zero = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    pm2 = model.set_point(PHI ** (-2), sp.Integer(0), ID="Pm2", classes=["golden"])
    pm1 = model.set_point(PHI ** (-1), sp.Integer(0), ID="Pm1", classes=["golden"])
    p0 = model.set_point(sp.Integer(1), sp.Integer(0), ID="P0", classes=["given"])
    p1 = model.set_point(PHI, sp.Integer(0), ID="P1", classes=["golden"])
    p2 = model.set_point(PHI**2, sp.Integer(0), ID="P2", classes=["golden"])
    p3 = model.set_point(PHI**3, sp.Integer(0), ID="P3", classes=["golden"])
    model.set_segment(p_zero, p3)
    for pt_pow in (pm2, pm1, p0, p1, p2):
        del pt_pow

    # Row y = 1: 2 = Phi^1 + Phi^-2 (10.01_Phi)
    r2_0 = model.set_point(sp.Integer(0), sp.Integer(1), ID="A2")
    r2_1 = model.set_point(PHI, sp.Integer(1), ID="M2", classes=["golden"])
    r2_2 = model.set_point(sp.Integer(2), sp.Integer(1), ID="B2", classes=["given"])
    model.set_segment(r2_0, r2_1, classes=["golden"])
    model.set_segment(r2_1, r2_2)

    # Row y = 2: 3 = Phi^2 + Phi^-2 (100.01_Phi)
    r3_0 = model.set_point(sp.Integer(0), sp.Integer(2), ID="A3")
    r3_1 = model.set_point(PHI**2, sp.Integer(2), ID="M3", classes=["golden"])
    r3_2 = model.set_point(sp.Integer(3), sp.Integer(2), ID="B3", classes=["given"])
    model.set_segment(r3_0, r3_1, classes=["golden"])
    model.set_segment(r3_1, r3_2)

    # Row y = 3: 4 = Phi^2 + Phi^0 + Phi^-2 (101.01_Phi)
    r4_0 = model.set_point(sp.Integer(0), sp.Integer(3), ID="A4")
    r4_1 = model.set_point(PHI**2, sp.Integer(3), ID="M4", classes=["golden"])
    r4_2 = model.set_point(PHI**2 + 1, sp.Integer(3), ID="N4", classes=["golden"])
    r4_3 = model.set_point(sp.Integer(4), sp.Integer(3), ID="B4", classes=["given"])
    model.set_segment(r4_0, r4_1, classes=["golden"])
    model.set_segment(r4_1, r4_2, classes=["golden"])
    model.set_segment(r4_2, r4_3)

    # Guide verticals dropping from Phi^1 and Phi^2 onto the base scale:
    model.set_segment(p1, r2_1, classes=["guide"], guide=True)
    model.set_segment(p2, r4_1, classes=["guide"], guide=True)
    model.set_polygon([p_zero, p2, r4_1, r4_0], classes=["golden"])

    assert_zero(r2_2.x - (PHI + PHI ** (-2)), "2 == Phi + Phi^-2")
    assert_zero(r3_2.x - (PHI**2 + PHI ** (-2)), "3 == Phi^2 + Phi^-2")
    assert_zero(r4_3.x - (PHI**2 + 1 + PHI ** (-2)), "4 == Phi^2 + 1 + Phi^-2")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-4.3",
        model=model,
        invariants={
            "phigits_2_decoded": from_phigits(to_phigits(2)),
            "phigits_5_form_count": sp.Integer(len(all_phigit_forms(5))),
            "phigits_8_form_count": sp.Integer(len(all_phigit_forms(8))),
            "phigits_13_form_count": sp.Integer(len(all_phigit_forms(13))),
            "phigits_21_form_count": sp.Integer(len(all_phigit_forms(21))),
            "lucas_7_form_count": sp.Integer(len(all_phigit_forms(7))),
            "lucas_11_form_count": sp.Integer(len(all_phigit_forms(11))),
        },
    )
