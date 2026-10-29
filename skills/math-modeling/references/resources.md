# 资料与技能入口

核查日期：2026-10-29。按任务读取相关部分，避免同时启动多个不一致的完整流程。

| 需要什么 | 优先入口 | 使用约定 |
| --- | --- | --- |
| 用户提到的本地 math-model-skills | 当前宿主技能列表及用户明确提供的安装位置 | 先核实名称、来源与实际 SKILL.md，不根据近似名称猜测 |
| 可替换的建模资料候选 | [WuXinbo-bo/Math-model-skills](https://github.com/WuXinbo-bo/Math-model-skills/blob/main/SKILL.md) 与 [model-quality-contracts.md](https://github.com/WuXinbo-bo/Math-model-skills/blob/main/references/model-quality-contracts.md) | 根技能实际名为 meta-model-agent，尚未确认与用户本地技能相同；按需参考变量、机制、数学表达和证据检查 |
| 中文润色 | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh/blob/main/SKILL.md) | 保留事实、公式、结论强度与学术语气 |
| Nature 绘图 | [Yuan1z0825/nature-skills / nature-figure](https://github.com/Yuan1z0825/nature-skills/blob/main/skills/nature-figure/SKILL.md) | 核实相邻 nature-shared 和所需脚本；不只复制一个子目录 |
| 完整绘图流程 | [本项目 paper-figures](https://github.com/Song921012/Research-Flow-Skills/tree/main/skills/paper-figures) | 自主选图，真实数据绘制，看图修改并交接 |
| CUMCM 模板候选 | [latexstudio/CUMCMThesis](https://github.com/latexstudio/CUMCMThesis) | 用户原有 CUMCMThesis-master 优先；模板与本届赛事适用性需核对，不能替代官网要求 |
| 当届比赛规则 | 比赛主办方官网 | 当前规则决定匿名、AI 说明、附录、篇幅和提交格式 |

## 原作者优先，用户 fork 备用

- Humanizer-zh 备用：[Song921012/Humanizer-zh](https://github.com/Song921012/Humanizer-zh)。
- Nature 备用：[Song921012/nature-skills](https://github.com/Song921012/nature-skills)，相同路径 skills/nature-figure/SKILL.md。
- 优先使用原作者来源的安装或仓库；只有原仓库删除或确实不可用，才使用已核实的备用副本。短暂限流应先核实；备用更新不改变主来源优先级。
- 本次未核实用户的 Math-model-skills 或 CUMCMThesis fork，不填写猜测的备用地址。

已安装的 skill 按宿主实际接口使用；可读取时打开入口与所需资源。外部源不可用时按本流程继续可独立完成的工作，不假称已调用。

建模候选含固定目录、额外阶段确认、三轮评审等默认值，不能覆盖用户的目录、任务范围与至少两轮审改要求。humanizer-zh 只用于语言编辑，不用于隐去实际使用情况。

Math-model-skills 候选与 Humanizer-zh 当前为 MIT；Nature 根目录为 Apache-2.0，第三方素材另有声明。本次未确认 CUMCMThesis 的完整再分发许可，只保存模板来源链接，不将其打包为本仓库 MIT 内容。

