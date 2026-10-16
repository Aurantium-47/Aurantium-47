# Aurantium

<sub><a href="https://github.com/Aurantium-47">English</a> · <b>简体中文</b></sub>

**AI for Math · NLP**

探索 AI 在推理与软件工程中的能力边界。

兴趣：**量化策略 · 加密市场**

[数学研究](https://github.com/Aurantium-47/aurantium-mathematics) · [开源贡献](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)

<p><img alt="Python" src="https://img.shields.io/badge/Python-e9edf2?style=flat-square&amp;logo=python&amp;logoColor=57606a"> <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-e9edf2?style=flat-square&amp;logo=pytorch&amp;logoColor=57606a"> <img alt="Transformers" src="https://img.shields.io/badge/Transformers-e9edf2?style=flat-square&amp;logo=huggingface&amp;logoColor=57606a"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-e9edf2?style=flat-square&amp;logo=numpy&amp;logoColor=57606a"> <img alt="Lean 4" src="https://img.shields.io/badge/Lean%204-e9edf2?style=flat-square"> <img alt="mathlib" src="https://img.shields.io/badge/mathlib-e9edf2?style=flat-square"> <img alt="SymPy" src="https://img.shields.io/badge/SymPy-e9edf2?style=flat-square&amp;logo=sympy&amp;logoColor=57606a"> <img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-e9edf2?style=flat-square&amp;logo=latex&amp;logoColor=57606a"> <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-e9edf2?style=flat-square&amp;logo=cplusplus&amp;logoColor=57606a"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-e9edf2?style=flat-square&amp;logo=typescript&amp;logoColor=57606a"> <img alt="Node.js" src="https://img.shields.io/badge/Node.js-e9edf2?style=flat-square&amp;logo=nodedotjs&amp;logoColor=57606a"> <img alt="Git" src="https://img.shields.io/badge/Git-e9edf2?style=flat-square&amp;logo=git&amp;logoColor=57606a"></p>

## 数学研究

[**24 个研究项目 · 8 项 Lean 形式化**](https://github.com/Aurantium-47/aurantium-mathematics)

**7 组含进一步推广**。21 项可核对年代、且不属于同题文献对照的研究，其来源首发距今平均约 **4 年**，最早可追溯至 **2014 年**。

**[Howroyd 27 集猜想](https://github.com/Aurantium-47/howroyd-27-conjecture)**

<sub>[2018 年提出 · 距今 8 年](https://oeis.org/A297557) · 极值图论</sub>

- **已有结果：** Machacek（2021）证明了可被 3 整除的分支，覆盖三个余类中的一类。
- **本项结果：** 补齐另外两个余类，证明所有允许规模都恰有 **27 个最大独立集**。结合已知分支，完成全部 d ≥ 9 的计数公式。
- **加强与验证：** 从计数推进到 **全部 27 个集合的显式分类**，并完成剩余分支的 Lean 4 形式化。

<details>
<summary>原文出处与证明方法</summary>

- **原问题出处:** Andrew Howroyd，[OEIS A297557（2018）](https://oeis.org/A297557)。
- **已有进展:** [John Machacek](https://arxiv.org/abs/2010.11112v2) 在 *Procedia Computer Science* 195（2021）证明 3 ∣ d 分支。两项结果合起来补全 d ≥ 9 的计数公式。
- **证明方法:** 以精确加权覆盖证书和坐标归约，将分类化为 3 种背景、每种 9 个角部延拓。
- **补充结果与材料:** 从猜想要求的计数，推进到全部 27 个最大独立集的显式分类。
- **验证方式:** Lean 4 覆盖完整的 d ≥ 10、3 ∤ d 命题；另提供 89 项有理数证书。

</details>

**[Lecture Hall：从有限验证到任意长度的证明](https://github.com/Aurantium-47/lecture-hall-polynomiality)**

<sub>[2018 年提出 · 距今 8 年](https://arxiv.org/abs/1809.01377) · 代数组合 / 交换代数</sub>

- **已有结果：** Katthän（2018）报告了长度不超过 **12** 的计算验证。
- **本项结果：** 通过带符号 Dyck 路径识别，证明 **任意长度** 的多项式性，将有限证据推进为全下标定理。
- **推广与验证：** 进一步给出显式系数公式、最小单首 SAGBI 基和平坦 toric 退化。核心多项式性与路径识别已用 Lean 形式化；代数推广有完整文字证明。

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

**[峰多项式的最后实根](https://github.com/Aurantium-47/peak-polynomial-last-real-root)**

<sub>[Experimental Mathematics · 2016 年期刊版 · 距今 10 年](https://arxiv.org/abs/1410.8506v2) · 多项式实根</sub>

- **已有结果：** Billey–Fahrbach–Talmage 提出猜想 6.6；Li 后来的系数定理已涵盖右侧正性及局部符号性质。
- **本项结果：** 补齐剩余非整数区间的符号论证，完成 **整个目标区间的排根结论**，不限制峰的数量和间隔。
- **补充结果：** 给出自包含积分证明，包含单峰情形和完整区间符号；与 Li 定理重叠的结论保留原归属。

- **原问题出处:** Sara Billey、Matthew Fahrbach、Alan Talmage，[*Experimental Mathematics* 25(2), 165–175（2016）](https://arxiv.org/abs/1410.8506v2)；预印本首发于 2014 年。
- **已有进展:** Billey–Fahrbach–Talmage 给出递推与对称恒等式。[Li 的系数定理](https://doi.org/10.5281/zenodo.22832569) 已涵盖右侧正性和若干局部符号性质；本项补足剩余非整数区间的分析。
- **证明方法:** 通过自包含的积分表示与符号分析，覆盖倒数第二峰之后的整个区间。
- **补充结果与材料:** 同时给出最大峰两侧的符号、根的单性和单峰情形；与 Li 定理重叠的推论在文稿中注明归属。
- **验证方式:** 全参数数学证明；附精确有限检查及单独记录的小规模复现。

**[K₆ 链：否定 22 色猜想，并给出全族锐界 23](https://github.com/Aurantium-47/k6-clique-chain-packing-coloring)**

<sub>[2025 年提出](https://arxiv.org/abs/2511.12761) · 图着色</sub>

- **已有结果：** Furmańczyk、Gözüpek、Özkan 猜想所有这类链都有 **22 色**统一上界。
- **本项结果：** 构造 **450 顶点**反例否定 22 色，再证明所有链均可用 23 色，且团数至少 75 时精确值就是 **23**。
- **推广与验证：** 从一个反例进一步得到 **整个家族的正确锐界**。下界附 **16,646,562 条**精确证书记录及 Python、C++ 检查器。

- **原问题出处:** Furmańczyk、Gözüpek、Özkan，[Packing coloring of graphs with long paths（2025）](https://arxiv.org/abs/2511.12761)，猜想 2。
- **已有进展:** 原文为沿路径连接的 K₆ 团链提出统一 22 色上界。
- **证明方法:** 以有限状态调度松弛和递减秩证书排除 22 色，再构造显式周期着色得到 23 色上界。
- **补充结果与材料:** 建立全族锐界 23，并证明所有 t ≥ 75 的精确值均为 23；尚未确定最短反例长度和所有较短链的精确值。
- **验证方式:** 16,646,562 条精确证书，由 Python 与 C++ 检查器核验；属于计算证书核验，并非 Lean 形式化。

</details>

**另有 [20 项研究与文献对照](https://github.com/Aurantium-47/aurantium-mathematics#全部项目)**，包含 Stern 正性、化学图极值、Hurwitz 实根性等。

<details>
<summary>成果统计与年代口径</summary>

- **10** 项原题的肯定解答 · **3** 项以反例为主的结果 · **7** 项更大原问题的部分结果 · **3** 项构造或分类 · **1** 项同题文献对照。
- **7** 组包含后续推广，**8** 组包含 Lean 形式化；两项统计与上述分类可以重叠。参考目录共 **60** 条问题来源与相关文献。
- 年代按 **2026 − 来源首发年** 计算，21 项平均约 **4.0 年**；排除无明确年份的来源、仅间接核实的 2000 年报告，以及已有更早公开证明的 Karp 同题对照。这是来源年代统计，不是连续未解决年数。

</details>

## NLP 与信息检索

**信息检索 · 表示学习 · 知识图谱**

关注半结构化知识库中的检索问题：稠密检索、文本与图关系融合、实体消歧，以及检索评测。当前围绕 STaRK-MAG 开展工作。

## 开源贡献

[9 条 PR 已合并，覆盖 7 个项目](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)。

### [REA](https://github.com/morluto/rea) <a href="https://github.com/morluto/rea/stargazers"><img alt="REA upstream stars: 288k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/morluto-rea-287879.svg" width="180" align="right"></a>

面向智能体的逆向工程工具，覆盖应用行为与原生二进制分析。参与跨平台兼容性与二进制诊断相关改进。

<sub>3 条 PR 已合并 · [#2422](https://github.com/morluto/rea/pull/2422) · [#2448](https://github.com/morluto/rea/pull/2448) · [#2429](https://github.com/morluto/rea/pull/2429)</sub>

### [Spec Kit](https://github.com/github/spec-kit) <a href="https://github.com/github/spec-kit/stargazers"><img alt="Spec Kit upstream stars: 142k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/github-spec-kit-141541.svg" width="180" align="right"></a>

GitHub 推出的规范驱动开发工具包，为编程智能体提供结构化工作流程。参与 Windows 工作流可靠性改进。

<sub>1 条 PR 已合并 · [#4956](https://github.com/github/spec-kit/pull/4956)</sub>

### [KOReader](https://github.com/koreader/koreader) <a href="https://github.com/koreader/koreader/stargazers"><img alt="KOReader upstream stars: 30.4k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/koreader-koreader-30358.svg" width="180" align="right"></a>

面向电子墨水设备与 Android 的文档阅读器。参与批注工作流改进。

<sub>1 条 PR 已合并 · [#16220](https://github.com/koreader/koreader/pull/16220)</sub>

### [JSON5](https://github.com/json5/json5) <a href="https://github.com/json5/json5/stargazers"><img alt="JSON5 upstream stars: 7.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/json5-json5-7172.svg" width="180" align="right"></a>

面向人工编写配置的 JSON 扩展格式。参与序列化正确性改进。

<sub>1 条 PR 已合并 · [#371](https://github.com/json5/json5/pull/371)</sub>

### [pydicom](https://github.com/pydicom/pydicom) <a href="https://github.com/pydicom/pydicom/stargazers"><img alt="pydicom upstream stars: 2.2k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/pydicom-pydicom-2225.svg" width="180" align="right"></a>

处理 DICOM 医学影像数据的 Python 库。参与数据转换与互操作性改进。

<sub>1 条 PR 已合并 · [#2388](https://github.com/pydicom/pydicom/pull/2388)</sub>

### [Developer Roadmap](https://github.com/nilbuild/developer-roadmap) <a href="https://github.com/nilbuild/developer-roadmap/stargazers"><img alt="Developer Roadmap upstream stars: 370k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/nilbuild-developer-roadmap-369547.svg" width="180" align="right"></a>

社区维护的开发者学习路线与技术指南。参与 Python 学习内容完善。

<sub>1 条 PR 已合并 · [#10451](https://github.com/nilbuild/developer-roadmap/pull/10451)</sub>

### [Free Programming Books](https://github.com/EbookFoundation/free-programming-books) <a href="https://github.com/EbookFoundation/free-programming-books/stargazers"><img alt="Free Programming Books upstream stars: 399k" src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/stars/EbookFoundation-free-programming-books-399196.svg" width="180" align="right"></a>

多语言免费编程书籍与学习资源库。参与贡献者文档完善。

<sub>1 条 PR 已合并 · [#13533](https://github.com/EbookFoundation/free-programming-books/pull/13533)</sub>


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
