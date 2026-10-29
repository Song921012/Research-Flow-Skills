# 按需参考其他绘图 skills

在构思图形或审核成图时读取本页。先执行本 skill 的四步流程，只选择当前任务确实需要的外部指导。核心流程应能独立完成；缺少外部 skill 时，继续使用自带参考和通用绘图库。

## 先确认当前环境实际可用的内容

1. 查看宿主提供的技能列表或已确认的安装位置，核对下表中的技能名称与入口；不要把相似名称当作同一项目。
2. 宿主提供技能调用能力时，按其实际接口调用；只能读取文件时，打开对应 `SKILL.md` 及当前任务所需文件。不要虚构通用的嵌套调用语法或自动安装机制。
3. 外部包不可用时，按需查看公开来源中的适用说明；需要运行其脚本时，先核实完整文件、运行环境和许可。不能运行就使用本项目的独立实现，并如实说明实际使用范围。
4. 保留用户的科学目标、当前任务范围和已明确偏好。由 AI 判断表达、布局和审美，不额外设置逐轮选配色、选模板或认可成图的前提。

## 什么时候用哪个来源

| 来源与精确名称 | 何时考虑 | 读取或使用方式 |
| --- | --- | --- |
| [Vivid Illustration Skill](https://github.com/yjz211/vivid-illustration-skill)，`vivid-illustration-skill` | 用户明确提及 Vivid，或需要了解其数据图、架构图分类与模板范围 | **默认仅保留外部链接。** 核对其现行许可；只有当前使用方式确实获准时，才使用已有完整安装。主入口是根目录 `SKILL.md`，数据图通道为 `channels/vivid-figure-skill/SKILL.md`，名称 `vivid-figure-skill`。子通道依赖完整包，不能将单个子目录视为完整安装。 |
| [Nature Figure](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-figure)，`nature-figure` | 组织论文多面板证据、检查最终尺寸与导出质量 | 读取 `skills/nature-figure/SKILL.md`，随后只读当前任务所需的 manifest、核心约定和参考文件。使用它的审核脚本前确认脚本与依赖实际存在；涉及相邻 `nature-shared` 的内容时确认该资源也可访问。 |
| [figures4papers](https://github.com/ChenLiu-1996/figures4papers)，`scientific-figure-making` | 需要具体的 matplotlib 论文成图参考，尤其是曲线、比较图、热图与多面板布局 | 入口为 `scientific-figure-making/SKILL.md`。按任务查 `references/common-patterns.md`、`design-theory.md` 或 `demos.md`，再打开选中的成图和相关说明。记录借鉴的具体表达；不要声称已运行未执行的示例。 |

## 组合时保留的规则

- 一次选择一个主要指导，其余资料用于补充具体问题。理论、数据含义和当前投稿要求决定表达；外部示例中的配色、语言、字号与布局需要判断是否适用。
- 沿用项目已有的 Python/R 工作方式及用户委托的选择范围。外部参考不能新增与用户明确指令相冲突的审美确认流程；必要的科学信息仍应先查现有材料。
- Vivid 的当前许可限制改编、二次开发和再分发，不把其文本、源码、模板或图片复制进本项目，不以“参考”为由绕过限制。
- figures4papers 当前为 CC BY-NC 4.0；Nature 根许可当前为 Apache-2.0，但其第三方文件另有边界。使用原文件时遵守对应许可，不能默认由本项目 MIT 覆盖。
- 缺少外部资源或许可不适用时，按本项目规则独立实现。无需为了继续画图而要求用户安装全部来源。
- 简短记录实际读到的来源、采用的做法和完成的检查。检查输入数据与打开最终图像分别完成，外部技能名称或自动检查通过都不能替代这两项证据。

本页核对日期：2026-10-29。精确版本与许可来源见公开仓库根目录的 `THIRD_PARTY_NOTICES.md`；本页本身已包含执行所需的许可边界，单独安装此 skill 时不依赖该仓库根文件。

## 原作者优先，用户 fork 备用

优先读取原作者来源的安装或仓库。确认原仓库删除、所需入口撤下且没有适用迁移入口，或当前确实不可用时，再用下表备用仓库中的相同路径。临时限流不等于删库；定期更新备用仓库不改变来源优先顺序。

| 原仓库 | 用户备用 fork |
| --- | --- |
| yjz211/vivid-illustration-skill | [Song921012/vivid-illustration-skill](https://github.com/Song921012/vivid-illustration-skill) |
| Yuan1z0825/nature-skills | [Song921012/nature-skills](https://github.com/Song921012/nature-skills) |
| ChenLiu-1996/figures4papers | [Song921012/figures4papers](https://github.com/Song921012/figures4papers) |

核实入口和所需共享资源完整，再按原许可使用；备用副本不改变许可，也不等于 Python、TeX、外部服务等运行环境已备份。两处均不可用时继续本项目独立绘图流程，并说明实际使用范围。
