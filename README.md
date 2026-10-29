# Research-Flow-Skills

把经常重复的科研工作整理成简短、可扩展的 AI 协作流程。第一项可用流程是 **论文画图（paper-figures）**：从论文故事与已有结果出发，由 AI 主动选图、查参考、绘制精修并完成审核交接。

## 以后怎样说

> 按论文画图流程处理这篇论文和已有结果。选图、参考查找和审美由你决定，交付成图、代码与简短图注。

也可以只说：

> 只调整这张图的图例和字号，保留数据、计算和其他内容。

在已经安装并支持选择 skill 的环境中，选择 **论文画图 / paper-figures**。Codex 可用 `$paper-figures`；其他宿主使用其支持的方式。尚未安装时，让 AI 先读取 [主流程](skills/paper-figures/SKILL.md)，再按其中的资料索引处理你的文件。

## 四步做什么

| 步骤 | 要完成的工作 |
| --- | --- |
| 读论文和数据，理清需求 | 明确图要回答什么，已有数据能支持什么，保留已有修改。 |
| 查资料、找范例、构思图形 | 按问题读取资料、范图与适用 skills，由 AI 自主选择表达。 |
| 画图、看图、改图 | 用真实输入执行绘图，打开最终尺寸的输出并修复具体问题。 |
| 审核与交接 | 分别核对数据和图像，交付成图、可运行代码、数据指向与图注。 |

用户不需要先选出喜欢的范图，也不需要逐轮批准配色和布局。科学含义缺失时，先查已有材料，再核实必要信息。只改样式时复用已有实验。

## 资料怎样用起来

[资料使用索引](skills/paper-figures/references/resources.md) 把来源组织成“遇到什么问题 → 查哪里 → 采取什么动作 → 怎样检查”。

例如，轨线拥挤时查分面与标注；局部结构看不清时查放大图；比较解场时查颜色映射；交付前查实际尺寸、裁切和数据对应。每次只读相关资料。

[可选 skills](skills/paper-figures/references/optional-skills.md) 记录 Vivid Illustration、Nature Figure 和 figures4papers 的准确入口。宿主支持且来源适用时可以读取或调用；本流程也能使用自己的参考与代码独立执行。写下技能名称或 GitHub 链接不会自动安装依赖。

## 安装到自己的工具

保留 `skills/paper-figures/` 的完整目录，包括 references、scripts 和 agents。

- **Codex 项目：** 把完整目录放到项目的 `.agents/skills/paper-figures/`。
- **Claude Code 项目：** 把完整目录放到项目的 `.claude/skills/paper-figures/`。
- **支持从 GitHub 导入 skills 的环境：** 使用本仓库，选择 `skills/paper-figures`；具体入口以该工具当前支持为准。
- **普通对话：** 提供主流程及相关资料，同时提供需要处理的数据、代码或图像。实际画图需要运行代码和查看图像的能力。

仓库保存和更新流程；当前工具负责发现与执行。更新仓库后，确认本地安装副本也已更新。

## 看一个可以重画的例子

这里用解析热方程解的线性插值做演示，不使用私人研究数据，也不宣称新的算法成果。

![解析函数插值的四面板演示](examples/output/interpolation.png)

输入、绘图代码与图注说明见 [演示说明](examples/README.md)。使用 Python 3.10 或更新版本，在仓库根目录运行：

```bash
python -m pip install -r requirements-demo.txt
python examples/render_demo.py
python tests/check_export.py
```

示例只重画保存的 CSV；导出辅助代码保持指定的物理尺寸，并默认保护已有输出。绘图结果仍需要人工或可看图的 AI 检查。

## 如何继续完善

先在真实绘图任务中使用，保存经数据核对和视觉检查的有效案例。把经验写成短小的适用条件与做法；用户反馈另用于校准偏好。向公开仓库提交案例前，确认有权公开对应数据、稿件、代码与图片。

将来新增文献整理、论文修改、基金写作等任务时，各自建立范围清楚的 skill。当前先把论文画图做扎实。

- [开发依据与技巧](docs/skill-design.md)
- [实际验证记录](docs/validation.md)
- [后续行为检查案例](tests/cases.md)

## 许可

本仓库的原创流程、说明、代码和演示采用 [MIT License](LICENSE)。

外部链接项目继续适用各自许可；本仓库没有打包、改编或重新授权其 skill 文本、代码、模板或图片。特别是 Vivid 的自定义非商业许可、figures4papers 的 CC BY-NC 4.0，以及 Nature 中的第三方资源，见 [第三方来源说明](THIRD_PARTY_NOTICES.md)。

