"""Theme-adaptive ``.euclid-graphic`` SVG serializer for ``geometor.model.Model``.

Generates canonical Digital Scriptorium ``.euclid-graphic`` SVGs with:

- Exact 3-vertex midpoint ``<path>`` segments (supporting ``#geom-tick-1..3`` equality markers);
- Dedicated ``#elements``, ``#graphics``, ``#highlights``, ``#points``, and ``#labels`` groups;
- Canonical ``data-ref`` tokens (``A``, ``/ A B /``, ``[ A B ]``, ``( A B )``, ``< A B C >``);
- Automatic non-colliding radial label placement around vertices.
"""

from __future__ import annotations

import html
import math
from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

_STANDALONE_STYLE = """    svg.euclid-graphic .geom-golden {
      stroke: #e0911b;
      stroke-width: 2.3;
    }
    svg.euclid-graphic polygon.geom-golden {
      fill: #e0911b;
      fill-opacity: 0.16;
      stroke: #e0911b;
      stroke-width: 1.8;
    }
    svg.euclid-graphic .geom-overlay {
      opacity: 0;
      fill: none;
      stroke: none;
      stroke-width: 0;
    }"""

_TICK_DEFS = """  <defs>
    <marker id="geom-tick-1" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="0" y1="-5" x2="0" y2="5" stroke="#16a34a" stroke-width="2.0" stroke-linecap="round" class="geom-tick-mark" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="-2" y1="-5" x2="-2" y2="5" stroke="#16a34a" stroke-width="2.0" stroke-linecap="round" class="geom-tick-mark" />
      <line x1="2" y1="-5" x2="2" y2="5" stroke="#16a34a" stroke-width="2.0" stroke-linecap="round" class="geom-tick-mark" />
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" orient="auto" markerUnits="userSpaceOnUse">
      <line x1="-3.5" y1="-5" x2="-3.5" y2="5" stroke="#16a34a" stroke-width="2.0" stroke-linecap="round" class="geom-tick-mark" />
      <line x1="0" y1="-5" x2="0" y2="5" stroke="#16a34a" stroke-width="2.0" stroke-linecap="round" class="geom-tick-mark" />
      <line x1="3.5" y1="-5" x2="3.5" y2="5" stroke="#16a34a" stroke-width="2.0" stroke-linecap="round" class="geom-tick-mark" />
    </marker>
  </defs>"""


def _pt_xy(pt: spg.Point, scale: float) -> tuple[float, float]:
    """Convert an exact SymPy point into SVG coordinates with ``+y`` upward."""
    return (float(pt.x.evalf()) * scale, -float(pt.y.evalf()) * scale)


def _clip_line_to_box(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    xmin: float,
    ymin: float,
    xmax: float,
    ymax: float,
) -> tuple[float, float, float, float] | None:
    """Clip the infinite line through ``(x1, y1)`` and ``(x2, y2)`` to a bounding box."""
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) < 1e-9 and abs(dy) < 1e-9:
        return None
    hits: list[tuple[float, float]] = []
    if abs(dx) >= 1e-9:
        for xb in (xmin, xmax):
            t_val = (xb - x1) / dx
            yb = y1 + t_val * dy
            if ymin - 1e-6 <= yb <= ymax + 1e-6:
                hits.append((xb, max(ymin, min(ymax, yb))))
    if abs(dy) >= 1e-9:
        for yb in (ymin, ymax):
            t_val = (yb - y1) / dy
            xb = x1 + t_val * dx
            if xmin - 1e-6 <= xb <= xmax + 1e-6:
                hits.append((max(xmin, min(xmax, xb)), yb))
    unique_hits: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(math.hypot(hx - ux, hy - uy) < 1e-4 for ux, uy in unique_hits):
            unique_hits.append((hx, hy))
    if len(unique_hits) < 2:
        return None
    unique_hits.sort()
    return (unique_hits[0][0], unique_hits[0][1], unique_hits[-1][0], unique_hits[-1][1])


def _semantic_classes(base_class: str, classes_dict: dict[str, str], guide: bool) -> str:
    """Compose semantic CSS class list matching ``_geometor.scss`` conventions."""
    tokens = [base_class]
    if guide or "guide" in classes_dict:
        tokens.append("geom-dashed")
        tokens.append("geom-guide")
    if "golden" in classes_dict or "result" in classes_dict:
        tokens.append("geom-golden")
    if "given" in classes_dict:
        tokens.append("geom-given")
    if "bisector" in classes_dict:
        tokens.append("geom-bisector")
    return " ".join(tokens)


def render_euclid_svg(
    model: Model,
    *,
    folio_id: str,
    graphic_num: str = "g1",
    target_size: float = 520.0,
    padding: float = 48.0,
    include_circles_in_bbox: bool = True,
    label_overrides: dict[str, tuple[float, float]] | None = None,
) -> str:
    """Serialize an exact :class:`geometor.model.Model` into a ``.euclid-graphic`` SVG string.

    Args:
        model: Populated exact :class:`geometor.model.Model`.
        folio_id: Canonical item slug (e.g., ``"knott-1-1"``).
        graphic_num: Graphic identifier within the item (defaults to ``"g1"``).
        target_size: Target pixel span of the primary geometry before padding.
        padding: Outer margin in SVG units around the bounding box.
        include_circles_in_bbox: Whether non-guide circles expand the viewport bounding box.
        label_overrides: Optional ``{point_ID: (dx_px, dy_px)}`` manual label offsets.

    Returns:
        Complete UTF-8 SVG document string.
    """
    raw_coords: list[tuple[float, float]] = []
    for elem, details in model.items():
        if isinstance(elem, spg.Point):
            if not details.guide:
                raw_coords.append((float(elem.x.evalf()), -float(elem.y.evalf())))
        elif isinstance(elem, spg.Circle) and include_circles_in_bbox and not details.guide:
            cx = float(elem.center.x.evalf())
            cy = -float(elem.center.y.evalf())
            rad = float(elem.radius.evalf())
            raw_coords.extend([(cx - rad, cy - rad), (cx + rad, cy + rad)])

    if not raw_coords:
        for elem in model:
            if isinstance(elem, spg.Point):
                raw_coords.append((float(elem.x.evalf()), -float(elem.y.evalf())))

    xs = [pt[0] for pt in raw_coords] or [0.0, 1.0]
    ys = [pt[1] for pt in raw_coords] or [0.0, 1.0]
    span = max(max(xs) - min(xs), max(ys) - min(ys), 1e-6)
    scale = target_size / span

    sxs = [x * scale for x in xs]
    sys_vals = [y * scale for y in ys]
    xmin = min(sxs) - padding
    xmax = max(sxs) + padding
    ymin = min(sys_vals) - padding
    ymax = max(sys_vals) + padding
    width = xmax - xmin
    height = ymax - ymin

    cx_all = 0.5 * (min(sxs) + max(sxs))
    cy_all = 0.5 * (min(sys_vals) + max(sys_vals))

    elements_svg: list[str] = []
    graphics_svg: list[str] = []
    highlights_svg: list[str] = []
    points_svg: list[str] = []
    labels_svg: list[str] = []

    incident_dirs: dict[str, list[tuple[float, float]]] = {}
    point_positions: dict[str, tuple[float, float, bool, dict[str, str]]] = {}

    for elem, details in model.items():
        if isinstance(elem, spg.Point) and details.ID:
            px, py = _pt_xy(elem, scale)
            point_positions[str(details.ID)] = (px, py, bool(details.guide), dict(details.classes))
            incident_dirs.setdefault(str(details.ID), [])

    for elem, details in model.items():
        ref_raw = str(details.ID or "")
        ref = html.escape(ref_raw, quote=True)
        cls_map = dict(details.classes)
        is_guide = bool(details.guide) or ("guide" in cls_map)
        is_golden = ("golden" in cls_map) or ("result" in cls_map)

        if isinstance(elem, spg.Circle):
            cx, cy = _pt_xy(elem.center, scale)
            rad = float(elem.radius.evalf()) * scale
            css = _semantic_classes("geom-circle", cls_map, is_guide)
            c_stroke = "#e0911b" if is_golden else "#18181b"
            c_op = "0.45" if is_guide else ("0.85" if is_golden else "0.60")
            dash_attr = ' stroke-dasharray="4, 3"' if is_guide else ""
            elements_svg.append(
                f'    <circle data-ref="{ref}" data-type="circle" fill="none" '
                f'stroke="{c_stroke}" stroke-width="1.4" stroke-opacity="{c_op}"{dash_attr} '
                f'cx="{cx:.2f}" cy="{cy:.2f}" r="{rad:.2f}" class="{css}" />'
            )
            highlights_svg.append(
                f'    <circle data-ref="{ref}" data-type="circle" fill="none" opacity="0" '
                f'cx="{cx:.2f}" cy="{cy:.2f}" r="{rad:.2f}" class="geom-overlay" />'
            )

        elif isinstance(elem, spg.Line) and not isinstance(elem, spg.Segment):
            x1, y1 = _pt_xy(elem.p1, scale)
            x2, y2 = _pt_xy(elem.p2, scale)
            clipped = _clip_line_to_box(
                x1,
                y1,
                x2,
                y2,
                xmin + 8.0,
                ymin + 8.0,
                xmax - 8.0,
                ymax - 8.0,
            )
            if clipped is not None:
                lx1, ly1, lx2, ly2 = clipped
                css = _semantic_classes("geom-line", cls_map, is_guide)
                l_stroke = "#e0911b" if is_golden else "#18181b"
                l_op = "0.45" if is_guide else "0.60"
                dash_attr = ' stroke-dasharray="4, 3"' if is_guide else ""
                elements_svg.append(
                    f'    <line data-ref="{ref}" data-type="line" fill="none" '
                    f'stroke="{l_stroke}" stroke-width="1.3" stroke-opacity="{l_op}"{dash_attr} '
                    f'x1="{lx1:.2f}" y1="{ly1:.2f}" x2="{lx2:.2f}" y2="{ly2:.2f}" class="{css}" />'
                )
                highlights_svg.append(
                    f'    <line data-ref="{ref}" data-type="line" fill="none" opacity="0" '
                    f'x1="{lx1:.2f}" y1="{ly1:.2f}" x2="{lx2:.2f}" y2="{ly2:.2f}" class="geom-overlay" />'
                )

        elif isinstance(elem, spg.Polygon):
            v_coords = [_pt_xy(v, scale) for v in elem.vertices]
            pts_attr = " ".join(f"{vx:.2f},{vy:.2f}" for vx, vy in v_coords)
            base_poly_cls = (
                "geom-polygon geom-polygon-gnomon"
                if is_golden
                else "geom-polygon geom-polygon-bordered"
            )
            css = _semantic_classes(base_poly_cls, cls_map, is_guide)
            p_stroke = "#e0911b" if is_golden else "#18181b"
            p_fill_op = "0.16" if is_golden else "0.07"
            graphics_svg.insert(
                0,
                f'    <polygon data-ref="{ref}" data-type="polygon" '
                f'fill="#e0911b" fill-opacity="{p_fill_op}" stroke="{p_stroke}" '
                f'stroke-width="1.5" stroke-linejoin="round" '
                f'points="{pts_attr}" class="{css}" />',
            )
            highlights_svg.insert(
                0,
                f'    <polygon data-ref="{ref}" data-type="polygon" fill="none" opacity="0" '
                f'points="{pts_attr}" class="geom-overlay" />',
            )
            n_v = len(elem.vertices)
            for idx, v_pt in enumerate(elem.vertices):
                if v_pt in model and model[v_pt].ID:
                    pid = str(model[v_pt].ID)
                    vx, vy = v_coords[idx]
                    for nb_idx in ((idx - 1) % n_v, (idx + 1) % n_v):
                        nx, ny = v_coords[nb_idx]
                        dist = math.hypot(nx - vx, ny - vy)
                        if dist > 1e-6:
                            incident_dirs.setdefault(pid, []).append(((nx - vx) / dist, (ny - vy) / dist))

        elif isinstance(elem, spg.Segment):
            x1, y1 = _pt_xy(elem.p1, scale)
            x2, y2 = _pt_xy(elem.p2, scale)
            mx = 0.5 * (x1 + x2)
            my = 0.5 * (y1 + y2)
            d_attr = f"M {x1:.2f} {y1:.2f} L {mx:.2f} {my:.2f} L {x2:.2f} {y2:.2f}"
            css = _semantic_classes("geom-line geom-segment", cls_map, is_guide)
            s_stroke = "#e0911b" if is_golden else "#18181b"
            s_width = "2.3" if is_golden else ("1.4" if is_guide else "1.9")
            dash_attr = ' stroke-dasharray="4, 3" stroke-opacity="0.50"' if is_guide else ""
            graphics_svg.append(
                f'    <path data-ref="{ref}" data-type="segment" fill="none" '
                f'stroke="{s_stroke}" stroke-width="{s_width}" stroke-linecap="round"{dash_attr} '
                f'd="{d_attr}" class="{css}" />'
            )
            highlights_svg.append(
                f'    <path data-ref="{ref}" data-type="segment" fill="none" opacity="0" '
                f'd="{d_attr}" class="geom-overlay" />'
            )
            dist = math.hypot(x2 - x1, y2 - y1)
            if dist > 1e-6:
                if elem.p1 in model and model[elem.p1].ID:
                    incident_dirs.setdefault(str(model[elem.p1].ID), []).append(
                        ((x2 - x1) / dist, (y2 - y1) / dist)
                    )
                if elem.p2 in model and model[elem.p2].ID:
                    incident_dirs.setdefault(str(model[elem.p2].ID), []).append(
                        ((x1 - x2) / dist, (y1 - y2) / dist)
                    )

    overrides = label_overrides or {}
    placed_labels: list[tuple[float, float]] = []

    for pid, (px, py, is_guide, cls_map) in point_positions.items():
        if is_guide and "labeled" not in cls_map:
            continue
        esc_pid = html.escape(pid, quote=True)
        radius = 4.2 if ("golden" in cls_map or "result" in cls_map or "given" in cls_map) else 3.6
        points_svg.append(
            f'    <circle data-ref="{esc_pid}" data-type="point" '
            f'fill="#18181b" stroke="#faf8f2" stroke-width="1.4" '
            f'cx="{px:.2f}" cy="{py:.2f}" r="{radius:.1f}" class="geom-point" />'
        )

        if pid in overrides:
            dx_off, dy_off = overrides[pid]
            lx, ly = px + dx_off, py + dy_off
        else:
            out_x = px - cx_all
            out_y = py - cy_all
            out_norm = math.hypot(out_x, out_y)
            if out_norm > 1e-6:
                out_x /= out_norm
                out_y /= out_norm
            else:
                out_x, out_y = 0.0, -1.0

            dirs = incident_dirs.get(pid, [])
            best_score = -1e9
            best_vec = (out_x, out_y)
            for k_ang in range(24):
                theta = (2.0 * math.pi * k_ang) / 24.0
                ux = math.cos(theta)
                uy = math.sin(theta)
                min_ang_sep = min(
                    (1.0 - (ux * ix + uy * iy) for ix, iy in dirs),
                    default=1.0,
                )
                outward_bonus = 0.35 * (ux * out_x + uy * out_y)
                cand_lx = px + 18.0 * ux
                cand_ly = py + 18.0 * uy
                collision_penalty = sum(
                    2.0
                    for ex_lx, ex_ly in placed_labels
                    if math.hypot(cand_lx - ex_lx, cand_ly - ex_ly) < 18.0
                )
                score = min_ang_sep + outward_bonus - collision_penalty
                if score > best_score:
                    best_score = score
                    best_vec = (ux, uy)
            lx = px + 18.0 * best_vec[0]
            ly = py + 18.0 * best_vec[1]

        placed_labels.append((lx, ly))
        labels_svg.append(
            f'    <text data-ref="{esc_pid}" x="{lx:.2f}" y="{ly:.2f}" '
            f'fill="#18181b" font-family="Georgia, serif" font-style="italic" font-size="15" '
            f'text-anchor="middle" dominant-baseline="central" class="geom-label">{esc_pid}</text>'
        )

    graphic_id = f"{folio_id}.{graphic_num}"
    clip_id = f"clip-{folio_id}-{graphic_num}"
    clip_def = (
        f'    <clipPath id="{html.escape(clip_id, quote=True)}">\n'
        f'      <rect x="{xmin:.2f}" y="{ymin:.2f}" width="{width:.2f}" height="{height:.2f}" />\n'
        f"    </clipPath>"
    )
    defs_with_clip = _TICK_DEFS.replace("  </defs>", f"{clip_def}\n  </defs>")
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="{xmin:.2f} {ymin:.2f} {width:.2f} {height:.2f}" '
        f'width="{width:.1f}" height="{height:.1f}" '
        f'class="euclid-graphic" '
        f'data-graphic-id="{html.escape(graphic_id, quote=True)}" '
        f'data-folio="{html.escape(folio_id, quote=True)}" '
        f'data-graphic="{html.escape(graphic_num, quote=True)}">',
        "  <style>",
        _STANDALONE_STYLE,
        "  </style>",
        defs_with_clip,
        f'  <g id="elements" clip-path="url(#{html.escape(clip_id, quote=True)})">',
        *elements_svg,
        "  </g>",
        '  <g id="graphics">',
        *graphics_svg,
        "  </g>",
        f'  <g id="highlights" clip-path="url(#{html.escape(clip_id, quote=True)})" style="pointer-events: none;">',
        *highlights_svg,
        "  </g>",
        '  <g id="points">',
        *points_svg,
        "  </g>",
        '  <g id="labels">',
        *labels_svg,
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(lines)


def write_euclid_svg(
    model: Model,
    output_path: Path,
    *,
    folio_id: str,
    graphic_num: str = "g1",
    target_size: float = 520.0,
    padding: float = 48.0,
    include_circles_in_bbox: bool = True,
    label_overrides: dict[str, tuple[float, float]] | None = None,
) -> Path:
    """Render and write an exact ``.euclid-graphic`` SVG file to ``output_path``.

    Args:
        model: Populated exact :class:`geometor.model.Model`.
        output_path: Destination ``.svg`` filesystem path.
        folio_id: Canonical item slug (e.g., ``"knott-1-1"``).
        graphic_num: Graphic identifier within the item (defaults to ``"g1"``).
        target_size: Target pixel span of the primary geometry before padding.
        padding: Outer margin in SVG units around the bounding box.
        include_circles_in_bbox: Whether non-guide circles expand the viewport bounding box.
        label_overrides: Optional ``{point_ID: (dx_px, dy_px)}`` manual label offsets.

    Returns:
        Resolved ``output_path``.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    svg_text = render_euclid_svg(
        model,
        folio_id=folio_id,
        graphic_num=graphic_num,
        target_size=target_size,
        padding=padding,
        include_circles_in_bbox=include_circles_in_bbox,
        label_overrides=label_overrides,
    )
    output_path.write_text(svg_text, encoding="utf-8")
    return output_path
