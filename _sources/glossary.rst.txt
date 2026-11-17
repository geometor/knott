:navigation: header
:order: 16
:nav_title: Glossary

.. _glossary:

========
Glossary
========

Exact geometric, trigonometric, and number-theoretic terms referenced across the **GEOMETOR Knott Mathematical Catalog**.

.. _term-golden-ratio:

Golden Ratio (Φ, φ)
-------------------

*Knott: Φ = (1+√5)/2, φ = (√5−1)/2*

Positive root Φ = (1+√5)/2 ≈ 1.6180339887 of x^2 − x − 1 = 0, paired in Dr. Ron Knott's notation with its reciprocal φ = Φ − 1 = 1/Φ ≈ 0.6180339887 (corresponding to SymPy/GEOMETOR sp.GoldenRatio and 1/sp.GoldenRatio).

.. _term-extreme-and-mean-ratio:

Extreme and Mean Ratio
----------------------

*ἄκρος καὶ μέσος λόγος (Euclid VI.def.3)*

Division of a straight segment AB at G such that the whole AB is to the greater part AG as AG is to the lesser part GB (AB : AG = AG : GB = Φ).

.. _term-cross-ratio:

Cross-Ratio
-----------

*(A, B; C, D)*

Projective four-point invariant (A−C)(B−D) / ((A−D)(B−C)) preserved under all central projections and linear fractional transformations.

.. _term-golden-rectangle:

Golden Rectangle
----------------

*1 × Φ or φ × 1 rectangle*

Rectangle whose side lengths stand in the Golden Ratio Φ : 1; removing a square gnomon leaves a congruent-shaped daughter golden rectangle rotated by 90°.

.. _term-gnomon:

Gnomon
------

*γνώμων*

Geometric figure which, when added to or removed from a given figure, leaves a new figure similar to the original (such as a unit square adjoined to a golden rectangle or an obtuse golden triangle adjoined to an acute golden triangle).

.. _term-quadrance:

Quadrance
---------

*Q(A, B) = (x₂−x₁)² + (y₂−y₁)²*

Exact squared Euclidean separation between two points in Rational Trigonometry, remaining purely polynomial over the coordinate field without square roots.

.. _term-spread:

Spread
------

*s(l₁, l₂) = sin² θ*

Exact Rational Trigonometry measure of separation between two lines, defined algebraically in [0, 1] with s = 0 for parallel lines and s = 1 for perpendicular lines.

.. _term-golden-triangle:

Golden Triangle (Acute)
-----------------------

*72°–72°–36° isosceles triangle*

Euclid IV.10 isosceles triangle with leg-to-base ratio Φ : 1 and exact spreads s(72°) = (5+√5)/8 and s(36°) = (5−√5)/8.

.. _term-golden-gnomon:

Golden Gnomon (Obtuse)
----------------------

*36°–36°–108° isosceles triangle*

Obtuse isosceles triangle with base-to-leg ratio Φ : 1 (or 1 : φ) and apex spread s(108°) = (5+√5)/8.

.. _term-pentagram:

Pentagram
---------

*{5/2} regular star pentagon*

Five-pointed star formed by the five diagonals of a regular pentagon, cutting every diagonal into segments in geometric progression φ² : φ : 1 : Φ.

.. _term-kepler-triangle:

Kepler Triangle
---------------

*(1, √Φ, Φ) right triangle*

Unique right triangle up to similarity whose side lengths (1, √Φ, Φ) — and side quadrances (1, Φ, Φ²) — form a geometric progression.

.. _term-penrose-tiling:

Penrose Prototiles (P2 / P3)
----------------------------

*Kite & Dart / Thick & Thin Rhombs*

Roger Penrose's golden-triangle and golden-gnomon prototile pairs with exact area ratio Φ : 1 that tile the plane only nonperiodically under matching rules.

.. _term-constructible-angle:

Constructible Angle
-------------------

*Straightedge-and-compass angle*

Angle whose sine and cosine lie in an iterated quadratic extension of Q; integer-degree constructible angles are exactly the multiples of 3°.

.. _term-golden-rhombohedron:

Golden Rhombohedra
------------------

*Acute (prolate) & Obtuse (oblate) 3D tiles*

Pair of hexahedra bounded by six congruent golden rhombi of diagonal ratio Φ : 1 with volume ratio Φ : 1, serving as 3D quasicrystal and rhombic-triacontahedron building blocks.

.. _term-continued-fraction:

Simple Continued Fraction
-------------------------

*[a₀; a₁, a₂, …]*

Canonical nested-reciprocal representation of a real number; Φ = [1; 1, 1, …] has minimal partial quotients and slowest possible rational convergence.

.. _term-cassini-identity:

Cassini's Identity
------------------

*F_{n−1} F_{n+1} − F_n² = (−1)ⁿ*

Determinant invariant of the Fibonacci Q-matrix ((1, 1), (1, 0))ⁿ governing convergent errors, area-paradox dissections, and Fibonacci arctangent telescoping.

.. _term-phigit:

Phigit (Base-Φ Digit)
---------------------

*George Bergman's base-Φ numeral*

Binary digit in {0, 1} weighting integer powers Φ^k; canonical minimal phigit form forbids adjacent 1s via the carry law 011_Φ = 100_Φ.

.. _term-zeckendorf-representation:

Zeckendorf Representation
-------------------------

*Canonical non-consecutive Fibonacci sum*

Unique representation of every positive integer N as a sum of non-adjacent Fibonacci numbers F_{k₁} + … + F_{k_r} (k_i ≥ k_{i+1} + 2, k_r ≥ 2).

.. _term-golden-string:

Golden String (Fibonacci Word)
------------------------------

*1011010110110101101…*

Infinite Sturmian sequence fixed by the substitution 1 ↦ 10, 0 ↦ 1 and generated equivalently by Beatty differences ⌊(n+1)φ⌋ − ⌊nφ⌋ or lattice crossings of y = φ x.

.. _term-beatty-sequence:

Beatty Complementary Pair
-------------------------

*(⌊nΦ⌋, ⌊nΦ²⌋)*

Disjoint, exhaustive partition of the positive integers into lower Wythoff numbers A_n = ⌊nΦ⌋ and upper Wythoff numbers B_n = ⌊nΦ²⌋ = A_n + n.

.. _term-wythoff-array:

Wythoff Array
-------------

*W(r, c) = ⌊(r+1)Φ⌋ F_{c+2} + r F_{c+1}*

Bijective two-dimensional interspersion array of all positive integers whose rows are generalized Fibonacci sequences classified by Zeckendorf shift classes.

.. _term-stolarsky-array:

Stolarsky Array
---------------

*Nearest-integer Golden Ratio interspersion*

Bijective array of all positive integers seeded by missing minimal integers and the nearest-integer Golden Ratio recurrence b = ⌊aΦ + 1/2⌋.

.. _term-fibonomial:

Fibonomial Coefficient
----------------------

*C(k, j)_F*

Fibonacci analogue of the binomial coefficient formed from descending and ascending products of Fibonacci numbers, governing linear recurrences of k-th powers F_n^k.

.. _term-golden-angle:

Golden Angle
------------

*360° / Φ² = 360° φ² ≈ 137.50776°*

Minor circular sector obtained by dividing a full 2π revolution in extreme and mean ratio, optimizing radial packing in botanical phyllotaxis.

.. _term-parastichy:

Parastichy
----------

*Opposing Fibonacci contact spirals (F_k, F_{k+1})*

Left- and right-handed visible spiral families in cylindrical or planar phyllotaxis whose counts advance through consecutive Fibonacci pairs.
