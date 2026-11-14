:type: item
:order: 6
:canonical_id: KNOTT-1.6

.. _knott-1-6:

==========================================================================
KNOTT-1.6 — Penrose Kites & Darts (P2) and Thick & Thin Golden Rhombs (P3)
==========================================================================

.. enunciation::

   A thick 72°–108° golden rhomb of side Φ divides at unit distance K along its long diagonal of length Φ² into a convex Penrose kite KBCD and a non-convex Penrose dart ABKD with exact area ratio Φ : 1, matching the Φ : 1 area ratio between thick (72°) and thin (36°) Penrose golden rhombs.

.. picture:: knott-1-6.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-1.6``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Phi in 2D Geometry and Trigonometry* (`#penrose <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#penrose>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#penrose>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.flat_geometry.construct_penrose_tiles` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/divine <https://geometor.github.io/divine/>`_, `geometor/wildberger <https://geometor.github.io/wildberger/>`_

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

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``Q rhomb side``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
   * - ``Q dart short edge``
     - :math:`1`
   * - ``Q kite spine KC``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
   * - ``kite to dart area ratio``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``thick to thin rhomb area ratio``
     - :math:`\frac{\sqrt{10} \sqrt{\sqrt{5} + 5}}{\sqrt{10} \sqrt{5 - \sqrt{5}} + 3 \sqrt{2} \sqrt{5 - \sqrt{5}}} + \frac{3 \sqrt{2} \sqrt{\sqrt{5} + 5}}{\sqrt{10} \sqrt{5 - \sqrt{5}} + 3 \sqrt{2} \sqrt{5 - \sqrt{5}}}`
   * - ``spread thick 72``
     - :math:`\frac{\sqrt{5}}{\sqrt{5} + 3} + \frac{5}{2 \sqrt{5} + 6}`
   * - ``spread thin 36``
     - :math:`\frac{\sqrt{5}}{4 \sqrt{5} + 12} + \frac{5}{4 \sqrt{5} + 12}`
