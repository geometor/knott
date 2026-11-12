:layout: book
:type: item
:order: 5
:canonical_id: KNOTT-6.5

.. _knott-6-5:

======================================================================
KNOTT-6.5 — Golden Angle (360° / Φ² ≈ 137.50776°) & Parastichy Bridges
======================================================================

.. enunciation::

   Dividing a full turn in extreme and mean ratio yields the Golden Angle 2π / Φ² = 2π φ² ≈ 137.50776°, whose cylindrical primordia satisfy Fₖ φ² − Fₖ₋₂ = (−φ)ᵏ, pairing opposing left- and right-handed parastichy spirals in consecutive Fibonacci numbers (Fₖ, Fₖ₊₁).

.. picture:: knott-6-5.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-6.5``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Fibonacci Numbers and Nature* (`#seeds <https://r-knott.surrey.ac.uk/Fibonacci/fibnat.html#seeds>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/fibnat.html#seeds>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.identities.construct_parastichy_lattice_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/phyllotaxis <https://geometor.github.io/phyllotaxis/>`_, `geometor/thompson <https://geometor.github.io/thompson/>`_, `geometor/fibonacci <https://geometor.github.io/fibonacci/>`_, `geometor/pacioli <https://geometor.github.io/pacioli/>`_, `geometor/divine <https://geometor.github.io/divine/>`_

Constructive Synthesis & Exact Proof
------------------------------------

Concluding the catalog on ``fibnat.html`` (:cite:`KnottNature`), :person:`Dr. Ron Knott <knott>`
connects the :term:`Golden Angle <golden-angle>` :math:`2\pi / \Phi^2 = 2\pi\phi^2 \approx 137.50776^\circ`
to the opposing Fibonacci spiral families (:term:`parastichies <parastichy>`) studied by
:person:`Luca Pacioli <pacioli>`, :person:`D'Arcy Wentworth Thompson <thompson>` (:cite:`Thompson1917`),
and :person:`H. S. M. Coxeter <coxeter>` (:cite:`Coxeter1973`).

* **Unrolled Cylindrical Primordia & Alternating Convergence**: Unrolling a cylindrical stem
  around central axis :g:`OS <knott-6-5.g1:/ O S />` (:g:`O <knott-6-5.g1:O>` to
  :g:`S <knott-6-5.g1:S>`), the :math:`F_k`-th primordium lands at signed angular offset
  :math:`F_k \phi^2 - F_{k-2} = (-\phi)^k`, placing :g:`P2 <knott-6-5.g1:P2>` (:math:`F_2 = 1`),
  :g:`F2 <knott-6-5.g1:F2>` (:math:`F_3 = 2`), :g:`F3 <knott-6-5.g1:F3>` (:math:`F_4 = 3`),
  :g:`F5 <knott-6-5.g1:F5>` (:math:`F_5 = 5`), and :g:`F8 <knott-6-5.g1:F8>` (:math:`F_6 = 8`)
  on alternating sides of :g:`OS <knott-6-5.g1:/ O S />` along vectors
  :g:`OP2 <knott-6-5.g1:/ O P2 />` – :g:`OF8 <knott-6-5.g1:/ O F8 />`.
* **Unimodular Parastichy Parallelograms**: Because :math:`(-\phi)^k + (-\phi)^{k+1} = (-\phi)^{k+2}`
  and :math:`F_k + F_{k+1} = F_{k+2}`, vector :g:`F5 <knott-6-5.g1:F5>` is the exact
  2D vector sum of :g:`F2 <knott-6-5.g1:F2>` and :g:`F3 <knott-6-5.g1:F3>` (edges
  :g:`F2F5 <knott-6-5.g1:/ F2 F5 />` and :g:`F3F5 <knott-6-5.g1:/ F3 F5 />`), and
  :g:`F8 <knott-6-5.g1:F8>` is the vector sum of :g:`F3 <knott-6-5.g1:F3>` and
  :g:`F5 <knott-6-5.g1:/ O F5 />` (edges :g:`F3F8 <knott-6-5.g1:/ F3 F8 />` and
  :g:`F5F8 <knott-6-5.g1:/ F5 F8 />`). Moreover, :math:`\phi^k (F_k \phi + F_{k+1}) = \phi^k \Phi^k = 1`,
  proving that consecutive parastichy cells :g:`OF3F5F2 <knott-6-5.g1:< O F3 F5 F2 >>` and
  :g:`OF3F8F5 <knott-6-5.g1:< O F3 F8 F5 >>` are :eq:`equal <knott-6-5.g1:< O F3 F5 F2 > = knott-6-5.g1:< O F3 F8 F5 >>`
  unimodular fundamental domains of normalized area :math:`1`.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``minor turn fraction``
     - :math:`\frac{3 - \sqrt{5}}{2}`
   * - ``major turn fraction``
     - :math:`\frac{-1 + \sqrt{5}}{2}`
   * - ``golden angle radians``
     - :math:`- \sqrt{5} \pi + 3 \pi`
   * - ``golden angle degrees``
     - :math:`540 - 180 \sqrt{5}`
   * - ``reflex angle degrees``
     - :math:`-180 + 180 \sqrt{5}`
   * - ``fundamental parastichy cell area``
     - :math:`1`
