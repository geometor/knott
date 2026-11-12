r"""Original GEOMETOR mathematical expositions and interactive ``:g:``/``:eq:`` bindings.

Provides bespoke, copyright-clean constructive proofs and mathematical commentary
for all 22 catalog entries (``KNOTT-1.1`` – ``KNOTT-6.5``), binding prose tokens
directly to verified ``.euclid-graphic`` ``data-ref`` attributes.
"""

from __future__ import annotations

ITEM_EXPOSITIONS: dict[str, str] = {
    "KNOTT-1.1": r"""
Constructive Synthesis & Exact Proof
------------------------------------

:person:`Dr. Ron Knott <knott>` opens his 2D Golden Geometry survey (:cite:`KnottPhi2D`)
by pairing the two complementary compass-and-straightedge problems of :person:`Euclid <euclid>`
(:cite:`EuclidElements`, Books II.11 and VI.30): extending a given straight segment
externally in :term:`extreme and mean ratio <extreme-and-mean-ratio>`, and dividing
the same segment internally.

1. **External Golden Extension**: Starting from given segment :g:`AB <knott-1-1.g1:A; knott-1-1.g1:B>`
   of length :math:`2` and erecting square :g:`ABCD <knott-1-1.g1:< A B C D >>`, bisect the
   base at :g:`M <knott-1-1.g1:M>` so segment :g:`MC <knott-1-1.g1:/ M C />` has exact
   :term:`quadrance` :math:`Q(M, C) = 1^2 + 2^2 = 5`. Sweeping guide circle
   :g:`(M, C) <knott-1-1.g1:( M C )>` onto line :g:`[AB] <knott-1-1.g1:[ A B ]>` beyond
   :g:`B <knott-1-1.g1:B>` determines :g:`E <knott-1-1.g1:E>` with
   :g:`AE <knott-1-1.g1:/ A E />` :math:`= 1 + \sqrt{5} = 2\Phi` and
   :g:`BE <knott-1-1.g1:/ B E />` :math:`= \sqrt{5} - 1 = 2\phi`, completing Golden
   Rectangle :g:`AEFD <knott-1-1.g1:< A E F D >>` above :g:`F <knott-1-1.g1:F>`.
2. **Internal Golden Division**: Joining :g:`A <knott-1-1.g1:A>` to midpoint
   :g:`H <knott-1-1.g1:H>` of :math:`BC` produces :g:`AH <knott-1-1.g1:/ A H />` of length
   :math:`\sqrt{5}`. Unit circle :g:`(H, B) <knott-1-1.g1:( H B )>` cuts :g:`AH <knott-1-1.g1:/ A H />`
   at :g:`K <knott-1-1.g1:K>` (:math:`AK = \sqrt{5} - 1 = 2\phi`), and circle
   :g:`(A, K) <knott-1-1.g1:( A K )>` transfers that length onto the base at internal
   golden cut :g:`G <knott-1-1.g1:G>`. Thus major internal segment :g:`AG <knott-1-1.g1:/ A G />`
   and external overhang :g:`BE <knott-1-1.g1:/ B E />` are :eq:`equal <knott-1-1.g1:/ A G / = knott-1-1.g1:/ B E />`
   (:math:`2\phi`), leaving minor segment :g:`GB <knott-1-1.g1:/ G B />` :math:`= 2\phi^2` and
   fixing the projective :term:`cross-ratio` :math:`(A, E; G, B) = \phi^2 = 2 - \Phi`.
""".strip(),
    "KNOTT-1.2": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Extending the midpoint-circle construction (:cite:`KnottPhi2D`) symmetrically to
both sides of unit square :g:`ABCD <knott-1-2.g1:< A B C D >>` centered on base
midpoint :g:`M <knott-1-2.g1:M>`, circle :g:`(M, C) <knott-1-2.g1:( M C )>` of radius
:math:`\sqrt{5}/2` meets base line :g:`[AB] <knott-1-2.g1:[ A B ]>` at both
:g:`E <knott-1-2.g1:E>` (:math:`x = \Phi`) and :g:`W <knott-1-2.g1:W>` (:math:`x = -\phi`).

* **Root-5 & Golden Rectangles**: Because :math:`\Phi + \phi = \sqrt{5}`, segment
  :g:`WE <knott-1-2.g1:/ W E />` spans exact width :math:`\sqrt{5}`, framing
  :person:`Luca Pacioli <pacioli>`'s and Jay Hambidge's :math:`1 \times \sqrt{5}`
  dynamic-symmetry rectangle :g:`WEFN <knott-1-2.g1:< W E F N >>` (:cite:`Hambidge1920`)
  partitioned into central unit square :g:`ABCD <knott-1-2.g1:< A B C D >>` and two
  flanking :math:`\phi \times 1` :term:`golden rectangles <golden-rectangle>`, including
  right :term:`gnomon` :g:`BEFC <knott-1-2.g1:< B E F C >>`.
* **Orthogonal Whirling-Square Diagonals**: Subdividing :g:`BEFC <knott-1-2.g1:< B E F C >>`
  recursively via golden cuts :g:`G2G1 <knott-1-2.g1:/ G2 G1 />`,
  :g:`H1H2 <knott-1-2.g1:/ H1 H2 />`, and :g:`J1J2 <knott-1-2.g1:/ J1 J2 />` aligns every
  successive square corner along the two diagonals :g:`AF <knott-1-2.g1:/ A F />` (slope
  :math:`1/\Phi = \phi`) and :g:`EC <knott-1-2.g1:/ E C />` (slope :math:`-1/\phi = -\Phi`).
  Since :math:`\phi \cdot (-\Phi) = -1`, lines :g:`[AF] <knott-1-2.g1:[ A F ]>` and
  :g:`[EC] <knott-1-2.g1:[ E C ]>` meet at exact :term:`spread` :math:`s = 1`
  (perpendicularity) at the self-similar spiral eye :g:`P <knott-1-2.g1:P>`
  :math:`= (\Phi^2/\sqrt{5},\; \Phi/\sqrt{5})`.
""".strip(),
    "KNOTT-1.3": r"""
Constructive Synthesis & Exact Proof
------------------------------------

In *Elements* IV.10 (:cite:`EuclidElements`), :person:`Euclid <euclid>` constructs
an isosceles triangle having each base angle double the apex angle; :person:`Dr. Ron Knott <knott>`
(:cite:`KnottPhi2D`) develops its paired acute/obtuse :term:`gnomon` recursion as the
backbone of pentagonal geometry.

* **Acute Golden Triangle & Bisector Deflation**: Over unit base :g:`AB <knott-1-3.g1:/ A B />`,
  sweeping radius :math:`\Phi` from :g:`A <knott-1-3.g1:A>` and :g:`B <knott-1-3.g1:B>`
  fixes apex :g:`C <knott-1-3.g1:C>` of acute :term:`golden triangle <golden-triangle>`
  :g:`ABC <knott-1-3.g1:< A B C >>`, whose legs :g:`AC <knott-1-3.g1:/ A C />` and
  :g:`BC <knott-1-3.g1:/ B C />` are :eq:`equal <knott-1-3.g1:/ A C / = knott-1-3.g1:/ B C />`
  with quadrance :math:`Q = \Phi^2 = \Phi + 1`. Intersecting leg :g:`BC <knott-1-3.g1:/ B C />`
  with unit circle :g:`(A, B) <knott-1-3.g1:( A B )>` at :g:`D <knott-1-3.g1:D>` makes
  bisector :g:`AD <knott-1-3.g1:/ A D />` and base :g:`AB <knott-1-3.g1:/ A B />`
  :eq:`equal <knott-1-3.g1:/ A B / = knott-1-3.g1:/ A D />` (:math:`AD = AB = CD = 1`),
  leaving :math:`BD = \Phi - 1 = \phi`.
* **Self-Similar Cascade & Exact Spreads**: Triangle :g:`ABC <knott-1-3.g1:< A B C >>`
  splits into obtuse :term:`golden gnomon <golden-gnomon>` :math:`\triangle CAD`
  (:math:`36^\circ\text{–}36^\circ\text{–}108^\circ`) and daughter acute golden triangle
  :g:`ABD <knott-1-3.g1:< A B D >>` of area ratio :math:`\Phi : 1`. Sweeping circle
  :g:`(D, B) <knott-1-3.g1:( D B )>` onto :g:`AC <knott-1-3.g1:/ A C />` at
  :g:`E <knott-1-3.g1:E>` (:g:`DE <knott-1-3.g1:/ D E />` :math:`= \phi`) repeats the
  deflation ad infinitum, with :person:`Norman J. Wildberger <wildberger>`'s exact
  pentagonal spreads :math:`s(36^\circ) = (5 - \sqrt{5})/8` and
  :math:`s(72^\circ) = (5 + \sqrt{5})/8` (:cite:`Wildberger2005`).
""".strip(),
    "KNOTT-1.4": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Every regular pentagon :g:`P0P1P2P3P4 <knott-1-4.g1:< P0 P1 P2 P3 P4 >>` of unit edge
:g:`P0P1 <knott-1-4.g1:/ P0 P1 />` :math:`= 1` is locked by golden triangles (:cite:`KnottPhi2D`,
:cite:`Pacioli1509`):

* **Pentagram Progression**: All five star diagonals—:g:`P0P2 <knott-1-4.g1:/ P0 P2 />`,
  :g:`P0P3 <knott-1-4.g1:/ P0 P3 />`, :g:`P1P3 <knott-1-4.g1:/ P1 P3 />`,
  :g:`P1P4 <knott-1-4.g1:/ P1 P4 />`, and :g:`P2P4 <knott-1-4.g1:/ P2 P4 />`—are
  :eq:`equal <knott-1-4.g1:/ P0 P2 / = knott-1-4.g1:/ P0 P3 / = knott-1-4.g1:/ P1 P3 />`
  of exact length :math:`\Phi`. Their pairwise intersections :g:`Q0 <knott-1-4.g1:Q0>`,
  :g:`Q1 <knott-1-4.g1:Q1>`, :g:`Q2 <knott-1-4.g1:Q2>`, :g:`Q3 <knott-1-4.g1:Q3>`, and
  :g:`Q4 <knott-1-4.g1:Q4>` bound a similar inverted inner pentagon
  :g:`Q0Q1Q2Q3Q4 <knott-1-4.g1:< Q0 Q1 Q2 Q3 Q4 >>` of side :math:`\phi^2 = 2 - \Phi`,
  dividing each :term:`pentagram` diagonal in the four-step geometric progression
  :math:`(Q_1 Q_2,\; P_0 Q_1,\; P_0 Q_2,\; P_0 P_2) = (\phi^2,\; \phi,\; 1,\; \Phi)`.
* **Overhand Paper-Strip Knot**: Dropping altitude :g:`P4H <knott-1-4.g1:/ P4 H />` from
  vertex :g:`P4 <knott-1-4.g1:P4>` onto the extended base line of :g:`P0P1 <knott-1-4.g1:/ P0 P1 />`
  (parallel to opposite diagonal :g:`P2P4 <knott-1-4.g1:/ P2 P4 />`) at :g:`H <knott-1-4.g1:H>`
  isolates the parallel strip width :math:`w = \sin 72^\circ = \frac{1}{4}\sqrt{10 + 2\sqrt{5}}`.
  Consequently, folding a uniform paper ribbon of width :math:`w = 1` into a flat overhand
  knot forces an exact regular pentagon of side quadrance
  :math:`Q_{\text{side}} = \sec^2 18^\circ = \frac{8}{5 + \sqrt{5}} = \frac{5 - \sqrt{5}}{5} \Phi^2`.
""".strip(),
    "KNOTT-1.5": r"""
Constructive Synthesis & Exact Proof
------------------------------------

In an October 1597 letter to Michael Mästlin, :person:`Johannes Kepler <kepler>` combined
the Pythagorean theorem with the Golden Ratio to isolate the unique right triangle whose
sides form a geometric progression (:cite:`KnottPhi2D`).

* **Euclidean Geometric-Mean Construction**: Along diameter segment from
  :g:`D <knott-1-5.g1:D>` :math:`(-1, 0)` through :g:`B <knott-1-5.g1:B>` :math:`(0, 0)` to
  :g:`E <knott-1-5.g1:E>` :math:`(\Phi, 0)`, Thales semicircle :g:`(O, E) <knott-1-5.g1:( O E )>`
  cuts the vertical axis at :g:`C <knott-1-5.g1:C>` :math:`(0, \sqrt{\Phi})` (*Elements*
  VI.13). In :term:`Kepler triangle <kepler-triangle>` :g:`DBC <knott-1-5.g1:< D B C >>`,
  short leg :g:`BD <knott-1-5.g1:/ B D />`, long leg :g:`BC <knott-1-5.g1:/ B C />`, and
  hypotenuse :g:`DC <knott-1-5.g1:/ D C />` (which is :eq:`equal <knott-1-5.g1:/ D C / = knott-1-5.g1:/ B E />`
  to golden segment :g:`BE <knott-1-5.g1:/ B E />`, joined by chord :g:`CE <knott-1-5.g1:/ C E />`)
  have exact :term:`quadrances <quadrance>` :math:`(1, \Phi, \Phi^2)` satisfying both
  :math:`Q_{BC}^2 = Q_{BD} Q_{DC}` and :math:`1 + \Phi = \Phi^2`.
* **Coincidence of Cosine & Tangent and Near-Quadrature**: At acute apex :g:`C <knott-1-5.g1:C>`,
  :math:`\cos\theta_C = \tan\theta_C = \sin\theta_D = 1/\sqrt{\Phi}` (:math:`\cos^2\theta_C = \tan^2\theta_C = \phi`).
  Erecting square :g:`BGFC <knott-1-5.g1:< B G F C >>` (via :g:`F <knott-1-5.g1:F>` and
  :g:`G <knott-1-5.g1:G>`) of perimeter :math:`4\sqrt{\Phi} \approx 5.08808` alongside
  circle :g:`(M, C) <knott-1-5.g1:( M C )>` centered at hypotenuse midpoint
  :g:`M <knott-1-5.g1:M>` of circumference :math:`\pi\Phi \approx 5.08320` exhibits the
  celebrated circle–square perimeter near-quadrature highlighted by Dr. Knott
  (:math:`4 / (\pi\sqrt{\Phi}) \approx 1.000959`, within :math:`0.096\%`).
""".strip(),
    "KNOTT-1.6": r"""
Constructive Synthesis & Exact Proof
------------------------------------

:person:`Roger Penrose <penrose>` (:cite:`Penrose1974`, :cite:`Gardner1977`) reduced
aperiodic five-fold planar tiling to two golden prototile families cataloged by
:person:`Dr. Ron Knott <knott>` (:cite:`KnottPhi2D`): **P2** (:person:`John Conway <conway>`'s
*kite* and *dart*) and **P3** (*thick* and *thin* golden rhombs).

* **P2 Kite & Dart Dissection**: Inside thick :math:`72^\circ\text{–}108^\circ` rhomb
  :math:`ABCD` whose four sides :g:`AB <knott-1-6.g1:/ A B />`, :g:`BC <knott-1-6.g1:/ B C />`,
  :g:`CD <knott-1-6.g1:/ C D />`, and :g:`DA <knott-1-6.g1:/ D A />` are
  :eq:`equal <knott-1-6.g1:/ A B / = knott-1-6.g1:/ B C / = knott-1-6.g1:/ C D / = knott-1-6.g1:/ D A />`
  of length :math:`\Phi`, long diagonal :g:`AC <knott-1-6.g1:/ A C />` has length
  :math:`\Phi^2 = \Phi + 1`. Marking :g:`K <knott-1-6.g1:K>` along :g:`AC <knott-1-6.g1:/ A C />`
  so :g:`AK <knott-1-6.g1:/ A K />`, :g:`BK <knott-1-6.g1:/ B K />`, and
  :g:`DK <knott-1-6.g1:/ D K />` are :eq:`equal <knott-1-6.g1:/ A K / = knott-1-6.g1:/ B K / = knott-1-6.g1:/ D K />`
  to :math:`1` (leaving kite spine :g:`KC <knott-1-6.g1:/ K C />` :math:`= \Phi`) partitions
  the rhomb into convex **kite** :g:`KBCD <knott-1-6.g1:< K B C D >>` (two acute golden
  triangles) and non-convex **dart** :g:`ABKD <knott-1-6.g1:< A B K D >>` (two obtuse
  golden gnomons) in exact area ratio :math:`\Phi : 1`.
* **P3 Thick & Thin Golden Rhombs**: Adjoining thin :math:`36^\circ\text{–}144^\circ`
  rhomb :g:`AFEB <knott-1-6.g1:< A F E B >>` along shared edge :g:`AB <knott-1-6.g1:/ A B />`
  (with edges :g:`AF <knott-1-6.g1:/ A F />`, :g:`FE <knott-1-6.g1:/ F E />`, and
  :g:`EB <knott-1-6.g1:/ E B />` of length :math:`\Phi`) yields interior spreads
  :math:`s(72^\circ) = (5+\sqrt{5})/8` vs. :math:`s(36^\circ) = (5-\sqrt{5})/8` and the
  identical area ratio :math:`\sin 72^\circ / \sin 36^\circ = 2\cos 36^\circ = \Phi`.
""".strip(),
    "KNOTT-2.1": r"""
Constructive Synthesis & Exact Proof
------------------------------------

On ``simpleTrig.html`` (:cite:`KnottSimpleTrig`), :person:`Dr. Ron Knott <knott>` derives
the closed-form quadratic radicals for every multiple of :math:`18^\circ` directly from
the golden isosceles triangle—linking :person:`Claudius Ptolemy <ptolemy>`'s chord table
to :person:`Norman J. Wildberger <wildberger>`'s Rational Trigonometry spreads
(:cite:`Wildberger2005`).

* **Unit-Circle Pentagonal Rays**: On unit circle :g:`(O, U) <knott-2-1.g1:( O U )>` bounded
  by orthogonal axes :g:`OU <knott-2-1.g1:/ O U />` and :g:`OV <knott-2-1.g1:/ O V />`,
  the four acute pentagonal rays :g:`OP18 <knott-2-1.g1:/ O P18 />`,
  :g:`OP36 <knott-2-1.g1:/ O P36 />`, :g:`OP54 <knott-2-1.g1:/ O P54 />`, and
  :g:`OP72 <knott-2-1.g1:/ O P72 />` are :eq:`equal <knott-2-1.g1:/ O U / = knott-2-1.g1:/ O P36 / = knott-2-1.g1:/ O P72 />`
  unit radii. Dropping altitudes :g:`P36C36 <knott-2-1.g1:/ P36 C36 />` (forming right
  triangle :g:`OC36P36 <knott-2-1.g1:< O C36 P36 >>`) and :g:`P72C72 <knott-2-1.g1:/ P72 C72 />`
  onto :g:`OU <knott-2-1.g1:/ O U />` projects :g:`C36 <knott-2-1.g1:C36>` at
  :math:`x = \cos 36^\circ = \Phi/2` and :g:`C72 <knott-2-1.g1:C72>` at
  :math:`x = \cos 72^\circ = \sin 18^\circ = \phi/2`.
* **Rational Difference, Product & Five-Fold Spread Factor**: Because :math:`\Phi - \phi = 1`
  and :math:`\Phi\phi = 1`, segment :g:`C72C36 <knott-2-1.g1:/ C72 C36 />` has exact
  rational length :math:`\cos 36^\circ - \cos 72^\circ = 1/2` while
  :math:`\cos 36^\circ \cdot \cos 72^\circ = 1/4`. Squaring the ordinates eliminates the
  nested square roots :math:`\sqrt{10 \pm 2\sqrt{5}}` completely, leaving pure
  :math:`\mathbb{Q}(\sqrt{5})` :term:`spreads <spread>` :math:`s(18^\circ) = (3 - \sqrt{5})/8`,
  :math:`s(36^\circ) = (5 - \sqrt{5})/8`, :math:`s(54^\circ) = (5 + \sqrt{5})/8`, and
  :math:`s(72^\circ) = (5 + \sqrt{5})/8`, where :math:`s(36^\circ)` and :math:`s(72^\circ)`
  are the exact roots of :math:`16 s^2 - 20 s + 5 = 0`.
""".strip(),
    "KNOTT-2.2": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Combining the pentagonal subfield :math:`\mathbb{Q}(\sqrt{5}, \sqrt{10 \pm 2\sqrt{5}})`
with the equilateral and half-right subfield :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})`
generates closed-form square-root radicals for **all 29 acute multiples of** :math:`3^\circ`
(:cite:`KnottSimpleTrig`).

* **Euclid IV.16 Regular 15-Gon & 3° Generator**: On unit circle :g:`(O, U) <knott-2-2.g1:( O U )>`,
  superimposing equilateral ray :g:`OP60 <knott-2-2.g1:/ O P60 />` (:math:`60^\circ`) and
  pentagonal ray :g:`OP72 <knott-2-2.g1:/ O P72 />` (:math:`72^\circ`) isolates the
  :math:`12^\circ` regular pentadecagon arc, making chord :g:`P60P72 <knott-2-2.g1:/ P60 P72 />`
  and origin-based chord :g:`UP12 <knott-2-2.g1:/ U P12 />`
  :eq:`equal <knott-2-2.g1:/ P60 P72 / = knott-2-2.g1:/ U P12 />`. Equivalently, subtracting
  Ailles' :math:`15^\circ` ray :g:`OP15 <knott-2-2.g1:/ O P15 />` from pentagonal ray
  :g:`OP18 <knott-2-2.g1:/ O P18 />` (or bisecting :g:`OP12 <knott-2-2.g1:/ O P12 />`
  through :g:`OP6 <knott-2-2.g1:/ O P6 />` to :g:`OP3 <knott-2-2.g1:/ O P3 />`) yields the
  atomic :term:`constructible angle <constructible-angle>` :math:`3^\circ = 18^\circ - 15^\circ`,
  whose chord :g:`P15P18 <knott-2-2.g1:/ P15 P18 />` and unit-base chord
  :g:`UP3 <knott-2-2.g1:/ U P3 />` are :eq:`equal <knott-2-2.g1:/ P15 P18 / = knott-2-2.g1:/ U P3 />`.
* **Gauss's Regular 17-Gon Bridge**: While :math:`1^\circ` cannot be constructed with
  compass and straightedge (requiring cube roots via angle trisection), :person:`Carl Friedrich Gauss <gauss>`
  (:cite:`Gauss1801`) proved that Fermat prime :math:`F_2 = 2^{2^2} + 1 = 17` admits a
  four-step quadratic radical tower for :math:`\cos(\pi / 17)`, verified here symbolically
  via Chebyshev's polynomial :math:`T_{17}(\cos(\pi / 17)) + 1 = 0`.
""".strip(),
    "KNOTT-3.1": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Moving from the plane into three-space (:cite:`KnottPhi3D`), :person:`Luca Pacioli <pacioli>`
(:cite:`Pacioli1509`) and :person:`H. S. M. Coxeter <coxeter>` (:cite:`Coxeter1973`)
showed that three congruent :math:`2 \times 2\Phi` :term:`golden rectangles <golden-rectangle>`
slotted symmetrically along the coordinate planes interlock to span the twelve vertices of
a regular icosahedron.

* **Three Orthogonal Golden Frames**: In our exact rational cabinet projection, golden
  rectangle :g:`X1X2X3X4 <knott-3-1.g1:< X1 X2 X3 X4 >>` in :math:`x = 0` (:math:`(0, \pm 1, \pm\Phi)`),
  :g:`Y1Y2Y3Y4 <knott-3-1.g1:< Y1 Y2 Y3 Y4 >>` in :math:`y = 0` (:math:`(\pm\Phi, 0, \pm 1)`),
  and :g:`Z1Z2Z3Z4 <knott-3-1.g1:< Z1 Z2 Z3 Z4 >>` in :math:`z = 0` (:math:`(\pm 1, \pm\Phi, 0)`)
  contribute six short edges of length :math:`2`—such as :g:`X1X2 <knott-3-1.g1:/ X1 X2 />`,
  :g:`Y1Y2 <knott-3-1.g1:/ Y1 Y2 />`, and :g:`Z1Z2 <knott-3-1.g1:/ Z1 Z2 />`—together with
  twenty-four inter-frame edges such as :g:`X1Y1 <knott-3-1.g1:/ X1 Y1 />`,
  :g:`X1Z1 <knott-3-1.g1:/ X1 Z1 />`, and :g:`Y1Z1 <knott-3-1.g1:/ Y1 Z1 />` whose 3D
  :term:`quadrance` is identically :math:`1^2 + (\Phi - 1)^2 + \Phi^2 = 1 + \phi^2 + \Phi^2 = 4`.
* **Exact Volumes & Rational Dihedral Spreads**: Summing all twenty triangular pyramids
  from the origin gives exact icosahedral volume :math:`\frac{20}{3}\Phi^2 = \frac{10(3+\sqrt{5})}{3}`,
  while dualizing via :math:`(\pm 1, \pm 1, \pm 1) \cup \operatorname{cyc}(0, \pm\phi, \pm\Phi)`
  yields the regular dodecahedron of edge :math:`2\phi` and volume :math:`8 + 4\Phi`. Both
  solids exhibit pure rational dihedral :term:`spreads <spread>` (:cite:`Wildberger2005`):
  :math:`s_{\text{ico}} = 4/9` and :math:`s_{\text{dod}} = 4/5`.
""".strip(),
    "KNOTT-3.2": r"""
Constructive Synthesis & Exact Proof
------------------------------------

In *Elements* XIII.17 (:cite:`EuclidElements`), :person:`Euclid <euclid>` constructs the
regular dodecahedron by erecting roof-like pentagonal *hipped* wedges onto the six faces of
a cube; :person:`Dr. Ron Knott <knott>` (:cite:`KnottPhi3D`) highlights the resulting
symmetric compound of five cubes inscribed inside a single dodecahedron.

* **Primary Cube & Roof Ridges**: Starting from primary cube vertices
  :g:`C1 <knott-3-2.g1:C1>` through :g:`C8 <knott-3-2.g1:C8>` at :math:`(\pm 1, \pm 1, \pm 1)`
  with front face :g:`C1C2C3C4 <knott-3-2.g1:< C1 C2 C3 C4 >>` and cube edges
  :g:`C1C2 <knott-3-2.g1:/ C1 C2 />`, :g:`C2C3 <knott-3-2.g1:/ C2 C3 />`, and
  :g:`C1C5 <knott-3-2.g1:/ C1 C5 />` of length :math:`2`, adjoining the twelve golden ridge
  vertices :g:`D1 <knott-3-2.g1:D1>` – :g:`D12 <knott-3-2.g1:D12>` at cyclic permutations of
  :math:`(0, \pm\phi, \pm\Phi)` produces thirty dodecahedral edges—such as ridge
  :g:`D1D2 <knott-3-2.g1:/ D1 D2 />` and rafters :g:`C1D1 <knott-3-2.g1:/ C1 D1 />`,
  :g:`C1D5 <knott-3-2.g1:/ C1 D5 />`—each of exact 3D quadrance :math:`4\phi^2` (length
  :math:`2\phi`).
* **Partition of the 60 Face Diagonals**: Because every pentagonal face of side
  :math:`2\phi` has five diagonals of length :math:`\Phi \cdot (2\phi) = 2`, the
  :math:`12 \times 5 = 60` face diagonals partition cleanly into **5 congruent inscribed
  cubes** of volume :math:`8`, with every one of the 20 dodecahedral vertices belonging to
  exactly :math:`2` cubes and volume ratio :math:`V_{\text{dod}} / V_{\text{cube}} = 1 + \Phi/2`.
""".strip(),
    "KNOTT-3.3": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Just as :person:`Roger Penrose <penrose>`'s thick and thin golden rhombs tile the plane
with five-fold symmetry, three-dimensional icosahedral quasicrystals (Ammann–Kramer–Neri
tilings, cataloged by :person:`Dr. Ron Knott <knott>` on :cite:`KnottPhi3D`) are built from
two :term:`golden rhombohedra <golden-rhombohedron>` bounded by six congruent golden rhombi.

* **Acute (Prolate) vs. Obtuse (Oblate) Hexahedra**: Spanning vectors :math:`(0, 1, \Phi)`,
  :math:`(1, \Phi, 0)`, and :math:`(\Phi, 0, 1)` from :g:`A0 <knott-3-3.g1:A0>` through
  :g:`A1 <knott-3-3.g1:A1>`, :g:`A2 <knott-3-3.g1:A2>`, :g:`A3 <knott-3-3.g1:A3>` to apex
  :g:`A7 <knott-3-3.g1:A7>` generate the **acute** rhombohedron (with golden rhomb face
  :g:`A0A1A4A2 <knott-3-3.g1:< A0 A1 A4 A2 >>` and edges :g:`A0A1 <knott-3-3.g1:/ A0 A1 />`,
  :g:`A0A2 <knott-3-3.g1:/ A0 A2 />`, :g:`A0A3 <knott-3-3.g1:/ A0 A3 />`, and
  :g:`A4A7 <knott-3-3.g1:/ A4 A7 />`). Reversing two signs from :g:`B0 <knott-3-3.g1:B0>`
  through :g:`B1 <knott-3-3.g1:B1>`, :g:`B2 <knott-3-3.g1:B2>`, :g:`B3 <knott-3-3.g1:B3>`
  to :g:`B7 <knott-3-3.g1:B7>` generates the **obtuse** rhombohedron (front face
  :g:`B0B1B4B2 <knott-3-3.g1:< B0 B1 B4 B2 >>` and edges :g:`B0B1 <knott-3-3.g1:/ B0 B1 />`,
  :g:`B4B7 <knott-3-3.g1:/ B4 B7 />`).
* **Golden Volume Ratio & Triacontahedron**: Every edge has 3D quadrance
  :math:`1 + \Phi^2 = \Phi + 2`, every rhombic face has diagonals :math:`2\Phi` and
  :math:`2` (ratio :math:`\Phi : 1`), and exact 3D determinant evaluation proves
  :math:`V_{\text{acute}} = 2\Phi^2` and :math:`V_{\text{obtuse}} = 2\Phi` (ratio
  :math:`\Phi : 1`). Ten acute and ten obtuse tiles assemble :person:`Johannes Kepler <kepler>`'s
  30-faced rhombic triacontahedron of exact volume :math:`10(2\Phi^2 + 2\Phi) = 20\Phi^3`.
""".strip(),
    "KNOTT-4.1": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Because :math:`\Phi^2 = \Phi + 1`, :person:`Dr. Ron Knott <knott>` (:cite:`KnottPropsPhi`)
emphasizes that :math:`\Phi` is the unique positive proportion whose **geometric** power
sequence :math:`1, \Phi, \Phi^2, \Phi^3, \dots` is simultaneously an **additive**
Fibonacci sequence (:math:`\Phi^{n+1} = \Phi^n + \Phi^{n-1}`):

* **Linearization of All Integer Powers**: Induction over :math:`n \in \mathbb{Z}` reduces
  every positive and negative power to :math:`\Phi^n = F_n \Phi + F_{n-1}` and
  :math:`(-\phi)^n = F_{n+1} - F_n \Phi`. Visually, the :math:`\Phi^2 \times \Phi^2` square
  :g:`AEFH <knott-4-1.g1:< A E F H >>` on :g:`A <knott-4-1.g1:A>`, :g:`E <knott-4-1.g1:E>`,
  :g:`F <knott-4-1.g1:F>`, :g:`H <knott-4-1.g1:H>` (with main diagonal
  :g:`AF <knott-4-1.g1:/ A F />`) decomposes via internal cuts :g:`BJ <knott-4-1.g1:/ B J />`
  and :g:`DG <knott-4-1.g1:/ D G />` through :g:`C <knott-4-1.g1:C>` into unit square
  :g:`ABCD <knott-4-1.g1:< A B C D >>` (:math:`1`), :math:`\Phi \times \Phi` square
  :g:`CGFJ <knott-4-1.g1:< C G F J >>` (:math:`\Phi^2`), and two :math:`1 \times \Phi`
  golden rectangles (:math:`\Phi^4 = 3\Phi + 2 = 1 + 2\Phi + \Phi^2`).
* **The Unit-Volume Phibonacci Brick**: Alongside the square, rectangle
  :g:`APQR <knott-4-1.g1:< A P Q R >>` (with edges :g:`PQ <knott-4-1.g1:/ P Q />` and
  :g:`RQ <knott-4-1.g1:/ R Q />`) displays the unfolded cross-section of Dr. Knott's
  3D **Phibonacci brick** of edges :math:`(1, \phi, \Phi)`, whose volume is exact unit
  :math:`1 \cdot \phi \cdot \Phi = 1`, total surface area is :math:`2(\phi + \Phi + 1) = 4\Phi`,
  and 3D space diagonal has integer length :math:`\sqrt{1 + \phi^2 + \Phi^2} = \sqrt{4} = 2`.
""".strip(),
    "KNOTT-4.2": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Rewriting :math:`\Phi = 1 + \frac{1}{\Phi}` generates the all-ones simple
:term:`continued fraction <continued-fraction>` :math:`\Phi = [1; 1, 1, 1, \dots]` and
nested radical :math:`\Phi = \sqrt{1 + \sqrt{1 + \sqrt{1 + \cdots}}}` cataloged on
``propsOfPhi.html`` (:cite:`KnottPropsPhi`).

* **Alternating Fibonacci Convergent Lattice**: In the :math:`(F_k, F_{k+1})` plane from
  origin :g:`O <knott-4-2.g1:O>`, the exact golden-slope ray :g:`OP <knott-4-2.g1:/ O P />`
  (:math:`y = \Phi x`) is straddled alternately above and below by convergent vectors
  :g:`OC1 <knott-4-2.g1:/ O C1 />` (:math:`(1, 1)`), :g:`OC2 <knott-4-2.g1:/ O C2 />`
  (:math:`(1, 2)`), :g:`OC3 <knott-4-2.g1:/ O C3 />` (:math:`(2, 3)`),
  :g:`OC4 <knott-4-2.g1:/ O C4 />` (:math:`(3, 5)`), and :g:`OC5 <knott-4-2.g1:/ O C5 />`
  (:math:`(5, 8)`).
* **Cassini Sector Triangles & Hurwitz's √5 Barrier**: By :term:`Cassini's identity <cassini-identity>`
  :math:`F_{k+1} F_{k-1} - F_k^2 = (-1)^k`, consecutive convergent sector triangles
  :g:`OC1C2 <knott-4-2.g1:< O C1 C2 >>`, :g:`OC2C3 <knott-4-2.g1:< O C2 C3 >>`,
  :g:`OC3C4 <knott-4-2.g1:< O C3 C4 >>`, and :g:`OC4C5 <knott-4-2.g1:< O C4 C5 >>` are
  :eq:`equal <knott-4-2.g1:< O C1 C2 > = knott-4-2.g1:< O C2 C3 > = knott-4-2.g1:< O C3 C4 > = knott-4-2.g1:< O C4 C5 >>`
  in unsigned area (:math:`1/2`, zero interior lattice points), yielding exact error
  :math:`\frac{F_{k+1}}{F_k} - \Phi = \frac{(-\phi)^k}{F_k}` and saturating
  :person:`Adolf Hurwitz <hurwitz>`'s (:cite:`Hurwitz1891`) irrationality constant
  :math:`F_k^2 \left|\frac{F_{k+1}}{F_k} - \Phi\right| \to \frac{1}{\sqrt{5}}`.
""".strip(),
    "KNOTT-4.3": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Discovered in 1957 by fourteen-year-old :person:`George Bergman <bergman>` (:cite:`Bergman1957`)
and extensively developed by :person:`Dr. Ron Knott <knott>` on ``phigits.html``
(:cite:`KnottPhigits`), the **base-Φ ("phigit") numeral system** represents **every
positive integer** uniquely as a finite non-adjacent binary sum of powers of the irrational
radix :math:`\Phi`.

* **Carry Law & Minimal Phigit Scale**: Along base-:math:`\Phi` axis :g:`OP3 <knott-4-3.g1:/ O P3 />`
  carrying ticks :g:`Pm2 <knott-4-3.g1:Pm2>` (:math:`\Phi^{-2}`), :g:`Pm1 <knott-4-3.g1:Pm1>`
  (:math:`\Phi^{-1}`), :g:`P0 <knott-4-3.g1:P0>` (:math:`\Phi^0 = 1`),
  :g:`P1 <knott-4-3.g1:P1>` (:math:`\Phi^1`), :g:`P2 <knott-4-3.g1:P2>` (:math:`\Phi^2`),
  and :g:`P3 <knott-4-3.g1:P3>` (:math:`\Phi^3`), the identity :math:`\Phi + \Phi^{-2} = 2`
  decomposes :math:`2 = 10.01_\Phi` into segments :g:`A2M2 <knott-4-3.g1:/ A2 M2 />` and
  :g:`M2B2 <knott-4-3.g1:/ M2 B2 />` (aligned to :g:`P1 <knott-4-3.g1:P1>` via
  :g:`P1M2 <knott-4-3.g1:/ P1 M2 />`), :math:`3 = 100.01_\Phi` into
  :g:`A3M3 <knott-4-3.g1:/ A3 M3 />` and :g:`M3B3 <knott-4-3.g1:/ M3 B3 />`, and
  :math:`4 = 101.01_\Phi` into :g:`A4M4 <knott-4-3.g1:/ A4 M4 />` (framing
  :g:`OP2M4A4 <knott-4-3.g1:< O P2 M4 A4 >>` via :g:`P2M4 <knott-4-3.g1:/ P2 M4 />`),
  :g:`M4N4 <knott-4-3.g1:/ M4 N4 />`, and :g:`N4B4 <knott-4-3.g1:/ N4 B4 />`.
* **Maximal Phigit Form & Fibonacci Multiplicity**: Applying :math:`100_\Phi \to 011_\Phi`
  (while forbidding non-terminating :math:`\dots 011` tails via :math:`101_\Phi \to 01111_\Phi`)
  produces a unique ``00``-free **maximal** :term:`phigit` expansion, and every Fibonacci
  integer :math:`F_k` admits **exactly** :math:`F_k` valid finite phigit representations
  while :person:`Édouard Lucas <lucas>` numbers :math:`L_{2m}` achieve local minima.
""".strip(),
    "KNOTT-5.1": r"""
Constructive Synthesis & Exact Proof
------------------------------------

:person:`Dr. Ron Knott <knott>`'s signature page ``fibrab.html`` (:cite:`KnottGoldenString`)
unifies three seemingly distinct mathematical worlds—:person:`Fibonacci <fibonacci>`'s
monthly rabbit substitution (:math:`1 \mapsto 10,\; 0 \mapsto 1`), Sturmian Beatty
differences :math:`d_n = \lfloor (n+1)\phi \rfloor - \lfloor n\phi \rfloor`, and straight
lattice-cutting rays—into the single infinite **Golden String** ``1011010110110101101…``.

* **Cutting-Line Realization of the Golden String**: Tracing line
  :g:`[OR] <knott-5-1.g1:[ O R ]>` (segment :g:`OR <knott-5-1.g1:/ O R />` from origin
  :g:`O <knott-5-1.g1:O>` to :g:`R <knott-5-1.g1:R>` :math:`(5, 5\phi)`) of exact slope
  :math:`\phi` across vertical unit grid segments :g:`X1XT1 <knott-5-1.g1:/ X1 XT1 />`,
  :g:`X2XT2 <knott-5-1.g1:/ X2 XT2 />`, :g:`X3XT3 <knott-5-1.g1:/ X3 XT3 />` and horizontal
  grid segments :g:`Y1YR1 <knott-5-1.g1:/ Y1 YR1 />`, :g:`Y2YR2 <knott-5-1.g1:/ Y2 YR2 />`,
  :g:`Y3YR3 <knott-5-1.g1:/ Y3 YR3 />`: recording ``1`` at each vertical crossing
  (:g:`V1 <knott-5-1.g1:V1>` – :g:`V5 <knott-5-1.g1:V5>` at :math:`(k, k\phi)`) and ``0``
  at each horizontal crossing (:g:`H1 <knott-5-1.g1:H1>`, :g:`H2 <knott-5-1.g1:H2>`,
  :g:`H3 <knott-5-1.g1:H3>` at :math:`(m\Phi, m)`) spells out ``1, 0, 1, 1, 0, 1, 0, 1``
  in exact abscissa order :math:`1 < \Phi < 2 < 3 < 2\Phi < 4 < 3\Phi < 5`.
* **Palindrome Structure & Recursive Call Tree**: Removing the final two characters of
  every morphism word :math:`S_n` (length :math:`F_n` with :math:`F_{n-1}` ones and
  :math:`F_{n-2}` zeros) leaves a strict palindrome, while naive recursive evaluation of
  ``fib(n)`` performs :math:`F_{n+1} - 1` additions.
""".strip(),
    "KNOTT-5.2": r"""
Constructive Synthesis & Exact Proof
------------------------------------

On ``fibrep.html`` (:cite:`KnottFibRep`), :person:`Dr. Ron Knott <knott>` pairs
:term:`phigit` expansions with :person:`Édouard Zeckendorf <zeckendorf>`'s theorem
(:cite:`Zeckendorf1972`): every positive integer :math:`N \ge 1` decomposes uniquely as a
sum of non-consecutive :person:`Fibonacci <fibonacci>` numbers :math:`F_{k_1} + \cdots + F_{k_r}`
(:math:`k_i \ge k_{i+1} + 2,\; k_r \ge 2`).

* **Greedy Non-Consecutive Fibonacci Staircase**: Plotting Fibonacci place-value bars
  :g:`A2B2C2D2 <knott-5-2.g1:< A2 B2 C2 D2 >>` (:math:`F_2 = 1`),
  :g:`A3B3C3D3 <knott-5-2.g1:< A3 B3 C3 D3 >>` (:math:`F_3 = 2`),
  :g:`A4B4C4D4 <knott-5-2.g1:< A4 B4 C4 D4 >>` (:math:`F_4 = 3`),
  :g:`A5B5C5D5 <knott-5-2.g1:< A5 B5 C5 D5 >>` (:math:`F_5 = 5`), and
  :g:`A6B6C6D6 <knott-5-2.g1:< A6 B6 C6 D6 >>` (:math:`F_6 = 8`), any two adjacent bars
  :math:`F_{k-1} + F_k` immediately coalesce into the next single bar :math:`F_{k+1}`,
  eliminating every ``11`` pair in Fibonacci base.
* **Canonical Decomposition of N = 12**: Below the staircase, integer :math:`12` decomposes
  uniquely along :g:`S0 <knott-5-2.g1:S0>` :math:`\to` :g:`S8 <knott-5-2.g1:S8>` :math:`\to`
  :g:`S11 <knott-5-2.g1:S11>` :math:`\to` :g:`S12 <knott-5-2.g1:S12>` into non-adjacent
  summands :g:`S0S8 <knott-5-2.g1:/ S0 S8 />` (:math:`F_6 = 8`, matching
  :g:`A6D6 <knott-5-2.g1:/ A6 D6 />`), :g:`S8S11 <knott-5-2.g1:/ S8 S11 />` (:math:`F_4 = 3`,
  matching :g:`A4D4 <knott-5-2.g1:/ A4 D4 />`), and :g:`S11S12 <knott-5-2.g1:/ S11 S12 />`
  (:math:`F_2 = 1`, matching :g:`A2D2 <knott-5-2.g1:/ A2 D2 />`), encoding
  :math:`12 = (10101)_F` in :term:`Zeckendorf representation <zeckendorf-representation>`.
""".strip(),
    "KNOTT-5.3": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Because :math:`\frac{1}{\Phi} + \frac{1}{\Phi^2} = \phi + \phi^2 = 1`, Samuel Beatty's
theorem guarantees that lower and upper :term:`Beatty sequences <beatty-sequence>`
:math:`A_n = \lfloor n\Phi \rfloor` and :math:`B_n = \lfloor n\Phi^2 \rfloor = A_n + n`
partition :math:`\mathbb{Z}_{>0}` into disjoint cold positions of :person:`Willem Wythoff <wythoff>`'s
game (:cite:`Wythoff1907`, :cite:`KnottFibGen`).

* **Exact Wythoff & Beatty Cone**: From origin :g:`O <knott-5-3.g1:O>`, exact rays
  :g:`OR1 <knott-5-3.g1:/ O R1 />` (:math:`y = \Phi x`) and :g:`OR2 <knott-5-3.g1:/ O R2 />`
  (:math:`y = \Phi^2 x`) bound the cold Wythoff pairs :g:`W1 <knott-5-3.g1:W1>` :math:`(1, 2)`,
  :g:`W2 <knott-5-3.g1:W2>` :math:`(3, 5)`, :g:`W3 <knott-5-3.g1:W3>` :math:`(4, 7)`, and
  :g:`W4 <knott-5-3.g1:W4>` :math:`(6, 10)` (connected along :g:`W1W2 <knott-5-3.g1:/ W1 W2 />`,
  :g:`W2W3 <knott-5-3.g1:/ W2 W3 />`, and :g:`W3W4 <knott-5-3.g1:/ W3 W4 />` beneath ideal
  targets :g:`A1 <knott-5-3.g1:A1>` – :g:`A4 <knott-5-3.g1:A4>`).
* **Bijective Wythoff & Stolarsky Interspersions**: Seeding row :math:`r \ge 0` of the
  :term:`Wythoff array <wythoff-array>` with :math:`W(r, c) = \lfloor (r+1)\Phi \rfloor F_{c+2} + r F_{c+1}`
  groups integers whose :term:`Zeckendorf representations <zeckendorf-representation>` end
  in :math:`c` trailing zeros (:cite:`Morrison1980`), while :person:`Kenneth Stolarsky <stolarsky>`'s
  nearest-integer Golden Ratio rounding :math:`b = \lfloor a\Phi + 1/2 \rfloor`
  (:cite:`Stolarsky1977`) yields the dual :term:`Stolarsky array <stolarsky-array>` studied
  by :person:`John Conway <conway>` and :person:`Clark Kimberling <kimberling>`.
""".strip(),
    "KNOTT-6.1": r"""
Constructive Synthesis & Exact Proof
------------------------------------

On ``Pythag/pythag.html`` (:cite:`KnottPythag`), :person:`Dr. Ron Knott <knott>` catalogs
:person:`Alwyn Horadam <fibonacci>`'s (:cite:`Horadam1961`) four-term Fibonacci generator
of :person:`Pythagoras <pythagoras>`'s right triangles: any four consecutive positive
Fibonacci numbers :math:`(F_n, F_{n+1}, F_{n+2}, F_{n+3})` satisfy

.. math::

   (F_n F_{n+3})^2 + (2 F_{n+1} F_{n+2})^2 = (F_{n+1}^2 + F_{n+2}^2)^2 = F_{2n+3}^2.

* **Nested Exact Right Triangles & Rational Incircle**: Anchored at right-angle vertex
  :g:`O <knott-6-1.g1:O>`, :math:`n = 1 \mapsto (1, 1, 2, 3)` constructs the classic
  :math:`(3, 4, 5)` triangle :g:`OA1B1 <knott-6-1.g1:< O A1 B1 >>` with hypotenuse
  :g:`A1B1 <knott-6-1.g1:/ A1 B1 />` :math:`= F_5 = 5`, while :math:`n = 2 \mapsto (1, 2, 3, 5)`
  constructs the :math:`(5, 12, 13)` triangle :g:`OA2B2 <knott-6-1.g1:< O A2 B2 >>` on legs
  :g:`OA2 <knott-6-1.g1:/ O A2 />` :math:`= 5`, :g:`OB2 <knott-6-1.g1:/ O B2 />` :math:`= 12`,
  and hypotenuse :g:`A2B2 <knott-6-1.g1:/ A2 B2 />` :math:`= F_7 = 13`. Its exact incircle
  :g:`(I2, T2) <knott-6-1.g1:( I2 T2 )>` centered at :g:`I2 <knott-6-1.g1:I2>` :math:`(2, 2)`
  has integer inradius :math:`r = F_2 F_3 = 2` and triangle area
  :math:`F_2 F_3 F_4 F_5 = 1 \cdot 2 \cdot 3 \cdot 5 = 30`.
* **Divisibility Dichotomy**: Because :math:`\gcd(F_{n+1}, F_{n+2}) = 1` and :math:`2 \mid F_k \iff 3 \mid k`,
  the generated triple has :math:`\gcd = 1` (primitive) whenever :math:`3 \nmid n` and
  :math:`\gcd = 2` (twice a primitive triple, e.g. :math:`n = 3 \mapsto (16, 30, 34) = 2(8, 15, 17)`)
  whenever :math:`3 \mid n`.
""".strip(),
    "KNOTT-6.2": r"""
Constructive Synthesis & Exact Proof
------------------------------------

:person:`Giovanni Domenico Cassini <cassini>`'s 1680 determinant identity
:math:`F_{n-1} F_{n+1} - F_n^2 = (-1)^n` turns into a dramatic visual paradox at
:math:`n = 6` (:math:`5 \times 13 - 8^2 = +1`), examined by :person:`Dr. Ron Knott <knott>`
on ``fibpuzzles2.html`` (:cite:`KnottPuzzles2`) alongside :person:`Sam Loyd <loyd>` Jr. and
:person:`Henry Ernest Dudeney <dudeney>`'s complementary **64 = 63** rearrangement
(:cite:`Gardner1956`, :cite:`Horadam1962`).

* **Left Assembly — 5 × 13 = 65 (+1 Gap)**: Rearranging the four pieces of an
  :math:`8 \times 8 = 64` chessboard—triangles :g:`OB8P1 <knott-6-2.g1:< O B8 P1 >>` and
  :g:`P2QT5 <knott-6-2.g1:< P2 Q T5 >>` (each area :math:`12`) plus trapezoids
  :g:`B8R0QP1 <knott-6-2.g1:< B8 R0 Q P1 >>` and :g:`OP2T5T0 <knott-6-2.g1:< O P2 T5 T0 >>`
  (each area :math:`20`)—along diagonal :g:`O <knott-6-2.g1:O>` :math:`\to`
  :g:`Q <knott-6-2.g1:Q>` separates slopes :math:`3/8 = 0.375` (:g:`OP1 <knott-6-2.g1:/ O P1 />`)
  and :math:`2/5 = 0.400` (:g:`OP2 <knott-6-2.g1:/ O P2 />`), opening thin **+1 gap
  parallelogram** :g:`OP1QP2 <knott-6-2.g1:< O P1 Q P2 >>` of exact signed area :math:`+1`.
* **Right Assembly — 63-Unit Notched Block (−1 Overlap)**: Sliding the same four pieces
  into two :math:`5 \times 6 = 30` wings joined by a :math:`3 \times 1 = 3` bridge (outer
  polygon area :math:`63`, pieces :g:`S0S1U1U0 <knott-6-2.g1:< S0 S1 U1 U0 >>`,
  :g:`U0U3S2 <knott-6-2.g1:< U0 U3 S2 >>`, :g:`U3U2S4S3 <knott-6-2.g1:< U3 U2 S4 S3 >>`,
  and :g:`U1S5U2 <knott-6-2.g1:< U1 S5 U2 >>`) crosses edges :g:`U0U1 <knott-6-2.g1:/ U0 U1 />`
  and :g:`U0U3 <knott-6-2.g1:/ U0 U3 />` over **−1 overlap parallelogram**
  :g:`U0U3U2U1 <knott-6-2.g1:< U0 U3 U2 U1 >>`, whose unsigned area is
  :eq:`equal <knott-6-2.g1:< O P1 Q P2 > = knott-6-2.g1:< U0 U3 U2 U1 >>` to :math:`1`
  (:math:`64 - 1 = 63`).
""".strip(),
    "KNOTT-6.3": r"""
Constructive Synthesis & Exact Proof
------------------------------------

On ``fibFormulae.html`` (:cite:`KnottFormulae`), :person:`Dr. Ron Knott <knott>` organizes
the algebraic web linking :person:`Jacques Binet <binet>`'s closed forms,
:person:`Édouard Lucas <lucas>`'s companion sequence :math:`L_n = \Phi^n + (-\phi)^n`,
:person:`Eugène Catalan <catalan>`'s, d'Ocagne's, and Ross Honsberger's (:cite:`Honsberger1985`)
addition laws, and signed :term:`Fibonomial <fibonomial>` power recurrences (:cite:`Vajda1989`).

* **Pell–Lucas Alternating Hyperbola & Asymptote**: Plotting :math:`P_n = (L_n, F_n)` from
  origin :g:`O <knott-6-3.g1:O>` at :g:`P0 <knott-6-3.g1:P0>` :math:`(2, 0)`,
  :g:`P1 <knott-6-3.g1:P1>` :math:`(1, 1)`, :g:`P2 <knott-6-3.g1:P2>` :math:`(3, 1)`,
  :g:`P3 <knott-6-3.g1:P3>` :math:`(4, 2)`, and :g:`P4 <knott-6-3.g1:P4>` :math:`(7, 3)`
  places every even/odd point on the conjugate hyperbolas :math:`L_n^2 - 5 F_n^2 = 4(-1)^n`
  approaching golden asymptote :g:`OA <knott-6-3.g1:/ O A />` of slope :math:`1/\sqrt{5}`.
* **Unit-Area Sector Invariant & Fibonomials**: Because :math:`L_n F_{n+1} - F_n L_{n+1} = 2(-1)^n`,
  consecutive sector triangles :g:`OP0P1 <knott-6-3.g1:< O P0 P1 >>`,
  :g:`OP1P2 <knott-6-3.g1:< O P1 P2 >>`, :g:`OP2P3 <knott-6-3.g1:< O P2 P3 >>`, and
  :g:`OP3P4 <knott-6-3.g1:< O P3 P4 >>` bounded by chords :g:`P0P1 <knott-6-3.g1:/ P0 P1 />` –
  :g:`P3P4 <knott-6-3.g1:/ P3 P4 />` are
  :eq:`equal <knott-6-3.g1:< O P0 P1 > = knott-6-3.g1:< O P1 P2 > = knott-6-3.g1:< O P2 P3 > = knott-6-3.g1:< O P3 P4 >>`
  in unsigned area (exact area :math:`1`), while Fibonomial coefficients
  :math:`\binom{k+1}{j}_F` annihilate :math:`k`-th powers :math:`F_n^k` identically.
""".strip(),
    "KNOTT-6.4": r"""
Constructive Synthesis & Exact Proof
------------------------------------

How do :person:`Fibonacci <fibonacci>` numbers—governed by :math:`\sqrt{5}`—generate the
circle constant :math:`\pi`? On ``fibpi.html`` (:cite:`KnottFibPi`), :person:`Dr. Ron Knott <knott>`
derives :person:`D. H. Lehmer <lehmer>`'s (:cite:`Lehmer1936`) reciprocal Fibonacci
:person:`Euler <euler>`–Machin series directly from odd-index :term:`Cassini's identity <cassini-identity>`:

.. math::

   F_{2n+1}^2 - F_{2n} F_{2n+2} = 1 \implies
   \frac{\frac{1}{F_{2n+1}} + \frac{1}{F_{2n+2}}}{1 - \frac{1}{F_{2n+1} F_{2n+2}}}
   = \frac{F_{2n+2} + F_{2n+1}}{F_{2n} F_{2n+2}} = \frac{F_{2n+3}}{F_{2n} F_{2n+2}}? \quad
   \text{No: } F_{2n+1} F_{2n+2} - 1 = F_{2n+1} F_{2n+2} - (F_{2n+1}^2 - F_{2n} F_{2n+2}) = F_{2n}(F_{2n+1} + F_{2n+2}),

canceling :math:`(F_{2n+1} + F_{2n+2})` identically to leave :math:`1 / F_{2n}`!

* **Ko Hayashi's Exact Integer-Lattice Proof**: Over horizontal axis
  :g:`OX <knott-6-4.g1:/ O X />` to :g:`X <knott-6-4.g1:X>` :math:`(16, 0)`, plotting
  integer lattice points :g:`E <knott-6-4.g1:E>` :math:`(10, 10)` (slope :math:`1 = 1/F_2`),
  :g:`M <knott-6-4.g1:M>` :math:`(15, 5)` (slope :math:`1/3 = 1/F_4`), and
  :g:`N <knott-6-4.g1:N>` :math:`(16, 2)` (slope :math:`1/8 = 1/F_6`, vertical leg
  :g:`XN <knott-6-4.g1:/ X N />`): right triangle :g:`OME <knott-6-4.g1:< O M E >>` has
  exact perpendicularity :math:`s(OE, EM) = 1` between :g:`OE <knott-6-4.g1:/ O E />` and
  :g:`EM <knott-6-4.g1:/ E M />` with :math:`Q(E, M)/Q(O, E) = 50/200 = (1/2)^2`, while
  right triangle :g:`ONM <knott-6-4.g1:< O N M >>` has :math:`s(OM, MN) = 1` between
  :g:`OM <knott-6-4.g1:/ O M />` and :g:`MN <knott-6-4.g1:/ M N />` with
  :math:`Q(M, N)/Q(O, M) = 10/250 = (1/5)^2`, proving geometrically along ray
  :g:`ON <knott-6-4.g1:/ O N />` that :math:`\frac{\pi}{4} = \arctan\frac{1}{2} + \arctan\frac{1}{5} + \arctan\frac{1}{8}`.
""".strip(),
    "KNOTT-6.5": r"""
Constructive Synthesis & Exact Proof
------------------------------------

Concluding the catalog on ``fibnat.html`` (:cite:`KnottNature`), :person:`Dr. Ron Knott <knott>`
connects the :term:`Golden Angle <golden-angle>` :math:`2\pi / \Phi^2 = 2\pi\phi^2 \approx 137.50776^\circ`
to the opposing Fibonacci spiral families (:term:`parastichies <parastichy>`) studied by
:person:`Luca Pacioli <pacioli>`, :person:`D'Arcy Wentworth Thompson <thompson>` (:cite:`Thompson1917`),
and :person:`H. S. M. Coxeter <coxeter>` (:cite:`Coxeter1973`).

* **Unrolled Cylindrical Primordia & Alternating Convergence**: Unrolling a cylindrical stem
  around central axis :g:`OS <knott-6-5.g1:/ O S />` (:g:`O <knott-6-5.g1:O>` to
  :g:`S <knott-6-5.g1:S>`), the :math:`F_k`-th primordium lands at signed angular offset
  :math:`F_k \phi^2 - F_{k-2} = (-\phi)^k`, placing :g:`P2 <knott-6-5.g1:P2>` (:math:`F_2 = 1`),
  :g:`F2 <knott-6-5.g1:F2>` (:math:`F_3 = 2`), :g:`F3 <knott-6-5.g1:F3>` (:math:`F_4 = 3`),
  :g:`F5 <knott-6-5.g1:F5>` (:math:`F_5 = 5`), and :g:`F8 <knott-6-5.g1:F8>` (:math:`F_6 = 8`)
  on alternating sides of :g:`OS <knott-6-5.g1:/ O S />` along vectors
  :g:`OP2 <knott-6-5.g1:/ O P2 />` – :g:`OF8 <knott-6-5.g1:/ O F8 />`.
* **Unimodular Parastichy Parallelograms**: Because :math:`(-\phi)^k + (-\phi)^{k+1} = (-\phi)^{k+2}`
  and :math:`F_k + F_{k+1} = F_{k+2}`, vector :g:`F5 <knott-6-5.g1:F5>` is the exact
  2D vector sum of :g:`F2 <knott-6-5.g1:F2>` and :g:`F3 <knott-6-5.g1:F3>` (edges
  :g:`F2F5 <knott-6-5.g1:/ F2 F5 />` and :g:`F3F5 <knott-6-5.g1:/ F3 F5 />`), and
  :g:`F8 <knott-6-5.g1:F8>` is the vector sum of :g:`F3 <knott-6-5.g1:F3>` and
  :g:`F5 <knott-6-5.g1:/ O F5 />` (edges :g:`F3F8 <knott-6-5.g1:/ F3 F8 />` and
  :g:`F5F8 <knott-6-5.g1:/ F5 F8 />`). Moreover, :math:`\phi^k (F_k \phi + F_{k+1}) = \phi^k \Phi^k = 1`,
  proving that consecutive parastichy cells :g:`OF3F5F2 <knott-6-5.g1:< O F3 F5 F2 >>` and
  :g:`OF3F8F5 <knott-6-5.g1:< O F3 F8 F5 >>` are :eq:`equal <knott-6-5.g1:< O F3 F5 F2 > = knott-6-5.g1:< O F3 F8 F5 >>`
  unimodular fundamental domains of normalized area :math:`1`.
""".strip(),
}
