"""Collection 3: 3D Golden Geometry of Solids (`KNOTT-3.1` through `KNOTT-3.3`).

Catalogs the exact 3D algebraic coordinates, edge lengths, dihedral spreads,
volumes, 5-cube compounds, and acute/obtuse golden quasicrystal rhombohedra curated
by Dr. Ron Knott on ``phi3DGeom.html``, paired with exact rational axonometric
2D projections into ``geometor.model.Model``.
"""

from __future__ import annotations

from itertools import combinations

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

from geometor.knott.constants import (
    PHI,
    assert_no_floats,
    assert_zero,
    phi,
    simplify_exact,
)
from geometor.knott.flat_geometry import GeometricCatalogResult

Point3D = tuple[sp.Expr, sp.Expr, sp.Expr]


def project_3d_to_2d(pt3: Point3D) -> tuple[sp.Expr, sp.Expr]:
    r"""Project an exact 3D point ``(x, y, z)`` to 2D via an injective rational cabinet matrix.

    Uses exact rational coefficients :math:`(X, Y) = (x - \frac{2}{5} y,\; z - \frac{1}{4} y + \frac{1}{7} x)`
    so no floating-point approximations enter :class:`geometor.model.Model` and symmetric
    polyhedral vertices remain distinct in the plane.

    Args:
        pt3: Exact 3D coordinate triple ``(x, y, z)``.

    Returns:
        Exact 2D coordinate pair ``(X, Y)``.
    """
    x_c, y_c, z_c = pt3
    px = simplify_exact(x_c - sp.Rational(2, 5) * y_c)
    py = simplify_exact(z_c - sp.Rational(1, 4) * y_c + sp.Rational(1, 7) * x_c)
    return px, py


def quadrance_3d(a: Point3D, b: Point3D) -> sp.Expr:
    """Compute exact 3D Euclidean quadrance :math:`(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2`.

    Args:
        a: First 3D point.
        b: Second 3D point.

    Returns:
        Exact symbolic squared distance in 3D.
    """
    return simplify_exact((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)


def _cross_3d(u: Point3D, v: Point3D) -> Point3D:
    """Return exact 3D cross product ``u x v``."""
    return (
        simplify_exact(u[1] * v[2] - u[2] * v[1]),
        simplify_exact(u[2] * v[0] - u[0] * v[2]),
        simplify_exact(u[0] * v[1] - u[1] * v[0]),
    )


def _dot_3d(u: Point3D, v: Point3D) -> sp.Expr:
    """Return exact 3D dot product ``u . v``."""
    return simplify_exact(u[0] * v[0] + u[1] * v[1] + u[2] * v[2])


def icosahedron_vertices_3d() -> dict[str, Point3D]:
    """Return the 12 exact vertices of the regular icosahedron spanned by 3 golden rectangles.

    Returns:
        Ordered mapping of vertex IDs (``X1..X4``, ``Y1..Y4``, ``Z1..Z4``) to 3D points.
    """
    one = sp.Integer(1)
    zero = sp.Integer(0)
    return {
        # Rectangle in yz-plane (x = 0):
        "X1": (zero, one, PHI),
        "X2": (zero, -one, PHI),
        "X3": (zero, -one, -PHI),
        "X4": (zero, one, -PHI),
        # Rectangle in zx-plane (y = 0):
        "Y1": (PHI, zero, one),
        "Y2": (PHI, zero, -one),
        "Y3": (-PHI, zero, -one),
        "Y4": (-PHI, zero, one),
        # Rectangle in xy-plane (z = 0):
        "Z1": (one, PHI, zero),
        "Z2": (-one, PHI, zero),
        "Z3": (-one, -PHI, zero),
        "Z4": (one, -PHI, zero),
    }


def dodecahedron_vertices_3d() -> dict[str, Point3D]:
    r"""Return the 20 exact vertices of the regular dodecahedron of edge :math:`2\phi`.

    Combines the 8 cube vertices :math:`(\pm 1, \pm 1, \pm 1)` (``C1..C8``) with the
    12 cyclic permutations of :math:`(0, \pm\phi, \pm\Phi)` (``D1..D12``).

    Returns:
        Ordered mapping of 20 vertex IDs to exact 3D coordinate triples.
    """
    one = sp.Integer(1)
    zero = sp.Integer(0)
    return {
        "C1": (one, one, one),
        "C2": (one, -one, one),
        "C3": (-one, -one, one),
        "C4": (-one, one, one),
        "C5": (one, one, -one),
        "C6": (one, -one, -one),
        "C7": (-one, -one, -one),
        "C8": (-one, one, -one),
        "D1": (zero, phi, PHI),
        "D2": (zero, -phi, PHI),
        "D3": (zero, -phi, -PHI),
        "D4": (zero, phi, -PHI),
        "D5": (PHI, zero, phi),
        "D6": (PHI, zero, -phi),
        "D7": (-PHI, zero, -phi),
        "D8": (-PHI, zero, phi),
        "D9": (phi, PHI, zero),
        "D10": (-phi, PHI, zero),
        "D11": (-phi, -PHI, zero),
        "D12": (phi, -PHI, zero),
    }


def construct_orthogonal_golden_rectangles_solids() -> GeometricCatalogResult:
    r"""Construct `KNOTT-3.1`: Three orthogonal golden rectangles & regular icosahedron/dodecahedron.

    Verifies in 3D that:

    - The 12 corners of three mutually perpendicular :math:`2 \times 2\Phi` golden
      rectangles form a regular icosahedron with 30 edges of length ``2``, 20 equilateral
      faces, exact volume :math:`20\Phi^2 / 3`, and rational dihedral spread :math:`4/9`;
    - The 20 vertices :math:`(\pm 1, \pm 1, \pm 1) \cup \operatorname{cyc}(0, \pm\phi, \pm\Phi)`
      form a regular dodecahedron with 30 edges of length :math:`2\phi`, exact volume
      :math:`8 + 4\Phi`, and rational dihedral spread :math:`4/5`.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-3.1``.
    """
    ico_v = icosahedron_vertices_3d()
    dod_v = dodecahedron_vertices_3d()

    # Verify all 30 icosahedron edges have exact quadrance 4 (length 2):
    ico_edges: list[tuple[str, str]] = []
    for k1, k2 in combinations(ico_v.keys(), 2):
        if quadrance_3d(ico_v[k1], ico_v[k2]) == 4:
            ico_edges.append((k1, k2))
    if len(ico_edges) != 30:  # pragma: no cover
        raise AssertionError(f"Expected 30 icosahedron edges, got {len(ico_edges)}")

    # Compute exact icosahedron volume by summing 20 triangular pyramid volumes:
    ico_adj = {k: set() for k in ico_v}
    for k1, k2 in ico_edges:
        ico_adj[k1].add(k2)
        ico_adj[k2].add(k1)
    ico_faces: list[tuple[str, str, str]] = []
    keys_list = list(ico_v.keys())
    for i_idx, k1 in enumerate(keys_list):
        for j_idx in range(i_idx + 1, len(keys_list)):
            k2 = keys_list[j_idx]
            if k2 not in ico_adj[k1]:
                continue
            for m_idx in range(j_idx + 1, len(keys_list)):
                k3 = keys_list[m_idx]
                if k3 in ico_adj[k1] and k3 in ico_adj[k2]:
                    ico_faces.append((k1, k2, k3))
    if len(ico_faces) != 20:  # pragma: no cover
        raise AssertionError(f"Expected 20 icosahedron faces, got {len(ico_faces)}")

    ico_vol = sp.Integer(0)
    for k1, k2, k3 in ico_faces:
        mat = sp.Matrix([ico_v[k1], ico_v[k2], ico_v[k3]])
        det_val = simplify_exact(mat.det())
        # Since origin is inside, abs(det) == det if positively oriented; check sign via evalf only to orient:
        oriented_det = det_val if float(det_val.evalf()) > 0 else -det_val
        ico_vol += oriented_det / sp.Integer(6)
    ico_vol = simplify_exact(ico_vol)
    assert_zero(ico_vol - sp.Rational(20, 3) * PHI**2, "Icosahedron volume == 20*PHI^2 / 3")

    # Dihedral spread between two faces sharing edge (X1, X2): (X1, X2, Y1) and (X1, X2, Y4)
    f1_u = tuple(ico_v["X2"][i] - ico_v["X1"][i] for i in range(3))
    f1_v = tuple(ico_v["Y1"][i] - ico_v["X1"][i] for i in range(3))
    f2_v = tuple(ico_v["Y4"][i] - ico_v["X1"][i] for i in range(3))
    n1 = _cross_3d(f1_u, f1_v)  # type: ignore[arg-type]
    n2 = _cross_3d(f1_u, f2_v)  # type: ignore[arg-type]
    ico_dihedral_spread = simplify_exact(
        1 - (_dot_3d(n1, n2) ** 2) / (_dot_3d(n1, n1) * _dot_3d(n2, n2))
    )
    assert_zero(ico_dihedral_spread - sp.Rational(4, 9), "Icosahedron dihedral spread == 4/9")

    # Verify dodecahedron has 30 edges of exact quadrance 4*phi^2:
    four_phi_sq = sp.expand(4 * phi**2)
    dod_edges = [
        (k1, k2)
        for k1, k2 in combinations(dod_v.keys(), 2)
        if sp.expand(quadrance_3d(dod_v[k1], dod_v[k2]) - four_phi_sq) == 0
    ]
    if len(dod_edges) != 30:  # pragma: no cover
        raise AssertionError(f"Expected 30 dodecahedron edges, got {len(dod_edges)}")

    # Dihedral spread between two pentagonal faces sharing edge (D1, D2):
    # Pentagonal face 1 contains D1(0,phi,PHI), D2(0,-phi,PHI), C1(1,1,1), C2(1,-1,1), D5(PHI,0,phi)
    # Pentagonal face 2 contains D1, D2, C4(-1,1,1), C3(-1,-1,1), D8(-PHI,0,phi)
    dn1 = _cross_3d(
        tuple(dod_v["D2"][i] - dod_v["D1"][i] for i in range(3)),  # type: ignore[arg-type]
        tuple(dod_v["C1"][i] - dod_v["D1"][i] for i in range(3)),  # type: ignore[arg-type]
    )
    dn2 = _cross_3d(
        tuple(dod_v["D2"][i] - dod_v["D1"][i] for i in range(3)),  # type: ignore[arg-type]
        tuple(dod_v["C4"][i] - dod_v["D1"][i] for i in range(3)),  # type: ignore[arg-type]
    )
    dod_dihedral_spread = simplify_exact(
        1 - (_dot_3d(dn1, dn2) ** 2) / (_dot_3d(dn1, dn1) * _dot_3d(dn2, dn2))
    )
    assert_zero(dod_dihedral_spread - sp.Rational(4, 5), "Dodecahedron dihedral spread == 4/5")

    # Build 2D axonometric geometor.model of the 3 orthogonal golden rectangles + icosahedron hull:
    model = Model("knott-3-1", logger=False, auto_intersect=False)
    pts2d: dict[str, spg.Point] = {}
    for vid, p3 in ico_v.items():
        px, py = project_3d_to_2d(p3)
        cls = ["golden"] if vid.startswith("X") else ["given"]
        pts2d[vid] = model.set_point(px, py, ID=vid, classes=cls)

    # Three orthogonal golden rectangles:
    model.set_polygon([pts2d["X1"], pts2d["X2"], pts2d["X3"], pts2d["X4"]], classes=["golden"])
    model.set_polygon([pts2d["Y1"], pts2d["Y2"], pts2d["Y3"], pts2d["Y4"]])
    model.set_polygon([pts2d["Z1"], pts2d["Z2"], pts2d["Z3"], pts2d["Z4"]])

    for k1, k2 in ico_edges:
        is_rect_short = (k1[0] == k2[0])
        model.set_segment(
            pts2d[k1],
            pts2d[k2],
            classes=["golden"] if is_rect_short else None,
        )

    assert_no_floats(model)

    dod_vol = simplify_exact(
        sp.Rational(15, 4) * (2 * phi) ** 3 + sp.Rational(7, 4) * sp.sqrt(5) * (2 * phi) ** 3
    )
    assert_zero(dod_vol - (8 + 4 * PHI), "Dodecahedron volume == 8 + 4*PHI")

    return GeometricCatalogResult(
        canonical_id="KNOTT-3.1",
        model=model,
        invariants={
            "icosahedron_edge": sp.Integer(2),
            "icosahedron_volume": ico_vol,
            "icosahedron_dihedral_spread": ico_dihedral_spread,
            "dodecahedron_edge": simplify_exact(2 * phi),
            "dodecahedron_volume": dod_vol,
            "dodecahedron_dihedral_spread": dod_dihedral_spread,
        },
    )


def find_five_cubes_in_dodecahedron() -> list[tuple[str, ...]]:
    r"""Discover all 5 inscribed cubes of edge ``2`` among the 20 dodecahedron vertices.

    Each cube is an 8-element subset of :func:`dodecahedron_vertices_3d` in which
    every vertex has 3 orthogonal neighbors at exact 3D quadrance ``4`` (face diagonal
    of a regular pentagon of side :math:`2\phi`, since :math:`\Phi \cdot 2\phi = 2`).

    Returns:
        Sorted list of 5 8-tuples of vertex IDs partitioning the 60 face diagonals.
    """
    dod_v = dodecahedron_vertices_3d()
    coord_to_id = {
        (sp.expand(vp[0]), sp.expand(vp[1]), sp.expand(vp[2])): vid
        for vid, vp in dod_v.items()
    }
    diag_adj: dict[str, set[str]] = {k: set() for k in dod_v}
    for k1, k2 in combinations(dod_v.keys(), 2):
        if quadrance_3d(dod_v[k1], dod_v[k2]) == 4:
            diag_adj[k1].add(k2)
            diag_adj[k2].add(k1)

    cubes_set: set[tuple[str, ...]] = set()
    for v0, nbrs in diag_adj.items():
        for e1, e2, e3 in combinations(sorted(nbrs), 3):
            p0 = dod_v[v0]
            u1 = tuple(dod_v[e1][i] - p0[i] for i in range(3))
            u2 = tuple(dod_v[e2][i] - p0[i] for i in range(3))
            u3 = tuple(dod_v[e3][i] - p0[i] for i in range(3))
            if (
                _dot_3d(u1, u2) == 0  # type: ignore[arg-type]
                and _dot_3d(u2, u3) == 0  # type: ignore[arg-type]
                and _dot_3d(u3, u1) == 0  # type: ignore[arg-type]
            ):
                cube_ids: list[str] = []
                for c1 in (0, 1):
                    for c2 in (0, 1):
                        for c3 in (0, 1):
                            target = (
                                sp.expand(p0[0] + c1 * u1[0] + c2 * u2[0] + c3 * u3[0]),
                                sp.expand(p0[1] + c1 * u1[1] + c2 * u2[1] + c3 * u3[1]),
                                sp.expand(p0[2] + c1 * u1[2] + c2 * u2[2] + c3 * u3[2]),
                            )
                            matched_id = coord_to_id.get(target)
                            if matched_id is not None:
                                cube_ids.append(matched_id)
                if len(cube_ids) == 8:
                    cubes_set.add(tuple(sorted(cube_ids)))

    cubes = sorted(cubes_set)
    if len(cubes) != 5:  # pragma: no cover
        raise AssertionError(f"Expected 5 inscribed cubes in dodecahedron, got {len(cubes)}")
    return cubes


def construct_cube_in_dodecahedron_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-3.2`: Inscribed cube & compound of five cubes in a dodecahedron.

    Constructs the 20-vertex regular dodecahedron of edge :math:`2\phi`, highlights
    primary inscribed cube ``C1..C8`` of edge ``2`` (whose 12 edges are one face
    diagonal on each of the 12 pentagonal faces), and verifies all 5 inscribed cubes
    partition the 60 face diagonals with every dodecahedron vertex shared by 2 cubes.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-3.2``.
    """
    dod_v = dodecahedron_vertices_3d()
    cubes = find_five_cubes_in_dodecahedron()

    # Verify vertex incidence (every one of 20 vertices lies in exactly 2 cubes):
    counts = {vid: 0 for vid in dod_v}
    for cube in cubes:
        for vid in cube:
            counts[vid] += 1
    if any(cnt != 2 for cnt in counts.values()):  # pragma: no cover
        raise AssertionError(f"Cube vertex incidence mismatch: {counts}")

    model = Model("knott-3-2", logger=False, auto_intersect=False)
    pts2d: dict[str, spg.Point] = {}
    for vid, p3 in dod_v.items():
        px, py = project_3d_to_2d(p3)
        is_primary_cube = vid.startswith("C")
        pts2d[vid] = model.set_point(
            px,
            py,
            ID=vid,
            classes=["golden"] if is_primary_cube else None,
        )

    # 30 dodecahedron edges:
    four_phi_sq = sp.expand(4 * phi**2)
    for k1, k2 in combinations(dod_v.keys(), 2):
        if sp.expand(quadrance_3d(dod_v[k1], dod_v[k2]) - four_phi_sq) == 0:
            model.set_segment(pts2d[k1], pts2d[k2])

    # Highlight primary cube C1..C8 (12 edges of length 2):
    primary_cube_ids = [f"C{i}" for i in range(1, 9)]
    model.set_polygon([pts2d["C1"], pts2d["C2"], pts2d["C3"], pts2d["C4"]], classes=["golden"])
    for k1, k2 in combinations(primary_cube_ids, 2):
        if quadrance_3d(dod_v[k1], dod_v[k2]) == 4:
            model.set_segment(pts2d[k1], pts2d[k2], classes=["golden"])

    cube_edge = sp.Integer(2)
    dod_edge = simplify_exact(2 * phi)
    edge_ratio = simplify_exact(cube_edge / dod_edge)
    assert_zero(edge_ratio - PHI, "Cube edge / Dodecahedron edge == PHI")
    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-3.2",
        model=model,
        invariants={
            "cube_count": sp.Integer(len(cubes)),
            "cubes_per_vertex": sp.Integer(2),
            "cube_edge": cube_edge,
            "dodecahedron_edge": dod_edge,
            "face_diagonal_to_edge_ratio": edge_ratio,
            "cube_volume": sp.Integer(8),
            "volume_ratio_dodecahedron_to_cube": simplify_exact((8 + 4 * PHI) / 8),
        },
    )


def construct_golden_rhombohedra_model() -> GeometricCatalogResult:
    r"""Construct `KNOTT-3.3`: Acute & obtuse golden rhombohedra (3D quasicrystal tiles).

    Spans the acute (prolate) golden rhombohedron from icosahedral vectors
    :math:`u_1=(0,1,\Phi), u_2=(1,\Phi,0), u_3=(\Phi,0,1)` and the obtuse (oblate)
    golden rhombohedron from :math:`v_1=(0,1,\Phi), v_2=(1,-\Phi,0), v_3=(-\Phi,0,-1)`
    (translated alongside for visual comparison). Every rhombic face has exact
    diagonals :math:`2\Phi` and ``2`` (ratio :math:`\Phi : 1`), exact volumes
    :math:`V_{\text{acute}} = 2\Phi^2` and :math:`V_{\text{obtuse}} = 2\Phi`
    (ratio :math:`\Phi : 1`), and 10 of each assemble the rhombic triacontahedron
    of volume :math:`20\Phi^3`.

    Returns:
        Verified :class:`GeometricCatalogResult` for ``KNOTT-3.3``.
    """
    zero = sp.Integer(0)
    one = sp.Integer(1)

    u1: Point3D = (zero, one, PHI)
    u2: Point3D = (one, PHI, zero)
    u3: Point3D = (PHI, zero, one)

    v1: Point3D = (zero, one, PHI)
    v2: Point3D = (one, -PHI, zero)
    v3: Point3D = (-PHI, zero, -one)

    # Verify all 6 spanning vectors have identical quadrance PHI + 2, and face diagonals 2*PHI and 2:
    for vec in (u1, u2, u3, v1, v2, v3):
        assert_zero(_dot_3d(vec, vec) - (PHI + 2), "rhombohedron edge quadrance == PHI + 2")

    long_diag_q = quadrance_3d((zero, zero, zero), tuple(u1[i] + u2[i] for i in range(3)))  # type: ignore[arg-type]
    short_diag_q = quadrance_3d((zero, zero, zero), tuple(u1[i] - u2[i] for i in range(3)))  # type: ignore[arg-type]
    assert_zero(long_diag_q - 4 * PHI**2, "long face diagonal == 2*PHI")
    assert_zero(short_diag_q - 4, "short face diagonal == 2")

    obtuse_long_q = quadrance_3d((zero, zero, zero), tuple(v1[i] - v2[i] for i in range(3)))  # type: ignore[arg-type]
    obtuse_short_q = quadrance_3d((zero, zero, zero), tuple(v1[i] + v2[i] for i in range(3)))  # type: ignore[arg-type]
    assert_zero(obtuse_long_q - 4 * PHI**2, "obtuse long face diagonal == 2*PHI")
    assert_zero(obtuse_short_q - 4, "obtuse short face diagonal == 2")

    vol_acute = simplify_exact(-sp.Matrix([u1, u2, u3]).det())
    vol_obtuse = simplify_exact(-sp.Matrix([v1, v2, v3]).det())
    assert_zero(vol_acute - 2 * PHI**2, "V_acute == 2*PHI^2")
    assert_zero(vol_obtuse - 2 * PHI, "V_obtuse == 2*PHI")
    assert_zero(simplify_exact(vol_acute / vol_obtuse) - PHI, "V_acute / V_obtuse == PHI")

    triacontahedron_vol = simplify_exact(10 * vol_acute + 10 * vol_obtuse)
    assert_zero(triacontahedron_vol - 20 * PHI**3, "Rhombic triacontahedron volume == 20*PHI^3")

    model = Model("knott-3-3", logger=False, auto_intersect=False)

    # Acute rhombohedron A0..A7 at origin:
    acute_map: dict[tuple[int, int, int], spg.Point] = {}
    acute_labels = {
        (0, 0, 0): "A0",
        (1, 0, 0): "A1",
        (0, 1, 0): "A2",
        (0, 0, 1): "A3",
        (1, 1, 0): "A4",
        (1, 0, 1): "A5",
        (0, 1, 1): "A6",
        (1, 1, 1): "A7",
    }
    for bits, lbl in acute_labels.items():
        p3 = tuple(
            simplify_exact(bits[0] * u1[i] + bits[1] * u2[i] + bits[2] * u3[i])
            for i in range(3)
        )
        px, py = project_3d_to_2d(p3)  # type: ignore[arg-type]
        acute_map[bits] = model.set_point(px, py, ID=lbl, classes=["golden"])

    model.set_polygon(
        [acute_map[(0, 0, 0)], acute_map[(1, 0, 0)], acute_map[(1, 1, 0)], acute_map[(0, 1, 0)]],
        classes=["golden"],
    )
    for b1, b2 in combinations(acute_labels.keys(), 2):
        if sum(abs(b1[i] - b2[i]) for i in range(3)) == 1:
            model.set_segment(acute_map[b1], acute_map[b2], classes=["golden"])

    # Obtuse rhombohedron B0..B7 shifted along +x by 5 units for clean side-by-side comparison:
    shift: Point3D = (sp.Integer(5), zero, zero)
    obtuse_map: dict[tuple[int, int, int], spg.Point] = {}
    obtuse_labels = {
        (0, 0, 0): "B0",
        (1, 0, 0): "B1",
        (0, 1, 0): "B2",
        (0, 0, 1): "B3",
        (1, 1, 0): "B4",
        (1, 0, 1): "B5",
        (0, 1, 1): "B6",
        (1, 1, 1): "B7",
    }
    for bits, lbl in obtuse_labels.items():
        p3 = tuple(
            simplify_exact(shift[i] + bits[0] * v1[i] + bits[1] * v2[i] + bits[2] * v3[i])
            for i in range(3)
        )
        px, py = project_3d_to_2d(p3)  # type: ignore[arg-type]
        obtuse_map[bits] = model.set_point(px, py, ID=lbl)

    model.set_polygon(
        [obtuse_map[(0, 0, 0)], obtuse_map[(1, 0, 0)], obtuse_map[(1, 1, 0)], obtuse_map[(0, 1, 0)]]
    )
    for b1, b2 in combinations(obtuse_labels.keys(), 2):
        if sum(abs(b1[i] - b2[i]) for i in range(3)) == 1:
            model.set_segment(obtuse_map[b1], obtuse_map[b2])

    assert_no_floats(model)

    return GeometricCatalogResult(
        canonical_id="KNOTT-3.3",
        model=model,
        invariants={
            "edge_quadrance": simplify_exact(PHI + 2),
            "face_diagonal_ratio": PHI,
            "volume_acute": vol_acute,
            "volume_obtuse": vol_obtuse,
            "volume_ratio_acute_to_obtuse": simplify_exact(vol_acute / vol_obtuse),
            "triacontahedron_volume": triacontahedron_vol,
        },
    )
