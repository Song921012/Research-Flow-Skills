# 外部 skills 与备用仓库

## 使用顺序

**平时优先使用原作者的仓库。原仓库删除或确实不可用时，再使用用户的 fork。**定期更新只维护备用副本，不把备用地址变成日常主来源。

原作者迁移或改名时先核实新的正式入口；临时网络故障和限流不等于删库。需要备用时核对相同入口及共享文件，必要时使用已记录的可用提交。已安装的完整原版可以继续按实际任务使用。

各 skill 的资料卡已经写入对应备用地址，单独安装时也能找到，不依赖先读本页。

## 已核实的六组来源

| 平时使用的原仓库 | 备用副本 | 主要用途 |
| --- | --- | --- |
| [ChenLiu-1996/figures4papers](https://github.com/ChenLiu-1996/figures4papers) | [Song921012/figures4papers](https://github.com/Song921012/figures4papers) | 论文图形参考 |
| [yjz211/vivid-illustration-skill](https://github.com/yjz211/vivid-illustration-skill) | [Song921012/vivid-illustration-skill](https://github.com/Song921012/vivid-illustration-skill) | 可选绘图指导 |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | [Song921012/academic-research-skills](https://github.com/Song921012/academic-research-skills) | 研究、写作与审稿 |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | [Song921012/nature-skills](https://github.com/Song921012/nature-skills) | 绘图与论文表达 |
| [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) | [Song921012/Humanizer-zh](https://github.com/Song921012/Humanizer-zh) | 中文润色 |
| [huangwb8/ChineseResearchLaTeX](https://github.com/huangwb8/ChineseResearchLaTeX) | [Song921012/ChineseResearchLaTeX](https://github.com/Song921012/ChineseResearchLaTeX) | 基金写作与模板 |

2026-10-29 核查：六个仓库均为对应原仓库的 fork，默认分支均为 main，双方提交完全一致；本次无需同步。完整提交、入口与共享文件记录在 [dependency-sources.json](dependency-sources.json)。

英文 blader/humanizer 与 academic-writer 暂无已核实的用户备用仓库；Humanizer-zh 不是英文 humanizer 的相同副本。本地 math-model-skills 的来源需在使用环境核实，不猜测备用地址。

## 全部任务的语言编辑参考

2026-10-29 实际读取了 [blader/humanizer 的 SKILL.md](https://github.com/blader/humanizer/blob/main/SKILL.md)（v3.1.0，文件 blob `19fc634208e8cc6ae55d4ff287152583216fd244`）与 [op7418/Humanizer-zh 的 SKILL.md](https://github.com/op7418/Humanizer-zh/blob/main/SKILL.md)（文件 blob `ef07b54da21a41d4a7e4fe0b0afb928f597eb684`）。本次两者原库均可用；这项阅读核查不代表对备用仓库执行了同步。

将适合科研文体的编辑原则与用户要求整理为[统一语言约定](language-conventions.md)：术语先核实，表达具体自然，去工程记录化，保留条件与结论强度，逐项检查图示标签。两项外部 skill 用于语言编辑，不承担专业术语或数学结论核验；不照搬口语化、个性化表达或机械词表，也不把 AI 检测分数作为质量标准。各 skill 随附同一份语言约定，可独立执行；第三方正文仅外链，不复制进本仓库。

## 科研展示新增的使用入口

research-presentation 继续优先读取 Vivid 的 `channels/vivid-architecture-diagram-skill/SKILL.md` 和 Nature 的 `skills/nature-paper2ppt/SKILL.md`。两者沿用上表已核实的备用副本；本次已在记录的同一提交上检查架构图共同规则、PPTX 导出资料、架构依赖、paper2ppt manifest 与共享术语文件，并加入来源记录。

数学 Beamer 使用 [YixuanYang00/math-beamer-slides-skill](https://github.com/YixuanYang00/math-beamer-slides-skill)，报告组织可参考 [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)。本次已读取准确入口和相关依赖说明，未核实这些项目的用户 fork，也未新增自动维护对象。具体读取方法、输出限制与可选 PaperBanana、AutoFigure 入口见[科研展示资料卡](../skills/research-presentation/references/resources.md)。

新增引用不等于第三方工具已安装、外部服务已配置或所有路线完成运行验证；按任务选择并实际检查成品。

### PPT 与 Beamer 的补充调查

2026-10-29 进一步检查了 Anthropic pptx、MiniMax pptx-generator、Addsum slide-maker、mblode presentation-creator、frontend-slides、Slidev 官方 skill、Baoyu slide-deck、paper-to-slides 与 OpenAI 当前 Google Slides 入口。读取实际 SKILL.md 或任务相关章节，并检查涉及的说明、输出机制和许可；Addsum 的长说明仅阅读相关部分，未通读全文。完整来源、分工和配套文件见[科研展示资料卡](../skills/research-presentation/references/resources.md)。

吸收的内容已进入学术汇报任务卡：区分现场讲解和独立阅读，先盘点关键图与结果，按页组织信息和证据，按需要写逐页讲稿，检查各类对象的编辑能力以及源文件可移植性。新报告、新图与实质性重构在构思时继续检索相关 skill；局部修改沿用已有依据。

特别区分输出形式：Baoyu 默认合并图片页；frontend-slides 主要输出 HTML；Slidev 的普通 PPTX 导出为图片页，pptx-editable 仅在支持范围内重建对象，公式等仍可能为图片。旧 OpenAI slides 路径失效时使用已核实的新入口，不能因此直接改用备用 fork。本次没有为这些新增来源创建 fork、安装所有工具或调用外部生成服务。

## 定期维护怎样做

1. 读取来源记录，核实仓库身份、当前分支与双方提交；只维护记录中的用户备用仓库。
2. 无变化就结束。原仓库不可用时检查备用入口，保留现有内容并报告需要注意的变化。
3. 有新提交时比较差异，检查所用 SKILL.md、共享资源与许可。关键入口删除、依赖不完整、许可变化或分支分叉时，先保留现有可用版本，报告具体问题。
4. 确认只是正常向前更新时，将备用分支快进到已检查的上游提交；使用更新前的提交作为校验条件，不强制覆盖、不删除用户提交、不运行上游脚本。
5. 读回备用分支与关键入口，核对实际更新结果后，更新来源记录中的日期和静态核实版本。参考优先顺序保持不变。
6. 只有真实完成的同步才报告已更新。有写入权限、连接或冲突问题时，保留现状并说明具体阻碍。

这里的“已核实版本”指仓库关系、入口、依赖路径和许可的静态核对，不等于每个外部脚本、模型、模板都已经运行或编译验证。

## 备用副本能保留什么

保留完整 Git 仓库中的文件和历史，避免只复制一个 SKILL.md 而漏掉共享目录。Nature 的 nature-shared、Academic Research Skills 的 shared、Vivid 的根资源和子通道都要一起核对。

PyPI 包、TeX 环境、外部 API、发行附件和其他网络服务不会因为 fork 自动成为完整可用的备份。执行具体任务时仍需检查实际依赖；外部来源都不可用时，本项目的原创核心流程继续完成能够独立处理的工作。

fork 不改变原始许可与作者归属。第三方内容不复制进本 MIT 仓库；许可边界见 [第三方来源说明](../THIRD_PARTY_NOTICES.md)。

