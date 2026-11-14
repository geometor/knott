=========
Changelog
=========

0.1.1 (2026-11-14)
------------------

- Standardized Book Title Page, top-level header navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author and Translator profiles in People, and English structural terminology.

0.1.0 (2026-11-12)
------------------

- Establish the **GEOMETOR Knott Mathematical Catalog** (``geometor-knott``),
  cataloging 22 theorems, geometric constructions, 3D polyhedral structures,
  exact trigonometric radical tables, base-:math:`\Phi` ("phigit") algorithms,
  Golden String morphisms, Wythoff/Stolarsky arrays, and Fibonacci/Lucas
  identities curated by Dr. Ron Knott (University of Surrey, © 1996–2025).
- Implement 100% exact ``SymPy`` and ``geometor.model`` symbolic models across
  all six thematic collections (`KNOTT-1.1` through `KNOTT-6.5`) with zero
  floating-point coordinates.
- Render 22 interactive ``.euclid-graphic`` SVG figures with bidirectional
  ``:g:`` and ``:eq:`` prose-to-diagram highlighting and inline ``.. collection::``
  SVG thumbnail cards.
- Publish ``resources/catalog_manifest.json`` along with full scholarly
  apparatus (`glossary.rst`, `persons.rst`, `bibliography.rst`) and a
  comprehensive ``pytest`` verification suite.
