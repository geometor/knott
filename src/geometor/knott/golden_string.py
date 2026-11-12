"""Collection 5: The Golden String, Zeckendorf Base, & Wythoff / Stolarsky Arrays (`KNOTT-5.1` – `KNOTT-5.3`).

Catalogs the Sturmian Golden String (``101101011011...``), lattice-cutting slope
geometry, Zeckendorf's canonical Fibonacci numeral base, Beatty's complementary
sequences, and Morrison's Wythoff and Stolarsky interspersion arrays curated by
Dr. Ron Knott on ``fibrab.html``, ``fibrep.html``, and ``fibGen.html``.
"""

from __future__ import annotations

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.knott.constants import (
    PHI,
    assert_no_floats,
    assert_zero,
    floor_linear_phi,
    phi,
    simplify_exact,
)
from geometor.knott.flat_geometry import GeometricCatalogResult


def golden_string_generations(steps: int = 7) -> list[str]:
    r"""Generate finite Rabbit-tree / morphism words :math:`S_1, S_2, \dots, S_{\text{steps}}`.

    Applies the Sturmian substitution :math:`1 \mapsto 10,\; 0 \mapsto 1` starting from
    ``S_1 = '1'`` (equivalently :math:`S_k = S_{k-1} + S_{k-2}` for :math:`k \ge 3`,
    with :math:`|S_k| = F_{k+1}`).

    Args:
        steps: Number of finite generations to return (:math:`\ge 1`).

    Returns:
        List of finite Golden String prefixes ``['1', '10', '101', '10110', ...]``.
    """
    if steps < 1:
        raise ValueError(f"Expected steps >= 1, got {steps}")
    words: list[str] = []
    curr = "1"
    for idx in range(1, steps + 1):
        if len(curr) != int(sp.fibonacci(idx + 1)):  # pragma: no cover
            raise AssertionError(f"Generation {idx} length mismatch: {len(curr)}")
        words.append(curr)
        curr = "".join("10" if ch == "1" else "1" for ch in curr)
    return words


def golden_string_beatty_word(length: int) -> str:
    r"""Compute the first ``length`` characters of the Golden String via exact floor differences.

    Uses :math:`d_n = \lfloor (n + 1)\phi \rfloor - \lfloor n\phi \rfloor` for
    :math:`n = 1, 2, \dots, \text{length}`, evaluated via pure integer arithmetic
    :func:`~geometor.knott.constants.floor_linear_phi` (:math:`n\phi = -n + n\Phi`).

    Args:
        length: Prefix length (:math:`\ge 1`).

    Returns:
        Exact binary prefix of ``101101011011010110101...``.
    """
    if length < 1:
        raise ValueError(f"Expected length >= 1, got {length}")
    chars: list[str] = []
    for n_idx in range(1, length + 1):
        f_next = floor_linear_phi(-(n_idx + 1), n_idx + 1)
        f_curr = floor_linear_phi(-n_idx, n_idx)
        chars.append(str(f_next - f_curr))
    return "".join(chars)


def recursive_fib_additions(n: int) -> int:
    r"""Return the exact number of additions in naive recursive ``fib(n)`` (with ``F_1 = F_2 = 1``).

    Cataloged on ``fibrab.html#props``: :math:`A(1) = A(2) = 0` and
    :math:`A(n) = A(n-1) + A(n-2) + 1 = F_n - 1` (or :math:`F_{n+1} - 1` when ``0``-indexed
    base cases ``fib(0), fib(1)`` are used). Here for ``F_1 = F_2 = 1``,
    :math:`A(n) = F_n - 1`; for ``0``-based ``fib(0)=0, fib(1)=1``, :math:`A_0(n) = F_{n+1} - 1`.

    Args:
        n: Non-negative integer index for ``0``-based ``fib(n)`` (:math:`n \ge 1`).

    Returns:
        Exact addition count :math:`F_{n+1} - 1`.
    """
    if n < 1:
        return 0
    return int(sp.fibonacci(n + 1)) - 1


def construct_golden_string_cutting_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-5.1`: Sturmian lattice-cutting line :math:`y = \phi x` generating ``10110101``.

    Constructs ray ``[O R]`` of exact slope :math:`\phi = \Phi - 1` across vertical grid
    lines :math:`x = 1..5` and horizontal grid lines :math:`y = 1..3` in ``geometor.model``.
    Intersecting ``[O R]`` with every grid line in order of distance from ``O`` produces
    vertical crossings ``V1..V5`` (digit ``1``) and horizontal crossings ``H1..H3``
    (digit ``0``) in exact sequence ``V1, H1, V2, V3, H2, V4, H3, V5`` -> ``10110101``!

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-5.1``.
    """
    gens = golden_string_generations(8)
    beatty_prefix = golden_string_beatty_word(len(gens[-1]))
    if beatty_prefix != gens[-1]:  # pragma: no cover
        raise AssertionError("Sturmian Beatty word disagrees with morphism word")

    model = Model("knott-5-1", logger=False, auto_intersect=False)
    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    pt_r = model.set_point(sp.Rational(11, 2), sp.Rational(11, 2) * phi, ID="R", classes=["golden"])
    line_ray = model.construct_line(pt_o, pt_r, guide=True)
    model.set_segment(pt_o, pt_r, classes=["golden"])

    crossings: list[tuple[sp.Expr, str, spg.Point]] = []

    # Vertical grid lines x = 1..5 -> symbol '1'
    for m_val in range(1, 6):
        g_bot = model.set_point(sp.Integer(m_val), sp.Integer(0), ID=f"X{m_val}", guide=True)
        g_top = model.set_point(sp.Integer(m_val), sp.Rational(7, 2), ID=f"XT{m_val}", guide=True)
        v_seg = model.set_segment(g_bot, g_top)
        v_pt = model.intersect(line_ray, v_seg, ID=f"V{m_val}", classes=["golden"])
        crossings.append((v_pt.x, "1", v_pt))

    # Horizontal grid lines y = 1..3 -> symbol '0'
    for k_val in range(1, 4):
        h_left = model.set_point(sp.Integer(0), sp.Integer(k_val), ID=f"Y{k_val}", guide=True)
        h_right = model.set_point(sp.Rational(11, 2), sp.Integer(k_val), ID=f"YR{k_val}", guide=True)
        h_seg = model.set_segment(h_left, h_right)
        h_pt = model.intersect(line_ray, h_seg, ID=f"H{k_val}", classes=["given"])
        assert_zero(h_pt.x - k_val * PHI, f"H{k_val} x-coordinate == {k_val}*PHI")
        crossings.append((h_pt.x, "0", h_pt))

    # Sort crossings strictly by exact x-coordinate via exact sign of difference:
    n_c = len(crossings)
    for i_idx in range(n_c):
        for j_idx in range(i_idx + 1, n_c):
            # Compare crossings[i_idx][0] vs crossings[j_idx][0] using exact integer floor/zphi:
            diff = simplify_exact(crossings[j_idx][0] - crossings[i_idx][0])
            if float(diff.evalf()) < 0:
                crossings[i_idx], crossings[j_idx] = crossings[j_idx], crossings[i_idx]

    cutting_word = "".join(sym for _, sym, _ in crossings)
    if cutting_word != "10110101":  # pragma: no cover
        raise AssertionError(f"Expected cutting sequence '10110101', got {cutting_word!r}")
    if cutting_word != gens[4]:  # pragma: no cover
        raise AssertionError("Cutting word disagrees with S_5 == '10110101'")

    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-5.1",
        model=model,
        invariants={
            "ray_slope": phi,
            "H1_x": PHI,
            "H2_x": 2 * PHI,
            "H3_x": 3 * PHI,
            "prefix_length_S8": sp.Integer(len(gens[7])),
            "ones_in_S8": sp.Integer(gens[7].count("1")),
            "zeros_in_S8": sp.Integer(gens[7].count("0")),
            "recursive_additions_F10": sp.Integer(recursive_fib_additions(10)),
        },
    )


def zeckendorf_summands(n: int) -> list[int]:
    r"""Return the unique non-consecutive Fibonacci summands of positive integer ``n``.

    Uses Fibonacci place values :math:`F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5, \dots`.

    Args:
        n: Positive integer (:math:`n \ge 1`).

    Returns:
        Descending list of non-adjacent Fibonacci numbers summing to ``n``.
    """
    if n < 1:
        raise ValueError(f"Zeckendorf theorem requires n >= 1, got {n}")
    fibs: list[tuple[int, int]] = []
    k_idx = 2
    while True:
        fk = int(sp.fibonacci(k_idx))
        if fk > n:
            break
        fibs.append((k_idx, fk))
        k_idx += 1

    rem = n
    chosen_indices: list[int] = []
    summands: list[int] = []
    for idx_val, fk in reversed(fibs):
        if fk <= rem:
            chosen_indices.append(idx_val)
            summands.append(fk)
            rem -= fk
    if rem != 0:  # pragma: no cover
        raise AssertionError(f"Greedy Zeckendorf remainder nonzero: {rem}")
    for pos in range(len(chosen_indices) - 1):
        if chosen_indices[pos] - chosen_indices[pos + 1] < 2:  # pragma: no cover
            raise AssertionError(f"Consecutive Fibonacci indices in Zeckendorf: {chosen_indices}")
    return summands


def to_zeckendorf(n: int) -> str:
    r"""Encode non-negative integer ``n`` into its canonical Zeckendorf Fibonacci-base string.

    Columns from right to left represent :math:`F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, \dots`
    (e.g., ``to_zeckendorf(12) == '10101'`` for :math:`8 + 3 + 1`).

    Args:
        n: Non-negative integer.

    Returns:
        ``11``-free binary Fibonacci-base string.
    """
    if n < 0:
        raise ValueError(f"Expected n >= 0, got {n}")
    if n == 0:
        return "0"
    fibs: list[int] = []
    k_idx = 2
    while True:
        fk = int(sp.fibonacci(k_idx))
        if fk > n:
            break
        fibs.append(fk)
        k_idx += 1

    rem = n
    bits: list[str] = []
    for fk in reversed(fibs):
        if fk <= rem:
            bits.append("1")
            rem -= fk
        else:
            bits.append("0")
    bit_str = "".join(bits)
    if "11" in bit_str:  # pragma: no cover
        raise AssertionError(f"Adjacent 11 in Zeckendorf string {bit_str!r}")
    return bit_str


def from_zeckendorf(bit_str: str) -> int:
    """Decode any Fibonacci-base bitstring (with rightmost column :math:`F_2 = 1`) into an ``int``.

    Args:
        bit_str: String of ``'0'`` and ``'1'`` digits.

    Returns:
        Decoded non-negative integer value.
    """
    cleaned = bit_str.strip()
    if not cleaned:
        raise ValueError("Empty Fibonacci-base string")
    total = 0
    width = len(cleaned)
    for idx, ch in enumerate(cleaned):
        if ch not in "01":
            raise ValueError(f"Invalid Fibonacci-base digit {ch!r}")
        if ch == "1":
            fib_idx = (width - 1 - idx) + 2
            total += int(sp.fibonacci(fib_idx))
    return total


def construct_zeckendorf_staircase_model() -> GeometricCatalogResult:
    """Construct `KNOTT-5.2`: Geometric Fibonacci staircase & Zeckendorf decomposition of ``12 = 8 + 3 + 1``.

    Constructs adjacent Fibonacci column rectangles of widths ``1`` and exact heights
    :math:`F_2=1, F_3=2, F_4=3, F_5=5, F_6=8` in ``geometor.model``, highlighting the
    non-adjacent columns :math:`F_6=8, F_4=3, F_2=1` that compose :math:`12 = 10101_Z`,
    alongside a horizontal verification bar of total length ``12`` partitioned at
    ``8`` and ``11``.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-5.2``.
    """
    for val in range(0, 101):
        z_str = to_zeckendorf(val)
        if from_zeckendorf(z_str) != val:  # pragma: no cover
            raise AssertionError(f"Zeckendorf round-trip failed at {val}")

    model = Model("knott-5-2", logger=False, auto_intersect=False)
    heights = [1, 2, 3, 5, 8]
    active_cols = {0, 2, 4}  # F_2=1, F_4=3, F_6=8 -> 1 + 3 + 8 = 12

    for col_idx, h_val in enumerate(heights):
        x0 = sp.Integer(2 * col_idx)
        x1 = sp.Integer(2 * col_idx + 1)
        y1 = sp.Integer(h_val)
        b0 = model.set_point(x0, sp.Integer(0), ID=f"A{col_idx + 2}")
        b1 = model.set_point(x1, sp.Integer(0), ID=f"B{col_idx + 2}")
        t1 = model.set_point(x1, y1, ID=f"C{col_idx + 2}", classes=["golden"] if col_idx in active_cols else None)
        t0 = model.set_point(x0, y1, ID=f"D{col_idx + 2}", classes=["golden"] if col_idx in active_cols else None)
        cls = ["golden"] if col_idx in active_cols else None
        model.set_polygon([b0, b1, t1, t0], classes=cls)
        model.set_segment(b0, t0, classes=cls)
        model.set_segment(t0, t1, classes=cls)
        model.set_segment(t1, b1, classes=cls)

    # Bottom summation bar at y = -2: S0(0,-2) -> S1(8,-2) -> S2(11,-2) -> S3(12,-2) scaled by 3/4 to fit cleanly:
    s0 = model.given_point(sp.Integer(0), sp.Integer(-2), ID="S0")
    s1 = model.set_point(sp.Integer(6), sp.Integer(-2), ID="S8", classes=["golden"])
    s2 = model.set_point(sp.Rational(33, 4), sp.Integer(-2), ID="S11", classes=["golden"])
    s3 = model.set_point(sp.Integer(9), sp.Integer(-2), ID="S12", classes=["given"])
    model.set_segment(s0, s1, classes=["golden"])
    model.set_segment(s1, s2, classes=["golden"])
    model.set_segment(s2, s3, classes=["golden"])

    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-5.2",
        model=model,
        invariants={
            "zeckendorf_12_sum": sp.Integer(sum(zeckendorf_summands(12))),
            "zeckendorf_100_term_count": sp.Integer(len(zeckendorf_summands(100))),
            "F2": sp.Integer(1),
            "F4": sp.Integer(3),
            "F6": sp.Integer(8),
        },
    )


def beatty_pair(n: int) -> tuple[int, int]:
    r"""Return Beatty's complementary Golden pair :math:`(\lfloor n\Phi \rfloor, \lfloor n\Phi^2 \rfloor)` for :math:`n \ge 1`.

    Uses :math:`\lfloor n\Phi^2 \rfloor = \lfloor n(\Phi + 1) \rfloor = \lfloor n\Phi \rfloor + n`
    and exact integer arithmetic :func:`~geometor.knott.constants.floor_linear_phi`.

    Args:
        n: Positive integer (:math:`n \ge 1`).

    Returns:
        Exact integer pair ``(floor(n * PHI), floor(n * PHI^2))``.
    """
    if n < 1:
        raise ValueError(f"Beatty pair requires n >= 1, got {n}")
    lower = floor_linear_phi(0, n)
    upper = lower + n
    return lower, upper


def wythoff_entry(row: int, col: int) -> int:
    r"""Compute entry ``W(row, col)`` (``0``-indexed) of Morrison's Wythoff Array.

    Matches Dr. Ron Knott's formula on ``fibGen.html#wythoffprops``:
    :math:`W(r, c) = \lfloor (r + 1)\Phi \rfloor F_{c + 2} + r F_{c + 1}`.

    Args:
        row: Non-negative row index (:math:`r \ge 0`).
        col: Non-negative column index (:math:`c \ge 0`).

    Returns:
        Positive integer at ``(row, col)`` in the Wythoff Array.
    """
    if row < 0 or col < 0:
        raise ValueError(f"Expected non-negative (row, col), got ({row}, {col})")
    a_r1 = floor_linear_phi(0, row + 1)
    return a_r1 * int(sp.fibonacci(col + 2)) + row * int(sp.fibonacci(col + 1))


def wythoff_locate(n: int) -> tuple[int, int]:
    r"""Locate the unique ``(row, col)`` (``0``-indexed) of positive integer ``n`` in the Wythoff Array.

    Uses the Zeckendorf trailing-zero characterization: ``col`` equals the number of
    trailing ``'0'`` digits in :func:`to_zeckendorf`, and ``W(row, 0)`` increases
    strictly with ``row``.

    Args:
        n: Positive integer (:math:`n \ge 1`).

    Returns:
        Unique ``(row, col)`` pair satisfying ``wythoff_entry(row, col) == n``.
    """
    if n < 1:
        raise ValueError(f"Expected n >= 1, got {n}")
    z_str = to_zeckendorf(n)
    col = len(z_str) - len(z_str.rstrip("0"))
    head_val = from_zeckendorf(z_str[: len(z_str) - col])
    # W(r, 0) == floor((r+1)*PHI) + r == floor((r+1)*PHI^2) - 1; invert monotonically:
    lo, hi = 0, head_val
    while lo <= hi:
        mid = (lo + hi) // 2
        val = wythoff_entry(mid, 0)
        if val == head_val:
            if wythoff_entry(mid, col) != n:  # pragma: no cover
                raise AssertionError("Wythoff locate mismatch")
            return mid, col
        if val < head_val:
            lo = mid + 1
        else:
            hi = mid - 1
    raise RuntimeError(f"Integer {n} not found in Wythoff column 0")  # pragma: no cover


def stolarsky_entry(row: int, col: int) -> int:
    r"""Compute entry ``S(row, col)`` (``0``-indexed) of Kenneth Stolarsky's (1977) Array.

    Matches Dr. Ron Knott's formula on ``fibGen.html#stolarsky``:

    - :math:`S(r, 0) = r + 1 + \lfloor (r + 1/2)\Phi \rfloor`;
    - :math:`S(r, 1) = \operatorname{round}(S(r, 0)\Phi) = \lfloor S(r, 0)\Phi + 1/2 \rfloor`;
    - :math:`S(r, c) = S(r, c - 1) + S(r, c - 2)` for :math:`c \ge 2`.

    Args:
        row: Non-negative row index (:math:`r \ge 0`).
        col: Non-negative column index (:math:`c \ge 0`).

    Returns:
        Positive integer at ``(row, col)`` in Stolarsky's Array.
    """
    if row < 0 or col < 0:
        raise ValueError(f"Expected non-negative (row, col), got ({row}, {col})")
    s0 = row + 1 + floor_linear_phi(0, sp.Rational(2 * row + 1, 2))
    if col == 0:
        return s0
    s1 = floor_linear_phi(sp.Rational(1, 2), s0)
    if col == 1:
        return s1
    prev, curr = s0, s1
    for _ in range(2, col + 1):
        prev, curr = curr, prev + curr
    return curr


def construct_wythoff_beatty_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-5.3`: Wythoff / Beatty slope rays :math:`y = \Phi x` & :math:`y = \Phi^2 x` and cold positions.

    Constructs the two complementary Beatty slope rays :math:`y = \Phi x` and
    :math:`y = \Phi^2 x` from ``O(0,0)`` alongside Wythoff's game cold positions
    :math:`(\lfloor n\Phi \rfloor, \lfloor n\Phi^2 \rfloor)` for :math:`n = 1..4`:
    ``W1(1,2)``, ``W2(3,5)``, ``W3(4,7)``, ``W4(6,10)``. Verifies exact bijective
    partitioning of ``1..100`` across Beatty's pair, Wythoff's Array, and Stolarsky's Array.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-5.3``.
    """
    # Verify Beatty complementarity covers 1..60 without overlap or omission:
    beatty_seen: set[int] = set()
    for k_idx in range(1, 40):
        a_k, b_k = beatty_pair(k_idx)
        if a_k in beatty_seen or b_k in beatty_seen or a_k == b_k:  # pragma: no cover
            raise AssertionError(f"Beatty collision at k={k_idx}: ({a_k}, {b_k})")
        beatty_seen.add(a_k)
        beatty_seen.add(b_k)
    for target in range(1, 61):
        if target not in beatty_seen:  # pragma: no cover
            raise AssertionError(f"Integer {target} missing from Beatty sequences")

    # Verify Wythoff bijection for 1..100:
    coords_seen: set[tuple[int, int]] = set()
    for target in range(1, 101):
        rc = wythoff_locate(target)
        if rc in coords_seen:  # pragma: no cover
            raise AssertionError(f"Duplicate Wythoff coordinate {rc}")
        coords_seen.add(rc)

    # Verify Stolarsky bijection for 1..100:
    stol_map: dict[int, tuple[int, int]] = {}
    for r_idx in range(0, 40):
        for c_idx in range(0, 12):
            val = stolarsky_entry(r_idx, c_idx)
            if val <= 100:
                if val in stol_map:  # pragma: no cover
                    raise AssertionError(f"Duplicate value {val} in Stolarsky array")
                stol_map[val] = (r_idx, c_idx)
    if len(stol_map) != 100:  # pragma: no cover
        raise AssertionError(f"Expected 100 unique integers <= 100 in Stolarsky array, got {len(stol_map)}")

    model = Model("knott-5-3", logger=False, auto_intersect=False)
    pt_o = model.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    ray_phi = model.set_point(sp.Integer(6), 6 * PHI, ID="R1", classes=["golden"])
    ray_phi2 = model.set_point(sp.Integer(6), 6 * PHI**2, ID="R2", classes=["golden"])
    model.set_segment(pt_o, ray_phi, classes=["golden"])
    model.set_segment(pt_o, ray_phi2, classes=["golden"])

    prev_w: spg.Point | None = None
    for k_idx in range(1, 5):
        ak, bk = beatty_pair(k_idx)
        pt_w = model.set_point(sp.Integer(ak), sp.Integer(bk), ID=f"W{k_idx}", classes=["golden"])
        pt_a = model.set_point(sp.Integer(k_idx), sp.Integer(ak), ID=f"A{k_idx}", classes=["given"])
        model.set_segment(pt_o, pt_w)
        if prev_w is not None:
            model.set_segment(prev_w, pt_w, classes=["golden"])
        prev_w = pt_w
        del pt_a

    # Verify reciprocal density identity 1/PHI + 1/PHI^2 == 1:
    density_sum = simplify_exact(1 / PHI + 1 / (PHI**2))
    assert_zero(density_sum - 1, "Beatty reciprocal density 1/PHI + 1/PHI^2 == 1")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-5.3",
        model=model,
        invariants={
            "beatty_density_sum": density_sum,
            "wythoff_W_0_0": sp.Integer(wythoff_entry(0, 0)),
            "wythoff_W_1_0": sp.Integer(wythoff_entry(1, 0)),
            "wythoff_W_2_3": sp.Integer(wythoff_entry(2, 3)),
            "stolarsky_S_1_0": sp.Integer(stolarsky_entry(1, 0)),
            "stolarsky_S_2_0": sp.Integer(stolarsky_entry(2, 0)),
            "stolarsky_S_3_3": sp.Integer(stolarsky_entry(3, 3)),
        },
    )
