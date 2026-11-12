:layout: book
:type: item
:order: 2
:canonical_id: KNOTT-5.2

.. _knott-5-2:

==========================================================================
KNOTT-5.2 — Zeckendorf's Theorem (Canonical Fibonacci Base Representation)
==========================================================================

.. enunciation::

   Every positive integer N ≥ 1 decomposes uniquely as a sum of non-consecutive Fibonacci numbers F_{k₁} + F_{k₂} + … + F_{kᵣ} (kᵢ ≥ kᵢ₊₁ + 2, kᵣ ≥ 2), producing a unique 11-free binary numeral in Fibonacci place values (…, 13, 8, 5, 3, 2, 1).

.. picture:: knott-5-2.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-5.2``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Fibonacci Representations of Numbers* (`#zeck <https://r-knott.surrey.ac.uk/Fibonacci/fibrep.html#zeck>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/fibrep.html#zeck>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.golden_string.construct_zeckendorf_staircase_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/divine <https://geometor.github.io/divine/>`_, `geometor/trees <https://geometor.github.io/trees/>`_

Constructive Synthesis & Exact Proof
------------------------------------

On ``fibrep.html`` (:cite:`KnottFibRep`), :person:`Dr. Ron Knott <knott>` pairs
:term:`phigit` expansions with :person:`Édouard Zeckendorf <zeckendorf>`'s theorem
(:cite:`Zeckendorf1972`): every positive integer :math:`N \ge 1` decomposes uniquely as a
sum of non-consecutive :person:`Fibonacci <fibonacci>` numbers :math:`F_{k_1} + \cdots + F_{k_r}`
(:math:`k_i \ge k_{i+1} + 2,\; k_r \ge 2`).

* **Greedy Non-Consecutive Fibonacci Staircase**: Plotting Fibonacci place-value bars
  :g:`A2B2C2D2 <knott-5-2.g1:< A2 B2 C2 D2 >>` (:math:`F_2 = 1`),
  :g:`A3B3C3D3 <knott-5-2.g1:< A3 B3 C3 D3 >>` (:math:`F_3 = 2`),
  :g:`A4B4C4D4 <knott-5-2.g1:< A4 B4 C4 D4 >>` (:math:`F_4 = 3`),
  :g:`A5B5C5D5 <knott-5-2.g1:< A5 B5 C5 D5 >>` (:math:`F_5 = 5`), and
  :g:`A6B6C6D6 <knott-5-2.g1:< A6 B6 C6 D6 >>` (:math:`F_6 = 8`), any two adjacent bars
  :math:`F_{k-1} + F_k` immediately coalesce into the next single bar :math:`F_{k+1}`,
  eliminating every ``11`` pair in Fibonacci base.
* **Canonical Decomposition of N = 12**: Below the staircase, integer :math:`12` decomposes
  uniquely along :g:`S0 <knott-5-2.g1:S0>` :math:`\to` :g:`S8 <knott-5-2.g1:S8>` :math:`\to`
  :g:`S11 <knott-5-2.g1:S11>` :math:`\to` :g:`S12 <knott-5-2.g1:S12>` into non-adjacent
  summands :g:`S0S8 <knott-5-2.g1:/ S0 S8 />` (:math:`F_6 = 8`, matching
  :g:`A6D6 <knott-5-2.g1:/ A6 D6 />`), :g:`S8S11 <knott-5-2.g1:/ S8 S11 />` (:math:`F_4 = 3`,
  matching :g:`A4D4 <knott-5-2.g1:/ A4 D4 />`), and :g:`S11S12 <knott-5-2.g1:/ S11 S12 />`
  (:math:`F_2 = 1`, matching :g:`A2D2 <knott-5-2.g1:/ A2 D2 />`), encoding
  :math:`12 = (10101)_F` in :term:`Zeckendorf representation <zeckendorf-representation>`.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``zeckendorf 12 sum``
     - :math:`12`
   * - ``zeckendorf 100 term count``
     - :math:`3`
   * - ``F2``
     - :math:`1`
   * - ``F4``
     - :math:`3`
   * - ``F6``
     - :math:`8`
