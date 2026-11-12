# GEOMETOR Knott (`geometor-knott`)

## Purpose & Architectural Role ("Mathematical Cataloging")

`geometor/knott` is a **GEOMETOR Mathematical Catalog** documenting the Golden Ratio geometry, 3D polyhedral structures, exact pentagonal/constructible trigonometry, base-$\Phi$ ("phigit") numeral systems, Golden String Sturmian sequences, Wythoff/Stolarsky arrays, and Fibonacci/Lucas identities curated by **Dr. Ron Knott** in *Fibonacci Numbers, the Golden Section and the Golden String* (`https://r-knott.surrey.ac.uk/Fibonacci/fib.html`, University of Surrey, © 1996–2025).

### Cataloging vs. Editions

- **Historical Editions / Codices** (`euclid`, `pacioli`, `proclus`, `aristotle`, `aquinas`, `hoenen`, `hilbert`, `bertrand-russell`, `altshiller-court`) transcribe and calibrate **public-domain** source texts.
- **Mathematical Catalogs** (`etc`, `wildberger`, `knott`) document the mathematical facts, theorems, constructions, sequences, and identities curated in **modern copyrighted works** without copying a single sentence of copyrighted prose or any source image. Every entry in `geometor/knott` provides:
  1. Original formal enunciation (`.. enunciation::`);
  2. Structured source citation (`© 1996–2025 Dr. Ron Knott, University of Surrey`, exact URL + `#anchor`);
  3. 100% exact symbolic `SymPy` + `geometor.model` construction and proof (`0` `sp.Float` atoms);
  4. Original theme-adaptive `.euclid-graphic` SVG with `:g:` and `:eq:` bidirectional interactivity;
  5. Cross-corpus GEOMETOR links (`euclid`, `elements`, `pacioli`, `wildberger`, `etc`, `divine`, `phyllotaxis`).

## Notation Convention Bridge

- **Dr. Ron Knott**: $\Phi = \frac{1 + \sqrt{5}}{2} \approx 1.61803\dots$ (`PHI`) and $\phi = \Phi - 1 = \frac{1}{\Phi} = \frac{\sqrt{5} - 1}{2} \approx 0.61803\dots$ (`phi`).
- **GEOMETOR / SymPy**: `sp.GoldenRatio` denotes $\phi_{\text{GEOMETOR}} = \frac{1 + \sqrt{5}}{2} = \Phi_{\text{Knott}}$, while $\phi_{\text{GEOMETOR}}^{-1} = \phi_{\text{GEOMETOR}} - 1 = \phi_{\text{Knott}}$.

## Key Modules (`src/geometor/knott/`)

- `constants.py`: Exact $\mathbb{Q}(\sqrt{5})$ constants `PHI`, `phi`, `sp.GoldenRatio` bijection helpers, Rational Trigonometry `quadrance`, `spread`, `cross_ratio`, polygon signed area, and `assert_no_floats`.
- `flat_geometry.py`: Collection 1 (`KNOTT-1.1`–`KNOTT-1.6`) exact 2D `geometor.model` constructions.
- `trigonometry.py`: Collection 2 (`KNOTT-2.1`–`KNOTT-2.2`) pentagonal radicals, spreads, complete $3^\circ k$ ($k=1..29$) constructible lattice, and Gauss $\cos(\pi/17)$ radical verification.
- `solid_geometry.py`: Collection 3 (`KNOTT-3.1`–`KNOTT-3.3`) 3D orthogonal golden rectangles, icosahedron/dodecahedron, compound of 5 cubes, and acute/obtuse golden rhombohedra with exact isometric 2D `Model` projections.
- `phigits.py`: Collection 4 (`KNOTT-4.1`–`KNOTT-4.3`) $\Phi^n$ Fibonacci power linearization, continued fraction convergents, and Bergman's base-$\Phi$ ("phigit") minimal/maximal/all-forms engine.
- `golden_string.py`: Collection 5 (`KNOTT-5.1`–`KNOTT-5.3`) Sturmian Golden String morphism & slope-$\phi$ lattice-cutting ray, Zeckendorf Fibonacci base, and Wythoff / Beatty / Stolarsky bijective arrays.
- `identities.py`: Collection 6 (`KNOTT-6.1`–`KNOTT-6.5`) Fibonacci Pythagorean triples, Cassini $64 \leftrightarrow 65 / 63$ jigsaw dissections, Binet/Lucas/Catalan/d'Ocagne/Honsberger/Fibonomial identities, Fibonacci $\pi$ arctangent telescoping series, and Golden Angle parastichy invariants.
- `svg_renderer.py`: Exact `geometor.model.Model` $\to$ `.euclid-graphic` SVG serializer with 3-vertex midpoint `<path>` segments, `#highlights` overlays, and tick markers.
- `catalog.py` & `__main__.py`: Unified 22-item catalog registry, JSON manifest exporter (`resources/catalog_manifest.json`), verifier, and CLI.

## Verification Gates (Python 3.13 Sandbox)

```bash
ruff check src scripts tests
uv run --no-sync pytest
publish build
```
