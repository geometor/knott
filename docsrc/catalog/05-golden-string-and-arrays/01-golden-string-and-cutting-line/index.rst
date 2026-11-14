:type: item
:order: 1
:canonical_id: KNOTT-5.1

.. _knott-5-1:

==========================================================================================
KNOTT-5.1 — The Infinite Golden String (101101011011…), Rabbit Tree & Cutting-Line Slope φ
==========================================================================================

.. enunciation::

   Iterating the Rabbit substitution 1 ↦ 10, 0 ↦ 1 generates the infinite Sturmian Golden String dₙ = ⌊(n + 1)φ⌋ − ⌊nφ⌋, identically realized geometrically as the sequence of vertical ('1') and horizontal ('0') unit-lattice crossings of the ray y = φ x from the origin.

.. picture:: knott-5-1.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-5.1``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *The Fibonacci Rabbit Sequence (The Golden String)* (`#PhiPlot <https://r-knott.surrey.ac.uk/Fibonacci/fibrab.html#PhiPlot>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/fibrab.html#PhiPlot>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.golden_string.construct_golden_string_cutting_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/trees <https://geometor.github.io/trees/>`_, `geometor/divine <https://geometor.github.io/divine/>`_

Constructive Synthesis & Exact Proof
------------------------------------

:person:`Dr. Ron Knott <knott>`'s signature page ``fibrab.html`` (:cite:`KnottGoldenString`)
unifies three seemingly distinct mathematical worlds—:person:`Fibonacci <fibonacci>`'s
monthly rabbit substitution (:math:`1 \mapsto 10,\; 0 \mapsto 1`), Sturmian Beatty
differences :math:`d_n = \lfloor (n+1)\phi \rfloor - \lfloor n\phi \rfloor`, and straight
lattice-cutting rays—into the single infinite **Golden String** ``1011010110110101101…``.

* **Cutting-Line Realization of the Golden String**: Tracing line
  :g:`[OR] <knott-5-1.g1:[ O R ]>` (segment :g:`OR <knott-5-1.g1:/ O R />` from origin
  :g:`O <knott-5-1.g1:O>` to :g:`R <knott-5-1.g1:R>` :math:`(5, 5\phi)`) of exact slope
  :math:`\phi` across vertical unit grid segments :g:`X1XT1 <knott-5-1.g1:/ X1 XT1 />`,
  :g:`X2XT2 <knott-5-1.g1:/ X2 XT2 />`, :g:`X3XT3 <knott-5-1.g1:/ X3 XT3 />` and horizontal
  grid segments :g:`Y1YR1 <knott-5-1.g1:/ Y1 YR1 />`, :g:`Y2YR2 <knott-5-1.g1:/ Y2 YR2 />`,
  :g:`Y3YR3 <knott-5-1.g1:/ Y3 YR3 />`: recording ``1`` at each vertical crossing
  (:g:`V1 <knott-5-1.g1:V1>` – :g:`V5 <knott-5-1.g1:V5>` at :math:`(k, k\phi)`) and ``0``
  at each horizontal crossing (:g:`H1 <knott-5-1.g1:H1>`, :g:`H2 <knott-5-1.g1:H2>`,
  :g:`H3 <knott-5-1.g1:H3>` at :math:`(m\Phi, m)`) spells out ``1, 0, 1, 1, 0, 1, 0, 1``
  in exact abscissa order :math:`1 < \Phi < 2 < 3 < 2\Phi < 4 < 3\Phi < 5`.
* **Palindrome Structure & Recursive Call Tree**: Removing the final two characters of
  every morphism word :math:`S_n` (length :math:`F_n` with :math:`F_{n-1}` ones and
  :math:`F_{n-2}` zeros) leaves a strict palindrome, while naive recursive evaluation of
  ``fib(n)`` performs :math:`F_{n+1} - 1` additions.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``ray slope``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``H1 x``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``H2 x``
     - :math:`1 + \sqrt{5}`
   * - ``H3 x``
     - :math:`\frac{3}{2} + \frac{3 \sqrt{5}}{2}`
   * - ``prefix length S8``
     - :math:`34`
   * - ``ones in S8``
     - :math:`21`
   * - ``zeros in S8``
     - :math:`13`
   * - ``recursive additions F10``
     - :math:`88`
