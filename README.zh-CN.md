<p align="center">
  <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/aurantium-amber-pulse.gif" alt="Aurantium — an animated ASCII orange in warm amber light" width="840">
</p>

# Aurantium🍊

<sub><a href="https://github.com/Aurantium-47">English</a> · <b>简体中文</b></sub>

**NLP · AI for Math · 加密市场**

[数学研究](https://github.com/Aurantium-47/aurantium-mathematics) · [开源贡献](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)

<p><img alt="Python" src="https://img.shields.io/badge/Python-e9edf2?style=flat-square&amp;logo=python&amp;logoColor=57606a"> <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-e9edf2?style=flat-square&amp;logo=pytorch&amp;logoColor=57606a"> <img alt="Transformers" src="https://img.shields.io/badge/Transformers-e9edf2?style=flat-square&amp;logo=huggingface&amp;logoColor=57606a"> <img alt="Lean 4 / mathlib" src="https://img.shields.io/badge/Lean%204%20%2F%20mathlib-e9edf2?style=flat-square"> <img alt="SymPy" src="https://img.shields.io/badge/SymPy-e9edf2?style=flat-square&amp;logo=sympy&amp;logoColor=57606a"> <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-e9edf2?style=flat-square&amp;logo=cplusplus&amp;logoColor=57606a"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-e9edf2?style=flat-square&amp;logo=typescript&amp;logoColor=57606a"></p>

<!-- INTERESTS:START -->
<p>
  <picture>
    <source media="(max-width: 640px)" srcset="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/f66fade9b3a78cbb0cde0b1588fad17ff55e3075/assets/interests/records-mobile-zh.svg?v=5">
    <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/f66fade9b3a78cbb0cde0b1588fad17ff55e3075/assets/interests/records-zh.svg?v=5" width="920" alt="唱片与票根">
  </picture>
</p>
<p>
  <picture>
    <source media="(max-width: 640px)" srcset="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/f26d83ce59e24bd7c9000ae94a74b64fddeb616e/assets/interests/words-mobile-zh.svg?v=5">
    <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/f26d83ce59e24bd7c9000ae94a74b64fddeb616e/assets/interests/words-zh.svg?v=5" width="920" alt="兴趣">
  </picture>
</p>
<!-- INTERESTS:END -->

开源，让更多人有了新的可能。

## 数学研究

[**24 组研究成果 · 7 组含推广 · 8 组含 Lean 形式化**](https://github.com/Aurantium-47/aurantium-mathematics)

**10 项原问题获肯定解答 · 3 项反例。**

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

**[Lecture Hall：多项式性与代数推广](https://github.com/Aurantium-47/lecture-hall-polynomiality)** · <sub>[2018 年提出 · 距今 8 年](https://arxiv.org/abs/1809.01377) · 代数组合 / 交换代数</sub>

**从长度 12 的计算验证到任意长度的证明。** 进一步得到系数公式、SAGBI 基与 toric 退化等结构定理；多项式性与路径识别核心已用 Lean 形式化。

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

**从局部区间结果到完整的最后实根结论。** 通过积分符号分析补足非整数区间的论证，不限制峰的数量与间隔。

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

**[更多数学工作 · 20 项](https://github.com/Aurantium-47/aurantium-mathematics#全部项目)**

## NLP 与信息检索

**Dense & Hybrid Retrieval · Knowledge Graphs · Retrieval-Augmented QA**

研究文本与图关系共同约束下的检索与问答，重点是**多路召回的互补、关系约束下的实体消歧，以及召回与重排的协同**。

当前以 **STaRK-MAG** 为主要场景，探索如何联合实体文本、属性和图关系，让候选选择同时满足语义与关系条件。

## 开源贡献

部分已合并的上游贡献：

<p><a href="https://github.com/morluto/rea/stargazers"><img alt="REA upstream stars: 288k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/morluto-rea-287879.svg" width="180" align="right"></a><strong><a href="https://github.com/morluto/rea">REA</a></strong> · <sub><a href="https://github.com/morluto/rea/pull/2422">#2422</a> · <a href="https://github.com/morluto/rea/pull/2448">#2448</a> · <a href="https://github.com/morluto/rea/pull/2429">#2429</a></sub><br>面向智能体的逆向工程平台。贡献涉及跨平台兼容性与二进制诊断。</p>

<p><a href="https://github.com/vinta/awesome-python/stargazers"><img alt="awesome-python upstream stars: 328,335" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/vinta-awesome-python-328335.svg" width="180" align="right"></a><strong><a href="https://github.com/vinta/awesome-python">awesome-python</a></strong> · <sub><a href="https://github.com/vinta/awesome-python/pull/3376">#3376</a></sub><br>Python 资源精选。贡献涉及网站无障碍与交互导航。</p>

<p><a href="https://github.com/github/spec-kit/stargazers"><img alt="Spec Kit upstream stars: 142k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/github-spec-kit-141541.svg" width="180" align="right"></a><strong><a href="https://github.com/github/spec-kit">Spec Kit</a></strong> · <sub><a href="https://github.com/github/spec-kit/pull/4956">#4956</a></sub><br>GitHub 官方规范驱动开发工具包。贡献涉及 Windows 工作流可靠性。</p>

<p><a href="https://github.com/koreader/koreader/stargazers"><img alt="KOReader upstream stars: 30.4k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/koreader-koreader-30358.svg" width="180" align="right"></a><strong><a href="https://github.com/koreader/koreader">KOReader</a></strong> · <sub><a href="https://github.com/koreader/koreader/pull/16220">#16220</a></sub><br>面向电子墨水设备与 Android 的文档阅读器。贡献涉及批注工作流。</p>

<p><a href="https://github.com/json5/json5/stargazers"><img alt="JSON5 upstream stars: 7.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/json5-json5-7172.svg" width="180" align="right"></a><strong><a href="https://github.com/json5/json5">JSON5</a></strong> · <sub><a href="https://github.com/json5/json5/pull/371">#371</a></sub><br>JSON5 的 JavaScript 实现。贡献涉及序列化正确性。</p>

<p><a href="https://github.com/pydata/xarray/stargazers"><img alt="Xarray upstream stars: 4,211" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/pydata-xarray-4211.svg" width="180" align="right"></a><strong><a href="https://github.com/pydata/xarray">Xarray</a></strong> · <sub><a href="https://github.com/pydata/xarray/pull/11711">#11711</a></sub><br>面向科学计算的带标签数组库。贡献涉及文档工作流可靠性。</p>

<p><a href="https://github.com/pydicom/pydicom/stargazers"><img alt="pydicom upstream stars: 2.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/pydicom-pydicom-2225.svg" width="180" align="right"></a><strong><a href="https://github.com/pydicom/pydicom">pydicom</a></strong> · <sub><a href="https://github.com/pydicom/pydicom/pull/2388">#2388</a></sub><br>处理 DICOM 医学影像的 Python 库。贡献涉及数据转换与互操作性。</p>

<p><a href="https://github.com/nilbuild/developer-roadmap/stargazers"><img alt="Developer Roadmap upstream stars: 370k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/nilbuild-developer-roadmap-369547.svg" width="180" align="right"></a><strong><a href="https://github.com/nilbuild/developer-roadmap">Developer Roadmap</a></strong> · <sub><a href="https://github.com/nilbuild/developer-roadmap/pull/10451">#10451</a></sub><br>开发者学习路线与技术指南。贡献涉及 Python 学习内容。</p>

<p><a href="https://github.com/EbookFoundation/free-programming-books/stargazers"><img alt="Free Programming Books upstream stars: 399k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/EbookFoundation-free-programming-books-399196.svg" width="180" align="right"></a><strong><a href="https://github.com/EbookFoundation/free-programming-books">Free Programming Books</a></strong> · <sub><a href="https://github.com/EbookFoundation/free-programming-books/pull/13533">#13533</a></sub><br>多语言免费编程资源库。参与完善贡献者文档。</p>


<sub>Stars 快照 · 2026-10-17–18</sub>

## 动态精选

<sub>AI 辅助维护</sub>

<!-- ACTIVITY:START -->
- <sub>2026-10-18</sub> · [Xarray #11711 合并后，收到 VeckoTheGecko 的后续致谢。](https://github.com/pydata/xarray/pull/11711#issuecomment-6249123066)
- <sub>2026-10-17</sub> · [awesome-python #3376 获 vinta 批准并合并。](https://github.com/vinta/awesome-python/pull/3376)
- <sub>2026-10-17</sub> · [Xarray #11711 获 headtr1ck 批准并合并。](https://github.com/pydata/xarray/pull/11711)
- <sub>2026-10-17</sub> · [发布 Aurantium · Mathematics，汇总 24 个数学研究项目，其中 8 项包含 Lean 形式化。](https://github.com/Aurantium-47/aurantium-mathematics)
- <sub>2026-10-15</sub> · [JSON5 #371 已合并。](https://github.com/json5/json5/pull/371)
- <sub>2026-10-14</sub> · [Spec Kit #4956 已合并。](https://github.com/github/spec-kit/pull/4956)
- <sub>2026-10-13</sub> · [REA #2448 已合并；CassieFox23 在 Linux 上独立复现并确认修复有效。](https://github.com/morluto/rea/pull/2448#issuecomment-6138368698)
- <sub>2026-10-13</sub> · [REA #2422 已合并；N0zoM1z0 接续完成扩展 #2635，亦已并入上游。](https://github.com/morluto/rea/pull/2635)
- <sub>2026-10-12</sub> · [REA #2227](https://github.com/morluto/rea/pull/2227#issuecomment-6127162628) 的方案获维护者 morluto 评价「Brilliant」，并有[上游实现](https://github.com/morluto/rea/commit/c9fed50691ae014890e91a72534773d2fb58ce44)跟进。

<details>
<summary>更多动态</summary>

- <sub>2026-10-15</sub> · [Developer Roadmap #10451 已合并。](https://github.com/nilbuild/developer-roadmap/pull/10451)
- <sub>2026-10-15</sub> · [Free Programming Books #13533 已合并。](https://github.com/EbookFoundation/free-programming-books/pull/13533)
- <sub>2026-10-14</sub> · [KOReader #16220 已合并。](https://github.com/koreader/koreader/pull/16220)
- <sub>2026-10-15</sub> · [发布 Hardinian 渐近式 r = 2 的 Lean 补充证明。](https://github.com/Aurantium-47/hardinian-array-asymptotics/blob/477fcff33df19d5f752f9748d8596b31da15c81b/FORMALIZATION.md)

</details>
<!-- ACTIVITY:END -->

[全部项目](https://github.com/Aurantium-47?tab=repositories) · [已合并贡献](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)
