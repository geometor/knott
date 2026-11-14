:type: item
:order: 5
:canonical_id: KNOTT-1.5

.. _knott-1-5:

=====================================================================================
KNOTT-1.5 — Kepler's Golden Right Triangle (1, √Φ, Φ) & Circle-Square Near-Quadrature
=====================================================================================

.. enunciation::

   A right triangle with side lengths (1, √Φ, Φ) has side quadrances (1, Φ, Φ²) simultaneously in geometric progression and Pythagorean sum 1 + Φ = Φ², satisfies cos θ = tan θ = 1/√Φ, and equates the perimeter 4√Φ of the square on leg √Φ with the circumference πΦ of the circle on diameter Φ to within 0.096%.

.. picture:: knott-1-5.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-1.5``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Phi in 2D Geometry and Trigonometry* (`#PhiRightAng <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#PhiRightAng>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#PhiRightAng>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.flat_geometry.construct_kepler_triangle` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/wildberger <https://geometor.github.io/wildberger/>`_, `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/divine <https://geometor.github.io/divine/>`_

Constructive Synthesis & Exact Proof
------------------------------------

In an October 1597 letter to Michael Mästlin, :person:`Johannes Kepler <kepler>` combined
the Pythagorean theorem with the Golden Ratio to isolate the unique right triangle whose
sides form a geometric progression (:cite:`KnottPhi2D`).

* **Euclidean Geometric-Mean Construction**: Along diameter segment from
  :g:`D <knott-1-5.g1:D>` :math:`(-1, 0)` through :g:`B <knott-1-5.g1:B>` :math:`(0, 0)` to
  :g:`E <knott-1-5.g1:E>` :math:`(\Phi, 0)`, Thales semicircle :g:`(O, E) <knott-1-5.g1:( O E )>`
  cuts the vertical axis at :g:`C <knott-1-5.g1:C>` :math:`(0, \sqrt{\Phi})` (*Elements*
  VI.13). In :term:`Kepler triangle <kepler-triangle>` :g:`DBC <knott-1-5.g1:< D B C >>`,
  short leg :g:`BD <knott-1-5.g1:/ B D />`, long leg :g:`BC <knott-1-5.g1:/ B C />`, and
  hypotenuse :g:`DC <knott-1-5.g1:/ D C />` (which is :eq:`equal <knott-1-5.g1:/ D C / = knott-1-5.g1:/ B E />`
  to golden segment :g:`BE <knott-1-5.g1:/ B E />`, joined by chord :g:`CE <knott-1-5.g1:/ C E />`)
  have exact :term:`quadrances <quadrance>` :math:`(1, \Phi, \Phi^2)` satisfying both
  :math:`Q_{BC}^2 = Q_{BD} Q_{DC}` and :math:`1 + \Phi = \Phi^2`.
* **Coincidence of Cosine & Tangent and Near-Quadrature**: At acute apex :g:`C <knott-1-5.g1:C>`,
  :math:`\cos\theta_C = \tan\theta_C = \sin\theta_D = 1/\sqrt{\Phi}` (:math:`\cos^2\theta_C = \tan^2\theta_C = \phi`).
  Erecting square :g:`BGFC <knott-1-5.g1:< B G F C >>` (via :g:`F <knott-1-5.g1:F>` and
  :g:`G <knott-1-5.g1:G>`) of perimeter :math:`4\sqrt{\Phi} \approx 5.08808` alongside
  circle :g:`(M, C) <knott-1-5.g1:( M C )>` centered at hypotenuse midpoint
  :g:`M <knott-1-5.g1:M>` of circumference :math:`\pi\Phi \approx 5.08320` exhibits the
  celebrated circle–square perimeter near-quadrature highlighted by Dr. Knott
  (:math:`4 / (\pi\sqrt{\Phi}) \approx 1.000959`, within :math:`0.096\%`).

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``Q leg short``
     - :math:`1`
   * - ``Q leg long``
     - :math:`\frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``Q hypotenuse``
     - :math:`\frac{\sqrt{5}}{2} + \frac{3}{2}`
   * - ``spread acute D``
     - :math:`\frac{1}{\sqrt{5} + 3} + \frac{\sqrt{5}}{\sqrt{5} + 3}`
   * - ``spread apex C``
     - :math:`\frac{3 - \sqrt{5}}{2}`
   * - ``cos sq equals tan sq C``
     - :math:`- \frac{1}{2} + \frac{\sqrt{5}}{2}`
   * - ``square perimeter``
     - :math:`4 \sqrt{\frac{1}{2} + \frac{\sqrt{5}}{2}}`
   * - ``circle circumference``
     - :math:`\pi \left(\frac{1}{2} + \frac{\sqrt{5}}{2}\right)`
   * - ``quadrature ratio``
     - :math:`\frac{4}{\pi \sqrt{\frac{1}{2} + \frac{\sqrt{5}}{2}}}`
