:layout: book
:type: item
:order: 2
:canonical_id: KNOTT-3.2

.. _knott-3-2:

=====================================================================
KNOTT-3.2 — Inscribed Cube & Compound of Five Cubes in a Dodecahedron
=====================================================================

.. enunciation::

   Inside a regular dodecahedron of edge 2φ, the 60 face diagonals of length 2 = Φ · (2φ) partition into five congruent inscribed cubes of edge 2 and volume 8, with each of the 20 dodecahedral vertices belonging to exactly two cubes.

.. picture:: knott-3-2.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-3.2``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *The Golden Geometry of Solids or Phi in 3 Dimensions* (`#cubeinDod <https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#cubeinDod>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#cubeinDod>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.solid_geometry.construct_cube_in_dodecahedron_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/elements <https://geometor.github.io/elements/>`_, `geometor/pacioli <https://geometor.github.io/pacioli/>`_

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

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``cube count``
     - :math:`5`
   * - ``cubes per vertex``
     - :math:`2`
   * - ``cube edge``
     - :math:`2`
   * - ``dodecahedron edge``
     - :math:`-1 + \sqrt{5}`
   * - ``face diagonal to edge ratio``
     - :math:`\frac{1 + \sqrt{5}}{2}`
   * - ``cube volume``
     - :math:`8`
   * - ``volume ratio dodecahedron to cube``
     - :math:`\frac{\sqrt{5}}{4} + \frac{5}{4}`
