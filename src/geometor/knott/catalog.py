"""Master registry of the 6 Collections and 22 Catalog Items (`KNOTT-1.1` – `KNOTT-6.5`).

Maps every cataloged theorem, construction, sequence, and identity to Dr. Ron Knott's
exact University of Surrey source URL and section anchor, its exact SymPy /
``geometor.model`` validator function, scholarly apparatus keys, and cross-referenced
GEOMETOR repositories.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from geometor.knott.constants import assert_no_floats
from geometor.knott.flat_geometry import (
    GeometricCatalogResult,
    construct_golden_rectangles_and_spiral,
    construct_golden_section_segment,
    construct_golden_triangles_and_gnomons,
    construct_kepler_triangle,
    construct_penrose_tiles,
    construct_pentagon_and_paper_knot,
)
from geometor.knott.golden_string import (
    construct_golden_string_cutting_model,
    construct_wythoff_beatty_model,
    construct_zeckendorf_staircase_model,
)
from geometor.knott.identities import (
    construct_fibonacci_jigsaw_model,
    construct_fibonacci_pythagorean_model,
    construct_hayashi_arctan_grid_model,
    construct_lucas_binet_model,
    construct_parastichy_lattice_model,
)
from geometor.knott.phigits import (
    construct_convergents_model,
    construct_phi_powers_model,
    construct_phigit_scale_model,
)
from geometor.knott.solid_geometry import (
    construct_cube_in_dodecahedron_model,
    construct_golden_rhombohedra_model,
    construct_orthogonal_golden_rectangles_solids,
)
from geometor.knott.trigonometry import (
    construct_pentagonal_trig_model,
    construct_three_degree_lattice_model,
)

KNOTT_COPYRIGHT = "© 1996–2025 Dr. Ron Knott, University of Surrey"


@dataclass(frozen=True)
class CollectionSpec:
    """Metadata for one of the six thematic Collections in ``docsrc/catalog/``."""

    order: int
    slug: str
    code_prefix: str
    title: str
    enunciation: str
    source_pages: tuple[str, ...]


@dataclass(frozen=True)
class CatalogItemSpec:
    """Complete specification for a single cataloged mathematical item."""

    canonical_id: str
    collection_slug: str
    order: int
    item_slug: str
    folio_id: str
    title: str
    enunciation: str
    knott_url: str
    knott_page_title: str
    knott_anchor: str
    validator_qualname: str
    builder: Callable[[], GeometricCatalogResult]
    geometor_repos: tuple[str, ...]
    citations: tuple[str, ...]
    persons: tuple[str, ...]
    terms: tuple[str, ...]


COLLECTIONS: tuple[CollectionSpec, ...] = (
    CollectionSpec(
        order=1,
        slug="01-flat-geometry",
        code_prefix="KNOTT-1",
        title="2D Golden Geometry & Constructions",
        enunciation=(
            "Planar compass-and-straightedge divisions in extreme and mean ratio, "
            "golden and root-5 rectangles with orthogonal gnomonic spiral poles, "
            "self-deflating golden triangles and gnomons, pentagonal star progressions "
            "and overhand paper-strip knots, Kepler's geometric-progression right "
            "triangle, and Penrose aperiodic P2/P3 prototiles."
        ),
        source_pages=("phi2DGeomTrig.html",),
    ),
    CollectionSpec(
        order=2,
        slug="02-exact-trigonometry",
        code_prefix="KNOTT-2",
        title="Exact Pentagonal & Constructible Trigonometry",
        enunciation=(
            "Closed-form quadratic radicals and Rational Trigonometry spreads for "
            "18°, 36°, 54°, and 72°, extended by Euclid IV.16 pentagon-equilateral "
            "superposition across all 29 constructible multiples of 3° in the first "
            "quadrant and contrasted with Gauss's Fermat-prime regular 17-gon cosine."
        ),
        source_pages=("simpleTrig.html", "phi2DGeomTrig.html"),
    ),
    CollectionSpec(
        order=3,
        slug="03-solid-geometry",
        code_prefix="KNOTT-3",
        title="3D Golden Geometry of Solids",
        enunciation=(
            "Three-dimensional golden coordinates spanning the regular icosahedron "
            "and dodecahedron from three mutually orthogonal golden rectangles, "
            "Euclid XIII.17's inscribed cube and five-cube compound, and the acute "
            "and obtuse golden rhombohedra of icosahedral quasicrystals."
        ),
        source_pages=("phi3DGeom.html",),
    ),
    CollectionSpec(
        order=4,
        slug="04-phigits-and-algebra",
        code_prefix="KNOTT-4",
        title="Algebraic Powers of Φ, Continued Fractions & Base-Φ Phigits",
        enunciation=(
            "Linearization of all integer powers of Φ into Fibonacci multiples, "
            "the unit-volume Phibonacci brick, extremal continued fraction convergents "
            "F_{n+1}/F_n and Hurwitz's √5 irrationality barrier, and George Bergman's "
            "non-adjacent base-Φ ('phigit') numeral system."
        ),
        source_pages=("propsOfPhi.html", "phigits.html", "cfINTRO.html"),
    ),
    CollectionSpec(
        order=5,
        slug="05-golden-string-and-arrays",
        code_prefix="KNOTT-5",
        title="The Golden String, Zeckendorf Base, & Wythoff / Stolarsky Arrays",
        enunciation=(
            "The infinite Sturmian Golden String (101101011011...) generated both by "
            "morphism substitution and by a lattice-cutting ray of slope φ, "
            "Zeckendorf's canonical non-consecutive Fibonacci base, and the bijective "
            "Beatty, Wythoff, and Stolarsky interspersion arrays."
        ),
        source_pages=("fibrab.html", "fibrep.html", "fibGen.html"),
    ),
    CollectionSpec(
        order=6,
        slug="06-identities-and-bridges",
        code_prefix="KNOTT-6",
        title="Fibonacci-Lucas Identities, Pythagorean Triples, Jigsaw Paradoxes & π",
        enunciation=(
            "Four-term Fibonacci generators of Pythagorean right triangles, Cassini's "
            "alternating ±1 determinant realized as 64 ↔ 65 and 64 ↔ 63 four-piece "
            "dissections, Binet/Lucas/Catalan/d'Ocagne/Honsberger and Fibonomial "
            "power identities, Fibonacci arctangent telescoping series for π, and "
            "the Golden Angle parastichy lattice."
        ),
        source_pages=(
            "pythag.html",
            "fibpuzzles2.html",
            "fibFormulae.html",
            "fibpi.html",
            "fibnat.html",
        ),
    ),
)


CATALOG_ITEMS: tuple[CatalogItemSpec, ...] = (
    # Collection 1: 2D Golden Geometry & Constructions
    CatalogItemSpec(
        canonical_id="KNOTT-1.1",
        collection_slug="01-flat-geometry",
        order=1,
        item_slug="01-golden-section-segment",
        folio_id="knott-1-1",
        title="Internal & External Golden Section Constructions on a Segment",
        enunciation=(
            "Given a finite segment AB, midpoint-circle compass-and-straightedge "
            "constructions divide AB internally at G so AB : AG = AG : GB = Φ and "
            "extend AB externally to E so AE : AB = AB : BE = Φ, erecting Golden "
            "Rectangle AEFD."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#cons",
        knott_page_title="Phi in 2D Geometry and Trigonometry",
        knott_anchor="#cons",
        validator_qualname="geometor.knott.flat_geometry.construct_golden_section_segment",
        builder=construct_golden_section_segment,
        geometor_repos=("geometor/euclid", "geometor/elements", "geometor/divine", "geometor/fundamentals"),
        citations=("KnottPhi2D", "EuclidElements"),
        persons=("knott", "euclid"),
        terms=("golden-ratio", "extreme-and-mean-ratio", "cross-ratio"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-1.2",
        collection_slug="01-flat-geometry",
        order=2,
        item_slug="02-golden-rectangles-and-spiral",
        folio_id="knott-1-2",
        title="Golden Rectangles, √5 Rectangles, & Whirling-Square Gnomonic Spirals",
        enunciation=(
            "Flanking a unit square ABCD on both sides via its base-midpoint circle "
            "produces a 1 × √5 rectangle WEFN containing right golden rectangle AEFD; "
            "recursive whirling-square cuts in gnomon BEFC share perpendicular main "
            "and secondary diagonals [AF] ⊥ [EC] (spread s = 1) meeting at pole "
            "P = (Φ²/√5, Φ/√5)."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#root5",
        knott_page_title="Phi in 2D Geometry and Trigonometry",
        knott_anchor="#root5",
        validator_qualname="geometor.knott.flat_geometry.construct_golden_rectangles_and_spiral",
        builder=construct_golden_rectangles_and_spiral,
        geometor_repos=("geometor/euclid", "geometor/divine", "geometor/pacioli"),
        citations=("KnottPhi2D", "Hambidge1920"),
        persons=("knott", "pacioli"),
        terms=("golden-rectangle", "gnomon", "spread"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-1.3",
        collection_slug="01-flat-geometry",
        order=3,
        item_slug="03-golden-triangles-and-gnomons",
        folio_id="knott-1-3",
        title="Golden Triangles (72°–72°–36°) & Golden Gnomons (36°–36°–108°)",
        enunciation=(
            "An isosceles acute golden triangle ABC with base AB = 1 and legs "
            "AC = BC = Φ is partitioned by base-angle bisector AD (with AD = CD = 1 "
            "and BD = φ) into an obtuse golden gnomon CAD and a self-similar acute "
            "golden triangle DAB with exact spreads s(36°) = (5 − √5)/8 and "
            "s(72°) = (5 + √5)/8."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#isoc",
        knott_page_title="Phi in 2D Geometry and Trigonometry",
        knott_anchor="#isoc",
        validator_qualname="geometor.knott.flat_geometry.construct_golden_triangles_and_gnomons",
        builder=construct_golden_triangles_and_gnomons,
        geometor_repos=("geometor/euclid", "geometor/elements", "geometor/wildberger", "geometor/divine"),
        citations=("KnottPhi2D", "EuclidElements", "Wildberger2005"),
        persons=("knott", "euclid", "wildberger"),
        terms=("golden-triangle", "golden-gnomon", "spread"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-1.4",
        collection_slug="01-flat-geometry",
        order=4,
        item_slug="04-pentagon-pentagram-paper-knot",
        folio_id="knott-1-4",
        title="Regular Pentagon, Pentagram, Decagon & Paper-Knot Pentagon",
        enunciation=(
            "The five diagonals of a regular pentagon of side 1 enclose a similar "
            "inner pentagon of side φ² and cut each diagonal in the geometric "
            "progression φ² : φ : 1 : Φ; furthermore, folding a flat uniform strip "
            "of width w into a tight overhand knot locks parallel trapezoid edges "
            "into an exact regular pentagon of side w sec 18°."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#pent",
        knott_page_title="Phi in 2D Geometry and Trigonometry",
        knott_anchor="#pent",
        validator_qualname="geometor.knott.flat_geometry.construct_pentagon_and_paper_knot",
        builder=construct_pentagon_and_paper_knot,
        geometor_repos=("geometor/euclid", "geometor/elements", "geometor/pacioli", "geometor/divine"),
        citations=("KnottPhi2D", "EuclidElements", "Pacioli1509"),
        persons=("knott", "euclid", "pacioli"),
        terms=("pentagram", "golden-ratio", "quadrance"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-1.5",
        collection_slug="01-flat-geometry",
        order=5,
        item_slug="05-kepler-triangle-and-quadrature",
        folio_id="knott-1-5",
        title="Kepler's Golden Right Triangle (1, √Φ, Φ) & Circle-Square Near-Quadrature",
        enunciation=(
            "A right triangle with side lengths (1, √Φ, Φ) has side quadrances "
            "(1, Φ, Φ²) simultaneously in geometric progression and Pythagorean "
            "sum 1 + Φ = Φ², satisfies cos θ = tan θ = 1/√Φ, and equates the "
            "perimeter 4√Φ of the square on leg √Φ with the circumference πΦ of "
            "the circle on diameter Φ to within 0.096%."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#PhiRightAng",
        knott_page_title="Phi in 2D Geometry and Trigonometry",
        knott_anchor="#PhiRightAng",
        validator_qualname="geometor.knott.flat_geometry.construct_kepler_triangle",
        builder=construct_kepler_triangle,
        geometor_repos=("geometor/wildberger", "geometor/euclid", "geometor/divine"),
        citations=("KnottPhi2D", "Wildberger2005"),
        persons=("knott", "kepler", "wildberger"),
        terms=("kepler-triangle", "quadrance", "spread"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-1.6",
        collection_slug="01-flat-geometry",
        order=6,
        item_slug="06-penrose-kites-darts-and-rhombs",
        folio_id="knott-1-6",
        title="Penrose Kites & Darts (P2) and Thick & Thin Golden Rhombs (P3)",
        enunciation=(
            "A thick 72°–108° golden rhomb of side Φ divides at unit distance K "
            "along its long diagonal of length Φ² into a convex Penrose kite KBCD "
            "and a non-convex Penrose dart ABKD with exact area ratio Φ : 1, "
            "matching the Φ : 1 area ratio between thick (72°) and thin (36°) "
            "Penrose golden rhombs."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#penrose",
        knott_page_title="Phi in 2D Geometry and Trigonometry",
        knott_anchor="#penrose",
        validator_qualname="geometor.knott.flat_geometry.construct_penrose_tiles",
        builder=construct_penrose_tiles,
        geometor_repos=("geometor/divine", "geometor/wildberger"),
        citations=("KnottPhi2D", "Penrose1974", "Gardner1977"),
        persons=("knott", "penrose", "conway"),
        terms=("penrose-tiling", "golden-triangle", "golden-gnomon"),
    ),
    # Collection 2: Exact Pentagonal & Constructible Trigonometry
    CatalogItemSpec(
        canonical_id="KNOTT-2.1",
        collection_slug="02-exact-trigonometry",
        order=1,
        item_slug="01-pentagonal-radicals-and-spreads",
        folio_id="knott-2-1",
        title="Exact Radical Sines, Cosines, Tangents & Spreads of 18°, 36°, 54°, 72°",
        enunciation=(
            "On the unit circle, cos 36° = sin 54° = Φ/2 and sin 18° = cos 72° = φ/2 "
            "differ by exactly 1/2 and multiply to 1/4, while the pentagonal spreads "
            "s(36°) = (5 − √5)/8 and s(72°) = (5 + √5)/8 form the quadratic roots of "
            "Wildberger's five-fold spread factor 16 s² − 20 s + 5 = 0."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html#3654",
        knott_page_title="Exact Trig Values for Simple Angles",
        knott_anchor="#3654",
        validator_qualname="geometor.knott.trigonometry.construct_pentagonal_trig_model",
        builder=construct_pentagonal_trig_model,
        geometor_repos=("geometor/wildberger", "geometor/euclid", "geometor/divine"),
        citations=("KnottSimpleTrig", "KnottPhi2D", "Wildberger2005"),
        persons=("knott", "wildberger", "ptolemy"),
        terms=("spread", "golden-ratio", "quadrance"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-2.2",
        collection_slug="02-exact-trigonometry",
        order=2,
        item_slug="02-three-degree-constructible-lattice",
        folio_id="knott-2-2",
        title="The Complete 3° Constructible Angle Lattice (3°k for k = 1..29)",
        enunciation=(
            "Superimposing pentagonal angles in Q(√5) with equilateral and half-right "
            "angles in Q(√2, √3) expresses sin(3°k), cos(3°k), tan(3°k), and spread "
            "s(3°k) in explicit nested square roots for all 29 acute multiples of 3°, "
            "while Gauss's Fermat prime 17 = 2⁴ + 1 extends compass constructibility "
            "to cos(π/17)."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html#otherexact",
        knott_page_title="Exact Trig Values for Simple Angles",
        knott_anchor="#otherexact",
        validator_qualname="geometor.knott.trigonometry.construct_three_degree_lattice_model",
        builder=construct_three_degree_lattice_model,
        geometor_repos=("geometor/euclid", "geometor/elements", "geometor/wildberger"),
        citations=("KnottSimpleTrig", "EuclidElements", "Gauss1801"),
        persons=("knott", "euclid", "gauss"),
        terms=("constructible-angle", "spread", "quadrance"),
    ),
    # Collection 3: 3D Golden Geometry of Solids
    CatalogItemSpec(
        canonical_id="KNOTT-3.1",
        collection_slug="03-solid-geometry",
        order=1,
        item_slug="01-orthogonal-golden-rectangles-solids",
        folio_id="knott-3-1",
        title="Three Orthogonal Golden Rectangles → Regular Icosahedron & Dodecahedron",
        enunciation=(
            "Three mutually perpendicular 2 × 2Φ golden rectangles have 12 corners "
            "(0, ±1, ±Φ) forming a regular icosahedron of edge 2, volume 20Φ²/3, and "
            "rational dihedral spread 4/9, while (±1, ±1, ±1) ∪ cyc(0, ±φ, ±Φ) "
            "forms a regular dodecahedron of edge 2φ, volume 8 + 4Φ, and dihedral "
            "spread 4/5."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#coords",
        knott_page_title="The Golden Geometry of Solids or Phi in 3 Dimensions",
        knott_anchor="#coords",
        validator_qualname="geometor.knott.solid_geometry.construct_orthogonal_golden_rectangles_solids",
        builder=construct_orthogonal_golden_rectangles_solids,
        geometor_repos=("geometor/pacioli", "geometor/euclid", "geometor/wildberger"),
        citations=("KnottPhi3D", "Pacioli1509", "Coxeter1973", "Wildberger2005"),
        persons=("knott", "pacioli", "euclid", "coxeter"),
        terms=("golden-rectangle", "spread", "quadrance"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-3.2",
        collection_slug="03-solid-geometry",
        order=2,
        item_slug="02-five-cubes-in-dodecahedron",
        folio_id="knott-3-2",
        title="Inscribed Cube & Compound of Five Cubes in a Dodecahedron",
        enunciation=(
            "Inside a regular dodecahedron of edge 2φ, the 60 face diagonals of "
            "length 2 = Φ · (2φ) partition into five congruent inscribed cubes of "
            "edge 2 and volume 8, with each of the 20 dodecahedral vertices belonging "
            "to exactly two cubes."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#cubeinDod",
        knott_page_title="The Golden Geometry of Solids or Phi in 3 Dimensions",
        knott_anchor="#cubeinDod",
        validator_qualname="geometor.knott.solid_geometry.construct_cube_in_dodecahedron_model",
        builder=construct_cube_in_dodecahedron_model,
        geometor_repos=("geometor/euclid", "geometor/elements", "geometor/pacioli"),
        citations=("KnottPhi3D", "EuclidElements", "Coxeter1973"),
        persons=("knott", "euclid", "pacioli", "coxeter"),
        terms=("golden-ratio", "quadrance"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-3.3",
        collection_slug="03-solid-geometry",
        order=3,
        item_slug="03-golden-rhombohedra-quasicrystals",
        folio_id="knott-3-3",
        title="Acute & Obtuse Golden Rhombohedra (3D Quasicrystal / Ammann Tiles)",
        enunciation=(
            "Triples of five-fold icosahedral vectors of quadrance Φ + 2 span "
            "acute (prolate) and obtuse (oblate) golden rhombohedra bounded by six "
            "congruent golden rhombi of diagonal ratio Φ : 1, with exact volumes "
            "2Φ² and 2Φ in ratio Φ : 1 and 10 + 10 assembly into a rhombic "
            "triacontahedron of volume 20Φ³."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#quasicrystalsPhi",
        knott_page_title="The Golden Geometry of Solids or Phi in 3 Dimensions",
        knott_anchor="#quasicrystalsPhi",
        validator_qualname="geometor.knott.solid_geometry.construct_golden_rhombohedra_model",
        builder=construct_golden_rhombohedra_model,
        geometor_repos=("geometor/pacioli", "geometor/divine"),
        citations=("KnottPhi3D", "Coxeter1973", "Penrose1974"),
        persons=("knott", "kepler", "penrose", "coxeter"),
        terms=("golden-rhombohedron", "penrose-tiling", "golden-ratio"),
    ),
    # Collection 4: Algebraic Powers of Phi, Continued Fractions & Base-Phi Phigits
    CatalogItemSpec(
        canonical_id="KNOTT-4.1",
        collection_slug="04-phigits-and-algebra",
        order=1,
        item_slug="01-fibonacci-power-linearization",
        folio_id="knott-4-1",
        title="Fibonacci Power Linearization (Φⁿ = FₙΦ + Fₙ₋₁) & The Phibonacci Brick",
        enunciation=(
            "Every integer power n ∈ Z of the Golden Ratio reduces to the linear "
            "form Φⁿ = Fₙ Φ + Fₙ₋₁ and (−φ)ⁿ = Fₙ₊₁ − Fₙ Φ = Fₙ₋₁ − Fₙ φ, while "
            "a rectangular Phibonacci brick of edges (1, φ, Φ) has unit volume 1, "
            "surface area 4Φ, and integer space diagonal 2."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/propsOfPhi.html#powers",
        knott_page_title="Phi's Fascinating Figures",
        knott_anchor="#powers",
        validator_qualname="geometor.knott.phigits.construct_phi_powers_model",
        builder=construct_phi_powers_model,
        geometor_repos=("geometor/divine", "geometor/fundamentals"),
        citations=("KnottPropsPhi", "Vajda1989"),
        persons=("knott", "fibonacci", "lucas"),
        terms=("golden-ratio", "gnomon"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-4.2",
        collection_slug="04-phigits-and-algebra",
        order=2,
        item_slug="02-continued-fractions-and-hurwitz",
        folio_id="knott-4-2",
        title="Extremal Continued Fraction [1; 1, 1, …], Convergents Fₙ₊₁/Fₙ, & Nested Radicals",
        enunciation=(
            "The all-ones simple continued fraction Φ = [1; 1, 1, …] has rational "
            "convergents cₖ = Fₖ₊₁/Fₖ with exact alternating error cₖ − Φ = (−φ)ᵏ/Fₖ, "
            r"saturating Hurwitz's irrationality constant √5 via :math:`F_k^2 |c_k - \Phi| \to 1/\sqrt{5}`."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/propsOfPhi.html#contfract",
        knott_page_title="Phi's Fascinating Figures",
        knott_anchor="#contfract",
        validator_qualname="geometor.knott.phigits.construct_convergents_model",
        builder=construct_convergents_model,
        geometor_repos=("geometor/divine", "geometor/wildberger"),
        citations=("KnottPropsPhi", "Hurwitz1891"),
        persons=("knott", "fibonacci", "hurwitz", "lucas"),
        terms=("continued-fraction", "cassini-identity", "golden-ratio"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-4.3",
        collection_slug="04-phigits-and-algebra",
        order=3,
        item_slug="03-bergman-base-phi-phigits",
        folio_id="knott-4-3",
        title="Bergman's Base-Φ ('Phigit') Numeral System",
        enunciation=(
            "Under the carry law Φⁿ = Φⁿ⁻¹ + Φⁿ⁻² (100_Φ = 011_Φ), every positive "
            "integer N ≥ 1 admits a unique finite minimal non-adjacent {0, 1} "
            "expansion in powers of Φ; excluding infinite 011-tails yields a unique "
            "00-free maximal form and exactly Fₖ valid finite phigit forms for every "
            "Fibonacci number Fₖ."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/phigits.html#canonical",
        knott_page_title="Phigits and the Base Phi System",
        knott_anchor="#canonical",
        validator_qualname="geometor.knott.phigits.construct_phigit_scale_model",
        builder=construct_phigit_scale_model,
        geometor_repos=("geometor/divine",),
        citations=("KnottPhigits", "Bergman1957"),
        persons=("knott", "bergman", "lucas", "fibonacci"),
        terms=("phigit", "golden-ratio", "zeckendorf-representation"),
    ),
    # Collection 5: The Golden String, Zeckendorf Base, & Wythoff / Stolarsky Arrays
    CatalogItemSpec(
        canonical_id="KNOTT-5.1",
        collection_slug="05-golden-string-and-arrays",
        order=1,
        item_slug="01-golden-string-and-cutting-line",
        folio_id="knott-5-1",
        title="The Infinite Golden String (101101011011…), Rabbit Tree & Cutting-Line Slope φ",
        enunciation=(
            "Iterating the Rabbit substitution 1 ↦ 10, 0 ↦ 1 generates the infinite "
            "Sturmian Golden String dₙ = ⌊(n + 1)φ⌋ − ⌊nφ⌋, identically realized "
            "geometrically as the sequence of vertical ('1') and horizontal ('0') "
            "unit-lattice crossings of the ray y = φ x from the origin."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/fibrab.html#PhiPlot",
        knott_page_title="The Fibonacci Rabbit Sequence (The Golden String)",
        knott_anchor="#PhiPlot",
        validator_qualname="geometor.knott.golden_string.construct_golden_string_cutting_model",
        builder=construct_golden_string_cutting_model,
        geometor_repos=("geometor/trees", "geometor/divine"),
        citations=("KnottGoldenString", "Vajda1989"),
        persons=("knott", "fibonacci"),
        terms=("golden-string", "beatty-sequence", "golden-ratio"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-5.2",
        collection_slug="05-golden-string-and-arrays",
        order=2,
        item_slug="02-zeckendorf-fibonacci-base",
        folio_id="knott-5-2",
        title="Zeckendorf's Theorem (Canonical Fibonacci Base Representation)",
        enunciation=(
            "Every positive integer N ≥ 1 decomposes uniquely as a sum of "
            "non-consecutive Fibonacci numbers F_{k₁} + F_{k₂} + … + F_{kᵣ} "
            "(kᵢ ≥ kᵢ₊₁ + 2, kᵣ ≥ 2), producing a unique 11-free binary numeral "
            "in Fibonacci place values (…, 13, 8, 5, 3, 2, 1)."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/fibrep.html#zeck",
        knott_page_title="Fibonacci Representations of Numbers",
        knott_anchor="#zeck",
        validator_qualname="geometor.knott.golden_string.construct_zeckendorf_staircase_model",
        builder=construct_zeckendorf_staircase_model,
        geometor_repos=("geometor/divine", "geometor/trees"),
        citations=("KnottFibRep", "Zeckendorf1972"),
        persons=("knott", "zeckendorf", "fibonacci"),
        terms=("zeckendorf-representation", "phigit"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-5.3",
        collection_slug="05-golden-string-and-arrays",
        order=3,
        item_slug="03-wythoff-beatty-and-stolarsky-arrays",
        folio_id="knott-5-3",
        title="Wythoff's Array, Beatty's Complementary Sequences (⌊nΦ⌋, ⌊nΦ²⌋), & Stolarsky's Array",
        enunciation=(
            "Because 1/Φ + 1/Φ² = 1, Beatty's sequences Aₙ = ⌊nΦ⌋ and Bₙ = ⌊nΦ²⌋ = Aₙ + n "
            "partition Z_{>0} without overlap; seeding generalized Fibonacci rows via "
            "W(r, c) = ⌊(r + 1)Φ⌋ F_{c+2} + r F_{c+1} (Wythoff) or nearest-integer "
            "multiples [kΦ] (Stolarsky) places every positive integer in a unique "
            "(row, col) cell."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/fibGen.html#wythoff",
        knott_page_title="General Fibonacci Series, Wythoff and Stolarsky Arrays",
        knott_anchor="#wythoff",
        validator_qualname="geometor.knott.golden_string.construct_wythoff_beatty_model",
        builder=construct_wythoff_beatty_model,
        geometor_repos=("geometor/etc", "geometor/divine"),
        citations=("KnottFibGen", "Wythoff1907", "Stolarsky1977", "Morrison1980"),
        persons=("knott", "wythoff", "stolarsky", "conway", "kimberling"),
        terms=("beatty-sequence", "wythoff-array", "stolarsky-array", "zeckendorf-representation"),
    ),
    # Collection 6: Fibonacci-Lucas Identities, Pythagorean Triples, Jigsaw Paradoxes & Pi
    CatalogItemSpec(
        canonical_id="KNOTT-6.1",
        collection_slug="06-identities-and-bridges",
        order=1,
        item_slug="01-fibonacci-pythagorean-triples",
        folio_id="knott-6-1",
        title="Fibonacci Generator of Primitive Pythagorean Triples",
        enunciation=(
            "Any four consecutive positive Fibonacci numbers (Fₙ, Fₙ₊₁, Fₙ₊₂, Fₙ₊₃) "
            "form the Pythagorean right triangle (Fₙ Fₙ₊₃, 2 Fₙ₊₁ Fₙ₊₂, F₂ₙ₊₃) of "
            "area Fₙ Fₙ₊₁ Fₙ₊₂ Fₙ₊₃ and inradius Fₙ Fₙ₊₁, primitive whenever 3 ∤ n "
            "and twice a primitive triple when 3 ∣ n."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Pythag/pythag.html#pythfib",
        knott_page_title="Pythagorean Triangles and Triples",
        knott_anchor="#pythfib",
        validator_qualname="geometor.knott.identities.construct_fibonacci_pythagorean_model",
        builder=construct_fibonacci_pythagorean_model,
        geometor_repos=("geometor/wildberger", "geometor/euclid", "geometor/elements"),
        citations=("KnottPythag", "EuclidElements", "Horadam1961"),
        persons=("knott", "pythagoras", "euclid", "fibonacci"),
        terms=("quadrance", "spread"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-6.2",
        collection_slug="06-identities-and-bridges",
        order=2,
        item_slug="02-cassini-jigsaw-paradoxes",
        folio_id="knott-6-2",
        title="Cassini's Identity (Fₙ₋₁Fₙ₊₁ − Fₙ² = (−1)ⁿ) & The 64 ↔ 65 / 63 Jigsaw Dissections",
        enunciation=(
            "Cassini's alternating identity Fₙ₋₁ Fₙ₊₁ − Fₙ² = (−1)ⁿ manifests "
            "geometrically when the four pieces of an 8 × 8 = 64 square (two 3 × 8 "
            "triangles and two 5 × (3, 5) trapezoids) rearrange into a 5 × 13 = 65 "
            "rectangle with a +1 parallelogram gap OR into a 63-unit notched block "
            "with a −1 parallelogram overlap."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/fibpuzzles2.html#jigsaw1",
        knott_page_title="Harder Fibonacci Puzzles",
        knott_anchor="#jigsaw1",
        validator_qualname="geometor.knott.identities.construct_fibonacci_jigsaw_model",
        builder=construct_fibonacci_jigsaw_model,
        geometor_repos=("geometor/euclid", "geometor/divine"),
        citations=("KnottPuzzles2", "Gardner1956", "Horadam1962"),
        persons=("knott", "cassini", "loyd", "dudeney"),
        terms=("cassini-identity", "golden-ratio"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-6.3",
        collection_slug="06-identities-and-bridges",
        order=3,
        item_slug="03-binet-lucas-catalan-fibonomials",
        folio_id="knott-6-3",
        title="Binet, Lucas, Catalan, d'Ocagne, Honsberger & Fibonomial Power Identities",
        enunciation=(
            "Binet's closed forms Fₙ = (Φⁿ − (−φ)ⁿ)/√5 and Lₙ = Φⁿ + (−φ)ⁿ place "
            "(Lₙ, Fₙ) on the alternating Pell-Lucas hyperbolas Lₙ² − 5 Fₙ² = 4(−1)ⁿ "
            "with unit sector triangles, unify Catalan, d'Ocagne, and Honsberger "
            "identities, and annihilate k-th powers Fₙᵏ via signed Fibonomial "
            "coefficients."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/fibFormulae.html#defs",
        knott_page_title="Fibonacci and Phi Formulae",
        knott_anchor="#defs",
        validator_qualname="geometor.knott.identities.construct_lucas_binet_model",
        builder=construct_lucas_binet_model,
        geometor_repos=("geometor/divine", "geometor/wildberger"),
        citations=("KnottFormulae", "Vajda1989", "Honsberger1985"),
        persons=("knott", "binet", "lucas", "catalan", "fibonacci"),
        terms=("fibonomial", "cassini-identity", "golden-ratio"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-6.4",
        collection_slug="06-identities-and-bridges",
        order=4,
        item_slug="04-fibonacci-arctangent-pi-formulae",
        folio_id="knott-6-4",
        title="Fibonacci Arctangent Telescoping Formulae for π",
        enunciation=(
            "By Cassini's odd-index relation F₂ₙ₊₁² − 1 = F₂ₙ F₂ₙ₊₂, every even-indexed "
            "reciprocal Fibonacci angle splits as arctan(1/F₂ₙ) = arctan(1/F₂ₙ₊₁) + "
            "arctan(1/F₂ₙ₊₂), telescoping from arctan(1/F₂) = π/4 into Lehmer's "
            "series π/4 = ∑_{k=1}^∞ arctan(1/F₂ₖ₊₁)."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/fibpi.html#piandfib",
        knott_page_title="The Fibonacci Numbers in a Formula for Pi",
        knott_anchor="#piandfib",
        validator_qualname="geometor.knott.identities.construct_hayashi_arctan_grid_model",
        builder=construct_hayashi_arctan_grid_model,
        geometor_repos=("geometor/wildberger", "geometor/fundamentals"),
        citations=("KnottFibPi", "Lehmer1936"),
        persons=("knott", "lehmer", "euler", "fibonacci"),
        terms=("cassini-identity", "spread", "quadrance"),
    ),
    CatalogItemSpec(
        canonical_id="KNOTT-6.5",
        collection_slug="06-identities-and-bridges",
        order=5,
        item_slug="05-golden-angle-and-parastichy-bridges",
        folio_id="knott-6-5",
        title="Golden Angle (360° / Φ² ≈ 137.50776°) & Parastichy Bridges",
        enunciation=(
            "Dividing a full turn in extreme and mean ratio yields the Golden Angle "
            "2π / Φ² = 2π φ² ≈ 137.50776°, whose cylindrical primordia satisfy "
            "Fₖ φ² − Fₖ₋₂ = (−φ)ᵏ, pairing opposing left- and right-handed parastichy "
            "spirals in consecutive Fibonacci numbers (Fₖ, Fₖ₊₁)."
        ),
        knott_url="https://r-knott.surrey.ac.uk/Fibonacci/fibnat.html#seeds",
        knott_page_title="Fibonacci Numbers and Nature",
        knott_anchor="#seeds",
        validator_qualname="geometor.knott.identities.construct_parastichy_lattice_model",
        builder=construct_parastichy_lattice_model,
        geometor_repos=(
            "geometor/phyllotaxis",
            "geometor/thompson",
            "geometor/fibonacci",
            "geometor/pacioli",
            "geometor/divine",
        ),
        citations=("KnottNature", "Coxeter1973", "Thompson1917"),
        persons=("knott", "coxeter", "thompson", "pacioli", "fibonacci"),
        terms=("golden-angle", "parastichy", "golden-ratio"),
    ),
)


def get_catalog_item(canonical_id: str) -> CatalogItemSpec:
    """Look up a :class:`CatalogItemSpec` by its ``canonical_id`` (e.g., ``"KNOTT-1.1"``).

    Args:
        canonical_id: Canonical catalog ID.

    Returns:
        Matching :class:`CatalogItemSpec`.

    Raises:
        KeyError: If ``canonical_id`` is not registered.
    """
    for item in CATALOG_ITEMS:
        if item.canonical_id == canonical_id:
            return item
    raise KeyError(f"Unknown catalog item ID: {canonical_id!r}")


def verify_all_catalog_items() -> dict[str, GeometricCatalogResult]:
    """Execute and verify all 22 catalog item builders (`0` ``sp.Float`` atoms).

    Returns:
        Mapping ``{canonical_id: GeometricCatalogResult}`` across ``KNOTT-1.1`` .. ``KNOTT-6.5``.
    """
    results: dict[str, GeometricCatalogResult] = {}
    for item in CATALOG_ITEMS:
        res = item.builder()
        if res.canonical_id != item.canonical_id:  # pragma: no cover
            raise AssertionError(f"ID mismatch: {res.canonical_id} != {item.canonical_id}")
        assert_no_floats(res.model)
        assert_no_floats(res.invariants)
        results[item.canonical_id] = res
    return results


def build_manifest_payload() -> dict[str, object]:
    """Build the serializable dictionary written to ``resources/catalog_manifest.json``.

    Returns:
        Structured JSON-serializable catalog manifest dictionary.
    """
    return {
        "catalog_name": "GEOMETOR Knott Mathematical Catalog",
        "package": "geometor-knott",
        "kind": "mathematical-catalog",
        "curated_source": {
            "title": "Fibonacci Numbers, the Golden Section and the Golden String",
            "author": "Dr. Ron Knott",
            "institution": "University of Surrey",
            "hub_url": "https://r-knott.surrey.ac.uk/Fibonacci/fib.html",
            "copyright": KNOTT_COPYRIGHT,
            "notation_bridge": {
                "knott_PHI": "(1 + sqrt(5)) / 2 == sp.GoldenRatio (~1.6180339887)",
                "knott_phi": "(sqrt(5) - 1) / 2 == PHI - 1 == 1 / PHI == 1 / sp.GoldenRatio (~0.6180339887)",
            },
        },
        "collections": [
            {
                "order": col.order,
                "slug": col.slug,
                "code_prefix": col.code_prefix,
                "title": col.title,
                "enunciation": col.enunciation,
                "source_pages": list(col.source_pages),
            }
            for col in COLLECTIONS
        ],
        "items": [
            {
                "canonical_id": item.canonical_id,
                "collection_slug": item.collection_slug,
                "order": item.order,
                "item_slug": item.item_slug,
                "doc_path": f"catalog/{item.collection_slug}/{item.item_slug}/index.rst",
                "svg_graphic_id": f"{item.folio_id}.g1",
                "svg_path": f"catalog/{item.collection_slug}/{item.item_slug}/{item.folio_id}.g1.svg",
                "title": item.title,
                "theorem_enunciation": item.enunciation,
                "knott_source_url": item.knott_url,
                "knott_page_title": item.knott_page_title,
                "knott_section_anchor": item.knott_anchor,
                "copyright_attribution": KNOTT_COPYRIGHT,
                "validator_function": item.validator_qualname,
                "geometor_cross_references": list(item.geometor_repos),
                "citations": list(item.citations),
                "persons": list(item.persons),
                "terms": list(item.terms),
            }
            for item in CATALOG_ITEMS
        ],
    }


def export_catalog_manifest(output_path: Path) -> Path:
    """Write ``resources/catalog_manifest.json`` with deterministic UTF-8 formatting.

    Args:
        output_path: Destination JSON file path.

    Returns:
        Resolved ``output_path``.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = build_manifest_payload()
    output_path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return output_path
