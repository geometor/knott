:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor-knott`` is an exact symbolic **Mathematical Catalog**, semantic index, and interactive geometric codex structured around the foundational mathematical compendium *Fibonacci Numbers, the Golden Section and the Golden String* (`https://r-knott.surrey.ac.uk/Fibonacci/fib.html <https://r-knott.surrey.ac.uk/Fibonacci/fib.html>`_), authored and continuously maintained since 1996 by :person:`Dr. Ron Knott <knott>` (formerly of the Department of Mathematics at the University of Surrey). Spanning planar and solid Golden Section constructions, constructible pentagonal trigonometry, base-:math:`\Phi` ("phigit") arithmetic, Sturmian Golden String morphisms, Zeckendorf representations, Wythoff and Stolarsky interspersion arrays, and Fibonacci–Lucas arctangent series for :math:`\pi`, Dr. Knott's work represents one of the richest pedagogical repositories of discrete geometry and number theory on the web.

Unlike GEOMETOR's public-domain historical editions derived directly from archival folios (such as ``geometor/elements``, ``geometor/pappus``, or ``geometor/kepler``), modern copyrighted works require a distinct editorial methodology: the **GEOMETOR Mathematical Catalog**. Rather than duplicating copyrighted prose, HTML markup, or bitmap figures, this edition extracts the underlying mathematical principles into independent, machine-addressable semantic enunciations across 22 catalog entries (``KNOTT-1.1`` through ``KNOTT-6.5``) arranged in 6 thematic collections. Each entry provides deep section-level attribution to Dr. Knott's corresponding pages, encouraging readers to consult his original exposition directly.

Every cataloged theorem, sequence identity, and geometric construction is reconstructed and verified from first principles in 100% exact symbolic algebra using `SymPy <https://www.sympy.org/>`_ and :mod:`geometor.model` without floating-point approximations. Each entry generates a clean, theme-adaptive interactive ``.euclid-graphic`` SVG diagram directly from its algebraic model. This connects Dr. Knott's contemporary corpus with the wider GEOMETOR ecosystem—linking Euclidean foundations in ``geometor.elements``, Luca Pacioli's *De Divina Proportione* in ``geometor.divine``, Johannes Kepler's crystallography in ``geometor.kepler``, and Norman Wildberger's Rational Trigonometry in ``geometor.model``.

The GEOMETOR Mission
--------------------

The **GEOMETOR** initiative, conceived and directed by **phi ARCHITECT**, is dedicated to the systematic recovery, symbolic formalization, and creative re-articulation of humanity's geometric heritage. GEOMETOR unites classical synthesis with modern algebraic rigor across three core pillars:

Extracting Historical Semantic Knowledge
    Moving beyond passive page scans, static facsimile bitmaps, and flat optical character recognition (OCR), GEOMETOR recovers the living deductive architecture of 2,300+ years of geometric, axiomatic, and philosophical treatises. Primary sources—spanning Euclid, Apollonius, Archimedes, Pappus, Johannes Kepler, Felix Klein, and Clark Kimberling—are analyzed to elevate enunciations, deductive steps, synthetic justifications, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.

Exact Symbolic Grounding (``geometor.model``)
    Geometric constructions must not depend on floating-point approximations or visual artifacts. GEOMETOR anchors geometric entities in 100% exact symbolic algebra via `SymPy <https://www.sympy.org/>`_ and the principles of Rational Trigonometry (quadrance, spread, cross-ratio). Points, lines, circles, and conic loci are evaluated over exact algebraic fields, ensuring that tangencies, incidences, harmonic conjugates, and collinearities represent absolute mathematical truths rather than numerical estimates.

Repurposing Knowledge Across Mediums
    Extracted semantic architectures and exact symbolic models are re-deployed across a unified digital ecosystem: synchronized multi-track **Book Codices** and EPUB 3 editions powered by ``photon-platform/publish``, computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG exploration laboratories (``geometor.explorer``), ultra-high-definition visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

Curated Reference Source
~~~~~~~~~~~~~~~~~~~~~~~~

* **Curated Work**: *Fibonacci Numbers, the Golden Section and the Golden String*, hosted at the University of Surrey (`https://r-knott.surrey.ac.uk/Fibonacci/fib.html <https://r-knott.surrey.ac.uk/Fibonacci/fib.html>`_).
* **Author**: :person:`Dr. Ron Knott <knott>`, formerly of the Department of Mathematics, University of Surrey, Guildford, UK.
* **Copyright Notice**: **© 1996–2025 Dr. Ron Knott**. All rights reserved by the author.

Mathematical Catalog Principles & Source Respect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Zero Copyrighted Text or Media Reproduction**: Not a single prose sentence, HTML markup block, or bitmap illustration is copied from ``r-knott.surrey.ac.uk``. Mathematical relations, recurrence relations, and geometric theorems are universal truths; Dr. Knott's pedagogical prose belongs exclusively to him.
2. **Exact Section-Level Attribution**: Every catalog entry (``KNOTT-1.1`` through ``KNOTT-6.5``) records the exact page title, full clickable URL with anchor (``#anchor``), and copyright credit to Dr. Ron Knott.
3. **100% Exact Symbolic Grounding**: Every cataloged identity and construction is implemented in ``geometor.knott`` over :math:`\mathbb{Q}`, :math:`\mathbb{Q}(\sqrt{5})`, :math:`\mathbb{Q}(\sqrt{\Phi})`, or explicit cyclotomic fields with zero ``float`` approximations, verified through polynomial reductions and Rational Trigonometry invariants.
4. **Original Interactive Euclid Graphics**: Every entry renders an original, theme-adaptive vector diagram synthesized directly from its ``geometor.model.Model`` instance, wired to inline ``:g:`` and ``:eq:`` highlights.
5. **Cross-Corpus Concordance**: Every entry links Dr. Knott's mathematical discoveries across the GEOMETOR canon, including ``geometor.elements``, ``geometor.divine``, ``geometor.kepler``, and ``geometor.etc``.
