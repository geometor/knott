:type: item
:order: 3
:canonical_id: KNOTT-6.3

.. _knott-6-3:

=====================================================================================
KNOTT-6.3 — Binet, Lucas, Catalan, d'Ocagne, Honsberger & Fibonomial Power Identities
=====================================================================================

.. enunciation::

   Binet's closed forms Fₙ = (Φⁿ − (−φ)ⁿ)/√5 and Lₙ = Φⁿ + (−φ)ⁿ place (Lₙ, Fₙ) on the alternating Pell-Lucas hyperbolas Lₙ² − 5 Fₙ² = 4(−1)ⁿ with unit sector triangles, unify Catalan, d'Ocagne, and Honsberger identities, and annihilate k-th powers Fₙᵏ via signed Fibonomial coefficients.

.. picture:: knott-6-3.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-6.3``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Fibonacci and Phi Formulae* (`#defs <https://r-knott.surrey.ac.uk/Fibonacci/fibFormulae.html#defs>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/fibFormulae.html#defs>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.identities.construct_lucas_binet_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/divine <https://geometor.github.io/divine/>`_, `geometor/wildberger <https://geometor.github.io/wildberger/>`_

Constructive Synthesis & Exact Proof
------------------------------------

On ``fibFormulae.html`` (:cite:`KnottFormulae`), :person:`Dr. Ron Knott <knott>` organizes
the algebraic web linking :person:`Jacques Binet <binet>`'s closed forms,
:person:`Édouard Lucas <lucas>`'s companion sequence :math:`L_n = \Phi^n + (-\phi)^n`,
:person:`Eugène Catalan <catalan>`'s, d'Ocagne's, and Ross Honsberger's (:cite:`Honsberger1985`)
addition laws, and signed :term:`Fibonomial <fibonomial>` power recurrences (:cite:`Vajda1989`).

* **Pell–Lucas Alternating Hyperbola & Asymptote**: Plotting :math:`P_n = (L_n, F_n)` from
  origin :g:`O <knott-6-3.g1:O>` at :g:`P0 <knott-6-3.g1:P0>` :math:`(2, 0)`,
  :g:`P1 <knott-6-3.g1:P1>` :math:`(1, 1)`, :g:`P2 <knott-6-3.g1:P2>` :math:`(3, 1)`,
  :g:`P3 <knott-6-3.g1:P3>` :math:`(4, 2)`, and :g:`P4 <knott-6-3.g1:P4>` :math:`(7, 3)`
  places every even/odd point on the conjugate hyperbolas :math:`L_n^2 - 5 F_n^2 = 4(-1)^n`
  approaching golden asymptote :g:`OA <knott-6-3.g1:/ O A />` of slope :math:`1/\sqrt{5}`.
* **Unit-Area Sector Invariant & Fibonomials**: Because :math:`L_n F_{n+1} - F_n L_{n+1} = 2(-1)^n`,
  consecutive sector triangles :g:`OP0P1 <knott-6-3.g1:< O P0 P1 >>`,
  :g:`OP1P2 <knott-6-3.g1:< O P1 P2 >>`, :g:`OP2P3 <knott-6-3.g1:< O P2 P3 >>`, and
  :g:`OP3P4 <knott-6-3.g1:< O P3 P4 >>` bounded by chords :g:`P0P1 <knott-6-3.g1:/ P0 P1 />` –
  :g:`P3P4 <knott-6-3.g1:/ P3 P4 />` are
  :eq:`equal <knott-6-3.g1:< O P0 P1 > = knott-6-3.g1:< O P1 P2 > = knott-6-3.g1:< O P2 P3 > = knott-6-3.g1:< O P3 P4 >>`
  in unsigned area (exact area :math:`1`), while Fibonomial coefficients
  :math:`\binom{k+1}{j}_F` annihilate :math:`k`-th powers :math:`F_n^k` identically.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``fibonomial 5 2``
     - :math:`15`
   * - ``fibonomial 6 3``
     - :math:`60`
   * - ``F10``
     - :math:`55`
   * - ``L10``
     - :math:`123`
   * - ``F20 via F10 L10``
     - :math:`6765`
   * - ``pell lucas sector area``
     - :math:`1`
   * - ``asymptote slope``
     - :math:`\frac{\sqrt{5}}{5}`
