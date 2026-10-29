# 外部技能详情

按本次所选来源读取对应条目；核查范围和组合方法见[资料与组合方法](resources.md)。

## 目录

- [内容与故事](#先把内容讲清楚)
- [可编辑演示文稿](#制作和修改可编辑演示文稿)
- [版式与图示](#丰富版式和图示)
- [配套文件](#读取时别丢掉配套文件)
- [备用来源与许可](#来源优先顺序与许可)

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

## 读取时别丢掉配套文件

**Vivid：**以仓库根为工作根，先读架构图入口与 `architecture/COMMON.md`；新建资产路线按需读 `architecture/WORKFLOW.md`、`architecture/catalog.json` 和所选资产的 `TEMPLATE.md`；原生 PPTX 读 `architecture/PPTX.md`。保留所需根级资源、脚本、字体和 `requirements-architecture.txt`，不能只拿子通道的 SKILL.md。其新文件默认 A/B 选择不适用于当前用户已授权的自主单方案任务；不改上游文件，明确本次任务要求后独立使用。实际 Office 验证只有在具备相应环境并执行后才能声称完成。

**Nature paper2ppt：**先读 `skills/nature-paper2ppt/manifest.yaml` 及其 `always_load`，包括 `static/core/` 下的 principles、toolchain、workflow、output-and-quality 和 `../nature-shared/core/terminology-ledger.md`，再读匹配的 `static/fragments/paper_type/` 文件。按需读图件、布局和自审资料；按实际版本使用其审核脚本。以 manifest 的真实路径为准，不误把 `static/core/` 简写成不存在的 `core/`。理论报告不硬补实验或消融，局部改稿不重跑整套论文读入。

**Math Beamer：**先读 `math-beamer-slides-skill/references/index.md`，按需读 mathematical-statements、proof-exposition、notation-and-dependencies、math-review-checklist 与 quality-standards。运行验证脚本前核对接口；使用 TeX 编译与 PDF 预览。其英文、完整 seminar、背景位图、禁 overlay 或成果页等默认值不成为本流程硬规则。PPT 数学页可以借用审阅方法，但不能擅自改交付格式。

**Scientific Slides：**读 `references/presentation_workflow.md`；按当前任务读 `references/beamer_guide.md` 或 `assets/powerpoint_design_guide.md`，视觉审核读 `references/visual_review_workflow.md`，执行脚本前读 `references/script_reference.md`。可单独使用叙事和可编辑页面指导，不必采用整页生图；固定页数、引用篇数和每分钟页数不适合作为所有报告的门槛。

**Scientific Schematics：**按需读 `references/iterative_refinement.md` 与 `best_practices.md`。当前图像生成路线依赖 OpenRouter 和可用额度，主要交付 PNG；不能包装成 PDF 就称矢量或原生可编辑。模型评分只作辅助，实际标签、关系和图像仍需逐项查看。当前环境若提供适合的图像生成工具，优先遵循宿主工具规范。

**故事与讲稿：**presentation-creator 按需读 `references/story-structure.md`、`writing-slides.md`、`visual-design.md` 与 `output-formats.md`；paper-to-slides 读 `references/storytelling.md`、`verification.md`。吸收听众分析、原图选择与逐页讲解方法，不强加固定页数、反复访谈或额外审批。

**页面与导出：**MiniMax 读 `references/pitfalls.md`；Anthropic 按当前入口所列路径读创建、模板修改或检查部分；Addsum 只读相关章节及其实际调用的渲染/验证文件。外部 skill 使用 Python、Node 或某个模型，不意味着当前宿主也允许或需要采用同一路线。

**视觉构思：**frontend-slides 先看 `STYLE_PRESETS.md` 与 `bold-template-pack/selection-index.json`，再打开选中的方案；Baoyu 读 `references/analysis-framework.md`、`outline-template.md`，需要导出时检查 `scripts/merge-to-pptx.ts`；Slidev 读 `references/diagram-latex.md`、`core-exporting.md`，并查看[展示案例](https://sli.dev/resources/showcases)和[主题](https://sli.dev/resources/theme-gallery)。源码检查能确认输出机制，视觉好坏仍需看实际作品。

## 来源优先顺序与许可

原作者仓库优先；确认删除或确实不可访问后，才使用已核实的用户同源 fork。临时抓取失败先换可用读取方式或重试，不能直接判为删库。

| 原作者 | 已核实备用 |
| --- | --- |
| [yjz211/vivid-illustration-skill](https://github.com/yjz211/vivid-illustration-skill) | [Song921012/vivid-illustration-skill](https://github.com/Song921012/vivid-illustration-skill) |
| [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | [Song921012/nature-skills](https://github.com/Song921012/nature-skills) |

其他来源尚未核实用户备用，不猜测地址。共享资源须跟随所用版本；来源可用不代表其所有工具都已安装或运行。

Vivid 采用自定义个人非商业许可；Anthropic pptx 目录为专有许可，只引用来源与一般方法，不将这些文件复制或改编进本 MIT 项目。Nature 根许可为 Apache-2.0；Math Beamer、K-Dense、paper-to-slides、mblode、MiniMax、Addsum、frontend-slides、Baoyu 与 Slidev 本次核实的根许可为 MIT。OpenAI 当前入口未据本次检查确认可重新分发的许可，只外链。PaperBanana 根许可为 Apache-2.0、skill 另有声明，AutoFigure 为 MIT。外部项目、模板、论文图、字体和素材分别适用各自许可；本 skill 只保存原创流程和来源链接。
