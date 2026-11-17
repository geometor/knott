:navigation: header
:order: 20
:nav_title: Usage

.. _knott-usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the GEOMETOR Mathematical Catalog

Welcome to the **GEOMETOR Knott Mathematical Catalog**. This catalog synthesizes the landmark research of :person:`Dr. Ron Knott <knott>` (*Fibonacci Numbers, the Golden Section and the Golden String*) into a formal, exact symbolic digital catalog.

The 22-Entry Catalog Collections
--------------------------------

The catalog is organized into six thematic collections spanning 22 milestone entries:

1. **Collection 1: Flat Geometry & Pentagonal Tile Systems** (``KNOTT-1.1`` – ``KNOTT-1.6``) — Segment divisions, golden rectangles, golden triangles, pentagrams, Kepler's right triangle, and Penrose tiling.
2. **Collection 2: Exact Pentagonal & 3° Trigonometry** (``KNOTT-2.1`` – ``KNOTT-2.2``) — Exact radical expressions and rational trigonometry spreads across the complete :math:`3^\circ` constructible angle lattice.
3. **Collection 3: Solid Geometry & Golden Quasicrystals** (``KNOTT-3.1`` – ``KNOTT-3.3``) — Orthogonal golden rectangles in icosahedra and dodecahedra, compounds of five cubes, and 3D golden rhombohedra.
4. **Collection 4: Base-Φ Phigits & Continued Fractions** (``KNOTT-4.1`` – ``KNOTT-4.3``) — Fibonacci power linearization, infinite continued fraction convergents, and Bergman's base-:math:`\Phi` ("phigit") system.
5. **Collection 5: Golden String Morphisms & Interspersion Arrays** (``KNOTT-5.1`` – ``KNOTT-5.3``) — The Sturmian golden cutting sequence, Zeckendorf representations, and Wythoff/Beatty/Stolarsky arrays.
6. **Collection 6: Fibonacci–Lucas Identities & π Bridges** (``KNOTT-6.1`` – ``KNOTT-6.5``) — Fibonacci Pythagorean triples, Cassini jigsaw dissections, Fibonomial powers, arctangent telescoping formulas for :math:`\pi`, and phyllotaxis parastichies.

Primary-Source Web Deep-Links
-----------------------------

As a Mathematical Catalog of a copyrighted modern web compendium, zero prose or images are copied from Dr. Knott's work. Instead, each catalog entry pairs an original GEOMETOR enunciation and independent SymPy proof with deep links to Dr. Knott's primary pages at the University of Surrey (`https://r-knott.surrey.ac.uk <https://r-knott.surrey.ac.uk>`_), citing his precise section anchors (such as ``#cons``, ``#penrose``, or ``#quasicrystalsPhi``).

Exact Symbolic Models & Interactive SVG Plates
----------------------------------------------

Every catalog item is verified symbolically and rendered visually:

* **Pure Symbolic Computation**: Invariants are computed over exact algebraic number fields :math:`\mathbb{Q}(\sqrt{5})` and :math:`\mathbb{Q}(\sqrt{\Phi})` with zero floating-point coordinates.
* **Interactive SVG Diagrams**: Vector diagrams rendered with responsive styling highlight geometric lines, vertices, and intersections.
* **Notation Mapping**: Explore exact conversions between Knott's uppercase :math:`\Phi` and SymPy/GEOMETOR notation in :doc:`/notation/index`.

Full-Text Search with In-Page Highlighting
------------------------------------------

Search across all catalog items, proofs, and API documentation using the built-in search tool.
Queries automatically pass terms via `?highlight=`, highlighting searched keywords directly inside mathematical definitions and theorem texts.

Categories, Tags & Collection Views
-----------------------------------

Content is structured along modular facets:

* Filter catalog items and logs by collection, tag, or topic using the sidebar taxonomy panels.
* In collection listings and the :doc:`/log/index`, toggle between **Cards**, **Banners**, and **List** views using the collection layout switcher.

People, Bibliography & Glossary Tooltips
----------------------------------------

The catalog includes comprehensive scholarly registries:

* **People (``:person:``)**: Reference cards connect mathematicians such as :person:`Leonardo Pisano (Fibonacci) <fibonacci>`, :person:`Édouard Lucas <lucas>`, and :person:`Dr. Ron Knott <knott>` to :doc:`/people/index`.
* **Citations (``:cite:``)**: Bibliographic keys link directly to literature entries in :doc:`/bibliography`.
* **Terms (``:term:``)**: Definitions of mathematical concepts connect to entries in the :doc:`/glossary`.
* **Theme Toggle**: Switch between Light and Dark display modes using the theme button in the header bar.

Command-Line & Python API
-------------------------

The ``geometor.knott`` package provides exact algorithms and construction routines:

.. code-block:: bash

   # Run CLI help
   /home/phi/PROJECTS/geometor/.venv/bin/python -m geometor.knott --help

   # Run test suite
   /home/phi/PROJECTS/geometor/.venv/bin/pytest

Explore complete module documentation in :doc:`/modules/index`.
