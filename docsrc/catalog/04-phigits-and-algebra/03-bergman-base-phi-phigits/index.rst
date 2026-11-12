:layout: book
:type: item
:order: 3
:canonical_id: KNOTT-4.3

.. _knott-4-3:

======================================================
KNOTT-4.3 — Bergman's Base-Φ ('Phigit') Numeral System
======================================================

.. enunciation::

   Under the carry law Φⁿ = Φⁿ⁻¹ + Φⁿ⁻² (100_Φ = 011_Φ), every positive integer N ≥ 1 admits a unique finite minimal non-adjacent {0, 1} expansion in powers of Φ; excluding infinite 011-tails yields a unique 00-free maximal form and exactly Fₖ valid finite phigit forms for every Fibonacci number Fₖ.

.. picture:: knott-4-3.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-4.3``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Phigits and the Base Phi System* (`#canonical <https://r-knott.surrey.ac.uk/Fibonacci/phigits.html#canonical>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phigits.html#canonical>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.phigits.construct_phigit_scale_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/divine <https://geometor.github.io/divine/>`_

Constructive Synthesis & Exact Proof
------------------------------------

Discovered in 1957 by fourteen-year-old :person:`George Bergman <bergman>` (:cite:`Bergman1957`)
and extensively developed by :person:`Dr. Ron Knott <knott>` on ``phigits.html``
(:cite:`KnottPhigits`), the **base-Φ ("phigit") numeral system** represents **every
positive integer** uniquely as a finite non-adjacent binary sum of powers of the irrational
radix :math:`\Phi`.

* **Carry Law & Minimal Phigit Scale**: Along base-:math:`\Phi` axis :g:`OP3 <knott-4-3.g1:/ O P3 />`
  carrying ticks :g:`Pm2 <knott-4-3.g1:Pm2>` (:math:`\Phi^{-2}`), :g:`Pm1 <knott-4-3.g1:Pm1>`
  (:math:`\Phi^{-1}`), :g:`P0 <knott-4-3.g1:P0>` (:math:`\Phi^0 = 1`),
  :g:`P1 <knott-4-3.g1:P1>` (:math:`\Phi^1`), :g:`P2 <knott-4-3.g1:P2>` (:math:`\Phi^2`),
  and :g:`P3 <knott-4-3.g1:P3>` (:math:`\Phi^3`), the identity :math:`\Phi + \Phi^{-2} = 2`
  decomposes :math:`2 = 10.01_\Phi` into segments :g:`A2M2 <knott-4-3.g1:/ A2 M2 />` and
  :g:`M2B2 <knott-4-3.g1:/ M2 B2 />` (aligned to :g:`P1 <knott-4-3.g1:P1>` via
  :g:`P1M2 <knott-4-3.g1:/ P1 M2 />`), :math:`3 = 100.01_\Phi` into
  :g:`A3M3 <knott-4-3.g1:/ A3 M3 />` and :g:`M3B3 <knott-4-3.g1:/ M3 B3 />`, and
  :math:`4 = 101.01_\Phi` into :g:`A4M4 <knott-4-3.g1:/ A4 M4 />` (framing
  :g:`OP2M4A4 <knott-4-3.g1:< O P2 M4 A4 >>` via :g:`P2M4 <knott-4-3.g1:/ P2 M4 />`),
  :g:`M4N4 <knott-4-3.g1:/ M4 N4 />`, and :g:`N4B4 <knott-4-3.g1:/ N4 B4 />`.
* **Maximal Phigit Form & Fibonacci Multiplicity**: Applying :math:`100_\Phi \to 011_\Phi`
  (while forbidding non-terminating :math:`\dots 011` tails via :math:`101_\Phi \to 01111_\Phi`)
  produces a unique ``00``-free **maximal** :term:`phigit` expansion, and every Fibonacci
  integer :math:`F_k` admits **exactly** :math:`F_k` valid finite phigit representations
  while :person:`Édouard Lucas <lucas>` numbers :math:`L_{2m}` achieve local minima.

Canonical Minimal, Maximal, & Multiplicity Phigit Table
-------------------------------------------------------

.. list-table:: Base-:math:`\Phi` ('Phigit') Expansions for :math:`N = 1\dots 12`
   :header-rows: 1
   :widths: 12 28 32 28

   * - :math:`N`
     - Minimal Form (``11``-free)
     - Maximal Form (``00``-free interior)
     - Valid Finite Phigit Forms
   * - ``1``
     - ``1``
     - ``1``
     - ``1``
   * - ``2``
     - ``10.01``
     - ``1.11``
     - ``2``
   * - ``3``
     - ``100.01``
     - ``10.1111``
     - ``3``
   * - ``4``
     - ``101.01``
     - ``11.1111``
     - ``3``
   * - ``5``
     - ``1000.1001``
     - ``101.1111``
     - ``5``
   * - ``6``
     - ``1010.0001``
     - ``111.0111``
     - ``5``
   * - ``7``
     - ``10000.0001``
     - ``1010.101111``
     - ``5``
   * - ``8``
     - ``10001.0001``
     - ``1011.101111``
     - ``8``
   * - ``9``
     - ``10010.0101``
     - ``1101.101111``
     - ``8``
   * - ``10``
     - ``10100.0101``
     - ``1110.111111``
     - ``8``
   * - ``11``
     - ``10101.0101``
     - ``1111.111111``
     - ``5``
   * - ``12``
     - ``100000.101001``
     - ``10101.111111``
     - ``10``

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``phigits 2 decoded``
     - :math:`2`
   * - ``phigits 5 form count``
     - :math:`5`
   * - ``phigits 8 form count``
     - :math:`8`
   * - ``phigits 13 form count``
     - :math:`13`
   * - ``phigits 21 form count``
     - :math:`21`
   * - ``lucas 7 form count``
     - :math:`5`
   * - ``lucas 11 form count``
     - :math:`5`
