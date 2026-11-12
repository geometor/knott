:layout: book
:type: item
:order: 3
:canonical_id: KNOTT-3.3

.. _knott-3-3:

==============================================================================
KNOTT-3.3 — Acute & Obtuse Golden Rhombohedra (3D Quasicrystal / Ammann Tiles)
==============================================================================

.. enunciation::

   Triples of five-fold icosahedral vectors of quadrance Φ + 2 span acute (prolate) and obtuse (oblate) golden rhombohedra bounded by six congruent golden rhombi of diagonal ratio Φ : 1, with exact volumes 2Φ² and 2Φ in ratio Φ : 1 and 10 + 10 assembly into a rhombic triacontahedron of volume 20Φ³.

.. picture:: knott-3-3.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-3.3``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *The Golden Geometry of Solids or Phi in 3 Dimensions* (`#quasicrystalsPhi <https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#quasicrystalsPhi>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#quasicrystalsPhi>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.solid_geometry.construct_golden_rhombohedra_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/pacioli <https://geometor.github.io/pacioli/>`_, `geometor/divine <https://geometor.github.io/divine/>`_

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

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``edge quadrance``
     - :math:`\frac{\sqrt{5}}{2} + \frac{5}{2}`
   * - ``face diagonal ratio``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``volume acute``
     - :math:`\sqrt{5} + 3`
   * - ``volume obtuse``
     - :math:`1 + \sqrt{5}`
   * - ``volume ratio acute to obtuse``
     - :math:`\frac{\sqrt{5}}{1 + \sqrt{5}} + \frac{3}{1 + \sqrt{5}}`
   * - ``triacontahedron volume``
     - :math:`40 + 20 \sqrt{5}`
