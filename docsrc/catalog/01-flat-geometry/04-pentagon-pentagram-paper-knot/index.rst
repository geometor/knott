:layout: book
:type: item
:order: 4
:canonical_id: KNOTT-1.4

.. _knott-1-4:

======================================================================
KNOTT-1.4 — Regular Pentagon, Pentagram, Decagon & Paper-Knot Pentagon
======================================================================

.. enunciation::

   The five diagonals of a regular pentagon of side 1 enclose a similar inner pentagon of side φ² and cut each diagonal in the geometric progression φ² : φ : 1 : Φ; furthermore, folding a flat uniform strip of width w into a tight overhand knot locks parallel trapezoid edges into an exact regular pentagon of side w sec 18°.

.. picture:: knott-1-4.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-1.4``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Phi in 2D Geometry and Trigonometry* (`#pent <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#pent>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#pent>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.flat_geometry.construct_pentagon_and_paper_knot` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/elements <https://geometor.github.io/elements/>`_, `geometor/pacioli <https://geometor.github.io/pacioli/>`_, `geometor/divine <https://geometor.github.io/divine/>`_

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

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``Q1Q2 crossbar``
     - :math:`\sqrt{- \frac{\sqrt{5}}{2} - \frac{10 \sqrt{2 \sqrt{5} + 5}}{2 \sqrt{2} \sqrt{\sqrt{5} + 5} + 2 \sqrt{5} \sqrt{2 \sqrt{5} + 5} + 6 \sqrt{2 \sqrt{5} + 5}} - \frac{3 \sqrt{2 \sqrt{5} + 5}}{\sqrt{2} \sqrt{\sqrt{5} + 5} + \sqrt{5} \sqrt{2 \sqrt{5} + 5} + 3 \sqrt{2 \sqrt{5} + 5}} - \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 5}}{\sqrt{2} \sqrt{\sqrt{5} + 5} + \sqrt{5} \sqrt{2 \sqrt{5} + 5} + 3 \sqrt{2 \sqrt{5} + 5}} + \frac{2 \sqrt{5} \sqrt{2 \sqrt{5} + 5}}{2 \sqrt{2} \sqrt{\sqrt{5} + 5} + 2 \sqrt{5} \sqrt{2 \sqrt{5} + 5} + 6 \sqrt{2 \sqrt{5} + 5}} + \frac{88 \sqrt{5}}{2 \sqrt{10} \sqrt{\sqrt{5} + 5} \sqrt{2 \sqrt{5} + 5} + 6 \sqrt{2} \sqrt{\sqrt{5} + 5} \sqrt{2 \sqrt{5} + 5} + 60 \sqrt{5} + 140} + \frac{200}{2 \sqrt{10} \sqrt{\sqrt{5} + 5} \sqrt{2 \sqrt{5} + 5} + 6 \sqrt{2} \sqrt{\sqrt{5} + 5} \sqrt{2 \sqrt{5} + 5} + 60 \sqrt{5} + 140} + \frac{3}{2}}`
   * - ``P0Q1 star arm``
     - :math:`\sqrt{\frac{3}{2} - \frac{\sqrt{5}}{2}}`
   * - ``P0Q2 pentagon side``
     - :math:`\sqrt{\frac{88 \sqrt{5}}{2 \sqrt{10} \sqrt{\sqrt{5} + 5} \sqrt{2 \sqrt{5} + 5} + 6 \sqrt{2} \sqrt{\sqrt{5} + 5} \sqrt{2 \sqrt{5} + 5} + 60 \sqrt{5} + 140} + \frac{200}{2 \sqrt{10} \sqrt{\sqrt{5} + 5} \sqrt{2 \sqrt{5} + 5} + 6 \sqrt{2} \sqrt{\sqrt{5} + 5} \sqrt{2 \sqrt{5} + 5} + 60 \sqrt{5} + 140}}`
   * - ``P0P2 diagonal``
     - :math:`\sqrt{\frac{\sqrt{5}}{2} + \frac{3}{2}}`
   * - ``strip width quadrance``
     - :math:`\frac{\sqrt{5}}{8} + \frac{5}{8}`
   * - ``unit strip pentagon side quadrance``
     - :math:`\frac{10 - 2 \sqrt{5}}{5}`
