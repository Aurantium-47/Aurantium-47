# Aurantium

<sub><b>English</b> · <a href="https://github.com/Aurantium-47/Aurantium-47/blob/main/README.zh-CN.md">简体中文</a></sub>

**AI for Math · NLP**

Exploring the limits of AI in reasoning and software engineering.

Interests: **Quantitative Strategies · Crypto**

[Mathematics](https://github.com/Aurantium-47/aurantium-mathematics) · [Contributions](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)

<p><img alt="Python" src="https://img.shields.io/badge/Python-e9edf2?style=flat-square&amp;logo=python&amp;logoColor=57606a"> <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-e9edf2?style=flat-square&amp;logo=pytorch&amp;logoColor=57606a"> <img alt="Transformers" src="https://img.shields.io/badge/Transformers-e9edf2?style=flat-square&amp;logo=huggingface&amp;logoColor=57606a"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-e9edf2?style=flat-square&amp;logo=numpy&amp;logoColor=57606a"> <img alt="Lean 4" src="https://img.shields.io/badge/Lean%204-e9edf2?style=flat-square"> <img alt="mathlib" src="https://img.shields.io/badge/mathlib-e9edf2?style=flat-square"> <img alt="SymPy" src="https://img.shields.io/badge/SymPy-e9edf2?style=flat-square&amp;logo=sympy&amp;logoColor=57606a"> <img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-e9edf2?style=flat-square&amp;logo=latex&amp;logoColor=57606a"> <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-e9edf2?style=flat-square&amp;logo=cplusplus&amp;logoColor=57606a"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-e9edf2?style=flat-square&amp;logo=typescript&amp;logoColor=57606a"> <img alt="Node.js" src="https://img.shields.io/badge/Node.js-e9edf2?style=flat-square&amp;logo=nodedotjs&amp;logoColor=57606a"> <img alt="Git" src="https://img.shields.io/badge/Git-e9edf2?style=flat-square&amp;logo=git&amp;logoColor=57606a"></p>

## Mathematical research

[**24 research projects · 8 with Lean formalization**](https://github.com/Aurantium-47/aurantium-mathematics)

**7 families include further generalizations.** Across 21 dated research sources, excluding the same-problem literature comparison, first publication was approximately **4 years ago on average**, with the earliest in **2014**.

**[Howroyd’s 27-set conjecture](https://github.com/Aurantium-47/howroyd-27-conjecture)**

<sub>[Posed in 2018 · 8 years ago](https://oeis.org/A297557) · Extremal graph theory</sub>

- **Prior work:** Machacek (2021) proved the divisible-by-three branch, one of the three residue classes.
- **My result:** Proved both remaining classes: **exactly 27 maximum independent sets** for every permitted size. Together with the known branch, this completes the count for every d ≥ 9.
- **Stronger result & verification:** Went beyond counting to **classify all 27 sets**; the remaining-branch theorem is formalized in Lean 4.

<details>
<summary>Original sources & proof method</summary>

- **Original source:** Andrew Howroyd, [OEIS A297557 (2018)](https://oeis.org/A297557).
- **Prior work:** [John Machacek](https://arxiv.org/abs/2010.11112v2), *Procedia Computer Science* 195 (2021), proved the 3 ∣ d branch. Combining the two results completes the counting formula for d ≥ 9.
- **Method:** An exact weighted-cover certificate and a coordinate-reduction argument reduce the classification to three backgrounds with nine corner extensions each.
- **Further results & materials:** Explicit classification of all 27 sets, beyond the conjectured count.
- **Verification:** Lean 4 proof of the full d ≥ 10, 3 ∤ d statement; 89 rational certificate entries.

</details>

**[Lecture Hall: from finite checks to an all-length theorem](https://github.com/Aurantium-47/lecture-hall-polynomiality)**

<sub>[Posed in 2018 · 8 years ago](https://arxiv.org/abs/1809.01377) · Algebraic combinatorics / Commutative algebra</sub>

- **Prior work:** Katthän (2018) reported computational verification through length **12**.
- **My result:** Proved polynomiality for **every length**, replacing the finite evidence with an all-index proof via signed Dyck paths.
- **Extensions & verification:** Obtained explicit coefficient formulas, a minimal monic SAGBI basis and a flat toric degeneration. The polynomiality and path-identification core is formalized in Lean; the algebraic extensions have written proofs.

<details>
<summary>Original sources & proof method</summary>

- **Original source:** Lukas Katthän, [The Lecture Hall Cone as a toric deformation (2018)](https://arxiv.org/abs/1809.01377), prepared for the Osaka lattice-polytopes workshop.
- **Prior work:** The original paper proposed the polynomiality and algebraic-structure statements and checked lengths at most 12. Flajolet’s continued-fraction theory and Sokal’s exposition provide credited classical tools.
- **Method:** A signed Dyck-path identification, Toeplitz–Hankel identities and the defining recurrence give the all-index polynomiality proof.
- **Further results & materials:** Composition coefficient formulas and exact monomial counts; a minimal monic SAGBI basis, a Hilbert-basis correspondence and flat toric degeneration over every field, under the manuscript’s disclosed square-minor interpretation.
- **Verification:** Lean formalizes the genuine rational-function polynomiality and signed-path core. SAGBI and degeneration extensions have written mathematical proofs.

</details>

<details>
<summary>Two further results: a 2016 peak-polynomial conjecture · the sharp bound for K₆ chains</summary>

**[Peak polynomials: the last real root](https://github.com/Aurantium-47/peak-polynomial-last-real-root)**

<sub>[Experimental Mathematics · 2016 journal version · 10 years ago](https://arxiv.org/abs/1410.8506v2) · Real roots</sub>

- **Prior work:** Billey–Fahrbach–Talmage posed Conjecture 6.6; Li’s later coefficient theorem already covers right-side positivity and local sign consequences.
- **My result:** Supplied the missing noninteger-interval sign argument and proved the **full root-exclusion statement**, with no bound on peak count or spacing.
- **Further results:** A self-contained integral proof includes the singleton case and signs across the full interval. These complete the stated root claim rather than an unrelated generalization.

- **Original source:** Sara Billey, Matthew Fahrbach and Alan Talmage, [*Experimental Mathematics* 25(2), 165–175 (2016)](https://arxiv.org/abs/1410.8506v2); preprint first posted in 2014.
- **Prior work:** Billey–Fahrbach–Talmage supplied the recurrence and symmetry identities. [Li’s coefficient theorem](https://doi.org/10.5281/zenodo.22832569) already implies right-side positivity and several local sign properties; the additional argument covers the remaining noninteger interval.
- **Method:** A self-contained integral representation and sign analysis across the full interval beyond the penultimate peak.
- **Further results & materials:** Signs on both sides of the largest peak, its simplicity, and the singleton case are included; overlapping consequences of Li’s theorem are credited in the manuscript.
- **Verification:** All-parameter mathematical proof, with supplementary exact finite checks and a separately recorded small-case reproduction.

**[K₆ chains: a false 22-colour bound replaced by the sharp bound 23](https://github.com/Aurantium-47/k6-clique-chain-packing-coloring)**

<sub>[Conjecture posed in 2025](https://arxiv.org/abs/2511.12761) · Graph colouring</sub>

- **Prior work:** Furmańczyk–Gözüpek–Özkan conjectured a uniform upper bound of **22**.
- **My result:** A **450-vertex** counterexample refutes 22. A periodic construction proves 23 colours suffice for every chain, with the exact value **23** for every chain of at least 75 cliques.
- **Extension & verification:** Goes beyond one counterexample to the **sharp bound for the entire family**. The lower-bound certificate has **16,646,562** exact records, checked by Python and C++ implementations.

- **Original source:** Furmańczyk, Gözüpek and Özkan, [Packing coloring of graphs with long paths (2025)](https://arxiv.org/abs/2511.12761), Conjecture 2.
- **Prior work:** The proposed common upper bound was 22 for the path-aligned K₆ clique chains.
- **Method:** A finite-state scheduling relaxation and decreasing-rank certificate exclude 22; an explicit periodic colouring supplies the upper bound 23.
- **Further results & materials:** Sharp uniform bound 23 for the full chain family and exact value 23 for every t ≥ 75. The minimum counterexample length and all shorter-chain exact values are not determined.
- **Verification:** A 16,646,562-record exact certificate with Python and C++ checkers. This is computational certificate verification, not a Lean formalization.

</details>

**[20 additional projects and literature comparisons](https://github.com/Aurantium-47/aurantium-mathematics/blob/main/README.en.md#all-projects)** include Stern positivity, extremal chemical graphs and Hurwitz real-rootedness.

<details>
<summary>Result counts & dating methodology</summary>

- **10** affirmative original-target results · **3** counterexample-focused results · **7** partial results on broader original questions · **3** constructions or classifications · **1** same-problem literature comparison.
- **7** families contain subsequent generalizations and **8** contain Lean formalization; these counts overlap the result categories above. The bibliography contains **60** source and related-work records.
- Dates use **2026 minus the source’s first-publication year**, averaging **4.0 years across 21 entries**. The sample excludes an undated source, an indirectly authenticated 2000 report, and the Karp comparison with an earlier public proof. These are source ages, not durations continuously unsolved.

</details>

## NLP & information retrieval

**Information Retrieval · Representation Learning · Knowledge Graphs**

Interested in retrieval over semi-structured knowledge bases: dense retrieval, text–graph fusion, entity disambiguation and retrieval evaluation. Currently working with STaRK-MAG.

## Contributions

[9 merged pull requests across 7 projects](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests).

### [REA](https://github.com/morluto/rea) <a href="https://github.com/morluto/rea/stargazers"><img alt="REA upstream stars: 288k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/morluto-rea-287879.svg" width="180" align="right"></a>

Agent-driven reverse engineering, from application behavior to native binaries. Contributions in cross-platform compatibility and binary diagnostics.

<sub>3 merged PRs · [#2422](https://github.com/morluto/rea/pull/2422) · [#2448](https://github.com/morluto/rea/pull/2448) · [#2429](https://github.com/morluto/rea/pull/2429)</sub>

### [Spec Kit](https://github.com/github/spec-kit) <a href="https://github.com/github/spec-kit/stargazers"><img alt="Spec Kit upstream stars: 142k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/github-spec-kit-141541.svg" width="180" align="right"></a>

GitHub’s toolkit for spec-driven development with coding agents. Contributions to Windows workflow reliability.

<sub>1 merged PR · [#4956](https://github.com/github/spec-kit/pull/4956)</sub>

### [KOReader](https://github.com/koreader/koreader) <a href="https://github.com/koreader/koreader/stargazers"><img alt="KOReader upstream stars: 30.4k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/koreader-koreader-30358.svg" width="180" align="right"></a>

A document reader for e-ink devices and Android. Contributions to annotation workflows.

<sub>1 merged PR · [#16220](https://github.com/koreader/koreader/pull/16220)</sub>

### [JSON5](https://github.com/json5/json5) <a href="https://github.com/json5/json5/stargazers"><img alt="JSON5 upstream stars: 7.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/json5-json5-7172.svg" width="180" align="right"></a>

An extension of JSON for human-written configuration. Contributions to serialization correctness.

<sub>1 merged PR · [#371](https://github.com/json5/json5/pull/371)</sub>

### [pydicom](https://github.com/pydicom/pydicom) <a href="https://github.com/pydicom/pydicom/stargazers"><img alt="pydicom upstream stars: 2.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/pydicom-pydicom-2225.svg" width="180" align="right"></a>

A Python library for working with DICOM medical imaging data. Contributions to data conversion and interoperability.

<sub>1 merged PR · [#2388](https://github.com/pydicom/pydicom/pull/2388)</sub>

### [Developer Roadmap](https://github.com/nilbuild/developer-roadmap) <a href="https://github.com/nilbuild/developer-roadmap/stargazers"><img alt="Developer Roadmap upstream stars: 370k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/nilbuild-developer-roadmap-369547.svg" width="180" align="right"></a>

Community-driven roadmaps and guides for developers. Contributions to Python learning content.

<sub>1 merged PR · [#10451](https://github.com/nilbuild/developer-roadmap/pull/10451)</sub>

### [Free Programming Books](https://github.com/EbookFoundation/free-programming-books) <a href="https://github.com/EbookFoundation/free-programming-books/stargazers"><img alt="Free Programming Books upstream stars: 399k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/EbookFoundation-free-programming-books-399196.svg" width="180" align="right"></a>

A multilingual collection of free programming books and learning resources. Contributions to contributor documentation.

<sub>1 merged PR · [#13533](https://github.com/EbookFoundation/free-programming-books/pull/13533)</sub>


<sub>Stars and PR merge status checked 2026-10-17.</sub>

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
