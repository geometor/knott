:layout: book
:type: item
:order: 4
:canonical_id: KNOTT-6.4

.. _knott-6-4:

===========================================================
KNOTT-6.4 — Fibonacci Arctangent Telescoping Formulae for π
===========================================================

.. enunciation::

   By Cassini's odd-index relation F₂ₙ₊₁² − 1 = F₂ₙ F₂ₙ₊₂, every even-indexed reciprocal Fibonacci angle splits as arctan(1/F₂ₙ) = arctan(1/F₂ₙ₊₁) + arctan(1/F₂ₙ₊₂), telescoping from arctan(1/F₂) = π/4 into Lehmer's series π/4 = ∑_{k=1}^∞ arctan(1/F₂ₖ₊₁).

.. picture:: knott-6-4.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-6.4``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *The Fibonacci Numbers in a Formula for Pi* (`#piandfib <https://r-knott.surrey.ac.uk/Fibonacci/fibpi.html#piandfib>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/fibpi.html#piandfib>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.identities.construct_hayashi_arctan_grid_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/wildberger <https://geometor.github.io/wildberger/>`_, `geometor/fundamentals <https://geometor.github.io/fundamentals/>`_

Constructive Synthesis & Exact Proof
------------------------------------

How do :person:`Fibonacci <fibonacci>` numbers—governed by :math:`\sqrt{5}`—generate the
circle constant :math:`\pi`? On ``fibpi.html`` (:cite:`KnottFibPi`), :person:`Dr. Ron Knott <knott>`
derives :person:`D. H. Lehmer <lehmer>`'s (:cite:`Lehmer1936`) reciprocal Fibonacci
:person:`Euler <euler>`–Machin series directly from odd-index :term:`Cassini's identity <cassini-identity>`:

.. math::

   F_{2n+1}^2 - F_{2n} F_{2n+2} = 1 \implies
   \frac{\frac{1}{F_{2n+1}} + \frac{1}{F_{2n+2}}}{1 - \frac{1}{F_{2n+1} F_{2n+2}}}
   = \frac{F_{2n+2} + F_{2n+1}}{F_{2n} F_{2n+2}} = \frac{F_{2n+3}}{F_{2n} F_{2n+2}}? \quad
   \text{No: } F_{2n+1} F_{2n+2} - 1 = F_{2n+1} F_{2n+2} - (F_{2n+1}^2 - F_{2n} F_{2n+2}) = F_{2n}(F_{2n+1} + F_{2n+2}),

canceling :math:`(F_{2n+1} + F_{2n+2})` identically to leave :math:`1 / F_{2n}`!

* **Ko Hayashi's Exact Integer-Lattice Proof**: Over horizontal axis
  :g:`OX <knott-6-4.g1:/ O X />` to :g:`X <knott-6-4.g1:X>` :math:`(16, 0)`, plotting
  integer lattice points :g:`E <knott-6-4.g1:E>` :math:`(10, 10)` (slope :math:`1 = 1/F_2`),
  :g:`M <knott-6-4.g1:M>` :math:`(15, 5)` (slope :math:`1/3 = 1/F_4`), and
  :g:`N <knott-6-4.g1:N>` :math:`(16, 2)` (slope :math:`1/8 = 1/F_6`, vertical leg
  :g:`XN <knott-6-4.g1:/ X N />`): right triangle :g:`OME <knott-6-4.g1:< O M E >>` has
  exact perpendicularity :math:`s(OE, EM) = 1` between :g:`OE <knott-6-4.g1:/ O E />` and
  :g:`EM <knott-6-4.g1:/ E M />` with :math:`Q(E, M)/Q(O, E) = 50/200 = (1/2)^2`, while
  right triangle :g:`ONM <knott-6-4.g1:< O N M >>` has :math:`s(OM, MN) = 1` between
  :g:`OM <knott-6-4.g1:/ O M />` and :g:`MN <knott-6-4.g1:/ M N />` with
  :math:`Q(M, N)/Q(O, M) = 10/250 = (1/5)^2`, proving geometrically along ray
  :g:`ON <knott-6-4.g1:/ O N />` that :math:`\frac{\pi}{4} = \arctan\frac{1}{2} + \arctan\frac{1}{5} + \arctan\frac{1}{8}`.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``twist 1 over 2``
     - :math:`\frac{1}{4}`
   * - ``twist 1 over 3``
     - :math:`\frac{1}{9}`
   * - ``twist 1 over 5``
     - :math:`\frac{1}{25}`
   * - ``twist 1 over 8``
     - :math:`\frac{1}{64}`
   * - ``remainder after 8 steps``
     - :math:`\operatorname{atan}{\left(\frac{1}{2584} \right)}`
