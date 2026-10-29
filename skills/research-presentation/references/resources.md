# 资料与组合方法

核对日期：2026-10-29。以下是按任务读取的能力入口，不是每次都运行的完整清单。先读本次相关入口，再按它列出的实际路径读取必要文件；不要只提到 skill 名字就声称已经使用。

## 怎样让其他 skill 真正参与

1. **按当前问题选。**故事组织选论文汇报或科学演示指导；模型关系与可编辑图选架构图指导；公式和证明较多时选数学 Beamer；制作 PPT 使用当前环境的 Presentations/PPTX skill。
2. **带着同一份简短说明。**交给所选 skill 的信息包括要讲的核心观点、已核实内容、对象与关系、受众、格式、模板和修改范围；明确由 AI 自主选定推荐方案，无需用户审美确认。
3. **读取并实际执行。**已安装且可调用时按当前宿主方式使用；只有仓库可访问时读取 SKILL.md 及其必要参考，采用其中适合任务的方法，用实际可用工具制作。不要虚构通用“自动安装依赖 skill”的接口。
4. **接回当前作品。**提纲要变成逐页内容，图示方案要变成可编辑图，审阅发现要变成实际修改；每个环节的输出继续服务同一故事，不能各做一套互不一致的稿。
5. **保留当前任务约束。**外部默认确认、页数、配色、背景、固定节奏和工具路线不覆盖用户要求及宿主工具规范；不因读取新 skill 而重启已完成的步骤。
6. **有缺项也继续。**检查外部脚本所需软件和服务后再用。不默认开通付费服务或把私人材料发到新服务；可选生图接口缺失时，使用可用的原生对象、SVG 或 TikZ 路线，准确说明受影响部分。

## 主要能力入口

| 来源 | 用在什么环节 | 需要得到什么 |
| --- | --- | --- |
| 当前环境的 Presentations / PPTX skill | PowerPoint 的实际创建、编辑、渲染和交付 | 可编辑演示文稿及实际预览；具体工具和目标位置以当前宿主为准 |
| [Vivid architecture](https://github.com/yjz211/vivid-illustration-skill/blob/main/channels/vivid-architecture-diagram-skill/SKILL.md) | 方法、模型、方案结构图的构思与制作 | 正确的对象关系、清楚的视觉层次及可编辑图件 |
| [Nature paper2ppt](https://github.com/Yuan1z0825/nature-skills/blob/main/skills/nature-paper2ppt/SKILL.md) | 论文到汇报的故事、证据图和备注组织 | 与论文类型相符的逐页叙事、图件与来源 |
| [Math Beamer](https://github.com/YixuanYang00/math-beamer-slides-skill/blob/main/math-beamer-slides-skill/SKILL.md) | 数学报告中的定义、假设、定理、证明和编译审核 | 正确的符号依赖、讲解顺序与可编译 Beamer |
| [Scientific Slides](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-slides/SKILL.md) | 报告结构、信息密度、投影可读性与视觉复核 | 适合听众和时长的页面；精确数学和数据选可编辑路线 |
| [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-schematics/SKILL.md) | 确有需要且服务可用时的概念插图草案 | 当前主要输出 PNG；不承担精确数据、公式或原生可编辑结构图 |

## 读取时别丢掉配套文件

**Vivid：**以仓库根为工作根，先读架构图入口与 `architecture/COMMON.md`；新建资产路线按需读 `architecture/WORKFLOW.md`、`architecture/catalog.json` 和所选资产的 `TEMPLATE.md`；原生 PPTX 读 `architecture/PPTX.md`。保留所需根级资源、脚本、字体和 `requirements-architecture.txt`，不能只拿子通道的 SKILL.md。其新文件默认 A/B 选择不适用于当前用户已授权的自主单方案任务；不改上游文件，明确本次任务要求后独立使用。实际 Office 验证只有在具备相应环境并执行后才能声称完成。

**Nature paper2ppt：**先读 `skills/nature-paper2ppt/manifest.yaml` 及其 `always_load`，包括 `static/core/` 下的 principles、toolchain、workflow、output-and-quality 和 `../nature-shared/core/terminology-ledger.md`，再读匹配的 `static/fragments/paper_type/` 文件。按需读图件、布局和自审资料；按实际版本使用其审核脚本。以 manifest 的真实路径为准，不误把 `static/core/` 简写成不存在的 `core/`。理论报告不硬补实验或消融，局部改稿不重跑整套论文读入。

**Math Beamer：**先读 `math-beamer-slides-skill/references/index.md`，按需读 mathematical-statements、proof-exposition、notation-and-dependencies、math-review-checklist 与 quality-standards。运行验证脚本前核对接口；使用 TeX 编译与 PDF 预览。其英文、完整 seminar、背景位图、禁 overlay 或成果页等默认值不成为本流程硬规则。PPT 数学页可以借用审阅方法，但不能擅自改交付格式。

**Scientific Slides：**读 `references/presentation_workflow.md`；按当前任务读 `references/beamer_guide.md` 或 `assets/powerpoint_design_guide.md`，视觉审核读 `references/visual_review_workflow.md`，执行脚本前读 `references/script_reference.md`。可单独使用叙事和可编辑页面指导，不必采用整页生图；固定页数、引用篇数和每分钟页数不适合作为所有报告的门槛。

**Scientific Schematics：**按需读 `references/iterative_refinement.md` 与 `best_practices.md`。当前图像生成路线依赖 OpenRouter 和可用额度，主要交付 PNG；不能包装成 PDF 就称矢量或原生可编辑。模型评分只作辅助，实际标签、关系和图像仍需逐项查看。当前环境若提供适合的图像生成工具，优先遵循宿主工具规范。

## 怎样学习别人好看的图

- 从当前研究领域的原论文、作者项目页或出版社官方材料检索，优先看与本研究关系相似的图。实际打开图和图注；只有摘要或文字抓取时，不声称已经看过视觉效果。
- 每次只记有用的信息：来源、适合什么问题、借鉴哪种结构或阅读顺序、怎样适配本任务。可以从模型总览、训练与推断分区、反馈机制或多尺度示意中选择适合者。
- 借鉴组织方法与视觉层次，不复制别人的科学结论、数据和独特图形后当作本研究。需要直接使用原图时核实许可并保留来源。
- [Nature 图件制作指南](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/)用于检查可读性、可编辑文字及图件输出；具体期刊和报告使用各自要求，不照搬 Nature 字号。
- [Ten simple rules for effective presentation slides](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009554)用于思考单页重点、复杂内容逐步展开和实际讲述；具体节奏按报告内容判断。
- 可选研究 [PaperBanana](https://github.com/dwzhu-pku/PaperBanana/tree/main/skill) 的参考检索、构思与批评修正流程，或 [AutoFigure](https://github.com/ResearAI/AutoFigure) 的 SVG/draw.io 路线。前者当前主要生成 PNG，后者是工具项目；只有确有需要且环境适配时才使用，不作为完成本流程的前置条件。

## 来源优先顺序与许可

原作者仓库优先；确认删除或确实不可访问后，才使用已核实的用户同源 fork。临时抓取失败先换可用读取方式或重试，不能直接判为删库。

| 原作者 | 已核实备用 |
| --- | --- |
| [yjz211/vivid-illustration-skill](https://github.com/yjz211/vivid-illustration-skill) | [Song921012/vivid-illustration-skill](https://github.com/Song921012/vivid-illustration-skill) |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | [Song921012/nature-skills](https://github.com/Song921012/nature-skills) |

其他来源尚未核实用户备用，不猜测地址。共享资源须跟随所用版本；来源可用不代表其所有工具都已安装或运行。

Vivid 采用自定义个人非商业许可，只独立引用获准入口，不将其文本、代码或资产复制、改编进本 MIT 项目。Nature 根许可为 Apache-2.0，第三方资源单独判断；Math Beamer 与 K-Dense 当前根许可为 MIT，仍保留各自来源。PaperBanana 根许可为 Apache-2.0、skill 另有声明，AutoFigure 为 MIT。本 skill 仅包含原创流程与链接，外部项目及实际所用素材继续适用各自许可。
