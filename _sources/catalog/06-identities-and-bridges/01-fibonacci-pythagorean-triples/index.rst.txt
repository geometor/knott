:layout: book
:type: item
:order: 1
:canonical_id: KNOTT-6.1

.. _knott-6-1:

================================================================
KNOTT-6.1 — Fibonacci Generator of Primitive Pythagorean Triples
================================================================

.. enunciation::

   Any four consecutive positive Fibonacci numbers (Fₙ, Fₙ₊₁, Fₙ₊₂, Fₙ₊₃) form the Pythagorean right triangle (Fₙ Fₙ₊₃, 2 Fₙ₊₁ Fₙ₊₂, F₂ₙ₊₃) of area Fₙ Fₙ₊₁ Fₙ₊₂ Fₙ₊₃ and inradius Fₙ Fₙ₊₁, primitive whenever 3 ∤ n and twice a primitive triple when 3 ∣ n.

.. picture:: knott-6-1.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-6.1``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Pythagorean Triangles and Triples* (`#pythfib <https://r-knott.surrey.ac.uk/Pythag/pythag.html#pythfib>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Pythag/pythag.html#pythfib>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.identities.construct_fibonacci_pythagorean_model` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/wildberger <https://geometor.github.io/wildberger/>`_, `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/elements <https://geometor.github.io/elements/>`_

Constructive Synthesis & Exact Proof
------------------------------------

On ``Pythag/pythag.html`` (:cite:`KnottPythag`), :person:`Dr. Ron Knott <knott>` catalogs
:person:`Alwyn Horadam <fibonacci>`'s (:cite:`Horadam1961`) four-term Fibonacci generator
of :person:`Pythagoras <pythagoras>`'s right triangles: any four consecutive positive
Fibonacci numbers :math:`(F_n, F_{n+1}, F_{n+2}, F_{n+3})` satisfy

.. math::

   (F_n F_{n+3})^2 + (2 F_{n+1} F_{n+2})^2 = (F_{n+1}^2 + F_{n+2}^2)^2 = F_{2n+3}^2.

* **Nested Exact Right Triangles & Rational Incircle**: Anchored at right-angle vertex
  :g:`O <knott-6-1.g1:O>`, :math:`n = 1 \mapsto (1, 1, 2, 3)` constructs the classic
  :math:`(3, 4, 5)` triangle :g:`OA1B1 <knott-6-1.g1:< O A1 B1 >>` with hypotenuse
  :g:`A1B1 <knott-6-1.g1:/ A1 B1 />` :math:`= F_5 = 5`, while :math:`n = 2 \mapsto (1, 2, 3, 5)`
  constructs the :math:`(5, 12, 13)` triangle :g:`OA2B2 <knott-6-1.g1:< O A2 B2 >>` on legs
  :g:`OA2 <knott-6-1.g1:/ O A2 />` :math:`= 5`, :g:`OB2 <knott-6-1.g1:/ O B2 />` :math:`= 12`,
  and hypotenuse :g:`A2B2 <knott-6-1.g1:/ A2 B2 />` :math:`= F_7 = 13`. Its exact incircle
  :g:`(I2, T2) <knott-6-1.g1:( I2 T2 )>` centered at :g:`I2 <knott-6-1.g1:I2>` :math:`(2, 2)`
  has integer inradius :math:`r = F_2 F_3 = 2` and triangle area
  :math:`F_2 F_3 F_4 F_5 = 1 \cdot 2 \cdot 3 \cdot 5 = 30`.
* **Divisibility Dichotomy**: Because :math:`\gcd(F_{n+1}, F_{n+2}) = 1` and :math:`2 \mid F_k \iff 3 \mid k`,
  the generated triple has :math:`\gcd = 1` (primitive) whenever :math:`3 \nmid n` and
  :math:`\gcd = 2` (twice a primitive triple, e.g. :math:`n = 3 \mapsto (16, 30, 34) = 2(8, 15, 17)`)
  whenever :math:`3 \mid n`.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``n1 hypotenuse``
     - :math:`5`
   * - ``n1 area``
     - :math:`6`
   * - ``n2 hypotenuse``
     - :math:`13`
   * - ``n2 area``
     - :math:`30`
   * - ``n2 inradius``
     - :math:`2`
   * - ``n4 hypotenuse``
     - :math:`89`
   * - ``n4 area``
     - :math:`1560`
