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
    <source media="(max-width: 640px)" srcset="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/1f602d108664473913d750b0c40b35f375554d12/assets/interests/records-mobile-zh.svg?v=20261113">
    <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/1f602d108664473913d750b0c40b35f375554d12/assets/interests/records-zh.svg?v=20261113" width="920" alt="">
  </picture>
</p>
<p>
  <picture>
    <source media="(max-width: 640px)" srcset="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/interests/words-mobile-zh.svg?v=20261104">
    <img src="https://raw.githubusercontent.com/Aurantium-47/Aurantium-47/main/assets/interests/words-zh.svg?v=20261104" width="920" alt="">
  </picture>
</p>
<!-- INTERESTS:END -->

开源，让更多人有了新的可能。

## 数学研究

[**研究目录 · 证明、反例与推广**](https://github.com/Aurantium-47/aurantium-mathematics)

**[AIM 问题集：两项否定答案](https://github.com/Aurantium-47/aim23-czds-counterexample)** · <sub>2004 / 2007 · 多项式零点</sub>

从二十年前的问题出发，研究多项式变换能否保持零点性质。**AIM 23：构造反例，非实根由 4 个增至 6 个；[AIM 34](https://github.com/Aurantium-47/aim34-multiplier-sequence)：从“足够大的整数参数是否有效”，推进到“每个正实数参数都无效”。** 两项均附 Lean 源码与历史重放、独立 AI 复核记录。[原题背景：Craven–Csordas](https://math.hawaii.edu/~tom/mathfiles/czdssurvey.pdf) · [Chasse 博士论文](https://math.hawaii.edu/home/talks/thesis.pdf)

**[BRW 图多项式：1994 年问题的部分进展](https://github.com/Aurantium-47/brw-tau-clique-attachments/tree/dc6d35ba53c6a41064bc9982cb524b05b74dc2ff/extensions/2026-11-02-uniform-cycle-substitution)** · <sub>[Canadian Journal of Mathematics · 1994](https://doi.org/10.4153/CJM-1994-002-3) · 图论</sub>

研究图结构拼接后，多项式零点性质能否保留。**将特定圈长的结果统一到任意圈长**：把圈的一个顶点替换为满足条件的图，仍保持所研究的实根性质，并可继续沿边拼接。覆盖一个完整构造族，属于一般猜想的部分结果。

**[栈排序：排列计数规律的统一证明稿](https://github.com/Aurantium-47/aurantium-mathematics/tree/d6c4747db93eb8c7acfcb792215452cc1f2249dc/research/stack-sorting-fibre-log-concavity)** · <sub>2026 · 组合数学</sub>

研究按同一排序结果分组的排列，其计数分布为何满足更强的对数凹性。**[本稿 Git 提交：11 月 4 日](https://github.com/Aurantium-47/aurantium-mathematics/commit/d6c4747db93eb8c7acfcb792215452cc1f2249dc)**；对应结论亦见 Colin Defant <sub>（<a href="https://sites.google.com/view/colin-defant/home">哈佛大学博士后</a>）</sub> 的**[11 月 10 日 arXiv 预印本定理 1.1](https://arxiv.org/html/2611.13479v1#S1.Thmtheorem1)**。证明与文献对照已公开。

<sub>以上为 AI 辅助研究稿，已记录相应核验；尚非人类同行评审成果。文献与日期展示研究背景，不代表作者认可或优先权认定。</sub>

**[更多数学工作 · 完整目录与验证材料](https://github.com/Aurantium-47/aurantium-mathematics#全部项目)**

## NLP 与信息检索

**Dense & Hybrid Retrieval · Knowledge Graphs · Retrieval-Augmented QA**

研究文本与图关系共同约束下的检索与问答，重点是**多路召回的互补、关系约束下的实体消歧，以及召回与重排的协同**。

当前以 **STaRK-MAG** 为主要场景，探索如何联合实体文本、属性和图关系，让候选选择同时满足语义与关系条件。

## 调研工具

**[Research-to-Decision](https://github.com/Aurantium-47/Research-to-Decision)** — 从调研到抉择的 Agent 工作流。基于 BMad Deep Recon 和 OpenInquire 的跨平台读取，主动澄清需求、核对证据与实际利弊，给出首选、代价和改选条件。

## 开源贡献

**工程草稿 · [Sentence Transformers：按数据集同步批次 #4317](https://github.com/huggingface/sentence-transformers/pull/4317)**

让各 rank 在同一步处理同一任务，同时保留按任务配置的单 rank 批大小，并在 checkpoint 恢复后保持训练调度。**18 次真实双 rank CPU/Gloo Trainer 运行**（6 组配置 × 完整 / 前缀 / 恢复）通过原生目标检查，确定性测试中恢复后的轨迹与连续训练一致。

**尚未合并：** 依赖同样未合并的 [Accelerate 草稿 #4491](https://github.com/huggingface/accelerate/pull/4491)；上游 CI 等待维护者批准运行。

<details>
<summary>调度示意图、固定复现证据与边界</summary>

![先分组同一任务的 rank 批次再分片，保留各任务的单 rank 批大小](https://raw.githubusercontent.com/Aurantium-47/sentence-transformers/f4d3da733194cf46e5cbd8d6014df94f558e769a/research/synchronized-dataset-batches/assets/synchronized-task-scheduling.svg)

[固定复现材料 · 2026 年 11 月 2 日](https://github.com/Aurantium-47/sentence-transformers/tree/f4d3da733194cf46e5cbd8d6014df94f558e769a/research/synchronized-dataset-batches)包含 rank 轨迹、源文件哈希及纯 JSON 数值核对。18 次运行来自独立验证环境，不是上游 CI；图示说明调度，不代表吞吐测量。范围限于固定双 rank CPU/Gloo、普通 map-style 采样及确定性恢复测试，不宣称 GPU/NCCL、任意随机恢复或性能收益。实现、测试和证据复核使用 AI 辅助。

</details>

部分已合并的上游贡献：

<p><a href="https://github.com/huggingface/tokenizers/stargazers"><img alt="huggingface/tokenizers stars" src="https://img.shields.io/github/stars/huggingface/tokenizers?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/huggingface/tokenizers">Hugging Face Tokenizers</a></strong> · <sub><a href="https://github.com/huggingface/tokenizers/pull/2567">#2567</a> · 已合并</sub><br>修复 <strong>Kimi</strong> 预分词中 Han 字符与数字、标点类别重叠的处理，保持跨字节块边界的正则切分语义，并补充一致性与 JSON/BPE 编码回归测试。</p>

<p><a href="https://github.com/HKUDS/LightRAG/stargazers"><img alt="HKUDS/LightRAG stars" src="https://img.shields.io/github/stars/HKUDS/LightRAG?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/HKUDS/LightRAG">LightRAG</a></strong> · <sub><a href="https://github.com/HKUDS/LightRAG/pull/4368">#4368</a> · 已合并</sub><br>定位并修复 PostgreSQL 旧向量迁移中“部分完成却被视为成功”的数据完整性缺陷，提供复现、服务端复制方案和回归测试。维护者在此基础上完善了分段恢复与跨实例并发保护，并<a href="https://github.com/HKUDS/LightRAG/pull/4368#issuecomment-6828325439">验证 20,000 条 256 维向量逐行一致、30,000 条双实例并发迁移无重复</a>。</p>

<p><a href="https://github.com/huggingface/sentence-transformers/stargazers"><img alt="huggingface/sentence-transformers stars" src="https://img.shields.io/github/stars/huggingface/sentence-transformers?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/huggingface/sentence-transformers">Sentence Transformers</a></strong> · <sub><a href="https://github.com/huggingface/sentence-transformers/pull/4251">#4251</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4262">#4262</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4264">#4264</a> · <a href="https://github.com/huggingface/sentence-transformers/pull/4284">#4284</a></sub><br>句向量与语义检索。修复复用浮点 USearch 索引时的重排判断，避免浮点向量被截断后破坏检索排序。 另已合并：修复无分数过滤条件时困难负样本挖掘忽略 CrossEncoder 重排的问题（#4262）；处理重排评估中的空候选列表（#4264）；排除 GIST 引导分数相同时误作负样本的自身配对（#4284）。</p>

<p><a href="https://github.com/morluto/rea/stargazers"><img alt="morluto/rea stars" src="https://img.shields.io/github/stars/morluto/rea?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/morluto/rea">REA</a></strong> · <sub><a href="https://github.com/morluto/rea/pull/2422">#2422</a> · <a href="https://github.com/morluto/rea/pull/2448">#2448</a> · <a href="https://github.com/morluto/rea/pull/2429">#2429</a></sub><br>面向智能体的逆向工程平台。贡献涉及跨平台兼容性与二进制诊断。</p>

<p><a href="https://github.com/github/spec-kit/stargazers"><img alt="github/spec-kit stars" src="https://img.shields.io/github/stars/github/spec-kit?style=for-the-badge&amp;color=eac35d&amp;labelColor=e9edf2&amp;logo=github&amp;logoColor=9a6700" width="180" align="right"></a><strong><a href="https://github.com/github/spec-kit">Spec Kit</a></strong> · <sub><a href="https://github.com/github/spec-kit/pull/4956">#4956</a></sub><br>GitHub 官方规范驱动开发工具包。贡献涉及 Windows 工作流可靠性。</p>

**更多已合并贡献**

- **[Haystack](https://github.com/deepset-ai/haystack)** [![Stars](https://img.shields.io/github/stars/deepset-ai/haystack?style=flat&color=gold)](https://github.com/deepset-ai/haystack/stargazers) · [#13422](https://github.com/deepset-ai/haystack/pull/13422) · Python 代码切分边界
- **[spdlog](https://github.com/gabime/spdlog)** [![Stars](https://img.shields.io/github/stars/gabime/spdlog?style=flat&color=gold)](https://github.com/gabime/spdlog/stargazers) · [#3683](https://github.com/gabime/spdlog/pull/3683) · Windows TCP 错误处理
- **[Resty](https://github.com/go-resty/resty)** [![Stars](https://img.shields.io/github/stars/go-resty/resty?style=flat&color=gold)](https://github.com/go-resty/resty/stargazers) · [#1250](https://github.com/go-resty/resty/pull/1250) · curl 请求复现
- **[GitHub gitignore](https://github.com/github/gitignore)** [![Stars](https://img.shields.io/github/stars/github/gitignore?style=flat&color=gold)](https://github.com/github/gitignore/stargazers) · [#4931](https://github.com/github/gitignore/pull/4931) · 同步临时文件规则
- **[Claude Trading Skills](https://github.com/tradermonty/claude-trading-skills)** [![Stars](https://img.shields.io/github/stars/tradermonty/claude-trading-skills?style=flat&color=gold)](https://github.com/tradermonty/claude-trading-skills/stargazers) · [#596](https://github.com/tradermonty/claude-trading-skills/pull/596) · 仓位风险报告一致性
- **[awesome-python](https://github.com/vinta/awesome-python)** [![Stars](https://img.shields.io/github/stars/vinta/awesome-python?style=flat&color=gold)](https://github.com/vinta/awesome-python/stargazers) · [#3376](https://github.com/vinta/awesome-python/pull/3376) · 键盘导航
- **[IPython](https://github.com/ipython/ipython)** [![Stars](https://img.shields.io/github/stars/ipython/ipython?style=flat&color=gold)](https://github.com/ipython/ipython/stargazers) · [#15435](https://github.com/ipython/ipython/pull/15435) · pathlib 路径支持
- **[Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh)** [![Stars](https://img.shields.io/github/stars/ohmyzsh/ohmyzsh?style=flat&color=gold)](https://github.com/ohmyzsh/ohmyzsh/stargazers) · [#14184](https://github.com/ohmyzsh/ohmyzsh/pull/14184) · uv 文档
- **[KOReader](https://github.com/koreader/koreader)** [![Stars](https://img.shields.io/github/stars/koreader/koreader?style=flat&color=gold)](https://github.com/koreader/koreader/stargazers) · [#16220](https://github.com/koreader/koreader/pull/16220) · 批注导出
- **[JSON5](https://github.com/json5/json5)** [![Stars](https://img.shields.io/github/stars/json5/json5?style=flat&color=gold)](https://github.com/json5/json5/stargazers) · [#371](https://github.com/json5/json5/pull/371) · 序列化正确性
- **[Xarray](https://github.com/pydata/xarray)** [![Stars](https://img.shields.io/github/stars/pydata/xarray?style=flat&color=gold)](https://github.com/pydata/xarray/stargazers) · [#11711](https://github.com/pydata/xarray/pull/11711) · Windows 文档构建
- **[pydicom](https://github.com/pydicom/pydicom)** [![Stars](https://img.shields.io/github/stars/pydicom/pydicom?style=flat&color=gold)](https://github.com/pydicom/pydicom/stargazers) · [#2388](https://github.com/pydicom/pydicom/pull/2388) · 数值 JSON 转换
- **[Developer Roadmap](https://github.com/nilbuild/developer-roadmap)** [![Stars](https://img.shields.io/github/stars/nilbuild/developer-roadmap?style=flat&color=gold)](https://github.com/nilbuild/developer-roadmap/stargazers) · [#10451](https://github.com/nilbuild/developer-roadmap/pull/10451) · Python 学习内容
- **[Free Programming Books](https://github.com/EbookFoundation/free-programming-books)** [![Stars](https://img.shields.io/github/stars/EbookFoundation/free-programming-books?style=flat&color=gold)](https://github.com/EbookFoundation/free-programming-books/stargazers) · [#13533](https://github.com/EbookFoundation/free-programming-books/pull/13533) · 贡献文档导航


## 动态精选

<sub>AI 辅助维护</sub>

<!-- ACTIVITY:START -->
- <sub>2026-11-12</sub> · [Tokenizers #2567 获 SBrandeis 批准并合并，修复 Kimi 预分词的 Han 类别重叠问题。](https://github.com/huggingface/tokenizers/pull/2567)
- <sub>2026-10-22</sub> · [Sentence Transformers #4251 — Tom Aarsen 补充了精度参数说明和回归测试，并合并修复。](https://github.com/huggingface/sentence-transformers/pull/4251#issuecomment-6342707340)
- <sub>2026-10-21</sub> · [IPython #15435 由 Carreau 合并。](https://github.com/ipython/ipython/pull/15435)
- <sub>2026-10-20</sub> · [Oh My Zsh #14184 由 robbyrussell 合并。](https://github.com/ohmyzsh/ohmyzsh/pull/14184)
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

- <sub>2026-10-31</sub> · [claude-trading-skills #596](https://github.com/tradermonty/claude-trading-skills/pull/596) 已合并，使报告风险与实际采用的仓位计算方法一致；维护者 tradermonty 的[后续 #602](https://github.com/tradermonty/claude-trading-skills/pull/602) 补充止损校验、Decimal 风险舍入与文档。
- <sub>2026-10-15</sub> · [Developer Roadmap #10451 已合并。](https://github.com/nilbuild/developer-roadmap/pull/10451)
- <sub>2026-10-15</sub> · [Free Programming Books #13533 已合并。](https://github.com/EbookFoundation/free-programming-books/pull/13533)
- <sub>2026-10-15</sub> · [发布 Hardinian 渐近式 r = 2 的 Lean 补充证明。](https://github.com/Aurantium-47/hardinian-array-asymptotics/blob/477fcff33df19d5f752f9748d8596b31da15c81b/FORMALIZATION.md)
- <sub>2026-10-14</sub> · [KOReader #16220 已合并。](https://github.com/koreader/koreader/pull/16220)
- <sub>2026-10-14</sub> · [REA #3224 — Kotlin 源文件识别支持获上游采纳，并保留共同作者署名。](https://github.com/morluto/rea/commit/03ffb2c13dc6d3e8e0cc8cec70efb2a220c38607)

</details>
<!-- ACTIVITY:END -->

[全部项目](https://github.com/Aurantium-47?tab=repositories) · [已合并贡献](https://github.com/search?q=author%3AAurantium-47+is%3Apr+is%3Amerged&type=pullrequests)
