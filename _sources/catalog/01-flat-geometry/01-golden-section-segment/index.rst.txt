:layout: book
:type: item
:order: 1
:canonical_id: KNOTT-1.1

.. _knott-1-1:

=========================================================================
KNOTT-1.1 — Internal & External Golden Section Constructions on a Segment
=========================================================================

.. enunciation::

   Given a finite segment AB, midpoint-circle compass-and-straightedge constructions divide AB internally at G so AB : AG = AG : GB = Φ and extend AB externally to E so AE : AB = AB : BE = Φ, erecting Golden Rectangle AEFD.

.. picture:: knott-1-1.g1.svg

Curated Source & Catalog Provenance
-----------------------------------

.. list-table::
   :widths: 26 74

   * - **Catalog ID**
     - ``KNOTT-1.1``
   * - **Curated Source**
     - :person:`Dr. Ron Knott <knott>`, *Phi in 2D Geometry and Trigonometry* (`#cons <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#cons>`_)
   * - **Source Attribution**
     - **© 1996–2025 Dr. Ron Knott, University of Surrey** — `Explore Dr. Knott's original exposition <https://r-knott.surrey.ac.uk/Fibonacci/phi2DGeomTrig.html#cons>`_
   * - **Exact SymPy Validator**
     - :func:`geometor.knott.flat_geometry.construct_golden_section_segment` (`0` ``sp.Float`` atoms)
   * - **GEOMETOR Concordance**
     - `geometor/euclid <https://geometor.github.io/euclid/>`_, `geometor/elements <https://geometor.github.io/elements/>`_, `geometor/divine <https://geometor.github.io/divine/>`_, `geometor/fundamentals <https://geometor.github.io/fundamentals/>`_

Constructive Synthesis & Exact Proof
------------------------------------

:person:`Dr. Ron Knott <knott>` opens his 2D Golden Geometry survey (:cite:`KnottPhi2D`)
by pairing the two complementary compass-and-straightedge problems of :person:`Euclid <euclid>`
(:cite:`EuclidElements`, Books II.11 and VI.30): extending a given straight segment
externally in :term:`extreme and mean ratio <extreme-and-mean-ratio>`, and dividing
the same segment internally.

1. **External Golden Extension**: Starting from given segment :g:`AB <knott-1-1.g1:A; knott-1-1.g1:B>`
   of length :math:`2` and erecting square :g:`ABCD <knott-1-1.g1:< A B C D >>`, bisect the
   base at :g:`M <knott-1-1.g1:M>` so segment :g:`MC <knott-1-1.g1:/ M C />` has exact
   :term:`quadrance` :math:`Q(M, C) = 1^2 + 2^2 = 5`. Sweeping guide circle
   :g:`(M, C) <knott-1-1.g1:( M C )>` onto line :g:`[AB] <knott-1-1.g1:[ A B ]>` beyond
   :g:`B <knott-1-1.g1:B>` determines :g:`E <knott-1-1.g1:E>` with
   :g:`AE <knott-1-1.g1:/ A E />` :math:`= 1 + \sqrt{5} = 2\Phi` and
   :g:`BE <knott-1-1.g1:/ B E />` :math:`= \sqrt{5} - 1 = 2\phi`, completing Golden
   Rectangle :g:`AEFD <knott-1-1.g1:< A E F D >>` above :g:`F <knott-1-1.g1:F>`.
2. **Internal Golden Division**: Joining :g:`A <knott-1-1.g1:A>` to midpoint
   :g:`H <knott-1-1.g1:H>` of :math:`BC` produces :g:`AH <knott-1-1.g1:/ A H />` of length
   :math:`\sqrt{5}`. Unit circle :g:`(H, B) <knott-1-1.g1:( H B )>` cuts :g:`AH <knott-1-1.g1:/ A H />`
   at :g:`K <knott-1-1.g1:K>` (:math:`AK = \sqrt{5} - 1 = 2\phi`), and circle
   :g:`(A, K) <knott-1-1.g1:( A K )>` transfers that length onto the base at internal
   golden cut :g:`G <knott-1-1.g1:G>`. Thus major internal segment :g:`AG <knott-1-1.g1:/ A G />`
   and external overhang :g:`BE <knott-1-1.g1:/ B E />` are :eq:`equal <knott-1-1.g1:/ A G / = knott-1-1.g1:/ B E />`
   (:math:`2\phi`), leaving minor segment :g:`GB <knott-1-1.g1:/ G B />` :math:`= 2\phi^2` and
   fixing the projective :term:`cross-ratio` :math:`(A, E; G, B) = \phi^2 = 2 - \Phi`.

Machine-Verified Exact Symbolic Invariants
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 38 62

   * - Invariant
     - Exact Symbolic Value
   * - ``AB``
     - :math:`2`
   * - ``AG``
     - :math:`\sqrt{6 - 2 \sqrt{5}}`
   * - ``GB``
     - :math:`\sqrt{14 - 6 \sqrt{5}}`
   * - ``AE``
     - :math:`\sqrt{2 \sqrt{5} + 6}`
   * - ``internal ratio AB over AG``
     - :math:`\frac{1 + \sqrt{5}}{2}`
   * - ``external ratio AE over AB``
     - :math:`\frac{\sqrt{2 \sqrt{5} + 6}}{2}`
   * - ``cross ratio A E G B``
     - :math:`\frac{3}{2} - \frac{\sqrt{5}}{2}`
