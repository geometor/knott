"""Collection 1: 2D Golden Geometry & Constructions (`KNOTT-1.1` through `KNOTT-1.6`).

Catalogs the planar compass-and-straightedge constructions, self-similar triangles,
pentagonal star-chord progressions, Kepler right triangles, and Penrose aperiodic
prototiles curated by Dr. Ron Knott on ``phi2DGeomTrig.html``.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.knott.constants import (
    PHI,
    SQRT5,
    assert_no_floats,
    assert_zero,
    cross_ratio,
    phi,
    polygon_signed_area,
    quadrance,
    simplify_exact,
    spread,
)


@dataclass(frozen=True)
class GeometricCatalogResult:
    """Verified exact symbolic model and invariant summary for a catalog item."""

    canonical_id: str
    model: Model
    invariants: dict[str, sp.Expr]


def construct_golden_section_segment() -> GeometricCatalogResult:
    r"""Construct `KNOTT-1.1`: Internal and external golden sections on segment ``AB``.

    Models both classical Euclidean constructions on segment ``AB`` of length ``2``:

    1. **External extension**: From square ``ABCD`` and midpoint ``M`` of ``AB``, circle
       ``(M, C)`` of radius :math:`\sqrt{5}` meets line ``[AB]`` at ``E``, yielding
       :math:`AE / AB = AB / BE = \Phi` and Golden Rectangle ``AEFD``.
    2. **Internal division**: Joining ``A`` to midpoint ``H`` of ``BC``, circle ``(H, B)``
       cuts ``AH`` at ``K`` (:math:`AK = 2\phi`), and circle ``(A, K)`` cuts ``AB`` at
       the internal golden section ``G`` (:math:`AB / AG = AG / GB = \Phi`).

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-1.1``.
    """
    model = Model("knott-1-1", logger=False, auto_intersect=False)
    pt_a = model.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_b = model.given_point(sp.Integer(2), sp.Integer(0), ID="B")
    pt_c = model.set_point(sp.Integer(2), sp.Integer(2), ID="C", classes=["given"])
    pt_d = model.set_point(sp.Integer(0), sp.Integer(2), ID="D", classes=["given"])
    pt_m = model.set_point(sp.Integer(1), sp.Integer(0), ID="M")
    pt_h = model.set_point(sp.Integer(2), sp.Integer(1), ID="H")

    line_ab = model.construct_line(pt_a, pt_b, guide=True)
    model.set_polygon([pt_a, pt_b, pt_c, pt_d])
    seg_mc = model.set_segment(pt_m, pt_c, classes=["guide"], guide=True)
    del seg_mc

    circ_mc = model.construct_circle(pt_m, pt_c, classes=["guide"], guide=True)
    pt_e = model.intersect(
        line_ab,
        circ_mc,
        beyond=(pt_a, pt_b),
        ID="E",
        classes=["golden"],
        by="II.11",
    )
    pt_f = model.set_point(pt_e.x, sp.Integer(2), ID="F", classes=["golden"])
    model.set_polygon([pt_a, pt_e, pt_f, pt_d], classes=["golden"])
    model.set_segment(pt_a, pt_e, classes=["golden"])
    model.set_segment(pt_b, pt_e, classes=["golden"])
    model.set_segment(pt_m, pt_c)

    seg_ah = model.set_segment(pt_a, pt_h)
    circ_hb = model.construct_circle(pt_h, pt_b, classes=["guide"], guide=True)
    pt_k = model.intersect(
        seg_ah,
        circ_hb,
        between=(pt_a, pt_h),
        ID="K",
        classes=["golden"],
    )
    circ_ak = model.construct_circle(pt_a, pt_k, classes=["guide"], guide=True)
    pt_g = model.intersect(
        line_ab,
        circ_ak,
        between=(pt_a, pt_b),
        ID="G",
        classes=["golden"],
        by="VI.30",
    )
    model.set_segment(pt_a, pt_g, classes=["golden"])
    model.set_segment(pt_g, pt_b)

    len_ab = sp.sqrt(quadrance(pt_a, pt_b))
    len_ag = sp.sqrt(quadrance(pt_a, pt_g))
    len_gb = sp.sqrt(quadrance(pt_g, pt_b))
    len_ae = sp.sqrt(quadrance(pt_a, pt_e))
    len_be = sp.sqrt(quadrance(pt_b, pt_e))

    assert_zero(simplify_exact(len_ab / len_ag) - PHI, "AB / AG == PHI")
    assert_zero(simplify_exact(len_ag / len_gb) - PHI, "AG / GB == PHI")
    assert_zero(simplify_exact(len_ae / len_ab) - PHI, "AE / AB == PHI")
    assert_zero(simplify_exact(len_ab / len_be) - PHI, "AB / BE == PHI")
    cr_agbe = cross_ratio(pt_a, pt_e, pt_g, pt_b)
    assert_zero(cr_agbe - phi**2, "cross_ratio(A, E; G, B) == phi^2")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-1.1",
        model=model,
        invariants={
            "AB": simplify_exact(len_ab),
            "AG": simplify_exact(len_ag),
            "GB": simplify_exact(len_gb),
            "AE": simplify_exact(len_ae),
            "internal_ratio_AB_over_AG": simplify_exact(len_ab / len_ag),
            "external_ratio_AE_over_AB": simplify_exact(len_ae / len_ab),
            "cross_ratio_A_E_G_B": cr_agbe,
        },
    )


def construct_golden_rectangles_and_spiral() -> GeometricCatalogResult:
    r"""Construct `KNOTT-1.2`: Golden rectangle, :math:`\sqrt{5}` rectangle, & whirling squares.

    Surrounding unit square ``ABCD`` with midpoint circle ``(M, C)`` constructs both
    right golden rectangle ``AEFD`` (:math:`\Phi \times 1`) and full :math:`\sqrt{5} \times 1`
    rectangle ``WEFN``. Subdividing gnomon ``BEFC`` into whirling squares demonstrates
    that main diagonal ``[AF]`` and gnomon diagonal ``[EC]`` intersect orthogonally
    (exact spread :math:`s = 1`) at the logarithmic spiral pole ``P``.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-1.2``.
    """
    model = Model("knott-1-2", logger=False, auto_intersect=False)
    pt_a = model.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_b = model.given_point(sp.Integer(1), sp.Integer(0), ID="B")
    pt_c = model.set_point(sp.Integer(1), sp.Integer(1), ID="C", classes=["given"])
    pt_d = model.set_point(sp.Integer(0), sp.Integer(1), ID="D", classes=["given"])
    pt_m = model.set_point(sp.Rational(1, 2), sp.Integer(0), ID="M")

    line_ab = model.construct_line(pt_a, pt_b, guide=True)
    circ_mc = model.construct_circle(pt_m, pt_c, classes=["guide"], guide=True)

    pt_e = model.intersect(line_ab, circ_mc, beyond=(pt_a, pt_b), ID="E", classes=["golden"])
    pt_w = model.intersect(line_ab, circ_mc, beyond=(pt_b, pt_a), ID="W", classes=["golden"])
    pt_f = model.set_point(pt_e.x, sp.Integer(1), ID="F", classes=["golden"])
    pt_n = model.set_point(pt_w.x, sp.Integer(1), ID="N", classes=["golden"])

    model.set_polygon([pt_w, pt_e, pt_f, pt_n])
    model.set_polygon([pt_a, pt_b, pt_c, pt_d], classes=["given"])
    model.set_polygon([pt_b, pt_e, pt_f, pt_c], classes=["golden"])

    # Whirling-square cuts inside gnomon BEFC:
    # Step 1: square B E G1 G2 of side phi at bottom, leaving [1, PHI] x [phi, 1] at top
    pt_g1 = model.set_point(PHI, phi, ID="G1", classes=["golden"])
    pt_g2 = model.set_point(sp.Integer(1), phi, ID="G2", classes=["golden"])
    model.set_segment(pt_g2, pt_g1, classes=["golden"])

    # Step 2: square H1 G1 F H2 of side phi^2 at right (x in [2*phi, PHI])
    pt_h1 = model.set_point(2 * phi, phi, ID="H1")
    pt_h2 = model.set_point(2 * phi, sp.Integer(1), ID="H2")
    model.set_segment(pt_h1, pt_h2)

    # Step 3: square H1 H2 C? No, remaining left top rectangle is [1, 2*phi] x [phi, 1] (phi^3 x phi^2);
    # cut square of side phi^3 at top: y in [1 - phi^3, 1] = [2*phi, 1]? Wait: 1 - phi^3 = 2*phi - 1 + ... = phi + phi^2?
    # Let's check: 1 - phi^3 = 1 - (2*phi - 1) = 2 - 2*phi = 2*phi^2.
    pt_j1 = model.set_point(sp.Integer(1), 1 - phi**3, ID="J1")
    pt_j2 = model.set_point(2 * phi, 1 - phi**3, ID="J2")
    model.set_segment(pt_j1, pt_j2)

    line_af = model.construct_line(pt_a, pt_f, guide=True)
    line_ec = model.construct_line(pt_e, pt_c, guide=True)
    pt_p = model.intersect(line_af, line_ec, ID="P", classes=["golden"])

    seg_af = model.set_segment(pt_a, pt_f, classes=["golden"])
    seg_ec = model.set_segment(pt_e, pt_c, classes=["golden"])
    model.set_segment(pt_w, pt_e)

    width_we = simplify_exact(pt_e.x - pt_w.x)
    diag_spread = spread(seg_af, seg_ec)

    assert_zero(width_we - SQRT5, "sqrt(5) rectangle width == sqrt(5)")
    assert_zero(diag_spread - 1, "AF perpendicular to EC (spread == 1)")
    # Verify G2 lies on AF and H1 lies on EC (self-similar whirling pole):
    assert_zero(pt_g2.y - phi * pt_g2.x, "G2 collinear with AF")
    assert_zero((pt_h1.y - 1) + PHI * (pt_h1.x - 1), "H1 collinear with EC")
    assert_zero(pt_p.x - PHI**2 / SQRT5, "pole x == PHI^2 / sqrt(5)")
    assert_zero(pt_p.y - PHI / SQRT5, "pole y == PHI / sqrt(5)")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-1.2",
        model=model,
        invariants={
            "golden_rect_width": simplify_exact(pt_e.x - pt_a.x),
            "sqrt5_rect_width": width_we,
            "diagonal_spread": diag_spread,
            "pole_x": simplify_exact(pt_p.x),
            "pole_y": simplify_exact(pt_p.y),
            "gnomon_area": polygon_signed_area([pt_b, pt_e, pt_f, pt_c]),
        },
    )


def construct_golden_triangles_and_gnomons() -> GeometricCatalogResult:
    r"""Construct `KNOTT-1.3`: Acute golden triangle (:math:`72^\circ\text{-}72^\circ\text{-}36^\circ`) & gnomon deflation.

    Constructs acute golden triangle ``ABC`` (:math:`AB = 1, AC = BC = \Phi`) and
    intersects leg ``BC`` with unit circle ``(A, B)`` at ``D``, partitioning ``ABC``
    into obtuse golden gnomon ``CAD`` (:math:`36^\circ\text{-}36^\circ\text{-}108^\circ`,
    legs ``1``) and deflated acute golden triangle ``DAB`` (:math:`AB = AD = 1, BD = \phi`),
    followed by a second deflation step at ``E`` on ``AB``.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-1.3``.
    """
    model = Model("knott-1-3", logger=False, auto_intersect=False)
    pt_a = model.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_b = model.given_point(sp.Integer(1), sp.Integer(0), ID="B")
    pt_r = model.set_point(PHI, sp.Integer(0), ID="R", guide=True)
    pt_l = model.set_point(1 - PHI, sp.Integer(0), ID="L", guide=True)

    circ_ar = model.construct_circle(pt_a, pt_r, classes=["guide"], guide=True)
    circ_bl = model.construct_circle(pt_b, pt_l, classes=["guide"], guide=True)
    pt_c = model.intersect(
        circ_ar,
        circ_bl,
        side_of=(pt_a, pt_b, 1),
        ID="C",
        classes=["golden"],
    )

    model.set_polygon([pt_a, pt_b, pt_c])
    seg_ab = model.set_segment(pt_a, pt_b, classes=["given"])
    seg_ac = model.set_segment(pt_a, pt_c, classes=["golden"])
    seg_bc = model.set_segment(pt_b, pt_c, classes=["golden"])

    circ_ab = model.construct_circle(pt_a, pt_b, classes=["guide"], guide=True)
    pt_d = model.intersect(
        seg_bc,
        circ_ab,
        other_than=pt_b,
        ID="D",
        classes=["golden"],
        by="IV.10",
    )
    seg_ad = model.set_segment(pt_a, pt_d, classes=["golden"])
    model.set_polygon([pt_a, pt_b, pt_d], classes=["golden"])

    circ_db = model.construct_circle(pt_d, pt_b, classes=["guide"], guide=True)
    pt_e = model.intersect(
        seg_ab,
        circ_db,
        other_than=pt_b,
        ID="E",
        classes=["golden"],
    )
    model.set_segment(pt_d, pt_e, classes=["golden"])

    q_ac = quadrance(pt_a, pt_c)
    q_ad = quadrance(pt_a, pt_d)
    q_cd = quadrance(pt_c, pt_d)
    q_bd = quadrance(pt_b, pt_d)
    q_be = quadrance(pt_b, pt_e)
    s_base_72 = spread(seg_ab, seg_ac)
    s_apex_36 = spread(seg_ac, seg_bc)
    s_gnomon_108 = spread(seg_ad, seg_bc)

    assert_zero(q_ac - PHI**2, "Q(A, C) == PHI^2")
    assert_zero(q_ad - 1, "Q(A, D) == 1")
    assert_zero(q_cd - 1, "Q(C, D) == 1")
    assert_zero(q_bd - phi**2, "Q(B, D) == phi^2")
    assert_zero(q_be - phi**4, "Q(B, E) == phi^4")
    assert_zero(s_base_72 - (5 + SQRT5) / 8, "spread(72 deg) == (5 + sqrt(5))/8")
    assert_zero(s_apex_36 - (5 - SQRT5) / 8, "spread(36 deg) == (5 - sqrt(5))/8")
    assert_zero(s_gnomon_108 - s_base_72, "spread(108 deg) == spread(72 deg)")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-1.3",
        model=model,
        invariants={
            "Q_AC": q_ac,
            "Q_AD": q_ad,
            "Q_BD": q_bd,
            "Q_BE": q_be,
            "spread_36_deg": s_apex_36,
            "spread_72_deg": s_base_72,
            "area_ratio_ABC_to_DAB": simplify_exact(
                polygon_signed_area([pt_a, pt_b, pt_c]) / polygon_signed_area([pt_d, pt_a, pt_b])
            ),
        },
    )


def construct_pentagon_and_paper_knot() -> GeometricCatalogResult:
    r"""Construct `KNOTT-1.4`: Regular pentagon, pentagram :math:`1:\Phi:\Phi^2:\Phi^3` chords, & paper knot.

    Constructs regular pentagon ``P0 P1 P2 P3 P4`` of unit side, intersects its five
    pentagram diagonals to form inner pentagon ``Q0 Q1 Q2 Q3 Q4``, verifies the four-step
    golden geometric progression along ``P0 P2``, and drops perpendicular ``P4 H`` onto
    ``[P0 P1]`` to prove Dr. Ron Knott's overhand paper-strip knot theorem: two crossing
    parallel-sided strips of width :math:`w = P_4 H = \sin 72^\circ` lock into an exact
    regular pentagon of side :math:`w \sec 18^\circ`.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-1.4``.
    """
    model = Model("knott-1-4", logger=False, auto_intersect=False)
    p0 = model.given_point(sp.Integer(0), sp.Integer(0), ID="P0")
    p1 = model.given_point(sp.Integer(1), sp.Integer(0), ID="P1")
    r_p0 = model.set_point(PHI, sp.Integer(0), ID="R0", guide=True)
    r_p1 = model.set_point(1 - PHI, sp.Integer(0), ID="R1", guide=True)

    c_p0_phi = model.construct_circle(p0, r_p0, classes=["guide"], guide=True)
    c_p1_phi = model.construct_circle(p1, r_p1, classes=["guide"], guide=True)
    c_p0_1 = model.construct_circle(p0, p1, classes=["guide"], guide=True)
    c_p1_1 = model.construct_circle(p1, p0, classes=["guide"], guide=True)

    p3 = model.intersect(c_p0_phi, c_p1_phi, side_of=(p0, p1, 1), ID="P3", classes=["golden"])
    p2 = model.intersect(c_p1_1, c_p0_phi, side_of=(p0, p1, 1), ID="P2", classes=["golden"])
    p4 = model.intersect(c_p0_1, c_p1_phi, side_of=(p0, p1, 1), ID="P4", classes=["golden"])

    model.set_polygon([p0, p1, p2, p3, p4])
    d_02 = model.set_segment(p0, p2, classes=["golden"])
    d_03 = model.set_segment(p0, p3)
    d_13 = model.set_segment(p1, p3)
    d_14 = model.set_segment(p1, p4)
    d_24 = model.set_segment(p2, p4)

    q0 = model.intersect(d_03, d_14, ID="Q0", classes=["golden"])
    q1 = model.intersect(d_02, d_14, ID="Q1", classes=["golden"])
    q2 = model.intersect(d_02, d_13, ID="Q2", classes=["golden"])
    q3 = model.intersect(d_13, d_24, ID="Q3", classes=["golden"])
    q4 = model.intersect(d_03, d_24, ID="Q4", classes=["golden"])
    model.set_polygon([q0, q1, q2, q3, q4], classes=["golden"])

    # Paper-knot strip altitude from P4 onto base line [P0 P1]:
    pt_h = model.set_point(p4.x, sp.Integer(0), ID="H")
    seg_strip_w = model.set_segment(p4, pt_h, classes=["golden"])
    seg_base = model.set_segment(p0, p1, classes=["given"])

    len_q1q2 = simplify_exact(sp.sqrt(quadrance(q1, q2)))
    len_p0q1 = simplify_exact(sp.sqrt(quadrance(p0, q1)))
    len_p0q2 = simplify_exact(sp.sqrt(quadrance(p0, q2)))
    len_p0p2 = simplify_exact(sp.sqrt(quadrance(p0, p2)))
    q_strip_width = quadrance(p4, pt_h)

    assert_zero(len_q1q2 - phi**2, "Q1Q2 == phi^2")
    assert_zero(len_p0q1 - phi, "P0Q1 == phi")
    assert_zero(len_p0q2 - 1, "P0Q2 == 1")
    assert_zero(len_p0p2 - PHI, "P0P2 == PHI")
    assert_zero(spread(seg_base, d_24), "paper strip edges [P0 P1] || [P4 P2]")
    assert_zero(spread(seg_base, seg_strip_w) - 1, "P4 H perpendicular to P0 P1")
    assert_zero(q_strip_width - (5 + SQRT5) / 8, "strip width^2 == sin^2(72 deg) == (5+sqrt(5))/8")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-1.4",
        model=model,
        invariants={
            "Q1Q2_crossbar": len_q1q2,
            "P0Q1_star_arm": len_p0q1,
            "P0Q2_pentagon_side": len_p0q2,
            "P0P2_diagonal": len_p0p2,
            "strip_width_quadrance": q_strip_width,
            "unit_strip_pentagon_side_quadrance": simplify_exact(sp.Integer(1) / q_strip_width),
        },
    )


def construct_kepler_triangle() -> GeometricCatalogResult:
    r"""Construct `KNOTT-1.5`: Kepler's golden right triangle :math:`(1, \sqrt{\Phi}, \Phi)` & near-quadrature.

    Uses Euclid's semicircle geometric-mean construction on ``DE`` (:math:`D=(-1,0),
    B=(0,0), E=(\Phi,0)`) to construct :math:`C=(0, \sqrt{\Phi})` by exact compass
    intersection over :math:`\mathbb{Q}(\sqrt{\Phi})`. In right triangle ``DBC``:

    - Side quadrances :math:`(Q(B,D), Q(B,C), Q(D,C)) = (1, \Phi, \Phi^2)` form a
      geometric progression AND satisfy Pythagoras :math:`1 + \Phi = \Phi^2`;
    - The square ``BCFG`` on leg ``BC`` has perimeter :math:`4\sqrt{\Phi} \approx 5.08808`,
      while the Thales circle ``(M, C)`` on hypotenuse ``CD`` has circumference
      :math:`\pi\Phi \approx 5.08320` (agreement within :math:`0.096\%`).

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-1.5``.
    """
    model = Model("knott-1-5", logger=False, auto_intersect=False)
    pt_d = model.given_point(sp.Integer(-1), sp.Integer(0), ID="D")
    pt_b = model.given_point(sp.Integer(0), sp.Integer(0), ID="B")
    pt_e = model.given_point(PHI, sp.Integer(0), ID="E", classes=["golden"])
    pt_o = model.set_point((PHI - 1) / 2, sp.Integer(0), ID="O", guide=True)
    pt_y = model.set_point(sp.Integer(0), sp.Integer(1), ID="Y0", guide=True)

    line_de = model.construct_line(pt_d, pt_e, guide=True)
    del line_de
    line_by = model.construct_line(pt_b, pt_y, guide=True)
    circ_oe = model.construct_circle(pt_o, pt_e, classes=["guide"], guide=True)

    pt_c = model.intersect(
        line_by,
        circ_oe,
        side_of=(pt_d, pt_e, 1),
        ID="C",
        classes=["golden"],
        by="VI.13",
    )

    # Kepler right triangle D B C:
    model.set_polygon([pt_d, pt_b, pt_c], classes=["golden"])
    seg_bd = model.set_segment(pt_b, pt_d, classes=["given"])
    seg_bc = model.set_segment(pt_b, pt_c, classes=["golden"])
    seg_dc = model.set_segment(pt_d, pt_c, classes=["golden"])
    model.set_segment(pt_c, pt_e)
    model.set_segment(pt_b, pt_e)

    # Square B C F G of side sqrt(PHI) vs Thales circle (M, C) on diameter CD (length PHI):
    sqrt_phi = pt_c.y
    pt_f = model.set_point(sqrt_phi, sqrt_phi, ID="F")
    pt_g = model.set_point(sqrt_phi, sp.Integer(0), ID="G")
    model.set_polygon([pt_b, pt_g, pt_f, pt_c])

    pt_m = model.set_point((pt_d.x + pt_c.x) / 2, (pt_d.y + pt_c.y) / 2, ID="M", classes=["golden"])
    model.construct_circle(pt_m, pt_c, classes=["golden"])

    q_bd = quadrance(pt_b, pt_d)
    q_bc = quadrance(pt_b, pt_c)
    q_dc = quadrance(pt_d, pt_c)
    s_right = spread(seg_bd, seg_bc)
    s_base_d = spread(seg_bd, seg_dc)
    s_apex_c = spread(seg_bc, seg_dc)

    assert_zero(q_bd - 1, "Q(B, D) == 1")
    assert_zero(q_bc - PHI, "Q(B, C) == PHI")
    assert_zero(q_dc - PHI**2, "Q(D, C) == PHI^2")
    assert_zero(q_bd + q_bc - q_dc, "Pythagoras 1 + PHI == PHI^2")
    assert_zero(q_bc**2 - q_bd * q_dc, "Geometric progression Q_BC^2 == Q_BD * Q_DC")
    assert_zero(s_right - 1, "Right angle at B")
    # At apex C (theta_C ~ 38.17 deg), cos(theta_C) == tan(theta_C) == sin(theta_D) == 1 / sqrt(PHI):
    cos_c_sq = simplify_exact(1 - s_apex_c)
    tan_c_sq = simplify_exact(s_apex_c / (1 - s_apex_c))
    assert_zero(s_base_d - phi, "sin^2(theta_D) == phi == 1/PHI")
    assert_zero(cos_c_sq - phi, "cos^2(theta_C) == phi == 1/PHI")
    assert_zero(tan_c_sq - phi, "tan^2(theta_C) == phi == 1/PHI")
    assert_no_floats(model)

    square_perim = 4 * sp.sqrt(PHI)
    circle_circum = sp.pi * PHI

    return GeometricCatalogResult(
        canonical_id="KNOTT-1.5",
        model=model,
        invariants={
            "Q_leg_short": q_bd,
            "Q_leg_long": q_bc,
            "Q_hypotenuse": q_dc,
            "spread_acute_D": s_base_d,
            "spread_apex_C": s_apex_c,
            "cos_sq_equals_tan_sq_C": cos_c_sq,
            "square_perimeter": square_perim,
            "circle_circumference": circle_circum,
            "quadrature_ratio": square_perim / circle_circum,
        },
    )


def construct_penrose_tiles() -> GeometricCatalogResult:
    r"""Construct `KNOTT-1.6`: Penrose kites & darts (:math:`P2`) and thick/thin golden rhombs (:math:`P3`).

    Constructs thick Penrose golden rhomb ``ABCD`` (:math:`72^\circ / 108^\circ`, side :math:`\Phi`),
    intersects diagonal ``AC`` with unit circle ``(A, U)`` at ``K`` to partition ``ABCD``
    into Penrose dart ``ABKD`` (non-convex :math:`216^\circ` reflex at ``K``) and Penrose
    kite ``KBCD`` (:math:`72^\circ, 72^\circ, 72^\circ, 144^\circ`), and adjoins thin
    Penrose golden rhomb ``ABEF`` (:math:`36^\circ / 144^\circ`, side :math:`\Phi`).
    Proves both exact area ratios equal :math:`\Phi : 1`.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-1.6``.
    """
    model = Model("knott-1-6", logger=False, auto_intersect=False)
    sin_36 = sp.sqrt(10 - 2 * SQRT5) / 4
    sin_72 = sp.sqrt(10 + 2 * SQRT5) / 4

    pt_a = model.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    pt_b = model.given_point(PHI, sp.Integer(0), ID="B")
    # Thick rhomb ABCD (angles 72 deg at A, C; 108 deg at B, D; side PHI):
    # PHI * cos(72 deg) = PHI * (phi / 2) = 1 / 2
    pt_d = model.set_point(sp.Rational(1, 2), PHI * sin_72, ID="D", classes=["golden"])
    pt_c = model.set_point(PHI + sp.Rational(1, 2), PHI * sin_72, ID="C", classes=["golden"])

    seg_ac = model.set_segment(pt_a, pt_c, classes=["guide"], guide=True)
    pt_u = model.set_point(sp.Integer(1), sp.Integer(0), ID="U", guide=True)
    circ_au = model.construct_circle(pt_a, pt_u, classes=["guide"], guide=True)
    pt_k = model.intersect(
        seg_ac,
        circ_au,
        between=(pt_a, pt_c),
        ID="K",
        classes=["golden"],
    )

    # Penrose Kite KBCD and Penrose Dart ABKD inside Thick Rhomb ABCD:
    model.set_polygon([pt_k, pt_b, pt_c, pt_d], classes=["golden"])
    model.set_polygon([pt_a, pt_b, pt_k, pt_d])
    model.set_segment(pt_a, pt_b, classes=["given"])
    model.set_segment(pt_b, pt_c, classes=["golden"])
    model.set_segment(pt_c, pt_d, classes=["golden"])
    model.set_segment(pt_d, pt_a)
    model.set_segment(pt_b, pt_k, classes=["golden"])
    model.set_segment(pt_d, pt_k, classes=["golden"])
    model.set_segment(pt_a, pt_k)
    model.set_segment(pt_k, pt_c, classes=["golden"])

    # Thin Penrose Rhomb ABEF below AB (angle -36 deg, side PHI):
    # PHI * cos(36 deg) = PHI * (PHI / 2) = PHI^2 / 2 = (PHI + 1) / 2
    pt_f = model.set_point((PHI + 1) / 2, -PHI * sin_36, ID="F")
    pt_e = model.set_point(PHI + (PHI + 1) / 2, -PHI * sin_36, ID="E")
    model.set_polygon([pt_a, pt_f, pt_e, pt_b])
    model.set_segment(pt_a, pt_f)
    model.set_segment(pt_f, pt_e)
    model.set_segment(pt_e, pt_b)

    area_kite = polygon_signed_area([pt_k, pt_b, pt_c, pt_d])
    area_dart = polygon_signed_area([pt_a, pt_b, pt_k, pt_d])
    area_thick = polygon_signed_area([pt_a, pt_b, pt_c, pt_d])
    area_thin = polygon_signed_area([pt_a, pt_f, pt_e, pt_b])

    assert_zero(quadrance(pt_a, pt_b) - PHI**2, "Q(A, B) == PHI^2")
    assert_zero(quadrance(pt_a, pt_d) - PHI**2, "Q(A, D) == PHI^2")
    assert_zero(quadrance(pt_b, pt_k) - 1, "Q(B, K) == 1")
    assert_zero(quadrance(pt_d, pt_k) - 1, "Q(D, K) == 1")
    assert_zero(quadrance(pt_k, pt_c) - PHI**2, "Q(K, C) == PHI^2")
    assert_zero(quadrance(pt_a, pt_f) - PHI**2, "Q(A, F) == PHI^2")
    assert_zero(simplify_exact(area_kite / area_dart) - PHI, "Area(Kite) / Area(Dart) == PHI")
    assert_zero(simplify_exact(area_thick / area_thin) - PHI, "Area(Thick) / Area(Thin) == PHI")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-1.6",
        model=model,
        invariants={
            "Q_rhomb_side": quadrance(pt_a, pt_b),
            "Q_dart_short_edge": quadrance(pt_b, pt_k),
            "Q_kite_spine_KC": quadrance(pt_k, pt_c),
            "kite_to_dart_area_ratio": simplify_exact(area_kite / area_dart),
            "thick_to_thin_rhomb_area_ratio": simplify_exact(area_thick / area_thin),
            "spread_thick_72": spread(
                spg.Segment(pt_a, pt_b),
                spg.Segment(pt_a, pt_d),
            ),
            "spread_thin_36": spread(
                spg.Segment(pt_a, pt_b),
                spg.Segment(pt_a, pt_f),
            ),
        },
    )
