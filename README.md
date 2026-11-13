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
    <source media="(max-width: 640px)" srcset="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/e13d1db8ba8f6d2d3729db5f9236d573da1c1487/assets/interests/records-mobile.svg?v=20261113">
    <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/e13d1db8ba8f6d2d3729db5f9236d573da1c1487/assets/interests/records.svg?v=20261113" width="920" alt="">
  </picture>
</p>
<p>
  <picture>
    <source media="(max-width: 640px)" srcset="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/interests/words-mobile.svg?v=20261104">
    <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/interests/words.svg?v=20261104" width="920" alt="">
  </picture>
</p>
<!-- INTERESTS:END -->

Open source made new things possible for more people.

## Mathematical research

[**Research index · Proofs, counterexamples & extensions**](https://github.com/Aurantium-47/aurantium-mathematics)

**[Two negative answers from the AIM problem list](https://github.com/Aurantium-47/aim23-czds-counterexample)** · <sub>2004 / 2007 · Polynomial zeros</sub>

Questions dating back two decades ask whether polynomial transformations preserve properties of their zeros. **AIM 23: a counterexample increases nonreal zeros from 4 to 6. [AIM 34](https://github.com/Aurantium-47/aim34-multiplier-sequence): from asking whether sufficiently large integer parameters work to ruling out every positive real parameter.** Both include Lean sources, historical replay records and independent AI review. [Background: Craven–Csordas](https://math.hawaii.edu/~tom/mathfiles/czdssurvey.pdf) · [Chasse's dissertation](https://math.hawaii.edu/home/talks/thesis.pdf)

**[BRW graph polynomials: progress on a 1994 question](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/dc6d35ba53c6a41064bc9982cb524b05b74dc2ff/extensions/2026-11-02-uniform-cycle-substitution)** · <sub>[Canadian Journal of Mathematics · 1994](https://doi.org/10.4153/CJM-1994-002-3) · Graph theory</sub>

When graphs are assembled, which polynomial-zero properties survive? **A uniform result extends particular cycle lengths to every cycle length:** replacing one cycle vertex with a graph satisfying the stated condition preserves the relevant real-rootedness property and permits further attachment along an edge. This covers a whole construction family, as a partial result toward the general conjecture.

**[Stack-sorting: a uniform proof draft for permutation counts](https://github.com/Aurantium-47/aurantium-mathematics/tree/d6c4747db93eb8c7acfcb792215452cc1f2249dc/research/stack-sorting-fibre-log-concavity)** · <sub>2026 · Combinatorics</sub>

A proof draft explaining a stronger form of log-concavity in counts of permutations sharing a sorting output. **[This draft's Git commit: November 4](https://github.com/Aurantium-47/aurantium-mathematics/commit/d6c4747db93eb8c7acfcb792215452cc1f2249dc)**; the corresponding conclusion also appears as **[Theorem 1.1 in Colin Defant's November 10 arXiv preprint](https://arxiv.org/html/2611.13479v1#S1.Thmtheorem1)**. The proof and literature comparison are public.

<sub>AI-assisted research drafts with documented checks, not human-peer-reviewed results. References and dates provide research context, not author endorsement or a priority determination.</sub>

**[More mathematical work · Full index & verification materials](https://github.com/Aurantium-47/aurantium-mathematics#全部项目)**

## NLP & information retrieval

**Dense & Hybrid Retrieval · Knowledge Graphs · Retrieval-Augmented QA**

Research interests in retrieval and question answering over text–graph knowledge bases, focusing on **complementary retrieval channels, relation-aware entity disambiguation, and coordination between retrieval and reranking**.

Current work uses **STaRK-MAG** to explore how entity text, attributes and graph relations can jointly guide candidate selection under both semantic and relational constraints.

## Research tools

**[Research-to-Decision](https://github.com/Aurantium-47/Research-to-Decision)** — an agent workflow that turns research into a choice. Built on BMad Deep Recon and OpenInquire’s cross-platform reading, it clarifies requirements, compares evidence and trade-offs, and explains when to choose an alternative.

## Contributions

**Draft engineering · [Sentence Transformers: synchronized per-dataset batches #4317](https://github.com/huggingface/sentence-transformers/pull/4317)**

Align tasks across ranks while allowing task-specific per-rank batch sizes; preserve the training schedule across checkpoint resume. **18 real two-rank CPU/Gloo Trainer runs** (6 configurations × full / prefix / resume) matched native-objective checks and continuous-versus-resumed trajectories in deterministic fixtures.

**Not merged:** depends on the unmerged [Accelerate draft #4491](https://github.com/huggingface/accelerate/pull/4491); upstream CI awaits maintainer approval.

<details>
<summary>Scheduling diagram, fixed evidence & limits</summary>

![Synchronized task scheduling: group same-task rank slots before sharding, retaining task-specific per-rank batch sizes](https://raw.githubusercontent.com/Aurantium-47/sentence-transformers/f4d3da733194cf46e5cbd8d6014df94f558e769a/research/synchronized-dataset-batches/assets/synchronized-task-scheduling.svg)

[Fixed reproduction evidence · 2 November 2026](https://github.com/Aurantium-47/sentence-transformers/tree/f4d3da733194cf46e5cbd8d6014df94f558e769a/research/synchronized-dataset-batches) includes rank traces, source hashes and JSON-only oracle replay. The 18 jobs were run in an independent validation environment, not upstream CI. The diagram illustrates scheduling, not measured throughput. Scope: fixed two-rank CPU/Gloo, ordinary map-style sampling and deterministic resume fixtures; no GPU/NCCL, arbitrary stochastic-resume or performance claim. AI-assisted implementation, tests and evidence review.

</details>

Selected merged contributions:

<p><strong><a href="https://github.com/HKUDS/LightRAG">LightRAG</a></strong> · <sub><a href="https://github.com/HKUDS/LightRAG/pull/4368">#4368</a> · merged</sub><br>Identified and fixed a PostgreSQL legacy-vector migration defect that treated partial copies as complete, contributing a reproducer, server-side copying and regression tests. The maintainer built on this with resumable segments and cross-instance fencing, and <a href="https://github.com/HKUDS/LightRAG/pull/4368#issuecomment-6828325439">verified 20,000 256-dimensional vectors row by row and duplicate-free migration of 30,000 rows across two instances</a>.</p>

<p><strong><a href="https://github.com/huggingface/tokenizers">Hugging Face Tokenizers</a></strong> · <sub><a href="https://github.com/huggingface/tokenizers/pull/2567">#2567</a></sub> · Fixed Kimi pretokenization for overlapping Han, numeric and punctuation categories, preserving regex split semantics across byte-block boundaries; added parity and JSON/BPE encoding regressions.</p>

<p><a href="https://github.com/huggingface/sentence-transformers/stargazers"><img alt="Sentence Transformers upstream stars: 19,212" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/huggingface-sentence-transformers-19212.svg" width="180" align="right"></a><strong><a href="https://github.com/huggingface/sentence-transformers">Sentence Transformers</a></strong> · <sub><a href="https://github.com/huggingface/sentence-transformers/pull/4251">#4251</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4262">#4262</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4264">#4264</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4284">#4284</a></sub><br>Sentence embeddings and semantic search. Fixed rescoring for reused floating-point USearch indexes to preserve retrieval ranking. Also merged: honor CrossEncoder rescoring when mining negatives without score filters (#4262); handle empty candidate lists in reranking evaluation (#4264); exclude self-pairs when GIST guide scores tie (#4284).</p>

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
- <sub>2026-11-12</sub> · [Tokenizers #2567 — approved by SBrandeis and merged; corrected Kimi pretokenization for overlapping Han categories.](https://github.com/huggingface/tokenizers/pull/2567)
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

- <sub>2026-10-31</sub> · [claude-trading-skills #596](https://github.com/tradermonty/claude-trading-skills/pull/596) — merged a fix aligning reported risk with the selected position-sizing method; maintainer tradermonty’s [follow-up #602](https://github.com/tradermonty/claude-trading-skills/pull/602) added stop validation, Decimal risk rounding and documentation.
- <sub>2026-10-15</sub> · [Developer Roadmap #10451 — merged.](https://github.com/nilbuild/developer-roadmap/pull/10451)
- <sub>2026-10-15</sub> · [Free Programming Books #13533 — merged.](https://github.com/EbookFoundation/free-programming-books/pull/13533)
- <sub>2026-10-15</sub> · [Published the Lean supplement for Hardinian asymptotics at r = 2.](https://github.com/Aurantium-47/hardinian-array-asymptotics/blob/477fcff33df19d5f752f9748d8596b31da15c81b/FORMALIZATION.md)
- <sub>2026-10-14</sub> · [KOReader #16220 — merged.](https://github.com/koreader/koreader/pull/16220)
- <sub>2026-10-14</sub> · [REA #3224 — Kotlin source inventory support adopted upstream with co-author credit.](https://github.com/morluto/rea/commit/03ffb2c13dc6d3e8e0cc8cec70efb2a220c38607)

</details>
<!-- ACTIVITY:END -->

[All projects](https://github.com/Aurantium-47?tab=repositories) · [Merged contributions](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)
