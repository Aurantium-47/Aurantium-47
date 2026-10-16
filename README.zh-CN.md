# Aurantium

<sub><a href="https://github.com/Aurantium-47">English</a> · <b>简体中文</b></sub>

**AI for Math · NLP**

探索 AI 在推理与软件工程中的能力边界。

兴趣：**量化策略 · 加密市场**

[数学研究](https://github.com/Aurantium-47/aurantium-mathematics) · [开源贡献](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)

<p><img alt="Python" src="https://img.shields.io/badge/Python-e9edf2?style=flat-square&amp;logo=python&amp;logoColor=57606a"> <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-e9edf2?style=flat-square&amp;logo=pytorch&amp;logoColor=57606a"> <img alt="Transformers" src="https://img.shields.io/badge/Transformers-e9edf2?style=flat-square&amp;logo=huggingface&amp;logoColor=57606a"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-e9edf2?style=flat-square&amp;logo=numpy&amp;logoColor=57606a"> <img alt="Lean 4" src="https://img.shields.io/badge/Lean%204-e9edf2?style=flat-square"> <img alt="mathlib" src="https://img.shields.io/badge/mathlib-e9edf2?style=flat-square"> <img alt="SymPy" src="https://img.shields.io/badge/SymPy-e9edf2?style=flat-square&amp;logo=sympy&amp;logoColor=57606a"> <img alt="LaTeX" src="https://img.shields.io/badge/LaTeX-e9edf2?style=flat-square&amp;logo=latex&amp;logoColor=57606a"> <img alt="C++" src="https://img.shields.io/badge/C%2B%2B-e9edf2?style=flat-square&amp;logo=cplusplus&amp;logoColor=57606a"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-e9edf2?style=flat-square&amp;logo=typescript&amp;logoColor=57606a"> <img alt="Node.js" src="https://img.shields.io/badge/Node.js-e9edf2?style=flat-square&amp;logo=nodedotjs&amp;logoColor=57606a"> <img alt="Git" src="https://img.shields.io/badge/Git-e9edf2?style=flat-square&amp;logo=git&amp;logoColor=57606a"></p>

## 数学研究

[**24 个研究项目 · 8 项 Lean 形式化**](https://github.com/Aurantium-47/aurantium-mathematics)

**[Howroyd 27 集猜想](https://github.com/Aurantium-47/howroyd-27-conjecture)**

证明剩余两个模 3 余类：对所有 d ≥ 10、3 ∤ d，恰有 **27 个最大独立集**，并给出完整分类。

<sub>极值图论 · 枚举组合</sub>

<details>
<summary>出处、前人进展与验证</summary>

- **原问题出处:** Andrew Howroyd，[OEIS A297557（2018）](https://oeis.org/A297557)。
- **已有进展:** [John Machacek](https://arxiv.org/abs/2010.11112v2) 在 *Procedia Computer Science* 195（2021）证明 3 ∣ d 分支。两项结果合起来补全 d ≥ 9 的计数公式。
- **证明方法:** 以精确加权覆盖证书和坐标归约，将分类化为 3 种背景、每种 9 个角部延拓。
- **补充结果与材料:** 从猜想要求的计数，推进到全部 27 个最大独立集的显式分类。
- **验证方式:** Lean 4 覆盖完整的 d ≥ 10、3 ∤ d 命题；另提供 89 项有理数证书。

</details>

**[峰多项式的最后实根](https://github.com/Aurantium-47/peak-polynomial-last-real-root)**

证明 **Billey–Fahrbach–Talmage 猜想 6.6**：最大峰是倒数第二峰之后唯一的实根，不限制峰的数量或间隔。

<sub>代数组合 · 多项式根的分布</sub>

<details>
<summary>出处、前人进展与验证</summary>

- **原问题出处:** Sara Billey、Matthew Fahrbach、Alan Talmage，[*Experimental Mathematics* 25(2), 165–175（2016）](https://arxiv.org/abs/1410.8506v2)；预印本首发于 2014 年。
- **已有进展:** Billey–Fahrbach–Talmage 给出递推与对称恒等式。[Li 的系数定理](https://doi.org/10.5281/zenodo.22832569) 已涵盖右侧正性和若干局部符号性质；本项补足剩余非整数区间的分析。
- **证明方法:** 通过自包含的积分表示与符号分析，覆盖倒数第二峰之后的整个区间。
- **补充结果与材料:** 同时给出最大峰两侧的符号、根的单性和单峰情形；与 Li 定理重叠的推论在文稿中注明归属。
- **验证方式:** 全参数数学证明；附精确有限检查及单独记录的小规模复现。

</details>

<details>
<summary>另外两项代表结果：Stern 正性 · Fence 反例</summary>

**[Stern 多项式：正性与单调性](https://github.com/Aurantium-47/stern-polynomial-positivity)**

证明 Ulas **猜想 4.4，覆盖全部 n ≥ 0 和实参数 t**；另以 B₁₈₃ 的精确反例否定猜想 4.3 的单调性条款。

<sub>数论 · 多项式正性</sub>

- **原问题出处:** Maciej Ulas，[2019 年预印本](https://arxiv.org/abs/1909.10844v1)；期刊版发表于 [*Publicationes Mathematicae Debrecen* 96(3–4), 401–422（2020）](https://publi.math.unideb.hu/contents/2020)。猜想编号采用预印本版本。
- **已有进展:** 沿用 Stern 递推和已有二次恒等式，其中关键恒等式已见于 Ulas 原文。
- **证明方法:** 由递推证明正性，以精确有理数导数证据构造单调性反例。
- **补充结果与材料:** 一般正性定理之外，给出独立的单调性反例；猜想 4.3 的一般唯一实根条款不在本项结论内。
- **验证方式:** 两项结果均用 Lean 4 / mathlib 形式化，包含负导数推出单调性失效的步骤。

**[Fence rowmotion：轨道均值反例](https://github.com/Aurantium-47/fence-rowmotion-counterexample)**

以 32 元素 fence 和完整的 237 状态轨道，**否定猜想 5.4(b)**：精确均值 **1258/79 ≠ 16**。

<sub>代数组合动力系统 · 偏序集</sub>

- **原问题出处:** Sergi Elizalde、Matthew Plante、Tom Roby、Bruce Sagan，[*Algebraic Combinatorics* 6(1), 17–36（2023）](https://alco.centre-mersenne.org/articles/10.5802/alco.256/)。
- **已有进展:** 原作者建立多项轨道平均性质，并在猜想 5.4(b) 中提出理想基数的 homomesy 命题。
- **证明方法:** 显式构造偏序集，完整枚举轨道，以精确有理数计算均值。
- **补充结果与材料:** 公开完整轨道证书，便于复核；结论不涉及猜想的 (a) 部分。
- **验证方式:** 通过 Lean 内核归约核验证书，最终定理不依赖原生计算公理。

</details>

## NLP 与信息检索

**信息检索 · 表示学习 · 知识图谱**

关注半结构化知识库中的检索问题：稠密检索、文本与图关系融合、实体消歧，以及检索评测。当前围绕 STaRK-MAG 开展工作。

## 开源贡献

[9 条 PR 已合并，覆盖 7 个项目](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)。

### [REA](https://github.com/morluto/rea) <a href="https://github.com/morluto/rea/stargazers"><img alt="REA upstream stars" src="https://img.shields.io/github/stars/morluto/rea?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

面向智能体的逆向工程工具，覆盖应用行为与原生二进制分析。参与跨平台兼容性与二进制诊断相关改进。

<sub>3 条 PR 已合并 · [#2422](https://github.com/morluto/rea/pull/2422) · [#2448](https://github.com/morluto/rea/pull/2448) · [#2429](https://github.com/morluto/rea/pull/2429)</sub>

### [Spec Kit](https://github.com/github/spec-kit) <a href="https://github.com/github/spec-kit/stargazers"><img alt="Spec Kit upstream stars" src="https://img.shields.io/github/stars/github/spec-kit?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

GitHub 推出的规范驱动开发工具包，为编程智能体提供结构化工作流程。参与 Windows 工作流可靠性改进。

<sub>1 条 PR 已合并 · [#4956](https://github.com/github/spec-kit/pull/4956)</sub>

### [KOReader](https://github.com/koreader/koreader) <a href="https://github.com/koreader/koreader/stargazers"><img alt="KOReader upstream stars" src="https://img.shields.io/github/stars/koreader/koreader?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

面向电子墨水设备与 Android 的文档阅读器。参与批注工作流改进。

<sub>1 条 PR 已合并 · [#16220](https://github.com/koreader/koreader/pull/16220)</sub>

### [JSON5](https://github.com/json5/json5) <a href="https://github.com/json5/json5/stargazers"><img alt="JSON5 upstream stars" src="https://img.shields.io/github/stars/json5/json5?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

面向人工编写配置的 JSON 扩展格式。参与序列化正确性改进。

<sub>1 条 PR 已合并 · [#371](https://github.com/json5/json5/pull/371)</sub>

### [pydicom](https://github.com/pydicom/pydicom) <a href="https://github.com/pydicom/pydicom/stargazers"><img alt="pydicom upstream stars" src="https://img.shields.io/github/stars/pydicom/pydicom?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

处理 DICOM 医学影像数据的 Python 库。参与数据转换与互操作性改进。

<sub>1 条 PR 已合并 · [#2388](https://github.com/pydicom/pydicom/pull/2388)</sub>

### [Developer Roadmap](https://github.com/nilbuild/developer-roadmap) <a href="https://github.com/nilbuild/developer-roadmap/stargazers"><img alt="Developer Roadmap upstream stars" src="https://img.shields.io/github/stars/nilbuild/developer-roadmap?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

社区维护的开发者学习路线与技术指南。参与 Python 学习内容完善。

<sub>1 条 PR 已合并 · [#10451](https://github.com/nilbuild/developer-roadmap/pull/10451)</sub>

### [Free Programming Books](https://github.com/EbookFoundation/free-programming-books) <a href="https://github.com/EbookFoundation/free-programming-books/stargazers"><img alt="Free Programming Books upstream stars" src="https://img.shields.io/github/stars/EbookFoundation/free-programming-books?style=for-the-badge&amp;logo=github&amp;label=Stars&amp;color=eac35d&amp;labelColor=e9edf2&amp;logoColor=9a6700" width="180" align="right"></a>

多语言免费编程书籍与学习资源库。参与贡献者文档完善。

<sub>1 条 PR 已合并 · [#13533](https://github.com/EbookFoundation/free-programming-books/pull/13533)</sub>


<sub>徽章动态显示上游仓库 Stars；PR 合并状态核对于 2026-10-17。</sub>

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
