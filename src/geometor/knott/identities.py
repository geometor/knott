r"""Collection 6: Fibonacci-Lucas Identities, Pythagorean Triples, Jigsaw Paradoxes & :math:`\pi` (`KNOTT-6.1` – `KNOTT-6.5`).

Catalogs the Fibonacci generator of Pythagorean right triangles, Cassini's identity
and both :math:`64 \leftrightarrow 65` (:math:`+1` gap) and :math:`64 \leftrightarrow 63`
(:math:`-1` overlap) jigsaw dissections, Binet/Lucas/Catalan/d'Ocagne/Honsberger and
Jarden-Fibonomial power identities, Lehmer/Hayashi Fibonacci arctangent telescoping
series for :math:`\pi`, and the Golden Angle parastichy lattice curated by Dr. Ron
Knott on ``pythag.html``, ``fibpuzzles2.html``, ``fibFormulae.html``, ``fibpi.html``,
and ``fibnat.html``.
"""

from __future__ import annotations

import math
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
    polygon_signed_area,
    quadrance,
    simplify_exact,
    spread,
)
from geometor.knott.flat_geometry import GeometricCatalogResult


@dataclass(frozen=True)
class FibonacciPythagoreanRecord:
    r"""Exact Pythagorean right triangle generated from :math:`(F_n, F_{n+1}, F_{n+2}, F_{n+3})`."""

    n: int
    leg_a: int
    leg_b: int
    hypotenuse_c: int
    area: int
    inradius: int
    gcd_factor: int
    primitive_triple: tuple[int, int, int]


def fibonacci_pythagorean_triple(n: int) -> FibonacciPythagoreanRecord:
    r"""Generate and verify the Fibonacci Pythagorean triple for index :math:`n \ge 1`.

    Uses Euclid's generator :math:`(m, k) = (F_{n+2}, F_{n+1})`:

    - :math:`a_n = m^2 - k^2 = (F_{n+2} - F_{n+1})(F_{n+2} + F_{n+1}) = F_n F_{n+3}`;
    - :math:`b_n = 2 m k = 2 F_{n+1} F_{n+2}`;
    - :math:`c_n = m^2 + k^2 = F_{n+1}^2 + F_{n+2}^2 = F_{2n+3}`.

    Args:
        n: Positive integer (:math:`n \ge 1`).

    Returns:
        Verified :class:`FibonacciPythagoreanRecord`.
    """
    if n < 1:
        raise ValueError(f"Expected n >= 1, got {n}")
    f0 = int(sp.fibonacci(n))
    f1 = int(sp.fibonacci(n + 1))
    f2 = int(sp.fibonacci(n + 2))
    f3 = int(sp.fibonacci(n + 3))
    f_hyp = int(sp.fibonacci(2 * n + 3))

    leg_a = f0 * f3
    leg_b = 2 * f1 * f2
    hyp_c = f1 * f1 + f2 * f2

    if hyp_c != f_hyp:  # pragma: no cover
        raise AssertionError(f"Honsberger hypotenuse mismatch: {hyp_c} != {f_hyp}")
    if leg_a * leg_a + leg_b * leg_b != hyp_c * hyp_c:  # pragma: no cover
        raise AssertionError(f"Pythagoras failed for n={n}: ({leg_a}, {leg_b}, {hyp_c})")

    area = (leg_a * leg_b) // 2
    if area != f0 * f1 * f2 * f3:  # pragma: no cover
        raise AssertionError("Area product formula mismatch")

    inradius = (leg_a + leg_b - hyp_c) // 2
    if inradius != f0 * f1:  # pragma: no cover
        raise AssertionError("Inradius formula mismatch")

    gcd_val = math.gcd(math.gcd(leg_a, leg_b), hyp_c)
    expected_gcd = 2 if (n % 3 == 0) else 1
    if gcd_val != expected_gcd:  # pragma: no cover
        raise AssertionError(f"Expected gcd {expected_gcd} at n={n}, got {gcd_val}")

    prim = tuple(sorted((leg_a // gcd_val, leg_b // gcd_val, hyp_c // gcd_val)))
    return FibonacciPythagoreanRecord(
        n=n,
        leg_a=leg_a,
        leg_b=leg_b,
        hypotenuse_c=hyp_c,
        area=area,
        inradius=inradius,
        gcd_factor=gcd_val,
        primitive_triple=prim,  # type: ignore[arg-type]
    )


def construct_fibonacci_pythagorean_model() -> GeometricCatalogResult:
    """Construct `KNOTT-6.1`: Exact right triangles :math:`(3,4,5)` & :math:`(5,12,13)` with incircle.

    Constructs the first two Fibonacci Pythagorean right triangles ``O A1 B1`` (:math:`3, 4, 5`
    from :math:`1, 1, 2, 3`) and ``O A2 B2`` (:math:`5, 12, 13` from :math:`1, 2, 3, 5`)
    sharing right-angle vertex ``O(0, 0)``, together with incircle ``(I2, T2)`` of exact
    inradius :math:`r_2 = F_2 F_3 = 2` inside :math:`(5, 12, 13)`.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-6.1``.
    """
    records = [fibonacci_pythagorean_triple(k) for k in range(1, 9)]

    model = Model("knott-6-1", logger=False, auto_intersect=False)
    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")

    # Triangle 1 (n=1): (4, 0), (0, 3) -> hypotenuse 5
    a1 = model.set_point(sp.Integer(4), sp.Integer(0), ID="A1", classes=["given"])
    b1 = model.set_point(sp.Integer(0), sp.Integer(3), ID="B1", classes=["given"])
    model.set_polygon([pt_o, a1, b1])
    model.set_segment(a1, b1)

    # Triangle 2 (n=2): (12, 0), (0, 5) -> hypotenuse 13, incenter I2(2, 2), inradius 2
    a2 = model.set_point(sp.Integer(12), sp.Integer(0), ID="A2", classes=["golden"])
    b2 = model.set_point(sp.Integer(0), sp.Integer(5), ID="B2", classes=["golden"])
    model.set_polygon([pt_o, a2, b2], classes=["golden"])
    seg_oa2 = model.set_segment(pt_o, a2, classes=["golden"])
    seg_ob2 = model.set_segment(pt_o, b2, classes=["golden"])
    model.set_segment(a2, b2, classes=["golden"])

    i2 = model.set_point(sp.Integer(2), sp.Integer(2), ID="I2", classes=["golden"])
    t2 = model.set_point(sp.Integer(2), sp.Integer(0), ID="T2", classes=["golden"])
    model.construct_circle(i2, t2, classes=["golden"])

    assert_zero(spread(seg_oa2, seg_ob2) - 1, "Right angle at O")
    assert_zero(quadrance(a1, b1) - 25, "Q(A1, B1) == 25")
    assert_zero(quadrance(a2, b2) - 169, "Q(A2, B2) == 169")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-6.1",
        model=model,
        invariants={
            "n1_hypotenuse": sp.Integer(records[0].hypotenuse_c),
            "n1_area": sp.Integer(records[0].area),
            "n2_hypotenuse": sp.Integer(records[1].hypotenuse_c),
            "n2_area": sp.Integer(records[1].area),
            "n2_inradius": sp.Integer(records[1].inradius),
            "n4_hypotenuse": sp.Integer(records[3].hypotenuse_c),
            "n4_area": sp.Integer(records[3].area),
        },
    )


def verify_cassini(n: int) -> int:
    r"""Verify Cassini's identity :math:`F_{n-1} F_{n+1} - F_n^2 = (-1)^n`.

    Args:
        n: Integer index.

    Returns:
        Exact alternating determinant :math:`(-1)^n \in \{-1, +1\}`.
    """
    lhs = int(sp.fibonacci(n - 1)) * int(sp.fibonacci(n + 1)) - int(sp.fibonacci(n)) ** 2
    rhs = -1 if (n % 2 == 1) else 1
    if lhs != rhs:  # pragma: no cover
        raise AssertionError(f"Cassini failed at n={n}: {lhs} != {rhs}")
    return lhs


def construct_fibonacci_jigsaw_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-6.2`: Cassini's :math:`8 \times 8 = 64 \leftrightarrow 5 \times 13 = 65` & :math:`63` jigsaws.

    Models **both** classical four-piece dissections of the :math:`8 \times 8 = 64` square
    (two :math:`3 \times 8` right triangles of area ``12`` + two :math:`5 \times (3, 5)`
    right trapezoids of area ``20``) inside a single exact ``geometor.model.Model``:

    1. **Lower figure (:math:`5 \times 13 = 65` Hooper/Loyd rectangle)**: encloses the
       slender internal parallelogram ``O P1 Q P2`` of exact shoelace area ``+1``;
    2. **Upper figure (Sam Loyd Jr. / Dudeney / Knott 63-unit notched block, shifted to ``y >= 7``)**:
       two :math:`5 \times 6 = 30` wings joined by a :math:`3 \times 1 = 3` bridge
       (apparent outer area ``63``), concealing an internal overlap parallelogram
       ``U0 U1 U2 U3`` of exact shoelace area ``+1`` (:math:`64 - 1 = 63`).

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-6.2``.
    """
    for idx in range(1, 16):
        verify_cassini(idx)

    model = Model("knott-6-2", logger=False, auto_intersect=False)

    # 1. Lower 5 x 13 = 65 arrangement (y in [0, 5]):
    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    r_b8 = model.set_point(sp.Integer(8), sp.Integer(0), ID="B8")
    r_b13 = model.given_point(sp.Integer(13), sp.Integer(0), ID="R0")
    pt_p1 = model.set_point(sp.Integer(8), sp.Integer(3), ID="P1", classes=["golden"])
    pt_q = model.set_point(sp.Integer(13), sp.Integer(5), ID="Q", classes=["golden"])
    r_t0 = model.set_point(sp.Integer(0), sp.Integer(5), ID="T0")
    r_t5 = model.set_point(sp.Integer(5), sp.Integer(5), ID="T5")
    pt_p2 = model.set_point(sp.Integer(5), sp.Integer(2), ID="P2", classes=["golden"])

    # Four pieces in 5x13 + slender gap parallelogram O P1 Q P2:
    p_tri1 = [pt_o, r_b8, pt_p1]
    p_trap1 = [r_b8, r_b13, pt_q, pt_p1]
    p_trap2 = [pt_o, pt_p2, r_t5, r_t0]
    p_tri2 = [pt_p2, pt_q, r_t5]
    gap_poly = [pt_o, pt_p1, pt_q, pt_p2]

    for poly_pts in (p_tri1, p_trap1, p_trap2, p_tri2):
        model.set_polygon(poly_pts)
    model.set_polygon(gap_poly, classes=["golden"])
    model.set_segment(pt_o, pt_p1, classes=["golden"])
    model.set_segment(pt_p1, pt_q, classes=["golden"])
    model.set_segment(pt_o, pt_p2, classes=["golden"])
    model.set_segment(pt_p2, pt_q, classes=["golden"])

    sum_pieces_65 = (
        polygon_signed_area(p_tri1)
        + polygon_signed_area(p_trap1)
        + polygon_signed_area(p_trap2)
        + polygon_signed_area(p_tri2)
    )
    gap_area = polygon_signed_area(gap_poly)
    outer_65 = polygon_signed_area([pt_o, r_b13, pt_q, r_t0])
    assert_zero(sum_pieces_65 - 64, "Four pieces sum to 64")
    assert_zero(gap_area - 1, "Cassini +1 gap parallelogram area == 1")
    assert_zero(outer_65 - 65, "Outer 5x13 rectangle area == 65")

    # 2. Upper 63-unit overlap arrangement shifted upward by dy = 7:
    dy = sp.Integer(7)
    # Z1: (0,0)->(5,0)->(5,5)->(0,3); T1: (0,3)->(8,6)->(0,6)
    # Z2: (13,11)->(8,11)->(8,6)->(13,8); T2: (13,8)->(5,5)->(13,5)
    u_00 = model.set_point(sp.Integer(0), dy + 0, ID="S0")
    u_50 = model.set_point(sp.Integer(5), dy + 0, ID="S1")
    u_55 = model.set_point(sp.Integer(5), dy + 5, ID="U1", classes=["golden"])
    u_03 = model.set_point(sp.Integer(0), dy + 3, ID="U0", classes=["golden"])
    u_86 = model.set_point(sp.Integer(8), dy + 6, ID="U3", classes=["golden"])
    u_06 = model.set_point(sp.Integer(0), dy + 6, ID="S2")
    u_8_11 = model.set_point(sp.Integer(8), dy + 11, ID="S3")
    u_13_11 = model.set_point(sp.Integer(13), dy + 11, ID="S4")
    u_13_8 = model.set_point(sp.Integer(13), dy + 8, ID="U2", classes=["golden"])
    u_13_5 = model.set_point(sp.Integer(13), dy + 5, ID="S5")

    z1_pts = [u_00, u_50, u_55, u_03]
    t1_pts = [u_03, u_86, u_06]
    z2_pts = [u_86, u_13_8, u_13_11, u_8_11]
    t2_pts = [u_55, u_13_5, u_13_8]
    overlap_pts = [u_03, u_86, u_13_8, u_55]

    for poly_pts in (z1_pts, t1_pts, z2_pts, t2_pts):
        model.set_polygon(poly_pts)
    model.set_polygon(overlap_pts, classes=["golden"])
    model.set_segment(u_03, u_55, classes=["golden"])
    model.set_segment(u_55, u_13_8, classes=["golden"])
    model.set_segment(u_03, u_86, classes=["golden"])
    model.set_segment(u_86, u_13_8, classes=["golden"])

    # Outer 10-vertex non-convex boundary of the 63-unit notched block:
    u_56 = spg.Point(sp.Integer(5), dy + 6)
    u_85 = spg.Point(sp.Integer(8), dy + 5)
    outer_63_boundary = [
        u_00,
        u_50,
        u_55,
        u_85,
        u_13_5,
        u_13_11,
        u_8_11,
        u_86,
        u_56,
        u_06,
    ]
    sum_pieces_63 = (
        polygon_signed_area(z1_pts)
        + polygon_signed_area(t1_pts)
        + polygon_signed_area(z2_pts)
        + polygon_signed_area(t2_pts)
    )
    overlap_area = polygon_signed_area(overlap_pts)
    outer_63_area = polygon_signed_area(outer_63_boundary)

    assert_zero(sum_pieces_63 - 64, "Upper 4 pieces also have exact area 64")
    assert_zero(overlap_area - 1, "Sam Loyd Jr overlap parallelogram area == 1")
    assert_zero(outer_63_area - 63, "Outer notched silhouette area == 63 (64 - 1)")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-6.2",
        model=model,
        invariants={
            "square_area": sp.Integer(64),
            "rectangle_65_area": outer_65,
            "gap_parallelogram_area": gap_area,
            "notched_63_area": outer_63_area,
            "overlap_parallelogram_area": overlap_area,
            "cassini_n6": sp.Integer(verify_cassini(6)),
            "cassini_n7": sp.Integer(verify_cassini(7)),
        },
    )


def fibonomial(n: int, k: int) -> int:
    r"""Compute the exact integer Fibonomial coefficient :math:`\binom{n}{k}_F`.

    Defined on ``Fibonomials.html`` and ``fibFormulae.html#FibonomialFormulae`` as
    :math:`\frac{F_n F_{n-1} \cdots F_{n-k+1}}{F_k F_{k-1} \cdots F_1}` (with
    :math:`\binom{n}{0}_F = \binom{n}{n}_F = 1`).

    Args:
        n: Non-negative upper index.
        k: Integer lower index.

    Returns:
        Exact integer Fibonomial coefficient.
    """
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k_use = min(k, n - k)
    num = 1
    den = 1
    for j in range(1, k_use + 1):
        num *= int(sp.fibonacci(n - j + 1))
        den *= int(sp.fibonacci(j))
    if num % den != 0:  # pragma: no cover
        raise AssertionError(f"Non-integral Fibonomial ({n}, {k}): {num}/{den}")
    return num // den


def verify_classical_identities() -> dict[str, sp.Expr]:
    """Machine-verify Binet, Lucas, Catalan, d'Ocagne, Honsberger, and Fibonomial identities.

    Returns:
        Dictionary of representative verified exact quantities.
    """
    for n_idx in range(0, 14):
        fn = sp.fibonacci(n_idx)
        ln = sp.lucas(n_idx)
        # Binet formulas:
        assert_zero(fn - (PHI**n_idx - (-phi) ** n_idx) / SQRT5, f"Binet F_{n_idx}")
        assert_zero(ln - (PHI**n_idx + (-phi) ** n_idx), f"Binet L_{n_idx}")
        # Lucas bridges:
        assert_zero(ln - (sp.fibonacci(n_idx - 1) + sp.fibonacci(n_idx + 1)), f"L_{n_idx} sum")
        assert_zero(sp.fibonacci(2 * n_idx) - fn * ln, f"F_{2*n_idx} == F_n * L_n")
        assert_zero(ln**2 - 5 * fn**2 - 4 * ((-1) ** n_idx), f"Pell-Lucas norm at {n_idx}")

    # Catalan & d'Ocagne & Honsberger over grids of (m, n, r):
    for n_idx in range(2, 10):
        for r_idx in range(1, n_idx):
            lhs_cat = sp.fibonacci(n_idx) ** 2 - sp.fibonacci(n_idx - r_idx) * sp.fibonacci(n_idx + r_idx)
            rhs_cat = ((-1) ** (n_idx - r_idx)) * (sp.fibonacci(r_idx) ** 2)
            assert_zero(lhs_cat - rhs_cat, f"Catalan ({n_idx}, {r_idx})")

    for m_idx in range(1, 9):
        for n_idx in range(1, 9):
            lhs_doc = (
                sp.fibonacci(m_idx) * sp.fibonacci(n_idx + 1)
                - sp.fibonacci(m_idx + 1) * sp.fibonacci(n_idx)
            )
            rhs_doc = ((-1) ** n_idx) * sp.fibonacci(m_idx - n_idx)
            assert_zero(lhs_doc - rhs_doc, f"d'Ocagne ({m_idx}, {n_idx})")

            lhs_hon = sp.fibonacci(m_idx + n_idx)
            rhs_hon = (
                sp.fibonacci(m_idx - 1) * sp.fibonacci(n_idx)
                + sp.fibonacci(m_idx) * sp.fibonacci(n_idx + 1)
            )
            assert_zero(lhs_hon - rhs_hon, f"Honsberger ({m_idx}, {n_idx})")

    # Fibonomial recurrence and Jarden power recurrence for powers p = 1..4:
    for n_idx in range(2, 9):
        for k_idx in range(1, n_idx):
            rec = (
                int(sp.fibonacci(k_idx - 1)) * fibonomial(n_idx - 1, k_idx)
                + int(sp.fibonacci(n_idx - k_idx + 1)) * fibonomial(n_idx - 1, k_idx - 1)
            )
            if fibonomial(n_idx, k_idx) != rec:  # pragma: no cover
                raise AssertionError(f"Fibonomial recurrence failed at ({n_idx}, {k_idx})")

    for power_p in range(1, 5):
        order = power_p + 1
        for n_idx in range(order, order + 6):
            acc = 0
            for j_idx in range(0, order + 1):
                sgn = -1 if ((j_idx * (j_idx + 1) // 2) % 2 == 1) else 1
                acc += sgn * fibonomial(order, j_idx) * (int(sp.fibonacci(n_idx - j_idx)) ** power_p)
            if acc != 0:  # pragma: no cover
                raise AssertionError(f"Fibonomial power p={power_p} recurrence failed at n={n_idx}")

    return {
        "fibonomial_5_2": sp.Integer(fibonomial(5, 2)),
        "fibonomial_6_3": sp.Integer(fibonomial(6, 3)),
        "F10": sp.fibonacci(10),
        "L10": sp.lucas(10),
        "F20_via_F10_L10": sp.fibonacci(10) * sp.lucas(10),
    }


def construct_lucas_binet_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-6.3`: Pell-Lucas lattice points :math:`(L_n, F_n)` & asymptote :math:`y = x / \sqrt{5}`.

    Plots exact Pell-Lucas points :math:`P_n = (L_n, F_n)` for :math:`n = 0..4`
    (``P0(2,0)``, ``P1(1,1)``, ``P2(3,1)``, ``P3(4,2)``, ``P4(7,3)``) alternating across
    hyperbolas :math:`x^2 - 5 y^2 = \pm 4` around Binet's asymptote ray ``[O A]`` of
    exact slope :math:`1 / \sqrt{5}` (:math:`A = (8, 8/\sqrt{5})`).

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-6.3``.
    """
    verified = verify_classical_identities()

    model = Model("knott-6-3", logger=False, auto_intersect=False)
    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    pt_a = model.set_point(sp.Integer(8), sp.Integer(8) / SQRT5, ID="A", classes=["golden"])
    model.set_segment(pt_o, pt_a, classes=["golden"])

    pts: list[spg.Point] = []
    for n_idx in range(0, 5):
        ln = sp.lucas(n_idx)
        fn = sp.fibonacci(n_idx)
        cls = ["given"] if n_idx % 2 == 0 else ["golden"]
        pt_p = model.set_point(ln, fn, ID=f"P{n_idx}", classes=cls)
        pts.append(pt_p)
        model.set_segment(pt_o, pt_p)

    for idx in range(len(pts) - 1):
        model.set_segment(pts[idx], pts[idx + 1], classes=["golden"])
        # Area of triangle O P_n P_{n+1}: |L_n F_{n+1} - L_{n+1} F_n| / 2 == 1 !!
        # Let's check: n=0: |2*1 - 1*0|/2 = 1; n=1: |1*1 - 3*1|/2 = 1; n=2: |3*2 - 4*1|/2 = 1!
        tri_area = abs(polygon_signed_area([pt_o, pts[idx], pts[idx + 1]]))
        assert_zero(tri_area - 1, f"Pell-Lucas sector triangle O P_{idx} P_{idx+1} has unit area 1")
        model.set_polygon([pt_o, pts[idx], pts[idx + 1]])

    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-6.3",
        model=model,
        invariants={
            **verified,
            "pell_lucas_sector_area": sp.Integer(1),
            "asymptote_slope": 1 / SQRT5,
        },
    )


def verify_fibonacci_arctan_step(n: int) -> sp.Expr:
    r"""Verify Lehmer's step :math:`\arctan(1/F_{2n}) = \arctan(1/F_{2n+1}) + \arctan(1/F_{2n+2})`.

    Proves exact equality both via rational tangent-addition algebra
    :math:`(a + b)/(1 - a b) = 1/F_{2n}` and via SymPy's symbolic ``atan`` simplification.

    Args:
        n: Positive integer (:math:`n \ge 1`).

    Returns:
        Exact common tangent :math:`1 / F_{2n}` as :class:`sympy.Rational`.
    """
    if n < 1:
        raise ValueError(f"Expected n >= 1, got {n}")
    f_2n = sp.Rational(int(sp.fibonacci(2 * n)))
    f_2n1 = sp.Rational(int(sp.fibonacci(2 * n + 1)))
    f_2n2 = sp.Rational(int(sp.fibonacci(2 * n + 2)))

    t_a = sp.Integer(1) / f_2n1
    t_b = sp.Integer(1) / f_2n2
    tan_sum = sp.simplify((t_a + t_b) / (sp.Integer(1) - t_a * t_b))
    expected_tan = sp.Integer(1) / f_2n
    assert_zero(tan_sum - expected_tan, f"tan addition step at n={n}")

    # Also verify exact angle difference vanishes via sp.expand_trig(sp.tan(lhs - rhs)) == 0:
    angle_diff = sp.atan(expected_tan) - sp.atan(t_a) - sp.atan(t_b)
    assert_zero(sp.cancel(sp.expand_trig(sp.tan(angle_diff))), f"tan(atan_diff) == 0 at n={n}")
    return expected_tan


def verify_fibonacci_pi_telescoping(terms: int = 8) -> sp.Expr:
    r"""Verify :math:`\frac{\pi}{4} = \sum_{k=1}^{N} \arctan\frac{1}{F_{2k+1}} + \arctan\frac{1}{F_{2N+2}}`.

    Args:
        terms: Number of telescoping steps :math:`N \ge 1`.

    Returns:
        Exact symbolic remainder :math:`\arctan(1 / F_{2N+2})`.
    """
    if terms < 1:
        raise ValueError(f"Expected terms >= 1, got {terms}")
    # Compose exact rational tangent of partial sum + remainder recursively:
    rem_tan = sp.Rational(1, int(sp.fibonacci(2 * terms + 2)))
    curr_tan = rem_tan
    for k in range(terms, 0, -1):
        verify_fibonacci_arctan_step(k)
        step_tan = sp.Rational(1, int(sp.fibonacci(2 * k + 1)))
        curr_tan = sp.Rational(curr_tan + step_tan, 1 - curr_tan * step_tan)

    # At k = 1, curr_tan must equal 1 / F_2 == 1 == tan(pi / 4)!
    assert_zero(curr_tan - 1, "Telescoped tangent equals 1 == tan(pi/4)")
    return sp.atan(rem_tan)


def construct_hayashi_arctan_grid_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-6.4`: Ko Hayashi's integer-grid proof of :math:`\frac{\pi}{4} = \arctan\frac{1}{2} + \arctan\frac{1}{5} + \arctan\frac{1}{8}`.

    Constructs four integer lattice points ``O(0,0)``, ``E(10,10)``, ``M(15,5)``, and
    ``N(16,2)`` (with horizontal reference ``X(16,0)``):

    - Right triangle ``O E M`` has :math:`s([OE], [EM]) = 1` and :math:`Q(E,M)/Q(O,E) = 50/200 = 1/4 = (1/2)^2`,
      proving :math:`\angle EOM = \arctan(1/2)` between :math:`45^\circ` ray ``OE`` and slope-:math:`1/3` ray ``OM``;
    - Right triangle ``O M N`` has :math:`s([OM], [MN]) = 1` and :math:`Q(M,N)/Q(O,M) = 10/250 = 1/25 = (1/5)^2`,
      proving :math:`\angle MON = \arctan(1/5)` between slope-:math:`1/3` ray ``OM`` and slope-:math:`1/8` ray ``ON``.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-6.4``.
    """
    rem_8 = verify_fibonacci_pi_telescoping(8)

    model = Model("knott-6-4", logger=False, auto_intersect=False)
    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    pt_x = model.given_point(sp.Integer(16), sp.Integer(0), ID="X")
    pt_n = model.set_point(sp.Integer(16), sp.Integer(2), ID="N", classes=["golden"])
    pt_m = model.set_point(sp.Integer(15), sp.Integer(5), ID="M", classes=["golden"])
    pt_e = model.set_point(sp.Integer(10), sp.Integer(10), ID="E", classes=["golden"])

    seg_ox = model.set_segment(pt_o, pt_x, classes=["given"])
    seg_on = model.set_segment(pt_o, pt_n, classes=["golden"])
    seg_om = model.set_segment(pt_o, pt_m, classes=["golden"])
    seg_oe = model.set_segment(pt_o, pt_e, classes=["golden"])
    seg_em = model.set_segment(pt_e, pt_m, classes=["golden"])
    seg_mn = model.set_segment(pt_m, pt_n, classes=["golden"])
    model.set_segment(pt_x, pt_n)

    model.set_polygon([pt_o, pt_m, pt_e], classes=["golden"])
    model.set_polygon([pt_o, pt_n, pt_m])

    assert_zero(spread(seg_oe, seg_em) - 1, "Right angle at E in triangle OEM")
    assert_zero(spread(seg_om, seg_mn) - 1, "Right angle at M in triangle OMN")
    assert_zero(
        simplify_exact(quadrance(pt_e, pt_m) / quadrance(pt_o, pt_e)) - sp.Rational(1, 4),
        "tan^2(angle EOM) == (1/2)^2",
    )
    assert_zero(
        simplify_exact(quadrance(pt_m, pt_n) / quadrance(pt_o, pt_m)) - sp.Rational(1, 25),
        "tan^2(angle MON) == (1/5)^2",
    )
    assert_zero(spread(seg_ox, seg_oe) - sp.Rational(1, 2), "OE is at 45 deg (spread 1/2)")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-6.4",
        model=model,
        invariants={
            "twist_1_over_2": sp.Rational(1, 4),
            "twist_1_over_3": sp.Rational(1, 9),
            "twist_1_over_5": sp.Rational(1, 25),
            "twist_1_over_8": sp.Rational(1, 64),
            "remainder_after_8_steps": rem_8,
        },
    )


def golden_angle_invariants() -> dict[str, sp.Expr]:
    r"""Return exact symbolic invariants of the Golden Angle (:math:`360^\circ / \Phi^2`).

    Returns:
        Dictionary of exact turn fractions, radian/degree expressions, and parastichy offsets.
    """
    turn_minor = simplify_exact(1 / (PHI**2))
    turn_major = simplify_exact(1 / PHI)
    assert_zero(turn_minor - phi**2, "minor turn == phi^2 == 2 - PHI")
    assert_zero(turn_minor + turn_major - 1, "minor + major turn == 1")

    # Verify cylindrical parastichy offset F_k * phi^2 - F_{k-2} == (-phi)^k for k = 2..10:
    for k_idx in range(2, 11):
        fk = sp.fibonacci(k_idx)
        fk_m2 = sp.fibonacci(k_idx - 2)
        offset = simplify_exact(fk * (phi**2) - fk_m2)
        assert_zero(offset - ((-phi) ** k_idx), f"Parastichy offset at F_{k_idx}")

    return {
        "minor_turn_fraction": turn_minor,
        "major_turn_fraction": turn_major,
        "golden_angle_radians": simplify_exact(2 * sp.pi * turn_minor),
        "golden_angle_degrees": simplify_exact(360 * turn_minor),
        "reflex_angle_degrees": simplify_exact(360 * turn_major),
    }


def construct_parastichy_lattice_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-6.5`: Cylindrical Golden-Angle parastichy lattice & opposing Fibonacci spirals.

    Unrolls cylindrical phyllotaxis onto the :math:`(\Delta x, n)` plane around stem axis
    ``[O S]`` (:math:`x = 0`), plotting exact Fibonacci primordia
    :math:`P_k = (20 (F_k \phi^2 - F_{k-2}),\; F_k) = (20 (-\phi)^k,\; F_k)` for
    :math:`k = 2..6` (:math:`F_2=1, F_3=2, F_4=3, F_5=5, F_6=8`), plus their vector sum
    completing fundamental parastichy parallelograms ``O P3 Q34 P4`` and ``O P4 Q45 P5``.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-6.5``.
    """
    invariants = golden_angle_invariants()

    model = Model("knott-6-5", logger=False, auto_intersect=False)
    scale_x = sp.Integer(16)
    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    pt_s = model.set_point(sp.Integer(0), sp.Integer(9), ID="S", classes=["given"])
    model.set_segment(pt_o, pt_s, classes=["given"])

    p_map: dict[int, spg.Point] = {}
    for k_idx in range(2, 7):
        fk = sp.fibonacci(k_idx)
        dx = simplify_exact(scale_x * ((-phi) ** k_idx))
        cls = ["golden"] if k_idx % 2 == 0 else None
        p_map[k_idx] = model.set_point(dx, fk, ID=f"F{fk}" if fk > 1 else "P2", classes=cls)
        model.set_segment(pt_o, p_map[k_idx], classes=cls)

    # Complete opposing parastichy parallelograms (F_3=2, F_4=3 -> F_5=5) and (F_4=3, F_5=5 -> F_6=8)!
    # Notice: dx(P3) + dx(P4) = 16*(-phi^3 + phi^4) = 16*phi^3*(-1 + phi) = -16*phi^4?
    # Wait: phi^2 - phi^3 = phi^4, whereas (-phi)^3 + (-phi)^4 = -phi^3 + phi^4 = -phi^3*(1 - phi) = -phi^3*phi^2 = -phi^5 = dx(P5)!!
    # HOLD ON!! (-phi)^k + (-phi)^(k+1) = (-phi)^k * (1 - phi) = (-phi)^k * phi^2... wait:
    # For k=3: -phi^3 + phi^4 = -phi^3*(1 - phi) = -phi^5 = (-phi)^5!!
    # For k=4: +phi^4 - phi^5 = +phi^4*(1 - phi) = +phi^6 = (-phi)^6!!
    # THAT MEANS P_5 IS LITERALLY THE VECTOR SUM P_3 + P_4, AND P_6 IS LITERALLY P_4 + P_5!!
    assert_zero((p_map[3].x + p_map[4].x) - p_map[5].x, "Vector sum x: P3 + P4 == P5")
    assert_zero((p_map[3].y + p_map[4].y) - p_map[5].y, "Vector sum y: P3 + P4 == P5")
    assert_zero((p_map[4].x + p_map[5].x) - p_map[6].x, "Vector sum x: P4 + P5 == P6")
    assert_zero((p_map[4].y + p_map[5].y) - p_map[6].y, "Vector sum y: P4 + P5 == P6")

    model.set_polygon([pt_o, p_map[4], p_map[5], p_map[3]], classes=["golden"])
    model.set_polygon([pt_o, p_map[4], p_map[6], p_map[5]])
    model.set_segment(p_map[3], p_map[5], classes=["golden"])
    model.set_segment(p_map[4], p_map[5], classes=["golden"])
    model.set_segment(p_map[4], p_map[6], classes=["golden"])
    model.set_segment(p_map[5], p_map[6], classes=["golden"])

    # Every opposing Fibonacci parastichy basis (F_k, F_{k+1}) is unimodular of exact area 1:
    # |F_k (-phi)^(k+1) - F_{k+1} (-phi)^k| = phi^k * (F_k * phi + F_{k+1}) = phi^k * Phi^k = 1.
    unscaled_cell_34 = simplify_exact(
        abs(polygon_signed_area([pt_o, p_map[4], p_map[5], p_map[3]])) / scale_x
    )
    unscaled_cell_45 = simplify_exact(
        abs(polygon_signed_area([pt_o, p_map[4], p_map[6], p_map[5]])) / scale_x
    )
    assert_zero(unscaled_cell_34 - 1, "Unimodular parastichy cell (2, 3) area == 1")
    assert_zero(unscaled_cell_45 - 1, "Unimodular parastichy cell (3, 5) area == 1")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-6.5",
        model=model,
        invariants={
            **invariants,
            "fundamental_parastichy_cell_area": unscaled_cell_34,
        },
    )
