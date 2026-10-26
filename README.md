<p align="center">
  <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/aurantium-amber-pulse.gif" alt="Aurantium — an animated ASCII orange in warm amber light" width="840">
</p>

# Aurantium🍊

<sub><b>English</b> · <a href="https://github.com/Aurantium-47/Aurantium-47/blob/main/README.zh-CN.md">简体中文</a></sub>

**NLP · AI for Math · Crypto**

[Mathematics](https://github.com/Aurantium-47/aurantium-mathematics) · [Contributions](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)

<p><img alt="Python" src="https://img.shields.io/badge/Python-e9edf2?style=flat-square&amp;logo=python&amp;logoColor=57606a"> <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-e9edf2?style=flat-square&amp;logo=pytorch&amp;logoColor=57606a"> <img alt="Transformers" src="https://img.shields.io/badge/Transformers-e9edf2?style=flat-square&amp;logo=huggingface&amp;logoColor=57606a"> <img alt="Lean 4 / mathlib" src="https://img.shields.io/badge/Lean%204%20%2F%20mathlib-e9edf2?style=flat-square"> <img alt="SymPy" src="https://img.shields.io/badge/SymPy-e9edf2?style=flat-square&amp;logo=sympy&amp;logoColor=57606a"> <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-e9edf2?style=flat-square&amp;logo=cplusplus&amp;logoColor=57606a"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-e9edf2?style=flat-square&amp;logo=typescript&amp;logoColor=57606a"></p>

<!-- INTERESTS:START -->
<p>
  <picture>
    <source media="(max-width: 640px)" srcset="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/f66fade9b3a78cbb0cde0b1588fad17ff55e3075/assets/interests/records-mobile.svg?v=5">
    <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/f66fade9b3a78cbb0cde0b1588fad17ff55e3075/assets/interests/records.svg?v=5" width="920" alt="">
  </picture>
</p>
<p>
  <picture>
    <source media="(max-width: 640px)" srcset="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/f26d83ce59e24bd7c9000ae94a74b64fddeb616e/assets/interests/words-mobile.svg?v=5">
    <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/f26d83ce59e24bd7c9000ae94a74b64fddeb616e/assets/interests/words.svg?v=5" width="920" alt="">
  </picture>
</p>
<!-- INTERESTS:END -->

Open source made new things possible for more people.

## Mathematical research

[**24 research projects · 7 with generalizations · 8 with Lean formalization**](https://github.com/Aurantium-47/aurantium-mathematics)

**10 positive resolutions · 3 counterexamples.**

**[Howroyd’s 27-set conjecture](https://github.com/Aurantium-47/howroyd-27-conjecture)** · <sub>[Posed in 2018 · 8 years ago](https://oeis.org/A297557) · Extremal graph theory</sub>

**One known residue class → all three classes.** Completed the two remaining branches of the 2018 conjecture, then went beyond the count to classify **all 27 maximum independent sets**. The remaining-branch theorem is formalized in Lean 4.

<details>
<summary>Original sources & proof method</summary>

- **Original source:** Andrew Howroyd, [OEIS A297557 (2018)](https://oeis.org/A297557).
- **Prior work:** [John Machacek](https://arxiv.org/abs/2010.11112v2), *Procedia Computer Science* 195 (2021), proved the 3 ∣ d branch. Combining the two results completes the counting formula for d ≥ 9.
- **Method:** An exact weighted-cover certificate and a coordinate-reduction argument reduce the classification to three backgrounds with nine corner extensions each.
- **Further results & materials:** Explicit classification of all 27 sets, beyond the conjectured count.
- **Verification:** Lean 4 proof of the full d ≥ 10, 3 ∤ d statement; 89 rational certificate entries.

</details>

**[Lecture Hall polynomiality and algebraic extensions](https://github.com/Aurantium-47/lecture-hall-polynomiality)** · <sub>[Posed in 2018 · 8 years ago](https://arxiv.org/abs/1809.01377) · Algebraic combinatorics / Commutative algebra</sub>

**Checks through length 12 → a proof for every length.** Extended the result into a family of coefficient formulas, SAGBI-basis and toric-degeneration theorems. The polynomiality and signed-path core is formalized in Lean.

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

**[Peak polynomials: the last real root](https://github.com/Aurantium-47/peak-polynomial-last-real-root)** · <sub>[Experimental Mathematics · 2016 journal version · 10 years ago](https://arxiv.org/abs/1410.8506v2) · Real roots</sub>

**Partial interval results → the full last-real-root statement.** An integral sign argument covers the missing noninteger interval, without bounds on peak count or spacing.

- **Original source:** Sara Billey, Matthew Fahrbach and Alan Talmage, [*Experimental Mathematics* 25(2), 165–175 (2016)](https://arxiv.org/abs/1410.8506v2); preprint first posted in 2014.
- **Prior work:** Billey–Fahrbach–Talmage supplied the recurrence and symmetry identities. [Li’s coefficient theorem](https://doi.org/10.5281/zenodo.22832569) already implies right-side positivity and several local sign properties; the additional argument covers the remaining noninteger interval.
- **Method:** A self-contained integral representation and sign analysis across the full interval beyond the penultimate peak.
- **Further results & materials:** Signs on both sides of the largest peak, its simplicity, and the singleton case are included; overlapping consequences of Li’s theorem are credited in the manuscript.
- **Verification:** All-parameter mathematical proof, with supplementary exact finite checks and a separately recorded small-case reproduction.

**[K₆ chains: a false 22-colour bound replaced by the sharp bound 23](https://github.com/Aurantium-47/k6-clique-chain-packing-coloring)** · <sub>[Conjecture posed in 2025](https://arxiv.org/abs/2511.12761) · Graph colouring</sub>

**A conjectured bound of 22 → the correct sharp bound of 23.** Refuted 22 with a **450-vertex** graph, then established the uniform bound for the **entire family**, backed by a **16.6-million-record** exact certificate.

- **Original source:** Furmańczyk, Gözüpek and Özkan, [Packing coloring of graphs with long paths (2025)](https://arxiv.org/abs/2511.12761), Conjecture 2.
- **Prior work:** The proposed common upper bound was 22 for the path-aligned K₆ clique chains.
- **Method:** A finite-state scheduling relaxation and decreasing-rank certificate exclude 22; an explicit periodic colouring supplies the upper bound 23.
- **Further results & materials:** Sharp uniform bound 23 for the full chain family and exact value 23 for every t ≥ 75. The minimum counterexample length and all shorter-chain exact values are not determined.
- **Verification:** A 16,646,562-record exact certificate with Python and C++ checkers. This is computational certificate verification, not a Lean formalization.

</details>

**[More mathematical work · 20 projects](https://github.com/Aurantium-47/aurantium-mathematics/blob/main/README.en.md#all-projects)**

## NLP & information retrieval

**Dense & Hybrid Retrieval · Knowledge Graphs · Retrieval-Augmented QA**

Research interests in retrieval and question answering over text–graph knowledge bases, focusing on **complementary retrieval channels, relation-aware entity disambiguation, and coordination between retrieval and reranking**.

Current work uses **STaRK-MAG** to explore how entity text, attributes and graph relations can jointly guide candidate selection under both semantic and relational constraints.

## Research tools

**[Research-to-Decision](https://github.com/Aurantium-47/Research-to-Decision)** — an agent workflow that turns research into a choice. Built on BMad Deep Recon and OpenInquire’s cross-platform reading, it clarifies requirements, compares evidence and trade-offs, and explains when to choose an alternative.

## Contributions

Selected merged contributions:

<p><a href="https://github.com/huggingface/sentence-transformers/stargazers"><img alt="Sentence Transformers upstream stars: 19,212" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/huggingface-sentence-transformers-19212.svg" width="180" align="right"></a><strong><a href="https://github.com/huggingface/sentence-transformers">Sentence Transformers</a></strong> · <sub><a href="https://github.com/huggingface/sentence-transformers/pull/4251">#4251</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4262">#4262</a></sub><br>Sentence embeddings and semantic search. Fixed rescoring for reused floating-point USearch indexes to preserve retrieval ranking. Fixed hard-negative mining silently ignoring a supplied CrossEncoder without score filters, so candidate ordering and exported scores use the requested scorer rather than the bi-encoder, including for distillation targets.</p>

<p><a href="https://github.com/morluto/rea/stargazers"><img alt="REA upstream stars: 288k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/morluto-rea-287879.svg" width="180" align="right"></a><strong><a href="https://github.com/morluto/rea">REA</a></strong> · <sub><a href="https://github.com/morluto/rea/pull/2422">#2422</a> · <a href="https://github.com/morluto/rea/pull/2448">#2448</a> · <a href="https://github.com/morluto/rea/pull/2429">#2429</a></sub><br>An agent-driven reverse-engineering platform. Contributed improvements to cross-platform compatibility and binary diagnostics.</p>

<p><a href="https://github.com/vinta/awesome-python/stargazers"><img alt="awesome-python upstream stars: 328,335" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/vinta-awesome-python-328335.svg" width="180" align="right"></a><strong><a href="https://github.com/vinta/awesome-python">awesome-python</a></strong> · <sub><a href="https://github.com/vinta/awesome-python/pull/3376">#3376</a></sub><br>A curated collection of Python resources. Contributed improvements to website accessibility and navigation.</p>

<p><a href="https://github.com/github/spec-kit/stargazers"><img alt="Spec Kit upstream stars: 142k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/github-spec-kit-141541.svg" width="180" align="right"></a><strong><a href="https://github.com/github/spec-kit">Spec Kit</a></strong> · <sub><a href="https://github.com/github/spec-kit/pull/4956">#4956</a></sub><br>GitHub’s spec-driven development toolkit. Contributed improvements to Windows workflow reliability.</p>

<p><a href="https://github.com/ipython/ipython/stargazers"><img alt="IPython upstream stars: 16,794" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/ipython-ipython-16794.svg" width="180" align="right"></a><strong><a href="https://github.com/ipython/ipython">IPython</a></strong> · <sub><a href="https://github.com/ipython/ipython/pull/15435">#15435</a></sub><br>The interactive Python shell used in Jupyter notebooks. Fixed <code>FileLinks(Path(...))</code> to accept pathlib directory paths.</p>

<p><a href="https://github.com/ohmyzsh/ohmyzsh/stargazers"><img alt="Oh My Zsh upstream stars: 190,112" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/ohmyzsh-ohmyzsh-190112.svg" width="180" align="right"></a><strong><a href="https://github.com/ohmyzsh/ohmyzsh">Oh My Zsh</a></strong> · <sub><a href="https://github.com/ohmyzsh/ohmyzsh/pull/14184">#14184</a></sub><br>A framework for managing Zsh configuration. Clarified uv initialization aliases and parent-workspace membership.</p>

<p><a href="https://github.com/koreader/koreader/stargazers"><img alt="KOReader upstream stars: 30.4k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/koreader-koreader-30358.svg" width="180" align="right"></a><strong><a href="https://github.com/koreader/koreader">KOReader</a></strong> · <sub><a href="https://github.com/koreader/koreader/pull/16220">#16220</a></sub><br>A document reader for e-ink devices and Android. Contributed improvements to annotation workflows.</p>

<p><a href="https://github.com/json5/json5/stargazers"><img alt="JSON5 upstream stars: 7.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/json5-json5-7172.svg" width="180" align="right"></a><strong><a href="https://github.com/json5/json5">JSON5</a></strong> · <sub><a href="https://github.com/json5/json5/pull/371">#371</a></sub><br>The JavaScript implementation of JSON5. Contributed improvements to serialization correctness.</p>

<p><a href="https://github.com/pydata/xarray/stargazers"><img alt="Xarray upstream stars: 4,211" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/pydata-xarray-4211.svg" width="180" align="right"></a><strong><a href="https://github.com/pydata/xarray">Xarray</a></strong> · <sub><a href="https://github.com/pydata/xarray/pull/11711">#11711</a></sub><br>Labeled arrays for scientific Python. Contributed improvements to documentation workflow reliability.</p>

<p><a href="https://github.com/pydicom/pydicom/stargazers"><img alt="pydicom upstream stars: 2.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/pydicom-pydicom-2225.svg" width="180" align="right"></a><strong><a href="https://github.com/pydicom/pydicom">pydicom</a></strong> · <sub><a href="https://github.com/pydicom/pydicom/pull/2388">#2388</a></sub><br>A Python library for DICOM medical imaging. Contributed improvements to data conversion and interoperability.</p>

<p><a href="https://github.com/nilbuild/developer-roadmap/stargazers"><img alt="Developer Roadmap upstream stars: 370k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/nilbuild-developer-roadmap-369547.svg" width="180" align="right"></a><strong><a href="https://github.com/nilbuild/developer-roadmap">Developer Roadmap</a></strong> · <sub><a href="https://github.com/nilbuild/developer-roadmap/pull/10451">#10451</a></sub><br>Developer roadmaps and technical guides. Contributed to the Python learning content.</p>

<p><a href="https://github.com/EbookFoundation/free-programming-books/stargazers"><img alt="Free Programming Books upstream stars: 399k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/EbookFoundation-free-programming-books-399196.svg" width="180" align="right"></a><strong><a href="https://github.com/EbookFoundation/free-programming-books">Free Programming Books</a></strong> · <sub><a href="https://github.com/EbookFoundation/free-programming-books/pull/13533">#13533</a></sub><br>A multilingual collection of free programming resources. Improved the contributor documentation.</p>


<sub>Star snapshots · 2026-10-17–23</sub>

## Selected activity

<sub>AI-assisted updates</sub>

<!-- ACTIVITY:START -->
- <sub>2026-10-26</sub> · [Sentence Transformers #4262](https://github.com/huggingface/sentence-transformers/pull/4262) — Tom Aarsen merged the fix as-is, then simplified its regression tests in [#4277](https://github.com/huggingface/sentence-transformers/pull/4277).
- <sub>2026-10-22</sub> · [Sentence Transformers #4251 — Tom Aarsen clarified precision handling and expanded the regression tests before merging the fix.](https://github.com/huggingface/sentence-transformers/pull/4251#issuecomment-6342707340)
- <sub>2026-10-21</sub> · [IPython #15435 — merged by Carreau.](https://github.com/ipython/ipython/pull/15435)
- <sub>2026-10-20</sub> · [Oh My Zsh #14184 — merged by robbyrussell.](https://github.com/ohmyzsh/ohmyzsh/pull/14184)
- <sub>2026-10-18</sub> · [Xarray #11711 — follow-up thanks from VeckoTheGecko after merge.](https://github.com/pydata/xarray/pull/11711#issuecomment-6249123066)
- <sub>2026-10-17</sub> · [awesome-python #3376 — approved and merged by vinta.](https://github.com/vinta/awesome-python/pull/3376)
- <sub>2026-10-17</sub> · [Xarray #11711 — approved and merged by headtr1ck.](https://github.com/pydata/xarray/pull/11711)
- <sub>2026-10-17</sub> · [Published Aurantium · Mathematics: 24 research projects, including 8 with Lean formalization.](https://github.com/Aurantium-47/aurantium-mathematics)
- <sub>2026-10-15</sub> · [JSON5 #371 — merged.](https://github.com/json5/json5/pull/371)
- <sub>2026-10-14</sub> · [Spec Kit #4956 — merged.](https://github.com/github/spec-kit/pull/4956)
- <sub>2026-10-13</sub> · [REA #2448 — merged; CassieFox23 independently reproduced and verified the fix on Linux.](https://github.com/morluto/rea/pull/2448#issuecomment-6138368698)
- <sub>2026-10-13</sub> · [REA #2422 — merged; N0zoM1z0’s follow-up extension #2635 also merged upstream.](https://github.com/morluto/rea/pull/2635)
- <sub>2026-10-12</sub> · [REA #2227](https://github.com/morluto/rea/pull/2227#issuecomment-6127162628) — maintainer morluto called the contribution “Brilliant”; an [upstream implementation](https://github.com/morluto/rea/commit/c9fed50691ae014890e91a72534773d2fb58ce44) followed.

<details>
<summary>More activity</summary>

- <sub>2026-10-15</sub> · [Developer Roadmap #10451 — merged.](https://github.com/nilbuild/developer-roadmap/pull/10451)
- <sub>2026-10-15</sub> · [Free Programming Books #13533 — merged.](https://github.com/EbookFoundation/free-programming-books/pull/13533)
- <sub>2026-10-15</sub> · [Published the Lean supplement for Hardinian asymptotics at r = 2.](https://github.com/Aurantium-47/hardinian-array-asymptotics/blob/477fcff33df19d5f752f9748d8596b31da15c81b/FORMALIZATION.md)
- <sub>2026-10-14</sub> · [KOReader #16220 — merged.](https://github.com/koreader/koreader/pull/16220)
- <sub>2026-10-14</sub> · [REA #3224 — Kotlin source inventory support adopted upstream with co-author credit.](https://github.com/morluto/rea/commit/03ffb2c13dc6d3e8e0cc8cec70efb2a220c38607)

</details>
<!-- ACTIVITY:END -->

[All projects](https://github.com/Aurantium-47?tab=repositories) · [Merged contributions](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)
