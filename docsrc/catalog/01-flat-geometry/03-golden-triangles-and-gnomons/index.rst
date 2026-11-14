:type: item
:order: 3
:canonical_id: KNOTT-1.3

.. _knott-1-3:

==========================================================================
KNOTT-1.3 — Golden Triangles (72°–72°–36°) & Golden Gnomons (36°–36°–108°)
==========================================================================

.. enunciation::

   An isosceles acute golden triangle ABC with base AB = 1 and legs AC = BC = Φ is partitioned by base-angle bisector AD (with AD = CD = 1 and BD = φ) into an obtuse golden gnomon CAD and a self-similar acute golden triangle DAB with exact spreads s(36°) = (5 − √5)/8 and s(72°) = (5 + √5)/8.

.. picture:: knott-1-3.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-1.3``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Phi in 2D Geometry and Trigonometry* (`#isoc <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#isoc>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#isoc>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.flat_geometry.construct_golden_triangles_and_gnomons` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/elements <https://geometor.github.io/elements/>`_, `geometor/wildberger <https://geometor.github.io/wildberger/>`_, `geometor/divine <https://geometor.github.io/divine/>`_

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

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``Q AC``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
   * - ``Q AD``
     - :math:`1`
   * - ``Q BD``
     - :math:`\frac{3}{2} - \frac{\sqrt{5}}{2}`
   * - ``Q BE``
     - :math:`\frac{7}{2} - \frac{3 \sqrt{5}}{2}`
   * - ``spread 36 deg``
     - :math:`\frac{\sqrt{5}}{3 \sqrt{5} + 7} + \frac{5}{6 \sqrt{5} + 14}`
   * - ``spread 72 deg``
     - :math:`\frac{\sqrt{5}}{\sqrt{5} + 3} + \frac{5}{2 \sqrt{5} + 6}`
   * - ``area ratio ABC to DAB``
     - :math:`\frac{2 \sqrt{2 \sqrt{5} + 5}}{- \sqrt{5} \sqrt{2 \sqrt{5} + 5} + 3 \sqrt{2 \sqrt{5} + 5}}`
