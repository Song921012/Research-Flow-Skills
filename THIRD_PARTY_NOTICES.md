# 外部资料与许可说明

`researchflowskills` 的原创流程、说明和代码采用根目录的 MIT 许可。以下项目作为可选外部参考，继续适用各自许可。本仓库不随附这些项目的 SKILL 原文、代码、模板、图片或其他素材，也不以 MIT 重新授权它们。外部链接不代表作者认可或共同维护本项目。

核对日期：**2026-10-29**。以下版本用于说明本次核对范围；后来使用其他版本时，应重新查看其许可及所用文件的单独声明。

| 项目 | 核对版本 | 实际许可 | 本仓库的处理 |
| --- | --- | --- | --- |
| [Vivid Illustration Skill](https://github.com/yjz211/vivid-illustration-skill) | [`7adbe09d3d08c55a51733d3b1268fe54f7689559`](https://github.com/yjz211/vivid-illustration-skill/commit/7adbe09d3d08c55a51733d3b1268fe54f7689559) | [Personal Non-Commercial License v1.0](https://github.com/yjz211/vivid-illustration-skill/blob/7adbe09d3d08c55a51733d3b1268fe54f7689559/LICENSE)，自定义许可 | 默认仅保留来源与独立使用入口；不打包、改编或再分发其内容。 |
| [Nature skills / nature-figure](https://github.com/Yuan1z0825/nature-skills/tree/4a04b953c13c57adc51e202ce296597f00d29d67/skills/nature-figure) | [`4a04b953c13c57adc51e202ce296597f00d29d67`](https://github.com/Yuan1z0825/nature-skills/commit/4a04b953c13c57adc51e202ce296597f00d29d67) | 根目录为 [Apache-2.0](https://github.com/Yuan1z0825/nature-skills/blob/4a04b953c13c57adc51e202ce296597f00d29d67/LICENSE)；第三方材料另有声明 | 作为可选外部 skill，不复制其实现；不能将其中第三方资源一概视为 Apache 或 MIT。 |
| [figures4papers](https://github.com/ChenLiu-1996/figures4papers) | [`b709de17da7e8f9a72e51a5de5bced924a01eeab`](https://github.com/ChenLiu-1996/figures4papers/commit/b709de17da7e8f9a72e51a5de5bced924a01eeab) | [CC BY-NC 4.0](https://github.com/ChenLiu-1996/figures4papers/blob/b709de17da7e8f9a72e51a5de5bced924a01eeab/LICENSE) | 提供范图、说明和源码链接；所链接内容不属于本仓库的 MIT 授权范围。 |

## 新增研究与写作来源

以下入口于 2026-10-29 核对，均仅外链，不打包其正文、代码或素材。用户未指定精确仓库时，将它们作为可替换的候选来源。

| 项目 | 核实的许可 | 使用位置 |
| --- | --- | --- |
| [Academic Research Skills](https://github.com/Imbad0202/academic-research-skills) | [CC BY-NC 4.0](https://github.com/Imbad0202/academic-research-skills/blob/main/LICENSE) | deep-research、academic-paper、academic-paper-reviewer |
| [Humanizer](https://github.com/blader/humanizer) | [MIT](https://github.com/blader/humanizer/blob/main/LICENSE) | 学术修订之后的轻量语言编辑 |
| [research-skills / academic-writer](https://github.com/drarunmitra/research-skills/tree/main/academic-writer) | 仓库为 [CC BY 4.0](https://github.com/drarunmitra/research-skills/blob/main/LICENSE) | 学术措辞、论证与引用的一致性 |

论文模板索引只链接出版社、期刊或其发布的官方模板，具体文件继续遵守原许可。用户提供并授权加入的 NoteTemplate.zip 与这些外部模板不同：它作为原始资产随两个新 skill 提供，未打包它所依赖的第三方 TeX 宏包或字体。原包 SHA-256 为 36ceef0dd7e42a4fd778c32d792a988f9a40758c9f08d157beef3b1375b6ff00。

## 用户提供的回复与审稿模板

journal-submission/assets/response-template.tex 与 peer-review/assets/review-template.tex 从用户指定的回复及审稿 LaTeX 样式提炼，保留通用版式和组织方式。稿名、稿号、作者／邮箱、真实审稿意见及未公开科学内容均已移除，使用可填写位置替代。

两个模板分别依赖 elsarticle 与 amsart，以及标准 TeX 宏包。技能不打包或修改这些类文件，也不将它们重新授权为 MIT。编译验证使用的 [elsarticle 官方包](https://ctan.org/pkg/elsarticle) 继续适用其 LPPL 许可，验证依赖不包含在公开仓库中。

## 使用时需要注意的边界

- **Vivid：**现行许可限定个人非商业使用，并限制未经作者书面许可的修改、衍生、二次开发、再分发和商业使用。安装在本地不额外授予这些权利；引用它也不意味着可以将其模板改编后公开发布。
- **Nature：**若在别处复制或修改其 Apache 许可内容，应按原许可保留相应许可、归属和修改声明。特别留意其 `assets/figures4papers/` 中的第三方资源。当前部分内部说明仍提到旧的根 MIT 许可及 figures4papers 过去缺少许可的状态；这些旧描述不能代替本次核对的现行 LICENSE。
- **figures4papers：**复制、修改或分享其受许可材料时，仍须遵守非商业、署名及其他适用条件。将代码放在一个 MIT 仓库中不会消除这些条件。

核心绘图流程使用本项目原创说明，并可用通用绘图库独立执行。若某个外部来源的许可或安装条件不适合当前任务，继续采用独立实现；不通过转存、改名或删去来源来规避原许可。项目中新产生的图和代码，按其实际使用的数据、素材与代码来源分别判断发布条件。
