:type: item
:order: 1
:canonical_id: KNOTT-3.1

.. _knott-3-1:

===================================================================================
KNOTT-3.1 — Three Orthogonal Golden Rectangles → Regular Icosahedron & Dodecahedron
===================================================================================

.. enunciation::

   Three mutually perpendicular 2 × 2Φ golden rectangles have 12 corners (0, ±1, ±Φ) forming a regular icosahedron of edge 2, volume 20Φ²/3, and rational dihedral spread 4/9, while (±1, ±1, ±1) ∪ cyc(0, ±φ, ±Φ) forms a regular dodecahedron of edge 2φ, volume 8 + 4Φ, and dihedral spread 4/5.

.. picture:: knott-3-1.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-3.1``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *The Golden Geometry of Solids or Phi in 3 Dimensions* (`#coords <https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#coords>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#coords>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.solid_geometry.construct_orthogonal_golden_rectangles_solids` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/pacioli <https://geometor.github.io/pacioli/>`_, `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/wildberger <https://geometor.github.io/wildberger/>`_

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

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``icosahedron edge``
     - :math:`2`
   * - ``icosahedron volume``
     - :math:`\frac{10 \sqrt{5}}{3} + 10`
   * - ``icosahedron dihedral spread``
     - :math:`\frac{4}{9}`
   * - ``dodecahedron edge``
     - :math:`-1 + \sqrt{5}`
   * - ``dodecahedron volume``
     - :math:`2 \sqrt{5} + 10`
   * - ``dodecahedron dihedral spread``
     - :math:`- \frac{144}{720 - 320 \sqrt{5}} + 1 + \frac{64 \sqrt{5}}{720 - 320 \sqrt{5}}`
