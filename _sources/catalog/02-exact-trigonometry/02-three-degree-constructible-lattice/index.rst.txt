:type: item
:order: 2
:canonical_id: KNOTT-2.2

.. _knott-2-2:

===========================================================================
KNOTT-2.2 — The Complete 3° Constructible Angle Lattice (3°k for k = 1..29)
===========================================================================

.. enunciation::

   Superimposing pentagonal angles in Q(√5) with equilateral and half-right angles in Q(√2, √3) expresses sin(3°k), cos(3°k), tan(3°k), and spread s(3°k) in explicit nested square roots for all 29 acute multiples of 3°, while Gauss's Fermat prime 17 = 2⁴ + 1 extends compass constructibility to cos(π/17).

.. picture:: knott-2-2.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-2.2``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Exact Trig Values for Simple Angles* (`#otherexact <https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html#otherexact>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/simpleTrig.html#otherexact>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.trigonometry.construct_three_degree_lattice_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/elements <https://geometor.github.io/elements/>`_, `geometor/wildberger <https://geometor.github.io/wildberger/>`_

Constructive Synthesis & Exact Proof
------------------------------------

Combining the pentagonal subfield :math:`\mathbb{Q}(\sqrt{5}, \sqrt{10 \pm 2\sqrt{5}})`
with the equilateral and half-right subfield :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})`
generates closed-form square-root radicals for **all 29 acute multiples of** :math:`3^\circ`
(:cite:`KnottSimpleTrig`).

* **Euclid IV.16 Regular 15-Gon & 3° Generator**: On unit circle :g:`(O, U) <knott-2-2.g1:( O U )>`,
  superimposing equilateral ray :g:`OP60 <knott-2-2.g1:/ O P60 />` (:math:`60^\circ`) and
  pentagonal ray :g:`OP72 <knott-2-2.g1:/ O P72 />` (:math:`72^\circ`) isolates the
  :math:`12^\circ` regular pentadecagon arc, making chord :g:`P60P72 <knott-2-2.g1:/ P60 P72 />`
  and origin-based chord :g:`UP12 <knott-2-2.g1:/ U P12 />`
  :eq:`equal <knott-2-2.g1:/ P60 P72 / = knott-2-2.g1:/ U P12 />`. Equivalently, subtracting
  Ailles' :math:`15^\circ` ray :g:`OP15 <knott-2-2.g1:/ O P15 />` from pentagonal ray
  :g:`OP18 <knott-2-2.g1:/ O P18 />` (or bisecting :g:`OP12 <knott-2-2.g1:/ O P12 />`
  through :g:`OP6 <knott-2-2.g1:/ O P6 />` to :g:`OP3 <knott-2-2.g1:/ O P3 />`) yields the
  atomic :term:`constructible angle <constructible-angle>` :math:`3^\circ = 18^\circ - 15^\circ`,
  whose chord :g:`P15P18 <knott-2-2.g1:/ P15 P18 />` and unit-base chord
  :g:`UP3 <knott-2-2.g1:/ U P3 />` are :eq:`equal <knott-2-2.g1:/ P15 P18 / = knott-2-2.g1:/ U P3 />`.
* **Gauss's Regular 17-Gon Bridge**: While :math:`1^\circ` cannot be constructed with
  compass and straightedge (requiring cube roots via angle trisection), :person:`Carl Friedrich Gauss <gauss>`
  (:cite:`Gauss1801`) proved that Fermat prime :math:`F_2 = 2^{2^2} + 1 = 17` admits a
  four-step quadratic radical tower for :math:`\cos(\pi / 17)`, verified here symbolically
  via Chebyshev's polynomial :math:`T_{17}(\cos(\pi / 17)) + 1 = 0`.

Complete 29-Angle 3° Constructible Lattice
------------------------------------------

.. list-table:: Exact Radicals & Spreads for :math:`3^\circ k` (:math:`k = 1\dots 29`)
   :header-rows: 1
   :widths: 10 30 30 30

   * - Angle
     - :math:`\sin\theta`
     - :math:`\cos\theta`
     - Spread :math:`s(\theta) = \sin^2\theta`
   * - :math:`3^\circ`
     - :math:`- \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16} - \frac{\sqrt{6}}{16} - \frac{\sqrt{2}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} + \frac{\sqrt{30}}{16}`
     - :math:`- \frac{\sqrt{10}}{16} - \frac{\sqrt{6}}{16} + \frac{\sqrt{2}}{16} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} + \frac{\sqrt{30}}{16} + \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16}`
     - :math:`- \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 10}}{32} - \frac{\sqrt{15}}{16} - \frac{\sqrt{3}}{16} + \frac{\sqrt{2 \sqrt{5} + 10}}{32} + \frac{1}{2}`
   * - :math:`6^\circ`
     - :math:`- \frac{\sqrt{5}}{8} - \frac{1}{8} + \frac{\sqrt{3} \sqrt{10 - 2 \sqrt{5}}}{8}`
     - :math:`\frac{\sqrt{3}}{8} + \frac{\sqrt{10 - 2 \sqrt{5}}}{8} + \frac{\sqrt{15}}{8}`
     - :math:`- \frac{\sqrt{15} \sqrt{10 - 2 \sqrt{5}}}{32} - \frac{\sqrt{5}}{16} - \frac{\sqrt{3} \sqrt{10 - 2 \sqrt{5}}}{32} + \frac{9}{16}`
   * - :math:`9^\circ`
     - :math:`- \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{8} + \frac{\sqrt{2}}{8} + \frac{\sqrt{10}}{8}`
     - :math:`\frac{\sqrt{2}}{8} + \frac{\sqrt{10}}{8} + \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{8}`
     - :math:`- \frac{\sqrt{5} \sqrt{10 - 2 \sqrt{5}}}{16} - \frac{\sqrt{10 - 2 \sqrt{5}}}{16} + \frac{1}{2}`
   * - :math:`12^\circ`
     - :math:`- \frac{\sqrt{15}}{8} + \frac{\sqrt{3}}{8} + \frac{\sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{1}{8} + \frac{\sqrt{5}}{8} + \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{\sqrt{15} \sqrt{2 \sqrt{5} + 10}}{32} - \frac{\sqrt{5}}{16} + \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{32} + \frac{7}{16}`
   * - :math:`15^\circ`
     - :math:`- \frac{\sqrt{2}}{4} + \frac{\sqrt{6}}{4}`
     - :math:`\frac{\sqrt{2}}{4} + \frac{\sqrt{6}}{4}`
     - :math:`\frac{1}{2} - \frac{\sqrt{3}}{4}`
   * - :math:`18^\circ`
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
     - :math:`\frac{\sqrt{2 \sqrt{5} + 10}}{4}`
     - :math:`\frac{3}{8} - \frac{\sqrt{5}}{8}`
   * - :math:`21^\circ`
     - :math:`- \frac{\sqrt{30}}{16} - \frac{\sqrt{6}}{16} + \frac{\sqrt{2}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{6} \sqrt{10 - 2 \sqrt{5}}}{16}`
     - :math:`- \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{2}}{16} + \frac{\sqrt{6}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{30}}{16} + \frac{\sqrt{6} \sqrt{10 - 2 \sqrt{5}}}{16}`
     - :math:`- \frac{\sqrt{15}}{16} - \frac{\sqrt{5} \sqrt{10 - 2 \sqrt{5}}}{32} - \frac{\sqrt{10 - 2 \sqrt{5}}}{32} + \frac{\sqrt{3}}{16} + \frac{1}{2}`
   * - :math:`24^\circ`
     - :math:`- \frac{\sqrt{10 - 2 \sqrt{5}}}{8} + \frac{\sqrt{3}}{8} + \frac{\sqrt{15}}{8}`
     - :math:`\frac{1}{8} + \frac{\sqrt{5}}{8} + \frac{\sqrt{3} \sqrt{10 - 2 \sqrt{5}}}{8}`
     - :math:`- \frac{\sqrt{15} \sqrt{10 - 2 \sqrt{5}}}{32} - \frac{\sqrt{3} \sqrt{10 - 2 \sqrt{5}}}{32} + \frac{\sqrt{5}}{16} + \frac{7}{16}`
   * - :math:`27^\circ`
     - :math:`- \frac{\sqrt{10}}{8} + \frac{\sqrt{2}}{8} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{\sqrt{2}}{8} + \frac{\sqrt{10}}{8} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 10}}{16} + \frac{\sqrt{2 \sqrt{5} + 10}}{16} + \frac{1}{2}`
   * - :math:`30^\circ`
     - :math:`\frac{1}{2}`
     - :math:`\frac{\sqrt{3}}{2}`
     - :math:`\frac{1}{4}`
   * - :math:`33^\circ`
     - :math:`- \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} - \frac{\sqrt{6}}{16} - \frac{\sqrt{2}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{30}}{16} + \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16}`
     - :math:`- \frac{\sqrt{30}}{16} - \frac{\sqrt{2}}{16} + \frac{\sqrt{6}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} + \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16}`
     - :math:`- \frac{\sqrt{15}}{16} - \frac{\sqrt{2 \sqrt{5} + 10}}{32} - \frac{\sqrt{3}}{16} + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 10}}{32} + \frac{1}{2}`
   * - :math:`36^\circ`
     - :math:`\frac{\sqrt{10 - 2 \sqrt{5}}}{4}`
     - :math:`\frac{1}{4} + \frac{\sqrt{5}}{4}`
     - :math:`\frac{5}{8} - \frac{\sqrt{5}}{8}`
   * - :math:`39^\circ`
     - :math:`- \frac{\sqrt{6} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{2}}{16} + \frac{\sqrt{6}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{30}}{16}`
     - :math:`- \frac{\sqrt{10}}{16} - \frac{\sqrt{2}}{16} + \frac{\sqrt{6}}{16} + \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{30}}{16} + \frac{\sqrt{6} \sqrt{10 - 2 \sqrt{5}}}{16}`
     - :math:`- \frac{\sqrt{5} \sqrt{10 - 2 \sqrt{5}}}{32} - \frac{\sqrt{3}}{16} - \frac{\sqrt{10 - 2 \sqrt{5}}}{32} + \frac{\sqrt{15}}{16} + \frac{1}{2}`
   * - :math:`42^\circ`
     - :math:`- \frac{\sqrt{5}}{8} + \frac{1}{8} + \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{\sqrt{3}}{8} + \frac{\sqrt{2 \sqrt{5} + 10}}{8} + \frac{\sqrt{15}}{8}`
     - :math:`- \frac{\sqrt{15} \sqrt{2 \sqrt{5} + 10}}{32} + \frac{\sqrt{5}}{16} + \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{32} + \frac{9}{16}`
   * - :math:`45^\circ`
     - :math:`\frac{\sqrt{2}}{2}`
     - :math:`\frac{\sqrt{2}}{2}`
     - :math:`\frac{1}{2}`
   * - :math:`48^\circ`
     - :math:`- \frac{\sqrt{3}}{8} + \frac{\sqrt{2 \sqrt{5} + 10}}{8} + \frac{\sqrt{15}}{8}`
     - :math:`- \frac{\sqrt{5}}{8} + \frac{1}{8} + \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{32} - \frac{\sqrt{5}}{16} + \frac{7}{16} + \frac{\sqrt{15} \sqrt{2 \sqrt{5} + 10}}{32}`
   * - :math:`51^\circ`
     - :math:`- \frac{\sqrt{10}}{16} - \frac{\sqrt{2}}{16} + \frac{\sqrt{6}}{16} + \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{30}}{16} + \frac{\sqrt{6} \sqrt{10 - 2 \sqrt{5}}}{16}`
     - :math:`- \frac{\sqrt{6} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{2}}{16} + \frac{\sqrt{6}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{30}}{16}`
     - :math:`- \frac{\sqrt{15}}{16} + \frac{\sqrt{10 - 2 \sqrt{5}}}{32} + \frac{\sqrt{3}}{16} + \frac{\sqrt{5} \sqrt{10 - 2 \sqrt{5}}}{32} + \frac{1}{2}`
   * - :math:`54^\circ`
     - :math:`\frac{1}{4} + \frac{\sqrt{5}}{4}`
     - :math:`\frac{\sqrt{10 - 2 \sqrt{5}}}{4}`
     - :math:`\frac{\sqrt{5}}{8} + \frac{3}{8}`
   * - :math:`57^\circ`
     - :math:`- \frac{\sqrt{30}}{16} - \frac{\sqrt{2}}{16} + \frac{\sqrt{6}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} + \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16}`
     - :math:`- \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} - \frac{\sqrt{6}}{16} - \frac{\sqrt{2}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{30}}{16} + \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16}`
     - :math:`- \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 10}}{32} + \frac{\sqrt{3}}{16} + \frac{\sqrt{2 \sqrt{5} + 10}}{32} + \frac{\sqrt{15}}{16} + \frac{1}{2}`
   * - :math:`60^\circ`
     - :math:`\frac{\sqrt{3}}{2}`
     - :math:`\frac{1}{2}`
     - :math:`\frac{3}{4}`
   * - :math:`63^\circ`
     - :math:`- \frac{\sqrt{2}}{8} + \frac{\sqrt{10}}{8} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{\sqrt{10}}{8} + \frac{\sqrt{2}}{8} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{\sqrt{2 \sqrt{5} + 10}}{16} + \frac{1}{2} + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 10}}{16}`
   * - :math:`66^\circ`
     - :math:`\frac{1}{8} + \frac{\sqrt{5}}{8} + \frac{\sqrt{3} \sqrt{10 - 2 \sqrt{5}}}{8}`
     - :math:`- \frac{\sqrt{10 - 2 \sqrt{5}}}{8} + \frac{\sqrt{3}}{8} + \frac{\sqrt{15}}{8}`
     - :math:`- \frac{\sqrt{5}}{16} + \frac{\sqrt{3} \sqrt{10 - 2 \sqrt{5}}}{32} + \frac{\sqrt{15} \sqrt{10 - 2 \sqrt{5}}}{32} + \frac{9}{16}`
   * - :math:`69^\circ`
     - :math:`- \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{2}}{16} + \frac{\sqrt{6}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{30}}{16} + \frac{\sqrt{6} \sqrt{10 - 2 \sqrt{5}}}{16}`
     - :math:`- \frac{\sqrt{30}}{16} - \frac{\sqrt{6}}{16} + \frac{\sqrt{2}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{6} \sqrt{10 - 2 \sqrt{5}}}{16}`
     - :math:`- \frac{\sqrt{3}}{16} + \frac{\sqrt{10 - 2 \sqrt{5}}}{32} + \frac{\sqrt{5} \sqrt{10 - 2 \sqrt{5}}}{32} + \frac{\sqrt{15}}{16} + \frac{1}{2}`
   * - :math:`72^\circ`
     - :math:`\frac{\sqrt{2 \sqrt{5} + 10}}{4}`
     - :math:`- \frac{1}{4} + \frac{\sqrt{5}}{4}`
     - :math:`\frac{\sqrt{5}}{8} + \frac{5}{8}`
   * - :math:`75^\circ`
     - :math:`\frac{\sqrt{2}}{4} + \frac{\sqrt{6}}{4}`
     - :math:`- \frac{\sqrt{2}}{4} + \frac{\sqrt{6}}{4}`
     - :math:`\frac{\sqrt{3}}{4} + \frac{1}{2}`
   * - :math:`78^\circ`
     - :math:`- \frac{1}{8} + \frac{\sqrt{5}}{8} + \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{\sqrt{15}}{8} + \frac{\sqrt{3}}{8} + \frac{\sqrt{2 \sqrt{5} + 10}}{8}`
     - :math:`- \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{32} + \frac{\sqrt{5}}{16} + \frac{\sqrt{15} \sqrt{2 \sqrt{5} + 10}}{32} + \frac{9}{16}`
   * - :math:`81^\circ`
     - :math:`\frac{\sqrt{2}}{8} + \frac{\sqrt{10}}{8} + \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{8}`
     - :math:`- \frac{\sqrt{2} \sqrt{10 - 2 \sqrt{5}}}{8} + \frac{\sqrt{2}}{8} + \frac{\sqrt{10}}{8}`
     - :math:`\frac{\sqrt{10 - 2 \sqrt{5}}}{16} + \frac{\sqrt{5} \sqrt{10 - 2 \sqrt{5}}}{16} + \frac{1}{2}`
   * - :math:`84^\circ`
     - :math:`\frac{\sqrt{3}}{8} + \frac{\sqrt{10 - 2 \sqrt{5}}}{8} + \frac{\sqrt{15}}{8}`
     - :math:`- \frac{\sqrt{5}}{8} - \frac{1}{8} + \frac{\sqrt{3} \sqrt{10 - 2 \sqrt{5}}}{8}`
     - :math:`\frac{\sqrt{3} \sqrt{10 - 2 \sqrt{5}}}{32} + \frac{\sqrt{5}}{16} + \frac{\sqrt{15} \sqrt{10 - 2 \sqrt{5}}}{32} + \frac{7}{16}`
   * - :math:`87^\circ`
     - :math:`- \frac{\sqrt{10}}{16} - \frac{\sqrt{6}}{16} + \frac{\sqrt{2}}{16} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} + \frac{\sqrt{30}}{16} + \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16}`
     - :math:`- \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16} - \frac{\sqrt{6}}{16} - \frac{\sqrt{2}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} + \frac{\sqrt{30}}{16}`
     - :math:`- \frac{\sqrt{2 \sqrt{5} + 10}}{32} + \frac{\sqrt{3}}{16} + \frac{\sqrt{15}}{16} + \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 10}}{32} + \frac{1}{2}`

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``lattice count``
     - :math:`29`
   * - ``cos 3 deg``
     - :math:`- \frac{\sqrt{10}}{16} - \frac{\sqrt{6}}{16} + \frac{\sqrt{2}}{16} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} + \frac{\sqrt{30}}{16} + \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16}`
   * - ``sin 3 deg``
     - :math:`- \frac{\sqrt{6} \sqrt{2 \sqrt{5} + 10}}{16} - \frac{\sqrt{6}}{16} - \frac{\sqrt{2}}{16} + \frac{\sqrt{10}}{16} + \frac{\sqrt{2} \sqrt{2 \sqrt{5} + 10}}{16} + \frac{\sqrt{30}}{16}`
   * - ``spread 3 deg``
     - :math:`- \frac{\sqrt{5} \sqrt{2 \sqrt{5} + 10}}{32} - \frac{\sqrt{15}}{16} - \frac{\sqrt{3}}{16} + \frac{\sqrt{2 \sqrt{5} + 10}}{32} + \frac{1}{2}`
   * - ``spread 12 deg``
     - :math:`- \frac{\sqrt{15} \sqrt{2 \sqrt{5} + 10}}{32} - \frac{\sqrt{5}}{16} + \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{32} + \frac{7}{16}`
   * - ``spread 15 deg``
     - :math:`\frac{1}{2} - \frac{\sqrt{3}}{4}`
   * - ``fifteen gon chord quadrance``
     - :math:`- \frac{\sqrt{3} \sqrt{2 \sqrt{5} + 10}}{4} - \frac{\sqrt{5}}{4} + \frac{9}{4}`
   * - ``cos pi over 17``
     - :math:`\sqrt{\frac{\sqrt{17}}{32} + \frac{\sqrt{34 - 2 \sqrt{17}}}{32} + \frac{\sqrt{- 2 \sqrt{2 \sqrt{17} + 34} - \sqrt{34 - 2 \sqrt{17}} + 3 \sqrt{17} + 17}}{16} + \frac{15}{32}}`
