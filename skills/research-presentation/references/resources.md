# 资料与组合方法

核对日期：2026-10-29。以下来源已检查实际 skill 入口及相关说明、导出方式和许可；这不代表已经安装或运行全部第三方工具。按本次难点读取少量互补来源，所选方法须用于当前作品。

## 构思时主动查找

新报告、新图或实质性重构时执行；当前项目的字号、图例或局部措辞修改沿用已经核实的来源。

1. 根据本次题材、听众、时长和输出格式确定需要补充什么：故事组织、页面布局、数学表达、原生 PPT、模板编辑、方法图或验收。
2. 用具体需求检索 GitHub 和原作者文档中的 `SKILL.md`，结合已有资料选少量互补来源。核实正式入口、配套文件、近期可用性和许可，不以星数、营销名称或聚合站介绍代替判断。
3. 读入口及当前步骤所需的参考，确认实际输出：可编辑对象、SVG/TikZ、HTML 演示还是整页图片；检查对宿主、软件和外部服务的依赖。来源迁移先找正式新入口，原作者优先、用户 fork 备用。
4. 将采用的做法落到当前作品：怎样组织一页、怎样画清关系、怎样处理公式或怎样核验导出。若当前工具无法执行某条路线，采用可用方法完成相同目标，不声称已经运行该工具。
5. 在当前项目简短记录来源、采用环节和实际作用。检索后继续构思、制作和验收，不把长名单当成交付，也不要求用户先挑工具。

## 怎样让其他 skill 真正参与

1. **按当前问题选。**故事组织选论文汇报或科学演示指导；模型关系与可编辑图选架构图指导；公式和证明较多时选数学 Beamer；制作 PPT 使用当前环境的 Presentations/PPTX skill。
2. **带着同一份简短说明。**交给所选 skill 的信息包括要讲的核心观点、已核实内容、对象与关系、受众、格式、模板和修改范围；明确由 AI 自主选定推荐方案，无需用户审美确认。
3. **读取并实际执行。**已安装且可调用时按当前宿主方式使用；只有仓库可访问时读取 SKILL.md 及其必要参考，采用其中适合任务的方法，用实际可用工具制作。不要虚构通用“自动安装依赖 skill”的接口。
4. **接回当前作品。**提纲要变成逐页内容，图示方案要变成可编辑图，审阅发现要变成实际修改；每个环节的输出继续服务同一故事，不能各做一套互不一致的稿。
5. **保留当前任务约束。**外部默认确认、页数、配色、背景、固定节奏和工具路线不覆盖用户要求及宿主工具规范；不因读取新 skill 而重启已完成的步骤。
6. **有缺项也继续。**检查外部脚本所需软件和服务后再用。不默认开通付费服务或把私人材料发到新服务；可选生图接口缺失时，使用可用的原生对象、SVG 或 TikZ 路线，准确说明受影响部分。

## 主要能力入口

### 先把内容讲清楚

| 来源 | 实际吸收的方法 | 格式与使用边界 |
| --- | --- | --- |
| [Nature paper2ppt](https://github.com/Yuan1z0825/nature-skills/blob/main/skills/nature-paper2ppt/SKILL.md) | 按论文类型组织科学故事，固定术语，选择证据图并对应来源 | 参考内容与设计方法；当前宿主负责实际 PPT 制作。这是第三方项目名，不是 Nature 官方工具 |
| [presentation-creator](https://github.com/mblode/agent-skills/blob/main/skills/presentation-creator/SKILL.md) | 先确定听众和核心信息；区分现场讲解与独立阅读；每页标题、证据和讲稿各司其职 | 默认 Marp，导出依赖相应 CLI 和浏览器；不据此承诺原生可编辑 PPT，不照搬商业汇报话术 |
| [paper-to-slides](https://github.com/yigengjiang/paper-to-slides/blob/main/SKILL.md) | 先盘点论文关键图，安排逐页问题、证据、讲解时间与指图顺序；幻灯片和讲稿可使用不同语言 | 提供 Beamer 源码、PDF 和讲稿；依赖 TeX/Python。原论文图不因放进源码就变成可编辑对象 |
| [Math Beamer](https://github.com/YixuanYang00/math-beamer-slides-skill/blob/main/math-beamer-slides-skill/SKILL.md) | 按数学依赖引入定义、符号、定理和证明；保留假设、量词与结论 | 用于 Beamer 制作和数学审核；也可检查 PPT 数学内容，不改变用户指定格式 |
| [Scientific Slides](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-slides/SKILL.md) | 根据受众和时长安排深浅，检查信息密度、投影可读性与整场节奏 | 可选本地 PPT/Beamer 指导；整页生图分支依赖 OpenRouter，不能当作原生可编辑路线 |

### 制作和修改可编辑演示文稿

| 来源 | 实际吸收的方法 | 格式与使用边界 |
| --- | --- | --- |
| 当前环境的 Presentations / PPTX skill | 实际创建、编辑、渲染和交付；保持用户模板与原生对象 | 制作工具、保存方式和依赖以当前宿主要求为准，优先沿用已可用的工具 |
| [Anthropic pptx](https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md) | 区分新建与模板编辑；原生文本、图形、图表；检查占位符和结构，再渲染逐页修复 | 新建使用 PptxGenJS，模板修改涉及 OOXML；目录为专有许可，只引用入口与一般方法，不复制其文件 |
| [MiniMax pptx-generator](https://github.com/MiniMax-AI/skills/blob/main/skills/pptx-generator/SKILL.md) | 统一页面主题，按页面职责组织内容，检查文本和常见导出问题 | PptxGenJS/OOXML 路线；文字提取检查仍需补充实际看页；固定字体和 16:9 默认不覆盖用户要求 |
| [Addsum slide-maker](https://github.com/addsumtech/slides_maker/blob/main/skills/slide-maker/SKILL.md) | 每页观点对应证据；把内容、设计、素材与审阅工作接回同一报告；结合几何检查和图像检查 | 本次读 README、相关章节与许可，未通读其全部长说明。其 Python/deckkit 路线不替代宿主工具；部分公式为图片，不宣称全部对象可编辑 |
| [OpenAI Google Slides](https://github.com/openai/plugins/blob/main/plugins/google-drive/skills/google-slides/SKILL.md) | 从已有原生模板提取字体、布局和配色；修改后读回结构并检查导出 | 适合已有 Google Slides 模板，需要对应连接器；新建 PPT 使用宿主 Presentations。旧 openai/skills 的 slides 路径已迁移，不沿用失效入口 |

### 丰富版式和图示

| 来源 | 实际吸收的方法 | 格式与使用边界 |
| --- | --- | --- |
| [Vivid architecture](https://github.com/yjz211/vivid-illustration-skill/blob/main/channels/vivid-architecture-diagram-skill/SKILL.md) | 先确定对象和关系，再选择结构、视觉层次和可编辑图件 | 架构图共用文件与 PPTX 说明必须一并读取；遵守其自定义许可 |
| [frontend-slides](https://github.com/zarazhangrui/frontend-slides/blob/main/SKILL.md) | 按内容密度与正式程度选择少量版式；统一字体、间距与颜色；先读风格索引，再读所选方案 | 主要制作 HTML；PPT 转换方向是 PPT→HTML，PDF 路线可能使用截图。制作 PPT 时借鉴布局，再用原生对象实现 |
| [Baoyu slide-deck](https://github.com/JimLiu/baoyu-skills/blob/main/skills/baoyu-slide-deck/SKILL.md) | 一句话核心信息；每页分别构思叙事目的、内容、视觉形式和布局 | 默认 PPTX 合并脚本把每页图片放进幻灯片，不能逐项编辑。学术 PPT 主要借鉴构思；生图后端按实际环境核实 |
| [Slidev 官方 skill](https://github.com/slidevjs/slidev/blob/main/skills/slidev/SKILL.md) | 公式逐步展开、代码与结果联动、讲者备注；参考真实主题和展示案例 | 适合代码讲解或交互报告，依赖 Node/浏览器。普通 pptx 导出为图片页；pptx-editable 可重建部分文本和形状，但公式、SVG 等仍可能为图片，失败页还可能整页回退 |
| [Scientific Schematics](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-schematics/SKILL.md) | 概念插图的结构与迭代检查 | 当前主要输出 PNG，生成路线依赖 OpenRouter；不承担精确数据、公式或原生可编辑结构图 |

## 常见任务怎么组合

| 本次任务 | 从哪些方法开始 | 应落实到作品中的内容 |
| --- | --- | --- |
| 论文组会或会议 PPT | Nature + paper-to-slides，版式不足时补 presentation-creator 或 frontend-slides | 科学主线、核心图、逐页重点与讲解顺序；当前宿主制作原生 PPT |
| 数学 Beamer | Math Beamer + paper-to-slides | 定义和定理的依赖、证明路线、保留必要条件、讲稿与实际编译检查 |
| 基金或论文方法图 | Vivid + 当前题材的优秀原论文图 | 明确对象、作用和关系，先写准确标签，再制作可编辑图 |
| 修改已有 PPT 或模板 | 当前宿主工具，按需要参考 Anthropic、MiniMax；Google Slides 模板使用对应连接器 | 保留既有样式与用户修改，重建必要对象，实际渲染修改页 |
| 讲算法、代码或交互演示 | Slidev，用户要求 PPT 时仍按目标格式制作 | 分步解释、同步强调公式和结果，逐项检查导出后的编辑能力 |

按当前难点选用，来源不必固定成套；一个来源解决了问题即可继续。别把“多参考”变成重复制作多套稿件。

## 读取时别丢掉配套文件

**Vivid：**以仓库根为工作根，先读架构图入口与 `architecture/COMMON.md`；新建资产路线按需读 `architecture/WORKFLOW.md`、`architecture/catalog.json` 和所选资产的 `TEMPLATE.md`；原生 PPTX 读 `architecture/PPTX.md`。保留所需根级资源、脚本、字体和 `requirements-architecture.txt`，不能只拿子通道的 SKILL.md。其新文件默认 A/B 选择不适用于当前用户已授权的自主单方案任务；不改上游文件，明确本次任务要求后独立使用。实际 Office 验证只有在具备相应环境并执行后才能声称完成。

**Nature paper2ppt：**先读 `skills/nature-paper2ppt/manifest.yaml` 及其 `always_load`，包括 `static/core/` 下的 principles、toolchain、workflow、output-and-quality 和 `../nature-shared/core/terminology-ledger.md`，再读匹配的 `static/fragments/paper_type/` 文件。按需读图件、布局和自审资料；按实际版本使用其审核脚本。以 manifest 的真实路径为准，不误把 `static/core/` 简写成不存在的 `core/`。理论报告不硬补实验或消融，局部改稿不重跑整套论文读入。

**Math Beamer：**先读 `math-beamer-slides-skill/references/index.md`，按需读 mathematical-statements、proof-exposition、notation-and-dependencies、math-review-checklist 与 quality-standards。运行验证脚本前核对接口；使用 TeX 编译与 PDF 预览。其英文、完整 seminar、背景位图、禁 overlay 或成果页等默认值不成为本流程硬规则。PPT 数学页可以借用审阅方法，但不能擅自改交付格式。

**Scientific Slides：**读 `references/presentation_workflow.md`；按当前任务读 `references/beamer_guide.md` 或 `assets/powerpoint_design_guide.md`，视觉审核读 `references/visual_review_workflow.md`，执行脚本前读 `references/script_reference.md`。可单独使用叙事和可编辑页面指导，不必采用整页生图；固定页数、引用篇数和每分钟页数不适合作为所有报告的门槛。

**Scientific Schematics：**按需读 `references/iterative_refinement.md` 与 `best_practices.md`。当前图像生成路线依赖 OpenRouter 和可用额度，主要交付 PNG；不能包装成 PDF 就称矢量或原生可编辑。模型评分只作辅助，实际标签、关系和图像仍需逐项查看。当前环境若提供适合的图像生成工具，优先遵循宿主工具规范。

**故事与讲稿：**presentation-creator 按需读 `references/story-structure.md`、`writing-slides.md`、`visual-design.md` 与 `output-formats.md`；paper-to-slides 读 `references/storytelling.md`、`verification.md`。吸收听众分析、原图选择与逐页讲解方法，不强加固定页数、反复访谈或额外审批。

**页面与导出：**MiniMax 读 `references/pitfalls.md`；Anthropic 按当前入口所列路径读创建、模板修改或检查部分；Addsum 只读相关章节及其实际调用的渲染/验证文件。外部 skill 使用 Python、Node 或某个模型，不意味着当前宿主也允许或需要采用同一路线。

**视觉构思：**frontend-slides 先看 `STYLE_PRESETS.md` 与 `bold-template-pack/selection-index.json`，再打开选中的方案；Baoyu 读 `references/analysis-framework.md`、`outline-template.md`，需要导出时检查 `scripts/merge-to-pptx.ts`；Slidev 读 `references/diagram-latex.md`、`core-exporting.md`，并查看[展示案例](https://sli.dev/resources/showcases)和[主题](https://sli.dev/resources/theme-gallery)。源码检查能确认输出机制，视觉好坏仍需看实际作品。

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

Vivid 采用自定义个人非商业许可；Anthropic pptx 目录为专有许可，只引用来源与一般方法，不将这些文件复制或改编进本 MIT 项目。Nature 根许可为 Apache-2.0；Math Beamer、K-Dense、paper-to-slides、mblode、MiniMax、Addsum、frontend-slides、Baoyu 与 Slidev 本次核实的根许可为 MIT。OpenAI 当前入口未据本次检查确认可重新分发的许可，只外链。PaperBanana 根许可为 Apache-2.0、skill 另有声明，AutoFigure 为 MIT。外部项目、模板、论文图、字体和素材分别适用各自许可；本 skill 只保存原创流程和来源链接。
