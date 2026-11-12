:layout: book
:type: item
:order: 1
:canonical_id: KNOTT-2.1

.. _knott-2-1:

==================================================================================
KNOTT-2.1 — Exact Radical Sines, Cosines, Tangents & Spreads of 18°, 36°, 54°, 72°
==================================================================================

.. enunciation::

   On the unit circle, cos 36° = sin 54° = Φ/2 and sin 18° = cos 72° = φ/2 differ by exactly 1/2 and multiply to 1/4, while the pentagonal spreads s(36°) = (5 − √5)/8 and s(72°) = (5 + √5)/8 form the quadratic roots of Wildberger's five-fold spread factor 16 s² − 20 s + 5 = 0.

.. picture:: knott-2-1.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-2.1``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Exact Trig Values for Simple Angles* (`#3654 <https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html#3654>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html#3654>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.trigonometry.construct_pentagonal_trig_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/wildberger <https://geometor.github.io/wildberger/>`_, `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/divine <https://geometor.github.io/divine/>`_

Constructive Synthesis & Exact Proof
------------------------------------

On ``simpleTrig.html`` (:cite:`KnottSimpleTrig`), :person:`Dr. Ron Knott <knott>` derives
the closed-form quadratic radicals for every multiple of :math:`18^\circ` directly from
the golden isosceles triangle—linking :person:`Claudius Ptolemy <ptolemy>`'s chord table
to :person:`Norman J. Wildberger <wildberger>`'s Rational Trigonometry spreads
(:cite:`Wildberger2005`).

* **Unit-Circle Pentagonal Rays**: On unit circle :g:`(O, U) <knott-2-1.g1:( O U )>` bounded
  by orthogonal axes :g:`OU <knott-2-1.g1:/ O U />` and :g:`OV <knott-2-1.g1:/ O V />`,
  the four acute pentagonal rays :g:`OP18 <knott-2-1.g1:/ O P18 />`,
  :g:`OP36 <knott-2-1.g1:/ O P36 />`, :g:`OP54 <knott-2-1.g1:/ O P54 />`, and
  :g:`OP72 <knott-2-1.g1:/ O P72 />` are :eq:`equal <knott-2-1.g1:/ O U / = knott-2-1.g1:/ O P36 / = knott-2-1.g1:/ O P72 />`
  unit radii. Dropping altitudes :g:`P36C36 <knott-2-1.g1:/ P36 C36 />` (forming right
  triangle :g:`OC36P36 <knott-2-1.g1:< O C36 P36 >>`) and :g:`P72C72 <knott-2-1.g1:/ P72 C72 />`
  onto :g:`OU <knott-2-1.g1:/ O U />` projects :g:`C36 <knott-2-1.g1:C36>` at
  :math:`x = \cos 36^\circ = \Phi/2` and :g:`C72 <knott-2-1.g1:C72>` at
  :math:`x = \cos 72^\circ = \sin 18^\circ = \phi/2`.
* **Rational Difference, Product & Five-Fold Spread Factor**: Because :math:`\Phi - \phi = 1`
  and :math:`\Phi\phi = 1`, segment :g:`C72C36 <knott-2-1.g1:/ C72 C36 />` has exact
  rational length :math:`\cos 36^\circ - \cos 72^\circ = 1/2` while
  :math:`\cos 36^\circ \cdot \cos 72^\circ = 1/4`. Squaring the ordinates eliminates the
  nested square roots :math:`\sqrt{10 \pm 2\sqrt{5}}` completely, leaving pure
  :math:`\mathbb{Q}(\sqrt{5})` :term:`spreads <spread>` :math:`s(18^\circ) = (3 - \sqrt{5})/8`,
  :math:`s(36^\circ) = (5 - \sqrt{5})/8`, :math:`s(54^\circ) = (5 + \sqrt{5})/8`, and
  :math:`s(72^\circ) = (5 + \sqrt{5})/8`, where :math:`s(36^\circ)` and :math:`s(72^\circ)`
  are the exact roots of :math:`16 s^2 - 20 s + 5 = 0`.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``cos 36``
     - :math:`\frac{1}{4} + \frac{\sqrt{5}}{4}`
   * - ``sin 18``
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
   * - ``spread 18``
     - :math:`\frac{3}{8} - \frac{\sqrt{5}}{8}`
   * - ``spread 36``
     - :math:`\frac{5}{8} - \frac{\sqrt{5}}{8}`
   * - ``spread 54``
     - :math:`\frac{\sqrt{5}}{8} + \frac{3}{8}`
   * - ``spread 72``
     - :math:`\frac{\sqrt{5}}{8} + \frac{5}{8}`
   * - ``projection span C72 C36``
     - :math:`\frac{1}{2}`
