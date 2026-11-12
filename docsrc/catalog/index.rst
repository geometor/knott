:layout: book
:navigation: header
:order: 10

====================
Mathematical Catalog
====================

.. enunciation::

   Six thematic collections cataloging **22** Golden Ratio, trigonometric, polyhedral, phigit, Sturmian, and Fibonacci–Lucas structures from :person:`Dr. Ron Knott <knott>`'s *Fibonacci Numbers, the Golden Section and the Golden String* (**© 1996–2025 Dr. Ron Knott, University of Surrey**), each proven with 100% exact ``SymPy`` algebra and rendered as an interactive ``.euclid-graphic`` SVG.

.. collection::
   :type: collection
   :sort: order

Master 22-Entry Concordance
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 14 42 18 26

   * - ID
     - Title
     - Knott Anchor
     - Symbolic Validator
   * - :ref:`KNOTT-1.1 <knott-1-1>`
     - Internal & External Golden Section Constructions on a Segment
     - `#cons <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#cons>`_
     - :func:`~geometor.knott.flat_geometry.construct_golden_section_segment`
   * - :ref:`KNOTT-1.2 <knott-1-2>`
     - Golden Rectangles, √5 Rectangles, & Whirling-Square Gnomonic Spirals
     - `#root5 <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#root5>`_
     - :func:`~geometor.knott.flat_geometry.construct_golden_rectangles_and_spiral`
   * - :ref:`KNOTT-1.3 <knott-1-3>`
     - Golden Triangles (72°–72°–36°) & Golden Gnomons (36°–36°–108°)
     - `#isoc <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#isoc>`_
     - :func:`~geometor.knott.flat_geometry.construct_golden_triangles_and_gnomons`
   * - :ref:`KNOTT-1.4 <knott-1-4>`
     - Regular Pentagon, Pentagram, Decagon & Paper-Knot Pentagon
     - `#pent <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#pent>`_
     - :func:`~geometor.knott.flat_geometry.construct_pentagon_and_paper_knot`
   * - :ref:`KNOTT-1.5 <knott-1-5>`
     - Kepler's Golden Right Triangle (1, √Φ, Φ) & Circle-Square Near-Quadrature
     - `#PhiRightAng <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#PhiRightAng>`_
     - :func:`~geometor.knott.flat_geometry.construct_kepler_triangle`
   * - :ref:`KNOTT-1.6 <knott-1-6>`
     - Penrose Kites & Darts (P2) and Thick & Thin Golden Rhombs (P3)
     - `#penrose <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#penrose>`_
     - :func:`~geometor.knott.flat_geometry.construct_penrose_tiles`
   * - :ref:`KNOTT-2.1 <knott-2-1>`
     - Exact Radical Sines, Cosines, Tangents & Spreads of 18°, 36°, 54°, 72°
     - `#3654 <https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html#3654>`_
     - :func:`~geometor.knott.trigonometry.construct_pentagonal_trig_model`
   * - :ref:`KNOTT-2.2 <knott-2-2>`
     - The Complete 3° Constructible Angle Lattice (3°k for k = 1..29)
     - `#otherexact <https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html#otherexact>`_
     - :func:`~geometor.knott.trigonometry.construct_three_degree_lattice_model`
   * - :ref:`KNOTT-3.1 <knott-3-1>`
     - Three Orthogonal Golden Rectangles → Regular Icosahedron & Dodecahedron
     - `#coords <https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#coords>`_
     - :func:`~geometor.knott.solid_geometry.construct_orthogonal_golden_rectangles_solids`
   * - :ref:`KNOTT-3.2 <knott-3-2>`
     - Inscribed Cube & Compound of Five Cubes in a Dodecahedron
     - `#cubeinDod <https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#cubeinDod>`_
     - :func:`~geometor.knott.solid_geometry.construct_cube_in_dodecahedron_model`
   * - :ref:`KNOTT-3.3 <knott-3-3>`
     - Acute & Obtuse Golden Rhombohedra (3D Quasicrystal / Ammann Tiles)
     - `#quasicrystalsPhi <https://r-knott.surrey.ac.uk/Fibonacci/phi3DGeom.html#quasicrystalsPhi>`_
     - :func:`~geometor.knott.solid_geometry.construct_golden_rhombohedra_model`
   * - :ref:`KNOTT-4.1 <knott-4-1>`
     - Fibonacci Power Linearization (Φⁿ = FₙΦ + Fₙ₋₁) & The Phibonacci Brick
     - `#powers <https://r-knott.surrey.ac.uk/Fibonacci/propsOfPhi.html#powers>`_
     - :func:`~geometor.knott.phigits.construct_phi_powers_model`
   * - :ref:`KNOTT-4.2 <knott-4-2>`
     - Extremal Continued Fraction [1; 1, 1, …], Convergents Fₙ₊₁/Fₙ, & Nested Radicals
     - `#contfract <https://r-knott.surrey.ac.uk/Fibonacci/propsOfPhi.html#contfract>`_
     - :func:`~geometor.knott.phigits.construct_convergents_model`
   * - :ref:`KNOTT-4.3 <knott-4-3>`
     - Bergman's Base-Φ ('Phigit') Numeral System
     - `#canonical <https://r-knott.surrey.ac.uk/Fibonacci/phigits.html#canonical>`_
     - :func:`~geometor.knott.phigits.construct_phigit_scale_model`
   * - :ref:`KNOTT-5.1 <knott-5-1>`
     - The Infinite Golden String (101101011011…), Rabbit Tree & Cutting-Line Slope φ
     - `#PhiPlot <https://r-knott.surrey.ac.uk/Fibonacci/fibrab.html#PhiPlot>`_
     - :func:`~geometor.knott.golden_string.construct_golden_string_cutting_model`
   * - :ref:`KNOTT-5.2 <knott-5-2>`
     - Zeckendorf's Theorem (Canonical Fibonacci Base Representation)
     - `#zeck <https://r-knott.surrey.ac.uk/Fibonacci/fibrep.html#zeck>`_
     - :func:`~geometor.knott.golden_string.construct_zeckendorf_staircase_model`
   * - :ref:`KNOTT-5.3 <knott-5-3>`
     - Wythoff's Array, Beatty's Complementary Sequences (⌊nΦ⌋, ⌊nΦ²⌋), & Stolarsky's Array
     - `#wythoff <https://r-knott.surrey.ac.uk/Fibonacci/fibGen.html#wythoff>`_
     - :func:`~geometor.knott.golden_string.construct_wythoff_beatty_model`
   * - :ref:`KNOTT-6.1 <knott-6-1>`
     - Fibonacci Generator of Primitive Pythagorean Triples
     - `#pythfib <https://r-knott.surrey.ac.uk/Pythag/pythag.html#pythfib>`_
     - :func:`~geometor.knott.identities.construct_fibonacci_pythagorean_model`
   * - :ref:`KNOTT-6.2 <knott-6-2>`
     - Cassini's Identity (Fₙ₋₁Fₙ₊₁ − Fₙ² = (−1)ⁿ) & The 64 ↔ 65 / 63 Jigsaw Dissections
     - `#jigsaw1 <https://r-knott.surrey.ac.uk/Fibonacci/fibpuzzles2.html#jigsaw1>`_
     - :func:`~geometor.knott.identities.construct_fibonacci_jigsaw_model`
   * - :ref:`KNOTT-6.3 <knott-6-3>`
     - Binet, Lucas, Catalan, d'Ocagne, Honsberger & Fibonomial Power Identities
     - `#defs <https://r-knott.surrey.ac.uk/Fibonacci/fibFormulae.html#defs>`_
     - :func:`~geometor.knott.identities.construct_lucas_binet_model`
   * - :ref:`KNOTT-6.4 <knott-6-4>`
     - Fibonacci Arctangent Telescoping Formulae for π
     - `#piandfib <https://r-knott.surrey.ac.uk/Fibonacci/fibpi.html#piandfib>`_
     - :func:`~geometor.knott.identities.construct_hayashi_arctan_grid_model`
   * - :ref:`KNOTT-6.5 <knott-6-5>`
     - Golden Angle (360° / Φ² ≈ 137.50776°) & Parastichy Bridges
     - `#seeds <https://r-knott.surrey.ac.uk/Fibonacci/fibnat.html#seeds>`_
     - :func:`~geometor.knott.identities.construct_parastichy_lattice_model`
