:type: item
:order: 3
:canonical_id: KNOTT-5.3

.. _knott-5-3:

================================================================================================
KNOTT-5.3 — Wythoff's Array, Beatty's Complementary Sequences (⌊nΦ⌋, ⌊nΦ²⌋), & Stolarsky's Array
================================================================================================

.. enunciation::

   Because 1/Φ + 1/Φ² = 1, Beatty's sequences Aₙ = ⌊nΦ⌋ and Bₙ = ⌊nΦ²⌋ = Aₙ + n partition Z_{>0} without overlap; seeding generalized Fibonacci rows via W(r, c) = ⌊(r + 1)Φ⌋ F_{c+2} + r F_{c+1} (Wythoff) or nearest-integer multiples [kΦ] (Stolarsky) places every positive integer in a unique (row, col) cell.

.. picture:: knott-5-3.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-5.3``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *General Fibonacci Series, Wythoff and Stolarsky Arrays* (`#wythoff <https://r-knott.surrey.ac.uk/Fibonacci/fibGen.html#wythoff>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/fibGen.html#wythoff>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.golden_string.construct_wythoff_beatty_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/etc <https://geometor.github.io/etc/>`_, `geometor/divine <https://geometor.github.io/divine/>`_

Constructive Synthesis & Exact Proof
------------------------------------

Because :math:`\frac{1}{\Phi} + \frac{1}{\Phi^2} = \phi + \phi^2 = 1`, Samuel Beatty's
theorem guarantees that lower and upper :term:`Beatty sequences <beatty-sequence>`
:math:`A_n = \lfloor n\Phi \rfloor` and :math:`B_n = \lfloor n\Phi^2 \rfloor = A_n + n`
partition :math:`\mathbb{Z}_{>0}` into disjoint cold positions of :person:`Willem Wythoff <wythoff>`'s
game (:cite:`Wythoff1907`, :cite:`KnottFibGen`).

* **Exact Wythoff & Beatty Cone**: From origin :g:`O <knott-5-3.g1:O>`, exact rays
  :g:`OR1 <knott-5-3.g1:/ O R1 />` (:math:`y = \Phi x`) and :g:`OR2 <knott-5-3.g1:/ O R2 />`
  (:math:`y = \Phi^2 x`) bound the cold Wythoff pairs :g:`W1 <knott-5-3.g1:W1>` :math:`(1, 2)`,
  :g:`W2 <knott-5-3.g1:W2>` :math:`(3, 5)`, :g:`W3 <knott-5-3.g1:W3>` :math:`(4, 7)`, and
  :g:`W4 <knott-5-3.g1:W4>` :math:`(6, 10)` (connected along :g:`W1W2 <knott-5-3.g1:/ W1 W2 />`,
  :g:`W2W3 <knott-5-3.g1:/ W2 W3 />`, and :g:`W3W4 <knott-5-3.g1:/ W3 W4 />` beneath ideal
  targets :g:`A1 <knott-5-3.g1:A1>` – :g:`A4 <knott-5-3.g1:A4>`).
* **Bijective Wythoff & Stolarsky Interspersions**: Seeding row :math:`r \ge 0` of the
  :term:`Wythoff array <wythoff-array>` with :math:`W(r, c) = \lfloor (r+1)\Phi \rfloor F_{c+2} + r F_{c+1}`
  groups integers whose :term:`Zeckendorf representations <zeckendorf-representation>` end
  in :math:`c` trailing zeros (:cite:`Morrison1980`), while :person:`Kenneth Stolarsky <stolarsky>`'s
  nearest-integer Golden Ratio rounding :math:`b = \lfloor a\Phi + 1/2 \rfloor`
  (:cite:`Stolarsky1977`) yields the dual :term:`Stolarsky array <stolarsky-array>` studied
  by :person:`John Conway <conway>` and :person:`Clark Kimberling <kimberling>`.

Leading 6 × 6 Wythoff & Stolarsky Interspersion Subarrays
---------------------------------------------------------

.. list-table:: Wythoff Array :math:`W(r, c)` (:math:`0 \le r, c \le 5`)
   :header-rows: 1

   * - Row
     - :math:`c=0`
     - :math:`c=1`
     - :math:`c=2`
     - :math:`c=3`
     - :math:`c=4`
     - :math:`c=5`
   * - :math:`r=0`
     - ``1``
     - ``2``
     - ``3``
     - ``5``
     - ``8``
     - ``13``
   * - :math:`r=1`
     - ``4``
     - ``7``
     - ``11``
     - ``18``
     - ``29``
     - ``47``
   * - :math:`r=2`
     - ``6``
     - ``10``
     - ``16``
     - ``26``
     - ``42``
     - ``68``
   * - :math:`r=3`
     - ``9``
     - ``15``
     - ``24``
     - ``39``
     - ``63``
     - ``102``
   * - :math:`r=4`
     - ``12``
     - ``20``
     - ``32``
     - ``52``
     - ``84``
     - ``136``
   * - :math:`r=5`
     - ``14``
     - ``23``
     - ``37``
     - ``60``
     - ``97``
     - ``157``

.. list-table:: Stolarsky Array :math:`S(r, c)` (:math:`0 \le r, c \le 5`)
   :header-rows: 1

   * - Row
     - :math:`c=0`
     - :math:`c=1`
     - :math:`c=2`
     - :math:`c=3`
     - :math:`c=4`
     - :math:`c=5`
   * - :math:`r=0`
     - ``1``
     - ``2``
     - ``3``
     - ``5``
     - ``8``
     - ``13``
   * - :math:`r=1`
     - ``4``
     - ``6``
     - ``10``
     - ``16``
     - ``26``
     - ``42``
   * - :math:`r=2`
     - ``7``
     - ``11``
     - ``18``
     - ``29``
     - ``47``
     - ``76``
   * - :math:`r=3`
     - ``9``
     - ``15``
     - ``24``
     - ``39``
     - ``63``
     - ``102``
   * - :math:`r=4`
     - ``12``
     - ``19``
     - ``31``
     - ``50``
     - ``81``
     - ``131``
   * - :math:`r=5`
     - ``14``
     - ``23``
     - ``37``
     - ``60``
     - ``97``
     - ``157``

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``beatty density sum``
     - :math:`\frac{1}{\frac{\sqrt{5}}{2} + \frac{3}{2}} + \frac{1}{\frac{1}{2} + \frac{\sqrt{5}}{2}}`
   * - ``wythoff W 0 0``
     - :math:`1`
   * - ``wythoff W 1 0``
     - :math:`4`
   * - ``wythoff W 2 3``
     - :math:`26`
   * - ``stolarsky S 1 0``
     - :math:`4`
   * - ``stolarsky S 2 0``
     - :math:`7`
   * - ``stolarsky S 3 3``
     - :math:`39`
