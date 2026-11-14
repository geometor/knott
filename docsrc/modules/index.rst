:navigation: header
:order: 40
:nav_title: Modules

=======
Modules
=======

``geometor.knott`` is organized into focused exact-symbolic verification and
rendering modules:

- :mod:`geometor.knott` — Public package interface exporting constants,
  notation bridges, catalog registries, phigit/Zeckendorf/Wythoff algorithms,
  and ``.euclid-graphic`` SVG serializers.
- :mod:`geometor.knott.constants` — Exact :math:`\mathbb{Q}(\sqrt{5})`
  definitions of :math:`\Phi = (1+\sqrt{5})/2` (``PHI``),
  :math:`\phi = (\sqrt{5}-1)/2` (``phi``), and :math:`\Psi = (1-\sqrt{5})/2`
  (``PSI``), lossless ``sp.GoldenRatio`` conversion helpers, pure-integer
  Beatty floors (:func:`~geometor.knott.constants.floor_linear_phi`), and
  Rational Trigonometry invariants (``quadrance``, ``spread``, ``cross``,
  ``cross_ratio``).
- :mod:`geometor.knott.flat_geometry` — **Collection 1** (``KNOTT-1.1`` –
  ``KNOTT-1.6``): exact ``geometor.model`` constructions for internal/external
  golden section divisions, :math:`\sqrt{5}` and whirling-square golden
  rectangles, acute/obtuse golden triangles, pentagon/pentagram/paper-knot
  geometry, Kepler's :math:`(1, \sqrt{\Phi}, \Phi)` right triangle, and Penrose
  P2/P3 prototiles.
- :mod:`geometor.knott.trigonometry` — **Collection 2** (``KNOTT-2.1`` –
  ``KNOTT-2.2``): exact radical sines, cosines, tangents, and spreads for
  pentagonal angles (:math:`18^\circ, 36^\circ, 54^\circ, 72^\circ`), the full
  29-angle :math:`3^\circ k` constructible lattice, and Gauss's regular 17-gon
  cosine :math:`\cos(\pi / 17)`.
- :mod:`geometor.knott.solid_geometry` — **Collection 3** (``KNOTT-3.1`` –
  ``KNOTT-3.3``): exact 3D coordinates, volumes, and rational dihedral spreads
  for the regular icosahedron and dodecahedron, the compound of five cubes in a
  dodecahedron, and acute/obtuse golden quasicrystal rhombohedra.
- :mod:`geometor.knott.phigits` — **Collection 4** (``KNOTT-4.1`` –
  ``KNOTT-4.3``): integer-power Fibonacci linearization
  :math:`\Phi^n = F_n \Phi + F_{n-1}`, the unit-volume Phibonacci brick,
  continued-fraction convergents :math:`F_{k+1}/F_k`, and George Bergman's
  base-:math:`\Phi` ("phigit") minimal/maximal encoders and multi-form enumerator.
- :mod:`geometor.knott.golden_string` — **Collection 5** (``KNOTT-5.1`` –
  ``KNOTT-5.3``): Sturmian Golden String morphism vs. Beatty cutting-line slope
  :math:`\phi`, Zeckendorf non-consecutive Fibonacci base representations, and
  Beatty, Wythoff, and Stolarsky interspersion arrays.
- :mod:`geometor.knott.identities` — **Collection 6** (``KNOTT-6.1`` –
  ``KNOTT-6.5``): four-term Fibonacci Pythagorean triple generators, Cassini's
  :math:`64 \leftrightarrow 65` and :math:`64 \leftrightarrow 63` jigsaw
  dissections, Binet/Lucas/Catalan/d'Ocagne/Honsberger & Fibonomial power
  recurrences, reciprocal Fibonacci arctangent telescoping series for
  :math:`\pi / 4`, and the unimodular Golden Angle parastichy lattice.
- :mod:`geometor.knott.catalog` — Master registry of the 6 Collections
  (:data:`~geometor.knott.catalog.COLLECTIONS`) and 22 Catalog Items
  (:data:`~geometor.knott.catalog.CATALOG_ITEMS`), validator runner, and
  ``resources/catalog_manifest.json`` exporter.
- :mod:`geometor.knott.svg_renderer` — Deterministic theme-adaptive
  ``.euclid-graphic`` SVG serializer with 3-vertex midpoint ``<path>`` segments,
  ``#geom-tick-1..3`` equality markers, and radial collision-free label placement.
