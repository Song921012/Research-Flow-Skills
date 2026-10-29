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

