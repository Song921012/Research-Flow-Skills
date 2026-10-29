# 模板约定

## 期刊论文：由用户指定

先查当前项目是否已经确定模板；没有时问一次目标期刊、文章类型或模板。用户给的模板优先，在其官方投稿要求允许的范围内使用；不要擅自修改 .cls 文件。

下面是常用入口，不把某个出版社模板当作所有期刊都适用。使用时核对当时版本和具体期刊要求，保留模板原许可。

| 选择 | 官方入口 | 使用时注意 |
| --- | --- | --- |
| Elsevier | [LaTeX instructions](https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions) | 再查具体期刊 Guide for Authors，确定 elsarticle 或该刊指定模板 |
| PNAS | [NAS 官方研究论文模板](https://www.overleaf.com/latex/templates/template-for-preparing-your-research-report-submission-to-pnas-using-overleaf-2025/whbdryzwztnd)；[数学单栏模板](https://www.overleaf.com/latex/templates/pnas-latex-template-for-preparing-single-column-mathematics-articles-on-overleaf-2025/drfxwmkrtdhr) | 按文章类型选择，不默认一律双栏 |
| SIAM | [Information for Journal Authors](https://epubs.siam.org/journal-authors) | 按具体期刊选择 Standard 或 Online-only 宏包 |
| JMB | [Journal of Mathematical Biology 作者指南](https://link.springer.com/journal/285/submission-guidelines) | 此处暂按数学与生物背景理解为这个期刊；实际选择前确认全称 |
| PLOS Computational Biology | [LaTeX 模板](https://journals.plos.org/ploscompbiol/s/latex)；[投稿指南](https://journals.plos.org/ploscompbiol/s/submission-guidelines) | 同时核对该投稿阶段的文件与图表要求 |

入口核查日期：2026-10-29。这里只保存官方链接，不把第三方模板重标为本仓库的 MIT 内容。

## 独立中文笔记：使用 NoteTemplate

[NoteTemplate.zip](../assets/NoteTemplate.zip) 是用户指定并提供的原模板。想法综述和后续研究方向默认用它，不用每次重新问。

- 解压到新的任务目录，选择 NoteTemplate/Chinese/main.tex；保留 style.tex、chapters/、figures/ 与 references.bib。
- 中文版使用 ctexbook、XeLaTeX、biblatex/biber；字体是 Noto CJK 与 DejaVu，先核对环境。
- 在 Chinese/ 中依次运行 xelatex main.tex、biber main、xelatex main.tex、xelatex main.tex；遵守当前任务是否允许编译。
- 实际查看 PDF 的中文、公式、引用、目录和版面。无法编译时交付源码并说明具体缺口，不声称已验证。
- 用户给新版模板时优先采用；默认不把笔记模板用于期刊论文。

原始包 SHA-256：36ceef0dd7e42a4fd778c32d792a988f9a40758c9f08d157beef3b1375b6ff00。
