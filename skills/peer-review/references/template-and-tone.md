# 模板与中性口吻

使用主说明中的 review-template.tex。模板由用户常用的审稿 LaTeX 提炼，保留 amsart、原有版面尺寸、报告标题和编号意见，已去除旧稿名、稿号、作者信息、注释残留和具体评审内容。

## 组织方式

- 开头准确概括论文问题与工作，必要时说明整体需要改进的方面；不预填“创新突出”“结果重要”等评价。
- 主要意见采用编号列表。一条围绕一个明确问题，给定位、理由和可执行的修改请求。
- 记号、引用、typo 等较小问题按需要另列；没有问题就删除空段。
- 建议结论根据实际审查填写。审稿系统要求将推荐结果只提供给编辑时，作者可见报告按其要求组织。

## 句式参考

- “The manuscript studies ...”
- “In Theorem ..., please clarify whether ... is assumed.”
- “The argument from ... to ... requires an additional justification because ...”
- “Please explain how ... supports the conclusion that ...”
- “In Figure ..., the meaning of ... should be specified.”

按稿件实际问题填写，不把句式当现成审稿结论。确认有错误时可以直接指出并给出理由；语气中性不意味着回避关键问题。

## 使用模板

复制模板到本次报告目录，填写稿件信息、概述、意见和必要建议；正式交付前清除所有填写位置与无用小节。模板默认英文，依赖标准 TeX 宏包和 amsart；用 pdflatex 连续编译两次，实际查看公式、编号、换页和页边界。

报告属于本次审稿材料。公开的 skill 只保留空白模板，不将真实稿件或评审意见写回公开仓库。
