:type: item
:order: 1
:canonical_id: KNOTT-4.1

.. _knott-4-1:

==================================================================================
KNOTT-4.1 — Fibonacci Power Linearization (Φⁿ = FₙΦ + Fₙ₋₁) & The Phibonacci Brick
==================================================================================

.. enunciation::

   Every integer power n ∈ Z of the Golden Ratio reduces to the linear form Φⁿ = Fₙ Φ + Fₙ₋₁ and (−φ)ⁿ = Fₙ₊₁ − Fₙ Φ = Fₙ₋₁ − Fₙ φ, while a rectangular Phibonacci brick of edges (1, φ, Φ) has unit volume 1, surface area 4Φ, and integer space diagonal 2.

.. picture:: knott-4-1.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-4.1``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Phi's Fascinating Figures* (`#powers <https://r-knott.surrey.ac.uk/Fibonacci/propsOfPhi.html#powers>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/propsOfPhi.html#powers>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.phigits.construct_phi_powers_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/divine <https://geometor.github.io/divine/>`_, `geometor/fundamentals <https://geometor.github.io/fundamentals/>`_

Constructive Synthesis & Exact Proof
------------------------------------

Because :math:`\Phi^2 = \Phi + 1`, :person:`Dr. Ron Knott <knott>` (:cite:`KnottPropsPhi`)
emphasizes that :math:`\Phi` is the unique positive proportion whose **geometric** power
sequence :math:`1, \Phi, \Phi^2, \Phi^3, \dots` is simultaneously an **additive**
Fibonacci sequence (:math:`\Phi^{n+1} = \Phi^n + \Phi^{n-1}`):

* **Linearization of All Integer Powers**: Induction over :math:`n \in \mathbb{Z}` reduces
  every positive and negative power to :math:`\Phi^n = F_n \Phi + F_{n-1}` and
  :math:`(-\phi)^n = F_{n+1} - F_n \Phi`. Visually, the :math:`\Phi^2 \times \Phi^2` square
  :g:`AEFH <knott-4-1.g1:< A E F H >>` on :g:`A <knott-4-1.g1:A>`, :g:`E <knott-4-1.g1:E>`,
  :g:`F <knott-4-1.g1:F>`, :g:`H <knott-4-1.g1:H>` (with main diagonal
  :g:`AF <knott-4-1.g1:/ A F />`) decomposes via internal cuts :g:`BJ <knott-4-1.g1:/ B J />`
  and :g:`DG <knott-4-1.g1:/ D G />` through :g:`C <knott-4-1.g1:C>` into unit square
  :g:`ABCD <knott-4-1.g1:< A B C D >>` (:math:`1`), :math:`\Phi \times \Phi` square
  :g:`CGFJ <knott-4-1.g1:< C G F J >>` (:math:`\Phi^2`), and two :math:`1 \times \Phi`
  golden rectangles (:math:`\Phi^4 = 3\Phi + 2 = 1 + 2\Phi + \Phi^2`).
* **The Unit-Volume Phibonacci Brick**: Alongside the square, rectangle
  :g:`APQR <knott-4-1.g1:< A P Q R >>` (with edges :g:`PQ <knott-4-1.g1:/ P Q />` and
  :g:`RQ <knott-4-1.g1:/ R Q />`) displays the unfolded cross-section of Dr. Knott's
  3D **Phibonacci brick** of edges :math:`(1, \phi, \Phi)`, whose volume is exact unit
  :math:`1 \cdot \phi \cdot \Phi = 1`, total surface area is :math:`2(\phi + \Phi + 1) = 4\Phi`,
  and 3D space diagonal has integer length :math:`\sqrt{1 + \phi^2 + \Phi^2} = \sqrt{4} = 2`.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``PHI squared``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
   * - ``PHI to 5``
     - :math:`\frac{11}{2} + \frac{5 \sqrt{5}}{2}`
   * - ``phi to 4``
     - :math:`\frac{7}{2} - \frac{3 \sqrt{5}}{2}`
   * - ``brick volume``
     - :math:`1`
   * - ``brick surface area``
     - :math:`2 + 2 \sqrt{5}`
   * - ``brick space diagonal``
     - :math:`2`
