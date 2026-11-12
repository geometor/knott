r"""Exact symbolic constants, notation bridges, and Rational Trigonometry invariants.

Dr. Ron Knott's archive (*Fibonacci Numbers, the Golden Section and the Golden
String*, University of Surrey) uses uppercase :math:`\Phi = (1 + \sqrt{5})/2`
for the Golden Ratio (:math:`\approx 1.61803\dots`) and lowercase
:math:`\phi = \Phi - 1 = 1/\Phi = (\sqrt{5} - 1)/2` for its reciprocal
(:math:`\approx 0.61803\dots`). By contrast, SymPy and ``geometor.model`` denote
the larger root by ``sp.GoldenRatio`` (:math:`\phi_{\text{GEOMETOR}} = \Phi_{\text{Knott}}`).

This module provides exact closed-form :math:`\mathbb{Q}(\sqrt{5})` definitions
alongside lossless symbolic conversion helpers and Rational Trigonometry invariants.
"""

from __future__ import annotations

from collections.abc import Sequence

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

SQRT5: sp.Expr = sp.sqrt(5)
r"""Exact square root of 5 over :math:`\mathbb{Q}(\sqrt{5})`."""

PHI: sp.Expr = (sp.Integer(1) + SQRT5) / sp.Integer(2)
r"""Dr. Ron Knott's Golden Ratio :math:`\Phi = (1 + \sqrt{5})/2 \approx 1.6180339887\dots`."""

phi: sp.Expr = (SQRT5 - sp.Integer(1)) / sp.Integer(2)
r"""Dr. Ron Knott's reciprocal Golden Ratio :math:`\phi = \Phi - 1 = 1/\Phi \approx 0.6180339887\dots`."""

PSI: sp.Expr = (sp.Integer(1) - SQRT5) / sp.Integer(2)
r"""Galois conjugate :math:`\Psi = 1 - \Phi = -\phi = (1 - \sqrt{5})/2 \approx -0.6180339887\dots`."""


def simplify_exact(expr: sp.Expr | int | sp.Rational) -> sp.Expr:
    """Canonicalize an exact symbolic expression without introducing floats.

    Args:
        expr: Exact SymPy expression or integer/rational value.

    Returns:
        Simplified exact :class:`sympy.Expr`.
    """
    sym_expr = sp.sympify(expr)
    expanded = sp.expand(sym_expr.rewrite(sp.sqrt))
    if not expanded.has(sp.Pow):
        return expanded
    if sp.denom(expanded).has(sp.Pow):
        return sp.radsimp(expanded)
    return expanded


def assert_zero(expr: sp.Expr, message: str = "") -> None:
    """Assert that ``expr`` simplifies identically to symbolic ``0``.

    Args:
        expr: Difference expression expected to vanish identically.
        message: Optional diagnostic description on failure.

    Raises:
        AssertionError: If ``expr`` does not reduce to exact ``0``.
    """
    expanded = sp.expand(sp.sympify(expr).rewrite(sp.sqrt))
    if expanded == 0:
        return
    reduced = sp.simplify(sp.powsimp(expanded, force=True))
    if reduced != 0:
        detail = f" ({message})" if message else ""
        raise AssertionError(f"Expected exact symbolic 0{detail}, got: {reduced!r}")


def assert_no_floats(obj: Model | sp.Basic | Sequence[object] | dict[object, object]) -> None:
    """Verify recursively that no ``float`` or ``sp.Float`` exists in ``obj``.

    Args:
        obj: A :class:`geometor.model.Model`, SymPy expression/entity, sequence, or mapping.

    Raises:
        AssertionError: If any floating-point value or ``sp.Float`` atom is detected.
    """
    if isinstance(obj, float):
        raise AssertionError(f"Forbidden Python float detected: {obj!r}")
    if isinstance(obj, Model):
        for elem in obj:
            assert_no_floats(elem)
        return
    if isinstance(obj, sp.Basic):
        floats = obj.atoms(sp.Float)
        if floats:
            raise AssertionError(f"Forbidden sp.Float atoms detected in {obj!r}: {floats!r}")
        return
    if isinstance(obj, dict):
        for key, val in obj.items():
            assert_no_floats(key)
            assert_no_floats(val)
        return
    if isinstance(obj, Sequence) and not isinstance(obj, (str, bytes)):
        for item in obj:
            if isinstance(item, (Model, sp.Basic, Sequence, dict, float)):
                assert_no_floats(item)


def knott_to_geometor(
    expr: sp.Expr,
    *,
    knott_big_phi: sp.Symbol | None = None,
    knott_small_phi: sp.Symbol | None = None,
) -> sp.Expr:
    r"""Map an expression in Knott's :math:`(\Phi, \phi)` symbols to ``sp.GoldenRatio``.

    Args:
        expr: Symbolic expression written in terms of Knott's ``Phi`` and ``phi`` symbols.
        knott_big_phi: Optional symbol representing :math:`\Phi` (defaults to ``Symbol('Phi')``).
        knott_small_phi: Optional symbol representing :math:`\phi` (defaults to ``Symbol('phi')``).

    Returns:
        Equivalent SymPy expression written in terms of ``sp.GoldenRatio``.
    """
    big_sym = knott_big_phi or sp.Symbol("Phi", positive=True)
    small_sym = knott_small_phi or sp.Symbol("phi", positive=True)
    return sp.simplify(
        expr.subs(
            {
                big_sym: sp.GoldenRatio,
                small_sym: sp.GoldenRatio - sp.Integer(1),
            }
        )
    )


def geometor_to_knott_radicals(expr: sp.Expr) -> sp.Expr:
    r"""Expand an expression containing ``sp.GoldenRatio`` into :math:`\mathbb{Q}(\sqrt{5})`.

    Args:
        expr: Symbolic expression possibly containing ``sp.GoldenRatio``.

    Returns:
        Exact radical form over :math:`\mathbb{Q}(\sqrt{5})`.
    """
    return simplify_exact(expr.subs(sp.GoldenRatio, PHI))


def verify_notation_bijection() -> dict[str, sp.Expr]:
    """Verify all fundamental identities bridging Knott and GEOMETOR conventions.

    Returns:
        Dictionary of canonical zero-checked identities and exact radical constants.
    """
    assert_zero(PHI - sp.GoldenRatio.rewrite(sp.sqrt), "PHI == sp.GoldenRatio")
    assert_zero(phi - (PHI - 1), "phi == PHI - 1")
    assert_zero(PHI * phi - 1, "PHI * phi == 1")
    assert_zero(PHI**2 - PHI - 1, "PHI^2 == PHI + 1")
    assert_zero(phi**2 + phi - 1, "phi^2 == 1 - phi")
    assert_zero(PHI + PSI - 1, "PHI + PSI == 1")
    assert_zero(PHI * PSI + 1, "PHI * PSI == -1")
    return {
        "PHI": PHI,
        "phi": phi,
        "PSI": PSI,
        "PHI_minus_phi": simplify_exact(PHI - phi),
        "PHI_plus_phi": simplify_exact(PHI + phi),
    }


def quadrance(p1: spg.Point, p2: spg.Point) -> sp.Expr:
    """Compute the exact Euclidean quadrance :math:`Q(p_1, p_2) = (x_2 - x_1)^2 + (y_2 - y_1)^2`.

    Args:
        p1: First planar point.
        p2: Second planar point.

    Returns:
        Exact squared distance in SymPy without introducing square roots.
    """
    return simplify_exact((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def spread(l1: spg.Line | spg.Segment, l2: spg.Line | spg.Segment) -> sp.Expr:
    r"""Compute the exact Rational Trigonometry spread :math:`s(\ell_1, \ell_2) \in [0, 1]`.

    Args:
        l1: First line or segment.
        l2: Second line or segment.

    Returns:
        Exact symbolic spread :math:`(a_1 b_2 - a_2 b_1)^2 / ((a_1^2 + b_1^2)(a_2^2 + b_2^2))`.
    """
    dx1, dy1 = l1.p2.x - l1.p1.x, l1.p2.y - l1.p1.y
    dx2, dy2 = l2.p2.x - l2.p1.x, l2.p2.y - l2.p1.y
    cross_det = dx1 * dy2 - dy1 * dx2
    denom = (dx1**2 + dy1**2) * (dx2**2 + dy2**2)
    return simplify_exact(cross_det**2 / denom)


def cross(l1: spg.Line | spg.Segment, l2: spg.Line | spg.Segment) -> sp.Expr:
    r"""Compute the complementary Rational Trigonometry cross :math:`c(\ell_1, \ell_2) = 1 - s`.

    Args:
        l1: First line or segment.
        l2: Second line or segment.

    Returns:
        Exact symbolic cross :math:`(dx_1 dx_2 + dy_1 dy_2)^2 / ((dx_1^2 + dy_1^2)(dx_2^2 + dy_2^2))`.
    """
    return simplify_exact(sp.Integer(1) - spread(l1, l2))


def cross_ratio(a: spg.Point, b: spg.Point, c: spg.Point, d: spg.Point) -> sp.Expr:
    r"""Compute the projective cross-ratio :math:`(A, B; C, D)` of four collinear points.

    Args:
        a: First collinear point :math:`A`.
        b: Second collinear point :math:`B`.
        c: Third collinear point :math:`C`.
        d: Fourth collinear point :math:`D`.

    Returns:
        Exact projective invariant :math:`(\overline{AC}\cdot\overline{BD}) / (\overline{BC}\cdot\overline{AD})`.
    """
    dx = b.x - a.x
    dy = b.y - a.y
    use_x = sp.simplify(dx) != 0
    ca, cb, cc, cd = (a.x, b.x, c.x, d.x) if use_x else (a.y, b.y, c.y, d.y)
    return simplify_exact(((cc - ca) * (cd - cb)) / ((cc - cb) * (cd - ca)))


def polygon_signed_area(points: Sequence[spg.Point]) -> sp.Expr:
    """Compute the exact signed shoelace area of a planar polygon.

    Args:
        points: Ordered sequence of polygon vertices.

    Returns:
        Exact symbolic signed area (positive for counter-clockwise orientation).
    """
    n_pts = len(points)
    total = sp.Integer(0)
    for idx in range(n_pts):
        p_curr = points[idx]
        p_next = points[(idx + 1) % n_pts]
        total += p_curr.x * p_next.y - p_next.x * p_curr.y
    return simplify_exact(total / sp.Integer(2))


def floor_linear_phi(a: int | sp.Rational, b: int | sp.Rational) -> int:
    r"""Compute :math:`\lfloor a + b\Phi \rfloor` for :math:`a, b \in \mathbb{Q}` using pure integer algebra.

    Rewrites :math:`a + b\Phi = (2a + b + b\sqrt{5}) / 2` over a common positive
    integer denominator and determines the exact integer floor via integer square roots
    ``sp.integer_nthroot`` with zero floating-point evaluation.

    Args:
        a: Rational constant term.
        b: Rational coefficient of :math:`\Phi`.

    Returns:
        Exact Python ``int`` equal to :math:`\lfloor a + b\Phi \rfloor`.
    """
    ra = sp.Rational(a)
    rb = sp.Rational(b)
    if rb == 0:
        return int(sp.floor(ra))
    # Write a + b * (1 + sqrt(5))/2 = (P + Q * sqrt(5)) / D with D > 0 integer.
    denom = int(sp.ilcm(ra.q, 2 * rb.q))
    p_int = int(ra * denom + rb * sp.Rational(denom, 2))
    q_int = int(rb * sp.Rational(denom, 2))
    radicand = 5 * (q_int * q_int)
    root_floor, is_exact = sp.integer_nthroot(radicand, 2)
    # Floor of Q * sqrt(5):
    if q_int > 0:
        q_sqrt5_floor = int(root_floor)
    else:
        q_sqrt5_floor = -int(root_floor) if is_exact else -int(root_floor) - 1
    # Now k <= (p_int + q_int * sqrt(5)) / denom iff denom * k - p_int <= q_int * sqrt(5).
    approx_k = (p_int + q_sqrt5_floor) // denom
    # Refine locally with exact quadratic inequality:
    best = approx_k - 2
    for cand in range(approx_k - 2, approx_k + 4):
        lhs = denom * cand - p_int
        # Check lhs <= q_int * sqrt(5):
        if q_int > 0:
            ok = lhs <= 0 or lhs * lhs <= radicand
        else:
            # q_int < 0 => q_int * sqrt(5) < 0, so lhs must be < 0 and (-lhs)^2 >= radicand
            ok = lhs < 0 and lhs * lhs >= radicand
        if ok:
            best = cand
    return best
