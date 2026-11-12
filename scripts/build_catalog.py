"""Synthesize ``resources/catalog_manifest.json``, 22 ``.euclid-graphic`` SVGs, and ``docsrc/`` codex pages."""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = REPO_ROOT.parent
for _p in (REPO_ROOT / "src", WORKSPACE_ROOT / "model" / "src"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import sympy as sp  # noqa: E402

from geometor.knott.catalog import (  # noqa: E402
    CATALOG_ITEMS,
    COLLECTIONS,
    KNOTT_COPYRIGHT,
    CatalogItemSpec,
    CollectionSpec,
    export_catalog_manifest,
    verify_all_catalog_items,
)
from geometor.knott.expositions import ITEM_EXPOSITIONS  # noqa: E402
from geometor.knott.flat_geometry import GeometricCatalogResult  # noqa: E402
from geometor.knott.golden_string import stolarsky_entry, wythoff_entry  # noqa: E402
from geometor.knott.phigits import (  # noqa: E402
    all_phigit_forms,
    to_maximal_phigits,
    to_phigits,
)
from geometor.knott.svg_renderer import write_euclid_svg  # noqa: E402
from geometor.knott.trigonometry import three_degree_lattice  # noqa: E402

_G_ROLE_RE = re.compile(r":g:`([^`]+)`")
_EQ_ROLE_RE = re.compile(r":eq:`([^`]+)`")
_SVG_DATAREF_RE = re.compile(r'\bdata-ref="([^"]+)"')


def _apparatus_slug(key: str) -> str:
    """Create deterministic anchor slug matching ``photon_platform.publish.roles.geometry``."""
    return re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")


def _rst_heading(title: str, char: str = "=") -> str:
    """Format an underlined (or over/underlined) RST section heading."""
    bar = char * max(len(title), 4)
    if char == "=":
        return f"{bar}\n{title}\n{bar}"
    return f"{title}\n{bar}"


def _geometor_repo_links(repos: tuple[str, ...]) -> str:
    """Render clickable GitHub Pages / repo links for cross-referenced GEOMETOR packages."""
    parts: list[str] = []
    for repo_id in repos:
        short = repo_id.split("/")[-1]
        parts.append(f"`{repo_id} <https://geometor.github.io/{short}/>`_")
    return ", ".join(parts)


def _extra_domain_tables(canonical_id: str) -> str:
    """Generate specialized exact mathematical reference tables for key catalog items."""
    if canonical_id == "KNOTT-2.2":
        lattice = three_degree_lattice()
        lines = [
            _rst_heading("Complete 29-Angle 3° Constructible Lattice", "-"),
            "",
            ".. list-table:: Exact Radicals & Spreads for :math:`3^\\circ k` (:math:`k = 1\\dots 29`)",
            "   :header-rows: 1",
            "   :widths: 10 30 30 30",
            "",
            "   * - Angle",
            "     - :math:`\\sin\\theta`",
            "     - :math:`\\cos\\theta`",
            "     - Spread :math:`s(\\theta) = \\sin^2\\theta`",
        ]
        for deg in sorted(lattice):
            ent = lattice[deg]
            lines.extend(
                [
                    f"   * - :math:`{deg}^\\circ`",
                    f"     - :math:`{sp.latex(ent.sin)}`",
                    f"     - :math:`{sp.latex(ent.cos)}`",
                    f"     - :math:`{sp.latex(ent.spread)}`",
                ]
            )
        return "\n".join(lines)

    if canonical_id == "KNOTT-4.3":
        lines = [
            _rst_heading("Canonical Minimal, Maximal, & Multiplicity Phigit Table", "-"),
            "",
            ".. list-table:: Base-:math:`\\Phi` ('Phigit') Expansions for :math:`N = 1\\dots 12`",
            "   :header-rows: 1",
            "   :widths: 12 28 32 28",
            "",
            "   * - :math:`N`",
            "     - Minimal Form (``11``-free)",
            "     - Maximal Form (``00``-free interior)",
            "     - Valid Finite Phigit Forms",
        ]
        for num in range(1, 13):
            forms = all_phigit_forms(num)
            lines.extend(
                [
                    f"   * - ``{num}``",
                    f"     - ``{to_phigits(num)}``",
                    f"     - ``{to_maximal_phigits(num)}``",
                    f"     - ``{len(forms)}``",
                ]
            )
        return "\n".join(lines)

    if canonical_id == "KNOTT-5.3":
        lines = [
            _rst_heading("Leading 6 × 6 Wythoff & Stolarsky Interspersion Subarrays", "-"),
            "",
            ".. list-table:: Wythoff Array :math:`W(r, c)` (:math:`0 \\le r, c \\le 5`)",
            "   :header-rows: 1",
            "",
            "   * - Row",
            *[f"     - :math:`c={c}`" for c in range(6)],
        ]
        for r_idx in range(6):
            lines.append(f"   * - :math:`r={r_idx}`")
            for c_idx in range(6):
                lines.append(f"     - ``{wythoff_entry(r_idx, c_idx)}``")
        lines.extend(
            [
                "",
                ".. list-table:: Stolarsky Array :math:`S(r, c)` (:math:`0 \\le r, c \\le 5`)",
                "   :header-rows: 1",
                "",
                "   * - Row",
                *[f"     - :math:`c={c}`" for c in range(6)],
            ]
        )
        for r_idx in range(6):
            lines.append(f"   * - :math:`r={r_idx}`")
            for c_idx in range(6):
                lines.append(f"     - ``{stolarsky_entry(r_idx, c_idx)}``")
        return "\n".join(lines)

    return ""


def _validate_rst_svg_parity(rst_text: str, svg_text: str, item_id: str) -> None:
    """Assert 100% parity between ``:g:`` / ``:eq:`` roles in RST and ``data-ref`` in SVG."""
    svg_refs = {html.unescape(m.group(1)) for m in _SVG_DATAREF_RE.finditer(svg_text)}

    for match in _G_ROLE_RE.finditer(rst_text):
        raw = match.group(1).strip()
        target_part = re.match(r"^.+?\s+<(.+)>$", raw)
        target_str = target_part.group(1).strip() if target_part else raw
        for sub in target_str.split(";"):
            token = sub.strip()
            if not token:
                continue
            ref_id = token.split(":", 1)[1].strip() if ":" in token else token
            if ref_id not in svg_refs:
                raise AssertionError(
                    f"[{item_id}] :g: target {ref_id!r} (from {raw!r}) missing from SVG data-refs: {sorted(svg_refs)}"
                )

    for match in _EQ_ROLE_RE.finditer(rst_text):
        raw = match.group(1).strip()
        spec_match = re.match(r"^[^<>]+?\s+<(.+)>$", raw)
        spec_str = spec_match.group(1).strip() if spec_match else raw
        for lhs_rhs in spec_str.split("="):
            token = lhs_rhs.strip()
            if not token:
                continue
            ref_id = token.split(":", 1)[1].strip() if ":" in token else token
            if ref_id not in svg_refs:
                raise AssertionError(
                    f"[{item_id}] :eq: target {ref_id!r} (from {raw!r}) missing from SVG data-refs: {sorted(svg_refs)}"
                )


def _render_item_rst(spec: CatalogItemSpec, res: GeometricCatalogResult) -> str:
    """Render the complete standalone RST page for one ``CatalogItemSpec``."""
    exposition = ITEM_EXPOSITIONS[spec.canonical_id]
    extra_tables = _extra_domain_tables(spec.canonical_id)

    inv_rows: list[str] = []
    for key, expr in res.invariants.items():
        clean_key = key.replace("_", " ")
        inv_rows.extend(
            [
                f"   * - ``{clean_key}``",
                f"     - :math:`{sp.latex(expr)}`",
            ]
        )

    blocks = [
        ":layout: book",
        ":type: item",
        f":order: {spec.order}",
        f":canonical_id: {spec.canonical_id}",
        "",
        f".. _{spec.folio_id}:",
        "",
        _rst_heading(f"{spec.canonical_id} — {spec.title}", "="),
        "",
        ".. enunciation::",
        "",
        f"   {spec.enunciation}",
        "",
        f".. picture:: {spec.folio_id}.g1.svg",
        "",
        _rst_heading("Curated Source & Catalog Provenance", "-"),
        "",
        ".. list-table::",
        "   :widths: 26 74",
        "",
        "   * - **Catalog ID**",
        f"     - ``{spec.canonical_id}``",
        "   * - **Curated Source**",
        f"     - :person:`Dr. Ron Knott <knott>`, *{spec.knott_page_title}* (`{spec.knott_anchor} <{spec.knott_url}>`_)",
        "   * - **Source Attribution**",
        f"     - **{KNOTT_COPYRIGHT}** — `Explore Dr. Knott's original exposition <{spec.knott_url}>`_",
        "   * - **Exact SymPy Validator**",
        f"     - :func:`{spec.validator_qualname}` (`0` ``sp.Float`` atoms)",
        "   * - **GEOMETOR Concordance**",
        f"     - {_geometor_repo_links(spec.geometor_repos)}",
        "",
        exposition,
    ]
    if extra_tables:
        blocks.extend(["", extra_tables])
    blocks.extend(
        [
            "",
            _rst_heading("Machine-Verified Exact Symbolic Invariants", "-"),
            "",
            ".. list-table::",
            "   :header-rows: 1",
            "   :widths: 38 62",
            "",
            "   * - Invariant",
            "     - Exact Symbolic Value",
            *inv_rows,
            "",
        ]
    )
    return "\n".join(blocks)


def _render_collection_rst(col: CollectionSpec, items: list[CatalogItemSpec]) -> str:
    """Render ``docsrc/catalog/<col.slug>/index.rst``."""
    first = items[0]
    featured = f"catalog/{col.slug}/{first.item_slug}/{first.folio_id}.g1.svg"
    table_rows: list[str] = []
    for it in items:
        table_rows.extend(
            [
                f"   * - :ref:`{it.canonical_id} <{it.folio_id}>`",
                f"     - {it.title}",
                f"     - `{it.knott_page_title} ({it.knott_anchor}) <{it.knott_url}>`_",
            ]
        )

    lines = [
        ":layout: book",
        ":type: collection",
        f":order: {col.order}",
        f":featured_image: {featured}",
        "",
        f".. _collection-{col.slug}:",
        "",
        _rst_heading(f"{col.code_prefix} — {col.title}", "="),
        "",
        ".. enunciation::",
        "",
        f"   {col.enunciation}",
        "",
        f"Curated from :person:`Dr. Ron Knott <knott>`'s University of Surrey archive "
        f"(**{KNOTT_COPYRIGHT}**).",
        "",
        ".. collection::",
        "   :type: item",
        "   :sort: order",
        "",
        _rst_heading("Collection Concordance", "-"),
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 16 48 36",
        "",
        "   * - Catalog ID",
        "     - GEOMETOR Catalog Entry",
        "     - Curated Source Anchor",
        *table_rows,
        "",
    ]
    return "\n".join(lines)


def _render_catalog_root_rst() -> str:
    """Render ``docsrc/catalog/index.rst``."""
    rows: list[str] = []
    for it in CATALOG_ITEMS:
        rows.extend(
            [
                f"   * - :ref:`{it.canonical_id} <{it.folio_id}>`",
                f"     - {it.title}",
                f"     - `{it.knott_anchor} <{it.knott_url}>`_",
                f"     - :func:`~{it.validator_qualname}`",
            ]
        )
    lines = [
        ":layout: book",
        ":navigation: header",
        ":order: 10",
        "",
        _rst_heading("Mathematical Catalog", "="),
        "",
        ".. enunciation::",
        "",
        "   Six thematic collections cataloging **22** Golden Ratio, trigonometric, "
        "polyhedral, phigit, Sturmian, and Fibonacci–Lucas structures from "
        ":person:`Dr. Ron Knott <knott>`'s *Fibonacci Numbers, the Golden Section and "
        "the Golden String* (**" + KNOTT_COPYRIGHT + "**), each proven with 100% exact "
        "``SymPy`` algebra and rendered as an interactive ``.euclid-graphic`` SVG.",
        "",
        ".. collection::",
        "   :type: collection",
        "   :sort: order",
        "",
        _rst_heading("Master 22-Entry Concordance", "-"),
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 14 42 18 26",
        "",
        "   * - ID",
        "     - Title",
        "     - Knott Anchor",
        "     - Symbolic Validator",
        *rows,
        "",
    ]
    return "\n".join(lines)


def _write_apparatus_pages(resources_dir: Path, docsrc_dir: Path) -> None:
    """Generate ``glossary.rst``, ``persons.rst``, and ``bibliography.rst`` from ``resources/*.json``."""
    glossary_data: dict[str, dict[str, str]] = json.loads(
        (resources_dir / "glossary.json").read_text(encoding="utf-8")
    )
    persons_data: dict[str, dict[str, str]] = json.loads(
        (resources_dir / "persons.json").read_text(encoding="utf-8")
    )
    citations_data: dict[str, dict[str, str]] = json.loads(
        (resources_dir / "citations.json").read_text(encoding="utf-8")
    )

    g_lines = [
        ":layout: book",
        ":navigation: header",
        ":order: 70",
        "",
        _rst_heading("Glossary", "="),
        "",
        "Exact geometric, trigonometric, and number-theoretic terms referenced across "
        "the **GEOMETOR Knott Mathematical Catalog**.",
        "",
    ]
    for key, entry in glossary_data.items():
        slug = _apparatus_slug(key)
        hw = entry["headword"]
        trans = entry.get("translation", "")
        defn = entry["definition"]
        g_lines.extend(
            [
                f".. _term-{slug}:",
                "",
                _rst_heading(hw, "-"),
                "",
                f"*{trans}*" if trans else "",
                "",
                defn,
                "",
            ]
        )
    (docsrc_dir / "glossary.rst").write_text("\n".join(g_lines), encoding="utf-8")

    p_lines = [
        ":layout: book",
        ":navigation: header",
        ":order: 75",
        "",
        _rst_heading("Persons", "="),
        "",
        "Mathematicians, geometers, and scholars referenced across the "
        "**GEOMETOR Knott Mathematical Catalog**.",
        "",
    ]
    for key, entry in persons_data.items():
        slug = _apparatus_slug(key)
        name = entry["name"]
        dates = entry.get("dates", "")
        role = entry["role"]
        heading = f"{name} ({dates})" if dates else name
        p_lines.extend(
            [
                f".. _person-{slug}:",
                "",
                _rst_heading(heading, "-"),
                "",
                role,
                "",
            ]
        )
    (docsrc_dir / "persons.rst").write_text("\n".join(p_lines), encoding="utf-8")

    b_lines = [
        ":layout: book",
        ":navigation: header",
        ":order: 80",
        "",
        _rst_heading("Bibliography & Source Concordance", "="),
        "",
        "Primary online reference pages by **Dr. Ron Knott** (**" + KNOTT_COPYRIGHT + "**) "
        "and classical/modern mathematical treatises cited across this catalog.",
        "",
    ]
    for key, entry in citations_data.items():
        slug = _apparatus_slug(key)
        author = entry["author"]
        work = entry["work"]
        locus = entry.get("locus", "")
        url = entry.get("url", "")
        url_line = f" — `{url} <{url}>`_" if url else ""
        b_lines.extend(
            [
                f".. _cite-{slug}:",
                "",
                _rst_heading(f"[{key}] {work}", "-"),
                "",
                f"**{author}**, *{work}* ({locus}){url_line}.",
                "",
            ]
        )
    (docsrc_dir / "bibliography.rst").write_text("\n".join(b_lines), encoding="utf-8")


def build_all() -> None:
    """Execute all 22 symbolic proofs, render SVGs, write RST pages, and check parity."""
    resources_dir = REPO_ROOT / "resources"
    docsrc_dir = REPO_ROOT / "docsrc"
    catalog_dir = docsrc_dir / "catalog"

    manifest_path = export_catalog_manifest(resources_dir / "catalog_manifest.json")
    print(f"Wrote manifest: {manifest_path}")

    _write_apparatus_pages(resources_dir, docsrc_dir)
    print("Wrote apparatus pages: glossary.rst, persons.rst, bibliography.rst")

    results = verify_all_catalog_items()
    print(f"Verified {len(results)} catalog models with 0 Float atoms.")

    items_by_col: dict[str, list[CatalogItemSpec]] = {c.slug: [] for c in COLLECTIONS}
    for spec in CATALOG_ITEMS:
        items_by_col[spec.collection_slug].append(spec)
        res = results[spec.canonical_id]
        item_dir = catalog_dir / spec.collection_slug / spec.item_slug
        svg_path = item_dir / f"{spec.folio_id}.g1.svg"
        rst_path = item_dir / "index.rst"

        write_euclid_svg(res.model, svg_path, folio_id=spec.folio_id)
        rst_text = _render_item_rst(spec, res)
        rst_path.write_text(rst_text, encoding="utf-8")

        svg_text = svg_path.read_text(encoding="utf-8")
        _validate_rst_svg_parity(rst_text, svg_text, spec.canonical_id)
        print(f"  [{spec.canonical_id}] -> {svg_path.relative_to(REPO_ROOT)} + index.rst OK")

    for col in COLLECTIONS:
        col_rst = _render_collection_rst(col, items_by_col[col.slug])
        col_index = catalog_dir / col.slug / "index.rst"
        col_index.parent.mkdir(parents=True, exist_ok=True)
        col_index.write_text(col_rst, encoding="utf-8")

    (catalog_dir / "index.rst").write_text(_render_catalog_root_rst(), encoding="utf-8")
    print("Catalog codex generation complete.")


if __name__ == "__main__":
    build_all()
