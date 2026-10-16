# Aurantium

<sub><b>English</b> · <a href="https://github.com/Aurantium-47/Aurantium-47/blob/main/README.zh-CN.md">简体中文</a></sub>

**AI for Math · NLP**

Exploring the limits of AI in reasoning and software engineering.

Interests: **Quantitative Strategies · Crypto**

[Mathematics](https://github.com/Aurantium-47/aurantium-mathematics) · [Contributions](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)

<p><img alt="Python" src="https://img.shields.io/badge/Python-e9edf2?style=flat-square&amp;logo=python&amp;logoColor=57606a"> <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-e9edf2?style=flat-square&amp;logo=pytorch&amp;logoColor=57606a"> <img alt="Transformers" src="https://img.shields.io/badge/Transformers-e9edf2?style=flat-square&amp;logo=huggingface&amp;logoColor=57606a"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-e9edf2?style=flat-square&amp;logo=numpy&amp;logoColor=57606a"> <img alt="Lean 4" src="https://img.shields.io/badge/Lean%204-e9edf2?style=flat-square"> <img alt="mathlib" src="https://img.shields.io/badge/mathlib-e9edf2?style=flat-square"> <img alt="SymPy" src="https://img.shields.io/badge/SymPy-e9edf2?style=flat-square&amp;logo=sympy&amp;logoColor=57606a"> <img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-e9edf2?style=flat-square&amp;logo=latex&amp;logoColor=57606a"> <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-e9edf2?style=flat-square&amp;logo=cplusplus&amp;logoColor=57606a"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-e9edf2?style=flat-square&amp;logo=typescript&amp;logoColor=57606a"> <img alt="Node.js" src="https://img.shields.io/badge/Node.js-e9edf2?style=flat-square&amp;logo=nodedotjs&amp;logoColor=57606a"> <img alt="Git" src="https://img.shields.io/badge/Git-e9edf2?style=flat-square&amp;logo=git&amp;logoColor=57606a"></p>

## Mathematical research

[**24 research projects · 8 with Lean formalization**](https://github.com/Aurantium-47/aurantium-mathematics)

**[Howroyd’s 27-set conjecture](https://github.com/Aurantium-47/howroyd-27-conjecture)**

Proved the remaining two residue classes: **exactly 27 maximum independent sets**, with a complete classification, for every d ≥ 10 with 3 ∤ d.

<sub>Extremal graph theory · Enumerative combinatorics</sub>

<details>
<summary>Source, prior work & verification</summary>

- **Original source:** Andrew Howroyd, [OEIS A297557 (2018)](https://oeis.org/A297557).
- **Prior work:** [John Machacek](https://arxiv.org/abs/2010.11112v2), *Procedia Computer Science* 195 (2021), proved the 3 ∣ d branch. Combining the two results completes the counting formula for d ≥ 9.
- **Method:** An exact weighted-cover certificate and a coordinate-reduction argument reduce the classification to three backgrounds with nine corner extensions each.
- **Further results & materials:** Explicit classification of all 27 sets, beyond the conjectured count.
- **Verification:** Lean 4 proof of the full d ≥ 10, 3 ∤ d statement; 89 rational certificate entries.

</details>

**[Peak polynomials: the last real root](https://github.com/Aurantium-47/peak-polynomial-last-real-root)**

Proved **Billey–Fahrbach–Talmage Conjecture 6.6**: the largest peak is the only real root beyond the penultimate peak, with no bound on peak count or spacing.

<sub>Algebraic combinatorics · Polynomial root geometry</sub>

<details>
<summary>Source, prior work & verification</summary>

- **Original source:** Sara Billey, Matthew Fahrbach and Alan Talmage, [*Experimental Mathematics* 25(2), 165–175 (2016)](https://arxiv.org/abs/1410.8506v2); preprint first posted in 2014.
- **Prior work:** Billey–Fahrbach–Talmage supplied the recurrence and symmetry identities. [Li’s coefficient theorem](https://doi.org/10.5281/zenodo.22832569) already implies right-side positivity and several local sign properties; the additional argument covers the remaining noninteger interval.
- **Method:** A self-contained integral representation and sign analysis across the full interval beyond the penultimate peak.
- **Further results & materials:** Signs on both sides of the largest peak, its simplicity, and the singleton case are included; overlapping consequences of Li’s theorem are credited in the manuscript.
- **Verification:** All-parameter mathematical proof, with supplementary exact finite checks and a separately recorded small-case reproduction.

</details>

<details>
<summary>Two further results: Stern positivity · Fence counterexample</summary>

**[Stern polynomials: positivity and monotonicity](https://github.com/Aurantium-47/stern-polynomial-positivity)**

Proved Ulas’s **Conjecture 4.4 for every n ≥ 0 and real t**; an exact B₁₈₃ counterexample also refutes the monotonicity clause of Conjecture 4.3.

<sub>Number theory · Polynomial positivity</sub>

- **Original source:** Maciej Ulas, [arXiv preprint (2019)](https://arxiv.org/abs/1909.10844v1); journal version in [*Publicationes Mathematicae Debrecen* 96(3–4), 401–422 (2020)](https://publi.math.unideb.hu/contents/2020). Conjecture numbering follows the preprint.
- **Prior work:** The Stern recurrence and the quadratic identity used in the proof are established ingredients, including Ulas’s own identity.
- **Method:** Recurrence-based positivity and an exact rational derivative witness for the monotonicity counterexample.
- **Further results & materials:** The general positivity theorem and the separate monotonicity counterexample; the unique-real-root clause of Conjecture 4.3 remains outside this result.
- **Verification:** Both results formalized in Lean 4 / mathlib, including the implication from negative derivative to failure of monotonicity.

**[Fence rowmotion: a homomesy counterexample](https://github.com/Aurantium-47/fence-rowmotion-counterexample)**

Refuted **Conjecture 5.4(b)** with a 32-element fence and a complete 237-state orbit: its exact mean is **1258/79 ≠ 16**.

<sub>Dynamical algebraic combinatorics · Posets</sub>

- **Original source:** Sergi Elizalde, Matthew Plante, Tom Roby and Bruce Sagan, [*Algebraic Combinatorics* 6(1), 17–36 (2023)](https://alco.centre-mersenne.org/articles/10.5802/alco.256/).
- **Prior work:** The authors established several orbit-average results and proposed the ideal-cardinality homomesy statement in Conjecture 5.4(b).
- **Method:** Explicit poset construction, complete orbit enumeration and an exact rational average.
- **Further results & materials:** The entire orbit is distributed as a reproducible certificate. Part (a) of the conjecture is unaffected.
- **Verification:** Lean kernel reduction checks the finite certificate; the theorem avoids native-evaluation axioms.

</details>

## NLP & information retrieval

**Information Retrieval · Representation Learning · Knowledge Graphs**

Interested in retrieval over semi-structured knowledge bases: dense retrieval, text–graph fusion, entity disambiguation and retrieval evaluation. Currently working with STaRK-MAG.

## Contributions

[9 merged pull requests across 7 projects](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests).

### [REA](https://github.com/morluto/rea) <a href="https://github.com/morluto/rea/stargazers"><img alt="REA upstream stars" src="https://img.shields.io/github/stars/morluto/rea?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

Agent-driven reverse engineering, from application behavior to native binaries. Contributions in cross-platform compatibility and binary diagnostics.

<sub>3 merged PRs · [#2422](https://github.com/morluto/rea/pull/2422) · [#2448](https://github.com/morluto/rea/pull/2448) · [#2429](https://github.com/morluto/rea/pull/2429)</sub>

### [Spec Kit](https://github.com/github/spec-kit) <a href="https://github.com/github/spec-kit/stargazers"><img alt="Spec Kit upstream stars" src="https://img.shields.io/github/stars/github/spec-kit?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

GitHub’s toolkit for spec-driven development with coding agents. Contributions to Windows workflow reliability.

<sub>1 merged PR · [#4956](https://github.com/github/spec-kit/pull/4956)</sub>

### [KOReader](https://github.com/koreader/koreader) <a href="https://github.com/koreader/koreader/stargazers"><img alt="KOReader upstream stars" src="https://img.shields.io/github/stars/koreader/koreader?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

A document reader for e-ink devices and Android. Contributions to annotation workflows.

<sub>1 merged PR · [#16220](https://github.com/koreader/koreader/pull/16220)</sub>

### [JSON5](https://github.com/json5/json5) <a href="https://github.com/json5/json5/stargazers"><img alt="JSON5 upstream stars" src="https://img.shields.io/github/stars/json5/json5?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

An extension of JSON for human-written configuration. Contributions to serialization correctness.

<sub>1 merged PR · [#371](https://github.com/json5/json5/pull/371)</sub>

### [pydicom](https://github.com/pydicom/pydicom) <a href="https://github.com/pydicom/pydicom/stargazers"><img alt="pydicom upstream stars" src="https://img.shields.io/github/stars/pydicom/pydicom?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

A Python library for working with DICOM medical imaging data. Contributions to data conversion and interoperability.

<sub>1 merged PR · [#2388](https://github.com/pydicom/pydicom/pull/2388)</sub>

### [Developer Roadmap](https://github.com/nilbuild/developer-roadmap) <a href="https://github.com/nilbuild/developer-roadmap/stargazers"><img alt="Developer Roadmap upstream stars" src="https://img.shields.io/github/stars/nilbuild/developer-roadmap?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

Community-driven roadmaps and guides for developers. Contributions to Python learning content.

<sub>1 merged PR · [#10451](https://github.com/nilbuild/developer-roadmap/pull/10451)</sub>

### [Free Programming Books](https://github.com/EbookFoundation/free-programming-books) <a href="https://github.com/EbookFoundation/free-programming-books/stargazers"><img alt="Free Programming Books upstream stars" src="https://img.shields.io/github/stars/EbookFoundation/free-programming-books?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

A multilingual collection of free programming books and learning resources. Contributions to contributor documentation.

<sub>1 merged PR · [#13533](https://github.com/EbookFoundation/free-programming-books/pull/13533)</sub>


<sub>Badges show live upstream repository stars. PR merge status checked 2026-10-17.</sub>

## Selected activity

<sub>Maintained by my AI assistant · scheduled updates pending</sub>

<!-- ACTIVITY:START -->
- <sub>2026-10-13</sub> · [REA #2422 — merged; acknowledged and extended by N0zoM1z0 in merged PR #2635.](https://github.com/morluto/rea/pull/2635)
- <sub>2026-10-13</sub> · [REA #2448 — merged; verification report and thanks from CassieFox23.](https://github.com/morluto/rea/pull/2448#issuecomment-6138368698)
- <sub>2026-10-12</sub> · [REA #2227](https://github.com/morluto/rea/pull/2227#issuecomment-6127162628) — thanked by maintainer morluto, followed by an [upstream implementation](https://github.com/morluto/rea/commit/c9fed50691ae014890e91a72534773d2fb58ce44).
- <sub>2026-10-14</sub> · [Spec Kit #4956 — merged, with thanks from mnriem.](https://github.com/github/spec-kit/pull/4956#issuecomment-6169522572)
- <sub>2026-10-17</sub> · [Published Aurantium · Mathematics: 24 research projects, including 8 with Lean formalization.](https://github.com/Aurantium-47/aurantium-mathematics)
- <sub>2026-10-15</sub> · [JSON5 #371 — merged.](https://github.com/json5/json5/pull/371)

<details>
<summary>More activity</summary>

- <sub>2026-10-15</sub> · [Developer Roadmap #10451 — merged.](https://github.com/nilbuild/developer-roadmap/pull/10451)
- <sub>2026-10-15</sub> · [Free Programming Books #13533 — merged.](https://github.com/EbookFoundation/free-programming-books/pull/13533)
- <sub>2026-10-14</sub> · [KOReader #16220 — merged.](https://github.com/koreader/koreader/pull/16220)
- <sub>2026-10-15</sub> · [Published the Lean supplement for Hardinian asymptotics at r = 2.](https://github.com/Aurantium-47/hardinian-array-asymptotics/blob/477fcff33df19d5f752f9748d8596b31da15c81b/FORMALIZATION.md)

</details>
<!-- ACTIVITY:END -->

[All projects](https://github.com/Aurantium-47?tab=repositories) · [Merged contributions](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)
