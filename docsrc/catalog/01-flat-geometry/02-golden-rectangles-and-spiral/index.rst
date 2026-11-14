:type: item
:order: 2
:canonical_id: KNOTT-1.2

.. _knott-1-2:

================================================================================
KNOTT-1.2 — Golden Rectangles, √5 Rectangles, & Whirling-Square Gnomonic Spirals
================================================================================

.. enunciation::

   Flanking a unit square ABCD on both sides via its base-midpoint circle produces a 1 × √5 rectangle WEFN containing right golden rectangle AEFD; recursive whirling-square cuts in gnomon BEFC share perpendicular main and secondary diagonals [AF] ⊥ [EC] (spread s = 1) meeting at pole P = (Φ²/√5, Φ/√5).

.. picture:: knott-1-2.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-1.2``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Phi in 2D Geometry and Trigonometry* (`#root5 <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#root5>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#root5>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.flat_geometry.construct_golden_rectangles_and_spiral` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/divine <https://geometor.github.io/divine/>`_, `geometor/pacioli <https://geometor.github.io/pacioli/>`_

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

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``golden rect width``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``sqrt5 rect width``
     - :math:`\sqrt{5}`
   * - ``diagonal spread``
     - :math:`1`
   * - ``pole x``
     - :math:`\frac{1}{2} + \frac{3 \sqrt{5}}{10}`
   * - ``pole y``
     - :math:`\frac{\sqrt{5}}{10} + \frac{1}{2}`
   * - ``gnomon area``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`
