:layout: book
:type: item
:order: 2
:canonical_id: KNOTT-4.2

.. _knott-4-2:

============================================================================================
KNOTT-4.2 — Extremal Continued Fraction [1; 1, 1, …], Convergents Fₙ₊₁/Fₙ, & Nested Radicals
============================================================================================

.. enunciation::

   The all-ones simple continued fraction Φ = [1; 1, 1, …] has rational convergents cₖ = Fₖ₊₁/Fₖ with exact alternating error cₖ − Φ = (−φ)ᵏ/Fₖ, saturating Hurwitz's irrationality constant √5 via :math:`F_k^2 |c_k - \Phi| \to 1/\sqrt{5}`.

.. picture:: knott-4-2.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-4.2``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Phi's Fascinating Figures* (`#contfract <https://r-knott.surrey.ac.uk/Fibonacci/propsOfPhi.html#contfract>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/propsOfPhi.html#contfract>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.phigits.construct_convergents_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/divine <https://geometor.github.io/divine/>`_, `geometor/wildberger <https://geometor.github.io/wildberger/>`_

Constructive Synthesis & Exact Proof
------------------------------------

Rewriting :math:`\Phi = 1 + \frac{1}{\Phi}` generates the all-ones simple
:term:`continued fraction <continued-fraction>` :math:`\Phi = [1; 1, 1, 1, \dots]` and
nested radical :math:`\Phi = \sqrt{1 + \sqrt{1 + \sqrt{1 + \cdots}}}` cataloged on
``propsOfPhi.html`` (:cite:`KnottPropsPhi`).

* **Alternating Fibonacci Convergent Lattice**: In the :math:`(F_k, F_{k+1})` plane from
  origin :g:`O <knott-4-2.g1:O>`, the exact golden-slope ray :g:`OP <knott-4-2.g1:/ O P />`
  (:math:`y = \Phi x`) is straddled alternately above and below by convergent vectors
  :g:`OC1 <knott-4-2.g1:/ O C1 />` (:math:`(1, 1)`), :g:`OC2 <knott-4-2.g1:/ O C2 />`
  (:math:`(1, 2)`), :g:`OC3 <knott-4-2.g1:/ O C3 />` (:math:`(2, 3)`),
  :g:`OC4 <knott-4-2.g1:/ O C4 />` (:math:`(3, 5)`), and :g:`OC5 <knott-4-2.g1:/ O C5 />`
  (:math:`(5, 8)`).
* **Cassini Sector Triangles & Hurwitz's √5 Barrier**: By :term:`Cassini's identity <cassini-identity>`
  :math:`F_{k+1} F_{k-1} - F_k^2 = (-1)^k`, consecutive convergent sector triangles
  :g:`OC1C2 <knott-4-2.g1:< O C1 C2 >>`, :g:`OC2C3 <knott-4-2.g1:< O C2 C3 >>`,
  :g:`OC3C4 <knott-4-2.g1:< O C3 C4 >>`, and :g:`OC4C5 <knott-4-2.g1:< O C4 C5 >>` are
  :eq:`equal <knott-4-2.g1:< O C1 C2 > = knott-4-2.g1:< O C2 C3 > = knott-4-2.g1:< O C3 C4 > = knott-4-2.g1:< O C4 C5 >>`
  in unsigned area (:math:`1/2`, zero interior lattice points), yielding exact error
  :math:`\frac{F_{k+1}}{F_k} - \Phi = \frac{(-\phi)^k}{F_k}` and saturating
  :person:`Adolf Hurwitz <hurwitz>`'s (:cite:`Hurwitz1891`) irrationality constant
  :math:`F_k^2 \left|\frac{F_{k+1}}{F_k} - \Phi\right| \to \frac{1}{\sqrt{5}}`.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``c5 value``
     - :math:`\frac{8}{5}`
   * - ``c6 value``
     - :math:`\frac{13}{8}`
   * - ``c7 value``
     - :math:`\frac{21}{13}`
   * - ``c8 value``
     - :math:`\frac{34}{21}`
   * - ``hurwitz constant``
     - :math:`\frac{\sqrt{5}}{5}`
   * - ``cassini triangle area``
     - :math:`\frac{1}{2}`
