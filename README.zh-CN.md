# Aurantium

<sub><a href="https://github.com/Aurantium-47">English</a> · <b>简体中文</b></sub>

**AI for Math · NLP**

探索 AI 在推理与软件工程中的能力边界。

兴趣：**量化策略 · 加密市场**

[数学研究](https://github.com/Aurantium-47/aurantium-mathematics) · [开源贡献](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)

<p><img alt="Python" src="https://img.shields.io/badge/Python-e9edf2?style=flat-square&amp;logo=python&amp;logoColor=57606a"> <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-e9edf2?style=flat-square&amp;logo=pytorch&amp;logoColor=57606a"> <img alt="Transformers" src="https://img.shields.io/badge/Transformers-e9edf2?style=flat-square&amp;logo=huggingface&amp;logoColor=57606a"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-e9edf2?style=flat-square&amp;logo=numpy&amp;logoColor=57606a"> <img alt="Lean 4" src="https://img.shields.io/badge/Lean%204-e9edf2?style=flat-square"> <img alt="mathlib" src="https://img.shields.io/badge/mathlib-e9edf2?style=flat-square"> <img alt="SymPy" src="https://img.shields.io/badge/SymPy-e9edf2?style=flat-square&amp;logo=sympy&amp;logoColor=57606a"> <img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-e9edf2?style=flat-square&amp;logo=latex&amp;logoColor=57606a"> <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-e9edf2?style=flat-square&amp;logo=cplusplus&amp;logoColor=57606a"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-e9edf2?style=flat-square&amp;logo=typescript&amp;logoColor=57606a"> <img alt="Node.js" src="https://img.shields.io/badge/Node.js-e9edf2?style=flat-square&amp;logo=nodedotjs&amp;logoColor=57606a"> <img alt="Git" src="https://img.shields.io/badge/Git-e9edf2?style=flat-square&amp;logo=git&amp;logoColor=57606a"></p>

## 数学研究

[**24 组研究成果 · 7 组含推广 · 8 组含 Lean 形式化**](https://github.com/Aurantium-47/aurantium-mathematics)

**10 项原题的肯定解答 · 3 项反例。**

**[Howroyd 27 集猜想](https://github.com/Aurantium-47/howroyd-27-conjecture)** · <sub>[2018 年提出 · 距今 8 年](https://oeis.org/A297557) · 极值图论</sub>

**从一个已知分支到全部三个余类。** 补齐 2018 年猜想的剩余两类，完成计数公式，并进一步给出 **全部 27 个最大独立集的分类**；剩余分支定理已用 Lean 4 形式化。

<details>
<summary>原文出处与证明方法</summary>

- **原问题出处:** Andrew Howroyd，[OEIS A297557（2018）](https://oeis.org/A297557)。
- **已有进展:** [John Machacek](https://arxiv.org/abs/2010.11112v2) 在 *Procedia Computer Science* 195（2021）证明 3 ∣ d 分支。两项结果合起来补全 d ≥ 9 的计数公式。
- **证明方法:** 以精确加权覆盖证书和坐标归约，将分类化为 3 种背景、每种 9 个角部延拓。
- **补充结果与材料:** 从猜想要求的计数，推进到全部 27 个最大独立集的显式分类。
- **验证方式:** Lean 4 覆盖完整的 d ≥ 10、3 ∤ d 命题；另提供 89 项有理数证书。

</details>

**[Lecture Hall：从有限验证到任意长度的证明](https://github.com/Aurantium-47/lecture-hall-polynomiality)** · <sub>[2018 年提出 · 距今 8 年](https://arxiv.org/abs/1809.01377) · 代数组合 / 交换代数</sub>

**从长度 12 的计算验证到任意长度的证明。** 进一步发展出系数公式、SAGBI 基与 toric 退化等一组结构定理，形成原题证明之外的系列成果；多项式性与路径识别核心已用 Lean 形式化。

<details>
<summary>原文出处与证明方法</summary>

- **原问题出处:** Lukas Katthän，[The Lecture Hall Cone as a toric deformation（2018）](https://arxiv.org/abs/1809.01377)，为大阪格点多面体研讨会准备的论文。
- **已有进展:** 原文提出多项式性与代数结构猜想，并验证长度不超过 12 的情形。Flajolet 的连分数理论与 Sokal 的系统论述提供已有的经典工具。
- **证明方法:** 以带符号 Dyck 路径识别、Toeplitz–Hankel 恒等式和原递推，证明全下标多项式性。
- **补充结果与材料:** 给出组合系数公式、精确单项式计数、最小单首 SAGBI 基、Hilbert 基对应，以及对任意域成立的平坦 toric 退化；使用文稿已披露的方阵子式解释。
- **验证方式:** Lean 覆盖真正有理函数序列的多项式性与带符号路径核心；SAGBI 与退化推广以文字证明给出。

</details>

<details>
<summary>另外两项：10 年前的峰多项式猜想 · K₆ 链的全族锐界</summary>

**[峰多项式的最后实根](https://github.com/Aurantium-47/peak-polynomial-last-real-root)** · <sub>[Experimental Mathematics · 2016 年期刊版 · 距今 10 年](https://arxiv.org/abs/1410.8506v2) · 多项式实根</sub>

**从局部区间结论到完整的最后实根结论。** 补足 2016 年期刊猜想所需的非整数区间论证，不限制峰的数量与间隔；已有系数定理涵盖的结论保留原归属。

- **原问题出处:** Sara Billey、Matthew Fahrbach、Alan Talmage，[*Experimental Mathematics* 25(2), 165–175（2016）](https://arxiv.org/abs/1410.8506v2)；预印本首发于 2014 年。
- **已有进展:** Billey–Fahrbach–Talmage 给出递推与对称恒等式。[Li 的系数定理](https://doi.org/10.5281/zenodo.22832569) 已涵盖右侧正性和若干局部符号性质；本项补足剩余非整数区间的分析。
- **证明方法:** 通过自包含的积分表示与符号分析，覆盖倒数第二峰之后的整个区间。
- **补充结果与材料:** 同时给出最大峰两侧的符号、根的单性和单峰情形；与 Li 定理重叠的推论在文稿中注明归属。
- **验证方式:** 全参数数学证明；附精确有限检查及单独记录的小规模复现。

**[K₆ 链：否定 22 色猜想，并给出全族锐界 23](https://github.com/Aurantium-47/k6-clique-chain-packing-coloring)** · <sub>[2025 年提出](https://arxiv.org/abs/2511.12761) · 图着色</sub>

**从 22 色猜想到正确的全族锐界 23。** 以 **450 顶点**反例否定原上界，再给出 **整个家族** 的锐界定理，附 **1664 万余条**精确证书记录。

- **原问题出处:** Furmańczyk、Gözüpek、Özkan，[Packing coloring of graphs with long paths（2025）](https://arxiv.org/abs/2511.12761)，猜想 2。
- **已有进展:** 原文为沿路径连接的 K₆ 团链提出统一 22 色上界。
- **证明方法:** 以有限状态调度松弛和递减秩证书排除 22 色，再构造显式周期着色得到 23 色上界。
- **补充结果与材料:** 建立全族锐界 23，并证明所有 t ≥ 75 的精确值均为 23；尚未确定最短反例长度和所有较短链的精确值。
- **验证方式:** 16,646,562 条精确证书，由 Python 与 C++ 检查器核验；属于计算证书核验，并非 Lean 形式化。

</details>

**另有 [20 项研究与文献对照](https://github.com/Aurantium-47/aurantium-mathematics#全部项目)**，包含 Stern 正性、化学图极值、Hurwitz 实根性等。

<details>
<summary>成果分类</summary>

- **10** 项原题的肯定解答 · **3** 项以反例为主的结果 · **7** 项更大原问题的部分结果 · **3** 项构造或分类 · **1** 项同题文献对照。
- **7** 组包含后续推广，**8** 组包含 Lean 形式化；两项统计与上述分类可以重叠。参考目录共 **60** 条问题来源与相关文献。

</details>

## NLP 与信息检索

**Dense & Hybrid Retrieval · Knowledge Graphs · Retrieval-Augmented QA**

面向文本与关系混合知识库的检索与问答，关注如何联合语义表示、实体属性和图关系，改善复杂查询的候选召回与证据定位。当前围绕 **STaRK-MAG**，沿 HybGRAG 的文本—关系联合检索路线开展研究。

- **稠密与混合检索：** 查询—实体表示、实体属性编码、多路召回融合与路由。
- **图增强检索与问答：** 语义相似度与关系约束的结合、实体消歧，以及粗召回与重排序的协同。
- **检索评测：** Recall@K 与逐题误差分析，定位语义匹配、关系条件和证据覆盖之间的缺口。

## 开源贡献

**[9 条 PR 合并至 7 个上游项目](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)**，其中 **4 个项目超过 10 万 Stars**，包括 GitHub 官方的 Spec Kit。

贡献获[维护者致谢](https://github.com/morluto/rea/pull/2227#issuecomment-6127162628)，并有[后续工作接续、合并](https://github.com/morluto/rea/pull/2635)。

<p><a href="https://github.com/morluto/rea/stargazers"><img alt="REA upstream stars: 288k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/morluto-rea-287879.svg" width="180" align="right"></a><strong><a href="https://github.com/morluto/rea">REA</a></strong> · <sub>3 条 PR 已合并 · <a href="https://github.com/morluto/rea/pull/2422">#2422</a> · <a href="https://github.com/morluto/rea/pull/2448">#2448</a> · <a href="https://github.com/morluto/rea/pull/2429">#2429</a></sub><br>智能体逆向工程平台 · 跨平台兼容与二进制诊断。</p>

<p><a href="https://github.com/github/spec-kit/stargazers"><img alt="Spec Kit upstream stars: 142k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/github-spec-kit-141541.svg" width="180" align="right"></a><strong><a href="https://github.com/github/spec-kit">Spec Kit</a></strong> · <sub>1 条 PR 已合并 · <a href="https://github.com/github/spec-kit/pull/4956">#4956</a></sub><br>GitHub 官方规范驱动开发工具包 · Windows 工作流可靠性。</p>

<p><a href="https://github.com/koreader/koreader/stargazers"><img alt="KOReader upstream stars: 30.4k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/koreader-koreader-30358.svg" width="180" align="right"></a><strong><a href="https://github.com/koreader/koreader">KOReader</a></strong> · <sub>1 条 PR 已合并 · <a href="https://github.com/koreader/koreader/pull/16220">#16220</a></sub><br>电子墨水与 Android 阅读器 · 批注工作流。</p>

<p><a href="https://github.com/json5/json5/stargazers"><img alt="JSON5 upstream stars: 7.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/json5-json5-7172.svg" width="180" align="right"></a><strong><a href="https://github.com/json5/json5">JSON5</a></strong> · <sub>1 条 PR 已合并 · <a href="https://github.com/json5/json5/pull/371">#371</a></sub><br>JSON5 的 JavaScript 实现 · 序列化正确性。</p>

<p><a href="https://github.com/pydicom/pydicom/stargazers"><img alt="pydicom upstream stars: 2.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/pydicom-pydicom-2225.svg" width="180" align="right"></a><strong><a href="https://github.com/pydicom/pydicom">pydicom</a></strong> · <sub>1 条 PR 已合并 · <a href="https://github.com/pydicom/pydicom/pull/2388">#2388</a></sub><br>DICOM 医学影像库 · 数据转换与互操作性。</p>

<p><a href="https://github.com/nilbuild/developer-roadmap/stargazers"><img alt="Developer Roadmap upstream stars: 370k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/nilbuild-developer-roadmap-369547.svg" width="180" align="right"></a><strong><a href="https://github.com/nilbuild/developer-roadmap">Developer Roadmap</a></strong> · <sub>1 条 PR 已合并 · <a href="https://github.com/nilbuild/developer-roadmap/pull/10451">#10451</a></sub><br>开发者路线图与技术指南 · Python 学习内容。</p>

<p><a href="https://github.com/EbookFoundation/free-programming-books/stargazers"><img alt="Free Programming Books upstream stars: 399k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/EbookFoundation-free-programming-books-399196.svg" width="180" align="right"></a><strong><a href="https://github.com/EbookFoundation/free-programming-books">Free Programming Books</a></strong> · <sub>1 条 PR 已合并 · <a href="https://github.com/EbookFoundation/free-programming-books/pull/13533">#13533</a></sub><br>多语言编程资源库 · 贡献者文档。</p>


<sub>Stars 与 PR 合并状态核对于 2026-10-17。</sub>

## 动态精选

<sub>由我的 AI 助手维护 · 定期自动更新待启用</sub>

<!-- ACTIVITY:START -->
- <sub>2026-10-13</sub> · [REA #2422 已合并；N0zoM1z0 致谢并接续提交 #2635，后续工作也已合并。](https://github.com/morluto/rea/pull/2635)
- <sub>2026-10-13</sub> · [REA #2448 已合并；CassieFox23 发布验证报告并致谢。](https://github.com/morluto/rea/pull/2448#issuecomment-6138368698)
- <sub>2026-10-12</sub> · [REA #2227](https://github.com/morluto/rea/pull/2227#issuecomment-6127162628) 获维护者 morluto 致谢，随后有[上游实现](https://github.com/morluto/rea/commit/c9fed50691ae014890e91a72534773d2fb58ce44)跟进。
- <sub>2026-10-14</sub> · [Spec Kit #4956 已合并，并获 mnriem 致谢。](https://github.com/github/spec-kit/pull/4956#issuecomment-6169522572)
- <sub>2026-10-17</sub> · [发布 Aurantium · Mathematics，汇总 24 个数学研究项目，其中 8 项包含 Lean 形式化。](https://github.com/Aurantium-47/aurantium-mathematics)
- <sub>2026-10-15</sub> · [JSON5 #371 已合并。](https://github.com/json5/json5/pull/371)

<details>
<summary>更多动态</summary>

- <sub>2026-10-15</sub> · [Developer Roadmap #10451 已合并。](https://github.com/nilbuild/developer-roadmap/pull/10451)
- <sub>2026-10-15</sub> · [Free Programming Books #13533 已合并。](https://github.com/EbookFoundation/free-programming-books/pull/13533)
- <sub>2026-10-14</sub> · [KOReader #16220 已合并。](https://github.com/koreader/koreader/pull/16220)
- <sub>2026-10-15</sub> · [发布 Hardinian 渐近式 r = 2 的 Lean 补充证明。](https://github.com/Aurantium-47/hardinian-array-asymptotics/blob/477fcff33df19d5f752f9748d8596b31da15c81b/FORMALIZATION.md)

</details>
<!-- ACTIVITY:END -->

[全部项目](https://github.com/Aurantium-47?tab=repositories) · [已合并贡献](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)
