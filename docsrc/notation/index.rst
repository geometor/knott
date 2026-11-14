:navigation: header
:order: 15
:nav_title: Notation

====================================================
Notation Bridge — Knott (:math:`\Phi, \phi`) & SymPy
====================================================

.. enunciation::

   Dr. Ron Knott distinguishes the Golden Ratio :math:`\Phi = \frac{1+\sqrt{5}}{2}`
   from its positive reciprocal :math:`\phi = \Phi - 1 = \frac{1}{\Phi} = \frac{\sqrt{5}-1}{2}`
   strictly by letter case, whereas SymPy and ``geometor.model`` denote the
   larger root by ``sp.GoldenRatio`` (:math:`\phi_{\text{GEOMETOR}} = \Phi_{\text{Knott}}`).

Exact Algebraic Bijection
-------------------------

A recurring source of confusion across Golden Ratio literature is whether
:math:`\phi` denotes :math:`1.61803\dots` or :math:`0.61803\dots`. Throughout
*Fibonacci Numbers, the Golden Section and the Golden String*
(:cite:`KnottPropsPhi`), :person:`Dr. Ron Knott <knott>` adopts a remarkably
transparent convention in which **uppercase** :math:`\Phi` and **lowercase**
:math:`\phi` share the exact same fractional tail :math:`0.6180339887\dots`:

.. list-table:: Canonical Notation Concordance
   :header-rows: 1
   :widths: 22 24 28 26

   * - Quantity
     - Dr. Ron Knott Notation
     - Exact :math:`\mathbb{Q}(\sqrt{5})` Radical
     - SymPy / ``geometor.model``
   * - **Golden Ratio** (:math:`> 1`)
     - :math:`\Phi` (``geometor.knott.PHI``)
     - :math:`\dfrac{1 + \sqrt{5}}{2} \approx 1.6180339887\dots`
     - ``sp.GoldenRatio`` (:math:`\phi_{\text{GEOMETOR}}`)
   * - **Reciprocal Golden Ratio** (:math:`< 1`)
     - :math:`\phi` (``geometor.knott.phi``)
     - :math:`\dfrac{\sqrt{5} - 1}{2} \approx 0.6180339887\dots`
     - ``1 / sp.GoldenRatio`` (:math:`\phi_{\text{GEOMETOR}} - 1`)
   * - **Galois Conjugate** (:math:`< 0`)
     - :math:`-\phi = 1 - \Phi` (``geometor.knott.PSI``)
     - :math:`\dfrac{1 - \sqrt{5}}{2} \approx -0.6180339887\dots`
     - ``1 - sp.GoldenRatio``

Fundamental Coupled Identities
------------------------------

Every algebraic verification in :mod:`geometor.knott.constants` checks the
coupled :term:`Golden Ratio <golden-ratio>` laws symbolically over
:math:`\mathbb{Q}(\sqrt{5})`:

.. math::

   \Phi - \phi = 1, \qquad
   \Phi \cdot \phi = 1, \qquad
   \Phi + \phi = \sqrt{5}, \qquad
   \Phi^2 = \Phi + 1, \qquad
   \phi^2 = 1 - \phi = 2 - \Phi.

Lossless conversions between Dr. Knott's :math:`(\Phi, \phi)` expressions and
SymPy's ``sp.GoldenRatio`` are provided by
:func:`geometor.knott.constants.knott_to_geometor` and
:func:`geometor.knott.constants.geometor_to_knott_radicals`.

Rational Trigonometry Invariants
--------------------------------

To avoid introducing transcendental ``acos`` or floating-point rounding into
geometric proofs, ``geometor-knott`` pairs classical Euclidean ratios with
:person:`Norman J. Wildberger <wildberger>`'s Rational Trigonometry invariants
(:cite:`Wildberger2005`):

* **Quadrance** (:term:`quadrance`):
  :math:`Q(A, B) = (x_B - x_A)^2 + (y_B - y_A)^2` — exact squared Euclidean
  separation;
* **Spread** (:term:`spread`):
  :math:`s(\ell_1, \ell_2) = \sin^2\theta \in [0, 1]` — exact rational/algebraic
  line separation (:math:`s = 0` parallel, :math:`s = 1` perpendicular,
  :math:`s(36^\circ) = \frac{5 - \sqrt{5}}{8}`,
  :math:`s(72^\circ) = \frac{5 + \sqrt{5}}{8}`);
* **Projective Cross-Ratio** (:term:`cross-ratio`):
  :math:`(A, B; C, D) = \frac{(A - C)(B - D)}{(A - D)(B - C)}` — exact
  projective harmonic and golden range invariant.
