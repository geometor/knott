:type: item
:order: 2
:canonical_id: KNOTT-6.2

.. _knott-6-2:

=============================================================================================
KNOTT-6.2 — Cassini's Identity (Fₙ₋₁Fₙ₊₁ − Fₙ² = (−1)ⁿ) & The 64 ↔ 65 / 63 Jigsaw Dissections
=============================================================================================

.. enunciation::

   Cassini's alternating identity Fₙ₋₁ Fₙ₊₁ − Fₙ² = (−1)ⁿ manifests geometrically when the four pieces of an 8 × 8 = 64 square (two 3 × 8 triangles and two 5 × (3, 5) trapezoids) rearrange into a 5 × 13 = 65 rectangle with a +1 parallelogram gap OR into a 63-unit notched block with a −1 parallelogram overlap.

.. picture:: knott-6-2.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-6.2``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Harder Fibonacci Puzzles* (`#jigsaw1 <https://r-knott.surrey.ac.uk/Fibonacci/fibpuzzles2.html#jigsaw1>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/fibpuzzles2.html#jigsaw1>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.identities.construct_fibonacci_jigsaw_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/divine <https://geometor.github.io/divine/>`_

Constructive Synthesis & Exact Proof
------------------------------------

:person:`Giovanni Domenico Cassini <cassini>`'s 1680 determinant identity
:math:`F_{n-1} F_{n+1} - F_n^2 = (-1)^n` turns into a dramatic visual paradox at
:math:`n = 6` (:math:`5 \times 13 - 8^2 = +1`), examined by :person:`Dr. Ron Knott <knott>`
on ``fibpuzzles2.html`` (:cite:`KnottPuzzles2`) alongside :person:`Sam Loyd <loyd>` Jr. and
:person:`Henry Ernest Dudeney <dudeney>`'s complementary **64 = 63** rearrangement
(:cite:`Gardner1956`, :cite:`Horadam1962`).

* **Left Assembly — 5 × 13 = 65 (+1 Gap)**: Rearranging the four pieces of an
  :math:`8 \times 8 = 64` chessboard—triangles :g:`OB8P1 <knott-6-2.g1:< O B8 P1 >>` and
  :g:`P2QT5 <knott-6-2.g1:< P2 Q T5 >>` (each area :math:`12`) plus trapezoids
  :g:`B8R0QP1 <knott-6-2.g1:< B8 R0 Q P1 >>` and :g:`OP2T5T0 <knott-6-2.g1:< O P2 T5 T0 >>`
  (each area :math:`20`)—along diagonal :g:`O <knott-6-2.g1:O>` :math:`\to`
  :g:`Q <knott-6-2.g1:Q>` separates slopes :math:`3/8 = 0.375` (:g:`OP1 <knott-6-2.g1:/ O P1 />`)
  and :math:`2/5 = 0.400` (:g:`OP2 <knott-6-2.g1:/ O P2 />`), opening thin **+1 gap
  parallelogram** :g:`OP1QP2 <knott-6-2.g1:< O P1 Q P2 >>` of exact signed area :math:`+1`.
* **Right Assembly — 63-Unit Notched Block (−1 Overlap)**: Sliding the same four pieces
  into two :math:`5 \times 6 = 30` wings joined by a :math:`3 \times 1 = 3` bridge (outer
  polygon area :math:`63`, pieces :g:`S0S1U1U0 <knott-6-2.g1:< S0 S1 U1 U0 >>`,
  :g:`U0U3S2 <knott-6-2.g1:< U0 U3 S2 >>`, :g:`U3U2S4S3 <knott-6-2.g1:< U3 U2 S4 S3 >>`,
  and :g:`U1S5U2 <knott-6-2.g1:< U1 S5 U2 >>`) crosses edges :g:`U0U1 <knott-6-2.g1:/ U0 U1 />`
  and :g:`U0U3 <knott-6-2.g1:/ U0 U3 />` over **−1 overlap parallelogram**
  :g:`U0U3U2U1 <knott-6-2.g1:< U0 U3 U2 U1 >>`, whose unsigned area is
  :eq:`equal <knott-6-2.g1:< O P1 Q P2 > = knott-6-2.g1:< U0 U3 U2 U1 >>` to :math:`1`
  (:math:`64 - 1 = 63`).

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``square area``
     - :math:`64`
   * - ``rectangle 65 area``
     - :math:`65`
   * - ``gap parallelogram area``
     - :math:`1`
   * - ``notched 63 area``
     - :math:`63`
   * - ``overlap parallelogram area``
     - :math:`1`
   * - ``cassini n6``
     - :math:`1`
   * - ``cassini n7``
     - :math:`-1`
