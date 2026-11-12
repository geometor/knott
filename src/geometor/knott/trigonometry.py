r"""Collection 2: Exact Pentagonal & Constructible Trigonometry (`KNOTT-2.1` – `KNOTT-2.2`).

Catalogs closed-form radical sines, cosines, tangents, and Rational Trigonometry
spreads for the pentagonal family (:math:`18^\circ, 36^\circ, 54^\circ, 72^\circ`),
the complete 29-angle :math:`3^\circ k` constructible lattice (:math:`k = 1\dots 29`),
and Gauss's regular 17-gon cosine curated by Dr. Ron Knott on ``simpleTrig.html``
and ``phi2DGeomTrig.html``.
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
    phi,
    quadrance,
    simplify_exact,
    spread,
)
from geometor.knott.flat_geometry import GeometricCatalogResult


@dataclass(frozen=True)
class ExactAngleEntry:
    r"""Exact closed-form trigonometric invariants for a constructible angle."""

    degrees: int
    radians: sp.Expr
    sin: sp.Expr
    cos: sp.Expr
    tan: sp.Expr
    spread: sp.Expr


def pentagonal_trig_table() -> dict[int, ExactAngleEntry]:
    r"""Return exact radical trigonometric entries for :math:`18^\circ, 36^\circ, 54^\circ, 72^\circ`.

    Verifies every entry against :math:`\sin^2 + \cos^2 = 1`, :math:`\cos 36^\circ - \sin 18^\circ = 1/2`,
    :math:`\cos 36^\circ \cdot \sin 18^\circ = 1/4`, and Wildberger's 5-fold spread polynomial
    :math:`S_5(s) = s(16 s^2 - 20 s + 5)^2 = 0` for :math:`36^\circ` and :math:`72^\circ`.

    Returns:
        Mapping ``{18: ..., 36: ..., 54: ..., 72: ...}`` of verified :class:`ExactAngleEntry` records.
    """
    sin_18 = phi / 2
    cos_18 = sp.sqrt(10 + 2 * SQRT5) / 4
    tan_18 = sp.sqrt(25 - 10 * SQRT5) / 5

    sin_36 = sp.sqrt(10 - 2 * SQRT5) / 4
    cos_36 = PHI / 2
    tan_36 = sp.sqrt(5 - 2 * SQRT5)

    sin_54 = PHI / 2
    cos_54 = sp.sqrt(10 - 2 * SQRT5) / 4
    tan_54 = sp.sqrt(25 + 10 * SQRT5) / 5

    sin_72 = sp.sqrt(10 + 2 * SQRT5) / 4
    cos_72 = phi / 2
    tan_72 = sp.sqrt(5 + 2 * SQRT5)

    raw = {
        18: (sin_18, cos_18, tan_18, (3 - SQRT5) / 8),
        36: (sin_36, cos_36, tan_36, (5 - SQRT5) / 8),
        54: (sin_54, cos_54, tan_54, (3 + SQRT5) / 8),
        72: (sin_72, cos_72, tan_72, (5 + SQRT5) / 8),
    }

    table: dict[int, ExactAngleEntry] = {}
    for deg, (s_val, c_val, t_val, sp_val) in raw.items():
        assert_zero(s_val**2 + c_val**2 - 1, f"Pythagorean identity at {deg} deg")
        assert_zero(s_val**2 - sp_val, f"spread == sin^2 at {deg} deg")
        assert_zero(t_val**2 * c_val**2 - s_val**2, f"tan == sin/cos at {deg} deg")
        table[deg] = ExactAngleEntry(
            degrees=deg,
            radians=sp.Rational(deg, 180) * sp.pi,
            sin=s_val,
            cos=c_val,
            tan=t_val,
            spread=simplify_exact(sp_val),
        )

    # Verify Wildberger pentagonal spread polynomial S_5(s) = s * (16*s^2 - 20*s + 5)^2 == 0:
    for deg in (36, 72):
        s_pent = table[deg].spread
        assert_zero(16 * s_pent**2 - 20 * s_pent + 5, f"Wildberger S_5 root at {deg} deg")

    assert_zero(table[36].cos - table[72].cos - sp.Rational(1, 2), "cos 36 - cos 72 == 1/2")
    assert_zero(table[36].cos * table[72].cos - sp.Rational(1, 4), "cos 36 * cos 72 == 1/4")
    return table


def construct_pentagonal_trig_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-2.1`: First-quadrant unit circle pentagonal rays & golden projections.

    Places rays at :math:`18^\circ, 36^\circ, 54^\circ, 72^\circ` on unit circle ``(O, U)``
    and drops perpendiculars ``C36`` (:math:`x = \Phi/2`) and ``C72`` (:math:`x = \phi/2`)
    onto ``[O U]``, demonstrating :math:`OC_{36} - OC_{72} = 1/2` and
    :math:`OC_{36} \cdot OC_{72} = 1/4`.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-2.1``.
    """
    table = pentagonal_trig_table()
    model = Model("knott-2-1", logger=False, auto_intersect=False)

    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    pt_u = model.given_point(sp.Integer(1), sp.Integer(0), ID="U")
    pt_v = model.set_point(sp.Integer(0), sp.Integer(1), ID="V", classes=["given"])
    model.construct_circle(pt_o, pt_u)
    seg_ou = model.set_segment(pt_o, pt_u, classes=["given"])
    model.set_segment(pt_o, pt_v, classes=["given"])

    p18 = model.set_point(table[18].cos, table[18].sin, ID="P18")
    p36 = model.set_point(table[36].cos, table[36].sin, ID="P36", classes=["golden"])
    p54 = model.set_point(table[54].cos, table[54].sin, ID="P54")
    p72 = model.set_point(table[72].cos, table[72].sin, ID="P72", classes=["golden"])

    c36 = model.set_point(table[36].cos, sp.Integer(0), ID="C36", classes=["golden"])
    c72 = model.set_point(table[72].cos, sp.Integer(0), ID="C72", classes=["golden"])

    r18 = model.set_segment(pt_o, p18)
    r36 = model.set_segment(pt_o, p36, classes=["golden"])
    r54 = model.set_segment(pt_o, p54)
    r72 = model.set_segment(pt_o, p72, classes=["golden"])

    model.set_segment(p36, c36, classes=["golden"])
    model.set_segment(p72, c72, classes=["golden"])
    model.set_segment(c72, c36, classes=["golden"])
    model.set_polygon([pt_o, c36, p36], classes=["golden"])

    assert_zero(quadrance(c72, c36) - sp.Rational(1, 4), "len(C72 C36) == 1/2")
    assert_zero(spread(seg_ou, r18) - table[18].spread, "ray 18 spread")
    assert_zero(spread(seg_ou, r36) - table[36].spread, "ray 36 spread")
    assert_zero(spread(seg_ou, r54) - table[54].spread, "ray 54 spread")
    assert_zero(spread(seg_ou, r72) - table[72].spread, "ray 72 spread")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-2.1",
        model=model,
        invariants={
            "cos_36": table[36].cos,
            "sin_18": table[18].sin,
            "spread_18": table[18].spread,
            "spread_36": table[36].spread,
            "spread_54": table[54].spread,
            "spread_72": table[72].spread,
            "projection_span_C72_C36": sp.sqrt(quadrance(c72, c36)),
        },
    )


def _quarter_turn_basis() -> tuple[dict[int, tuple[sp.Expr, sp.Expr]], dict[int, tuple[sp.Expr, sp.Expr]]]:
    r"""Return exact ``(sin, cos)`` bases for multiples of :math:`15^\circ` and :math:`18^\circ`."""
    rt2 = sp.sqrt(2)
    rt3 = sp.sqrt(3)
    pent = pentagonal_trig_table()

    mult15: dict[int, tuple[sp.Expr, sp.Expr]] = {
        0: (sp.Integer(0), sp.Integer(1)),
        15: ((rt6 := rt2 * rt3) / 4 - rt2 / 4, rt6 / 4 + rt2 / 4),
        30: (sp.Rational(1, 2), rt3 / 2),
        45: (rt2 / 2, rt2 / 2),
        60: (rt3 / 2, sp.Rational(1, 2)),
        75: (rt6 / 4 + rt2 / 4, rt6 / 4 - rt2 / 4),
        90: (sp.Integer(1), sp.Integer(0)),
    }
    mult18: dict[int, tuple[sp.Expr, sp.Expr]] = {
        0: (sp.Integer(0), sp.Integer(1)),
        18: (pent[18].sin, pent[18].cos),
        36: (pent[36].sin, pent[36].cos),
        54: (pent[54].sin, pent[54].cos),
        72: (pent[72].sin, pent[72].cos),
        90: (sp.Integer(1), sp.Integer(0)),
    }
    return mult15, mult18


def three_degree_lattice() -> dict[int, ExactAngleEntry]:
    r"""Compute closed-form radicals and spreads for all 29 angles :math:`3^\circ k` (:math:`k = 1\dots 29`).

    Decomposes every integer multiple of :math:`3^\circ` in :math:`(0^\circ, 90^\circ)`
    as a single sum or difference :math:`a \cdot 18^\circ \pm b \cdot 15^\circ` between the
    pentagonal subfield :math:`\mathbb{Q}(\sqrt{5}, \sqrt{10 \pm 2\sqrt{5}})` and the
    hexagonal/octagonal subfield :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})`.

    Returns:
        Ordered mapping ``{3: ..., 6: ..., ..., 87: ...}`` of 29 verified :class:`ExactAngleEntry` records.
    """
    mult15, mult18 = _quarter_turn_basis()

    # Choose minimal one-step decomposition (deg = p18 + sign * p15):
    decompositions: dict[int, tuple[int, int, int]] = {}
    for k in range(1, 30):
        deg = 3 * k
        best_pair: tuple[int, int, int] | None = None
        best_cost = 999
        for a18 in (0, 18, 36, 54, 72, 90):
            for b15 in (0, 15, 30, 45, 60, 75, 90):
                for sgn in (1, -1):
                    if a18 + sgn * b15 == deg:
                        # Prefer pure 15-multiples or pure 18-multiples, then 30/60 over 15/75:
                        cost = (0 if a18 == 0 or b15 == 0 else 2) + (0 if b15 in (0, 30, 60, 90) else 1)
                        if cost < best_cost:
                            best_cost = cost
                            best_pair = (a18, sgn, b15)
        if best_pair is None:  # pragma: no cover
            raise RuntimeError(f"No 18/15 decomposition found for {deg} deg")
        decompositions[deg] = best_pair

    lattice: dict[int, ExactAngleEntry] = {}
    for k in range(1, 30):
        deg = 3 * k
        a18, sgn, b15 = decompositions[deg]
        s_a, c_a = mult18[a18]
        s_b, c_b = mult15[b15]
        if sgn == 1:
            sin_val = sp.expand(s_a * c_b + c_a * s_b)
            cos_val = sp.expand(c_a * c_b - s_a * s_b)
        else:
            sin_val = sp.expand(s_a * c_b - c_a * s_b)
            cos_val = sp.expand(c_a * c_b + s_a * s_b)

        spread_val = simplify_exact(sp.expand(sin_val**2))
        tan_val = sin_val / cos_val

        # Verify unit-circle norm sin^2 + cos^2 == 1:
        assert_zero(sin_val**2 + cos_val**2 - 1, f"sin^2 + cos^2 == 1 at {deg} deg")
        assert_no_floats(sin_val)
        assert_no_floats(cos_val)
        assert_no_floats(spread_val)

        lattice[deg] = ExactAngleEntry(
            degrees=deg,
            radians=sp.Rational(deg, 180) * sp.pi,
            sin=sin_val,
            cos=cos_val,
            tan=tan_val,
            spread=spread_val,
        )

    # Verify the fundamental 3-degree generator via Chebyshev T_5(cos 3 deg) == cos 15 deg:
    p_rad = sp.sqrt(10 + 2 * SQRT5)
    s_p = sp.Symbol("s_p", positive=True)
    c3_sym = lattice[3].cos.subs(p_rad, s_p)
    u_prev: sp.Expr = sp.Integer(1)
    u_curr: sp.Expr = c3_sym
    for _ in range(2, 6):
        u_prev, u_curr = u_curr, sp.expand(2 * c3_sym * u_curr - u_prev).subs(
            s_p**2, 10 + 2 * SQRT5
        )
    assert_zero(sp.expand(u_curr) - lattice[15].cos, "T_5(cos 3 deg) == cos 15 deg")

    # Verify complementarity cos(90 - theta) == sin(theta) across all 29 entries:
    for k in range(1, 30):
        deg = 3 * k
        comp = 90 - deg
        assert_zero(lattice[deg].sin - lattice[comp].cos, f"sin({deg}) == cos({comp})")
        assert_zero(lattice[deg].spread + lattice[comp].spread - 1, f"s({deg}) + s({comp}) == 1")

    return lattice


def gauss_seventeen_gon_cosine() -> sp.Expr:
    r"""Return Gauss's exact nested quadratic radical for :math:`\cos(\pi / 17)` (1796).

    Cataloged by Dr. Ron Knott on ``simpleTrig.html#pi17`` as the Fermat-prime bridge
    beyond Euclid's :math:`2^a \cdot 3 \cdot 5` angle lattice. Verified algebraically via
    Chebyshev's polynomial :math:`T_{17}(\cos(\pi / 17)) + 1 = 0` reduced step-by-step in
    Gauss's quadratic field tower :math:`\mathbb{Q} \subset K_1 \subset K_2 \subset K_3 \subset K_4`.

    Returns:
        Exact radical expression for :math:`\cos(\pi / 17)`.
    """
    rt17 = sp.sqrt(17)
    a_rad = sp.sqrt(34 - 2 * rt17)
    c_rad = sp.sqrt(34 + 2 * rt17)
    b_rad = sp.sqrt(17 + 3 * rt17 - a_rad - 2 * c_rad)
    cos_2pi_17 = (-sp.Integer(1) + rt17 + a_rad + 2 * b_rad) / sp.Integer(16)
    cos_pi_17 = sp.sqrt((sp.Integer(1) + cos_2pi_17) / sp.Integer(2))

    # 1. Verify exact defining identities of the positive radical atoms:
    assert_zero(a_rad**2 * c_rad**2 - (8 * rt17) ** 2, "a_rad * c_rad == 8*sqrt(17)")
    assert_zero(2 * cos_pi_17**2 - 1 - cos_2pi_17, "2*cos^2(pi/17) - 1 == cos(2*pi/17)")

    # 2. Step-by-step Chebyshev T_17 reduction in the verified quadratic tower:
    s_r, s_a, s_c, s_b, s_y = sp.symbols("s_r s_a s_c s_b s_y", positive=True)
    x_sym = (-sp.Integer(1) + s_r + s_a + 2 * s_b) / sp.Integer(16)

    def _reduce_tower(poly_expr: sp.Expr) -> sp.Expr:
        cur = sp.expand(poly_expr)
        cur = sp.expand(cur.subs(s_y**2, (sp.Integer(1) + x_sym) / sp.Integer(2)))
        cur = sp.expand(cur.subs(s_b**2, 17 + 3 * s_r - s_a - 2 * s_c))
        cur = sp.expand(
            cur.subs(
                {
                    s_a**2: 34 - 2 * s_r,
                    s_c**2: 34 + 2 * s_r,
                    s_a * s_c: 8 * s_r,
                }
            )
        )
        return sp.expand(cur.subs(s_r**2, 17))

    t_prev: sp.Expr = sp.Integer(1)
    t_curr: sp.Expr = s_y
    for _ in range(2, 18):
        t_prev, t_curr = t_curr, _reduce_tower(2 * s_y * t_curr - t_prev)
    assert_zero(t_curr + 1, "Chebyshev T_17(cos(pi/17)) == -1")
    assert_no_floats(cos_pi_17)
    return cos_pi_17


def construct_three_degree_lattice_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-2.2`: Euclid IV.16 regular 15-gon superposition & :math:`3^\circ` lattice.

    Superimposes equilateral-triangle ray ``P60`` (:math:`60^\circ`, :math:`\mathbb{Q}(\sqrt{3})`)
    and pentagonal central ray ``P72`` (:math:`72^\circ`, :math:`\mathbb{Q}(\sqrt{5})`) on unit
    circle ``(O, U)`` to isolate the :math:`12^\circ` regular 15-gon arc ``P60 P72`` (and origin
    ray ``P12``), together with bisected rays ``P6`` (:math:`6^\circ`) and ``P3`` (:math:`3^\circ`),
    and Ailles' :math:`15^\circ` ray ``P15`` (:math:`18^\circ - 15^\circ = 3^\circ`).

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-2.2``.
    """
    lattice = three_degree_lattice()
    cos_pi_17 = gauss_seventeen_gon_cosine()

    model = Model("knott-2-2", logger=False, auto_intersect=False)
    model._simplifier = simplify_exact  # noqa: SLF001
    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    pt_u = model.given_point(sp.Integer(1), sp.Integer(0), ID="U")
    pt_v = model.set_point(sp.Integer(0), sp.Integer(1), ID="V", classes=["given"])

    model.construct_circle(pt_o, pt_u)
    seg_ou = model.set_segment(pt_o, pt_u, classes=["given"])
    model.set_segment(pt_o, pt_v, classes=["given"])

    pts: dict[int, spg.Point] = {}
    for deg in (3, 6, 12, 15, 18, 30, 36, 60, 72):
        entry = lattice[deg]
        cls = ["golden"] if deg in (3, 12, 18, 36, 72) else None
        pts[deg] = model.set_point(entry.cos, entry.sin, ID=f"P{deg}", classes=cls)
        model.set_segment(pt_o, pts[deg], classes=cls)

    # Highlight the Euclid IV.16 15-gon difference chord P60-P72 == U-P12 and 3-degree chord P15-P18 == U-P3:
    model.set_segment(pts[60], pts[72], classes=["golden"])
    model.set_segment(pt_u, pts[12], classes=["golden"])
    model.set_segment(pts[15], pts[18], classes=["golden"])
    model.set_segment(pt_u, pts[3], classes=["golden"])

    assert_zero(
        quadrance(pts[60], pts[72]) - quadrance(pt_u, pts[12]),
        "Euclid IV.16 15-gon chord Q(P60, P72) == Q(U, P12)",
    )
    assert_zero(
        quadrance(pts[15], pts[18]) - quadrance(pt_u, pts[3]),
        "3-degree generator chord Q(P15, P18) == Q(U, P3)",
    )
    assert_zero(
        spread(seg_ou, spg.Segment(pt_o, pts[3])) - lattice[3].spread,
        "spread(3 deg) matches lattice",
    )
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-2.2",
        model=model,
        invariants={
            "lattice_count": sp.Integer(len(lattice)),
            "cos_3_deg": lattice[3].cos,
            "sin_3_deg": lattice[3].sin,
            "spread_3_deg": lattice[3].spread,
            "spread_12_deg": lattice[12].spread,
            "spread_15_deg": lattice[15].spread,
            "fifteen_gon_chord_quadrance": quadrance(pts[60], pts[72]),
            "cos_pi_over_17": cos_pi_17,
        },
    )
