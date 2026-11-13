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

A proof draft explaining a stronger form of log-concavity in counts of permutations sharing a sorting output. **[This draft's Git commit: November 4](https://github.com/Aurantium-47/aurantium-mathematics/commit/d6c4747db93eb8c7acfcb792215452cc1f2249dc)**. The proof and a comparison with related work by Colin Defant<sup>*</sup> are public.

> <sub>* <a href="https://sites.google.com/view/colin-defant/home">Colin Defant, Harvard postdoctoral fellow</a>; <a href="https://arxiv.org/html/2611.13479v1#S1.Thmtheorem1">Theorem 1.1 of his November 10 arXiv preprint</a> gives the corresponding conclusion.</sub>

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

<p><a href="https://github.com/huggingface/tokenizers/stargazers"><img alt="huggingface/tokenizers stars" src="https://img.shields.io/github/stars/huggingface/tokenizers?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/huggingface/tokenizers">Hugging Face Tokenizers</a></strong> · <sub><a href="https://github.com/huggingface/tokenizers/pull/2567">#2567</a> · merged</sub><br><sub>Rust · Tokenization</sub><br>Fixed <strong>Kimi-K2</strong> tokenization of special Han characters, restoring encoding consistency. The maintainer-reported regression was reviewed and merged.</p>

<p><a href="https://github.com/HKUDS/LightRAG/stargazers"><img alt="HKUDS/LightRAG stars" src="https://img.shields.io/github/stars/HKUDS/LightRAG?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/HKUDS/LightRAG">LightRAG</a></strong> · <sub><a href="https://github.com/HKUDS/LightRAG/pull/4368">#4368</a> · merged</sub><br><sub>Python · PostgreSQL · pgvector</sub><br>Fixed missing data after interrupted vector migrations. The maintainer extended the fix and <a href="https://github.com/HKUDS/LightRAG/pull/4368#issuecomment-6828325439">verified duplicate-free migration of 30,000 vectors across two instances</a>.</p>

<p><a href="https://github.com/huggingface/sentence-transformers/stargazers"><img alt="huggingface/sentence-transformers stars" src="https://img.shields.io/github/stars/huggingface/sentence-transformers?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/huggingface/sentence-transformers">Sentence Transformers</a></strong> · <sub><a href="https://github.com/huggingface/sentence-transformers/pull/4251">#4251</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4262">#4262</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4264">#4264</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4284">#4284</a></sub><br><sub>Python · PyTorch · Semantic retrieval</sub><br><strong>4 merged fixes</strong>: corrected retrieval rankings and training negatives, restored reranker scoring, and kept empty results from aborting evaluation.</p>

<p><a href="https://github.com/morluto/rea/stargazers"><img alt="morluto/rea stars" src="https://img.shields.io/github/stars/morluto/rea?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/morluto/rea">REA</a></strong> · <sub><a href="https://github.com/morluto/rea/pull/2422">#2422</a> · <a href="https://github.com/morluto/rea/pull/2448">#2448</a> · <a href="https://github.com/morluto/rea/pull/2429">#2429</a></sub><br><sub>TypeScript · Node.js · Reverse engineering</sub><br><strong>3 merged contributions</strong>: cross-platform path matching, binary diagnostics and installation guidance. The diagnostic fix was independently verified on Linux.</p>

<p><a href="https://github.com/github/spec-kit/stargazers"><img alt="github/spec-kit stars" src="https://img.shields.io/github/stars/github/spec-kit?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/github/spec-kit">Spec Kit</a></strong> · <sub><a href="https://github.com/github/spec-kit/pull/4956">#4956</a></sub><br><sub>PowerShell · Python · Spec-driven development</sub><br>Prevented plan files from being overwritten on Windows paths containing special characters. Verified on two PowerShell generations and merged.</p>

**More merged contributions**

- **[Haystack](https://github.com/deepset-ai/haystack)** [![Stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=flat&color=gold)](https://github.com/deepset-ai/haystack/stargazers) · [#13422](https://github.com/deepset-ai/haystack/pull/13422) · RAG data preprocessing
- **[spdlog](https://github.com/gabime/spdlog)** [![Stars](https://img.shields.io/github/stars/gabime/spdlog?style=flat&color=gold)](https://github.com/gabime/spdlog/stargazers) · [#3683](https://github.com/gabime/spdlog/pull/3683) · Cross-platform logging reliability
- **[Resty](https://github.com/go-resty/resty)** [![Stars](https://img.shields.io/github/stars/go-resty/resty?style=flat&color=gold)](https://github.com/go-resty/resty/stargazers) · [#1250](https://github.com/go-resty/resty/pull/1250) · HTTP client tooling
- **[GitHub gitignore](https://github.com/github/gitignore)** [![Stars](https://img.shields.io/github/stars/github/gitignore?style=flat&color=gold)](https://github.com/github/gitignore/stargazers) · [#4931](https://github.com/github/gitignore/pull/4931) · Development environments & version control
- **[Claude Trading Skills](https://github.com/tradermonty/claude-trading-skills)** [![Stars](https://img.shields.io/github/stars/tradermonty/claude-trading-skills?style=flat&color=gold)](https://github.com/tradermonty/claude-trading-skills/stargazers) · [#596](https://github.com/tradermonty/claude-trading-skills/pull/596) · Trading risk & position management
- **[awesome-python](https://github.com/vinta/awesome-python)** [![Stars](https://img.shields.io/github/stars/vinta/awesome-python?style=flat&color=gold)](https://github.com/vinta/awesome-python/stargazers) · [#3376](https://github.com/vinta/awesome-python/pull/3376) · Web accessibility & navigation
- **[IPython](https://github.com/ipython/ipython)** [![Stars](https://img.shields.io/github/stars/ipython/ipython?style=flat&color=gold)](https://github.com/ipython/ipython/stargazers) · [#15435](https://github.com/ipython/ipython/pull/15435) · Interactive Python file workflows
- **[Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh)** [![Stars](https://img.shields.io/github/stars/ohmyzsh/ohmyzsh?style=flat&color=gold)](https://github.com/ohmyzsh/ohmyzsh/stargazers) · [#14184](https://github.com/ohmyzsh/ohmyzsh/pull/14184) · Shell workflow documentation
- **[KOReader](https://github.com/koreader/koreader)** [![Stars](https://img.shields.io/github/stars/koreader/koreader?style=flat&color=gold)](https://github.com/koreader/koreader/stargazers) · [#16220](https://github.com/koreader/koreader/pull/16220) · Reading & annotation workflows
- **[JSON5](https://github.com/json5/json5)** [![Stars](https://img.shields.io/github/stars/json5/json5?style=flat&color=gold)](https://github.com/json5/json5/stargazers) · [#371](https://github.com/json5/json5/pull/371) · Data serialization
- **[Xarray](https://github.com/pydata/xarray)** [![Stars](https://img.shields.io/github/stars/pydata/xarray?style=flat&color=gold)](https://github.com/pydata/xarray/stargazers) · [#11711](https://github.com/pydata/xarray/pull/11711) · Documentation workflow reliability
- **[pydicom](https://github.com/pydicom/pydicom)** [![Stars](https://img.shields.io/github/stars/pydicom/pydicom?style=flat&color=gold)](https://github.com/pydicom/pydicom/stargazers) · [#2388](https://github.com/pydicom/pydicom/pull/2388) · Data conversion & interoperability
- **[Developer Roadmap](https://github.com/nilbuild/developer-roadmap)** [![Stars](https://img.shields.io/github/stars/nilbuild/developer-roadmap?style=flat&color=gold)](https://github.com/nilbuild/developer-roadmap/stargazers) · [#10451](https://github.com/nilbuild/developer-roadmap/pull/10451) · Python learning resources
- **[Free Programming Books](https://github.com/EbookFoundation/free-programming-books)** [![Stars](https://img.shields.io/github/stars/EbookFoundation/free-programming-books?style=flat&color=gold)](https://github.com/EbookFoundation/free-programming-books/stargazers) · [#13533](https://github.com/EbookFoundation/free-programming-books/pull/13533) · Open-source collaboration docs

[All projects](https://github.com/Aurantium-47?tab=repositories) · [Merged contributions](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)
