==============
GEOMETOR Knott
==============

**A GEOMETOR Mathematical Catalog of Dr. Ron Knott's Golden Ratio, Phigit, Golden String, and Fibonacci Archive**

``geometor-knott`` catalogs **22 foundational theorems, compass-and-straightedge
constructions, 3D polyhedral structures, exact trigonometric lattices, base-**:math:`\Phi`
**("phigit") numeral algorithms, Golden String Sturmian morphisms, and Fibonacci/Lucas
identities** (`KNOTT-1.1` through `KNOTT-6.5`) curated by **Dr. Ron Knott** in
*Fibonacci Numbers, the Golden Section and the Golden String*
(`https://r-knott.surrey.ac.uk/Fibonacci/fib.html <https://r-knott.surrey.ac.uk/Fibonacci/fib.html>`_,
University of Surrey, © 1996–2025).

Every cataloged item is modeled and machine-verified from scratch using **100% exact
symbolic algebra** in `SymPy <https://www.sympy.org/>`_ and
`geometor.model <https://github.com/geometor/model>`_, rendered as an original
interactive ``.euclid-graphic`` SVG with bidirectional ``:g:`` and ``:eq:``
highlighting.

Why a "Mathematical Catalog"?
-----------------------------

Within the **GEOMETOR** ecosystem, scholarly repositories follow a strict methodological
distinction between **Editions / Codices** and **Mathematical Catalogs**:

- **Editions & Codices** (such as ``geometor/euclid``, ``geometor/pacioli``,
  ``geometor/proclus``, ``geometor/hilbert``, and ``geometor/altshiller-court``)
  present folio-calibrated transcriptions and translations of **public-domain**
  historical treatises.
- **Mathematical Catalogs** (such as ``geometor/etc`` for Clark Kimberling's
  *Encyclopedia of Triangle Centers*, ``geometor/wildberger`` for N. J. Wildberger's
  *Divine Proportions*, and ``geometor/knott`` for Dr. Ron Knott's Surrey archive)
  document mathematical facts from **modern works under copyright** in a consistent,
  machine-verifiable canonical form for study and cross-corpus reasoning.

Accordingly, ``geometor-knott`` reproduces **zero copyrighted prose and zero images**
from ``r-knott.surrey.ac.uk``. Instead, each catalog entry records:

1. **Canonical Enunciation** of the underlying mathematical theorem, construction, or
   identity in GEOMETOR's formal mathematical prose;
2. **Structured Source Attribution** citing Dr. Ron Knott's exact page URL, HTML
   section anchor, and copyright notice (``© 1996–2025 Dr. Ron Knott, University of Surrey``);
3. **100% Exact Symbolic Verification** over :math:`\mathbb{Q}`,
   :math:`\mathbb{Q}(\sqrt{5})`, :math:`\mathbb{Q}(\sqrt{\Phi})`, or
   :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3}, \sqrt{5})` with zero floating-point
   approximations;
4. **Original Interactive** ``.euclid-graphic`` **SVG** generated directly from
   ``geometor.model.Model`` coordinates; and
5. **Cross-Corpus GEOMETOR Concordance** linking Euclid's *Elements*, Pacioli,
   Wildberger's Rational Trigonometry, phyllotaxis, and the ``geometor.divine``
   proportion scanner.

Notation Bridge: Knott (:math:`\Phi, \phi`) vs. GEOMETOR (``sp.GoldenRatio``)
-----------------------------------------------------------------------------

Dr. Ron Knott distinguishes the Golden Ratio and its reciprocal by case, whereas
SymPy and ``geometor.model`` denote the larger root by :math:`\phi`:

.. list-table::
   :widths: 28 36 36
   :header-rows: 1

   * - Quantity
     - Dr. Ron Knott Convention
     - GEOMETOR / SymPy Convention
   * - Golden Ratio (:math:`\approx 1.6180339887\dots`)
     - :math:`\Phi = \dfrac{1 + \sqrt{5}}{2}` (``knott.PHI``)
     - :math:`\phi = \dfrac{1 + \sqrt{5}}{2}` (``sp.GoldenRatio``)
   * - Reciprocal Golden Ratio (:math:`\approx 0.6180339887\dots`)
     - :math:`\phi = \Phi - 1 = \dfrac{1}{\Phi} = \dfrac{\sqrt{5} - 1}{2}` (``knott.phi``)
     - :math:`\phi^{-1} = \phi - 1 = \dfrac{\sqrt{5} - 1}{2}` (``1 / sp.GoldenRatio``)
   * - Defining Quadratic Identities
     - :math:`\Phi^2 = \Phi + 1`, :math:`\phi^2 = 1 - \phi`, :math:`\Phi \cdot \phi = 1`
     - :math:`\phi^2 = \phi + 1`, :math:`\phi^{-2} = 1 - \phi^{-1}`

Both ``PHI`` and ``phi`` are exported in ``geometor.knott.constants`` as exact closed-form
:math:`\mathbb{Q}(\sqrt{5})` radical expressions with explicit bijection helpers to
``sp.GoldenRatio``.

Six Thematic Collections (22 Catalog Items)
-------------------------------------------

1. **01 — 2D Golden Geometry & Constructions** (``KNOTT-1.1`` – ``KNOTT-1.6``):
   Internal/external golden sections, golden & :math:`\sqrt{5}` rectangles with
   perpendicular gnomonic diagonals, golden triangles & gnomons, pentagon/pentagram &
   paper-knot pentagon, Kepler's :math:`(1, \sqrt{\Phi}, \Phi)` right triangle, and
   Penrose :math:`P2/P3` aperiodic tilings.
2. **02 — Exact Pentagonal & Constructible Trigonometry** (``KNOTT-2.1`` – ``KNOTT-2.2``):
   Closed-form radicals and Rational Trigonometry spreads for :math:`18^\circ, 36^\circ,
   54^\circ, 72^\circ` and the complete 29-angle :math:`3^\circ` constructible lattice
   (:math:`3^\circ k`, :math:`k = 1\dots 29`) plus Gauss's :math:`17`-gon cosine.
3. **03 — 3D Golden Geometry of Solids** (``KNOTT-3.1`` – ``KNOTT-3.3``):
   Three orthogonal golden rectangles spanning the icosahedron and dodecahedron,
   the inscribed cube & compound of five cubes, and the acute/obtuse golden
   rhombohedra of 3D quasicrystals.
4. **04 — Algebraic Powers of** :math:`\Phi` **, Continued Fractions & Base-**:math:`\Phi` **"Phigits"** (``KNOTT-4.1`` – ``KNOTT-4.3``):
   Fibonacci power linearization & the Phibonacci brick, extremal continued fraction
   :math:`[1; 1, 1, \dots]` & Hurwitz bound, and George Bergman's base-:math:`\Phi`
   ("phigit") numeral encoder/decoder.
5. **05 — The Golden String, Zeckendorf Base, & Wythoff / Stolarsky Arrays** (``KNOTT-5.1`` – ``KNOTT-5.3``):
   Infinite Sturmian Golden String ``101101011011...`` via morphism & lattice-cutting
   line of slope :math:`\phi`, Zeckendorf's canonical Fibonacci base, and the bijective
   Wythoff, Beatty, and Stolarsky arrays.
6. **06 — Fibonacci-Lucas Identities, Pythagorean Triples, Jigsaw Paradoxes &** :math:`\pi` (``KNOTT-6.1`` – ``KNOTT-6.5``):
   Primitive Pythagorean triple generator, Cassini's :math:`64 \leftrightarrow 65 / 63`
   jigsaw dissections, Binet/Lucas/Catalan/d'Ocagne/Honsberger/Fibonomial identities,
   Fibonacci arctangent telescoping series for :math:`\pi`, and the Golden Angle
   parastichy bridge.

Quick Verification
------------------

.. code-block:: bash

   ruff check src scripts tests
   uv run --no-sync pytest
   publish build
