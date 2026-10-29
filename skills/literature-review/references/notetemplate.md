# 中文 NoteTemplate

使用随技能提供的 [NoteTemplate.zip](../assets/NoteTemplate.zip)。这是用户提供并指定的模板，原包保留中文与英文两套；独立文献综述默认用中文版本，不需要每次重新索要。

1. 将模板解压到本次任务的新目录，使用 NoteTemplate/Chinese/main.tex 作为入口。
2. 保留 style.tex、chapters/、figures/ 和 references.bib 的关系。填写题目与正文，作者信息以当前用户明确提供的信息为准。
3. 模板使用 ctexbook、XeLaTeX 和 biblatex/biber；中文字体为 Noto CJK，西文字体为 DejaVu。先确认环境具备所需字体和宏包，不能把缺字或编译失败当作完成。
4. 在 Chinese/ 中依次运行 xelatex main.tex、biber main、xelatex main.tex、xelatex main.tex；实际任务没有允许编译时遵守其限制。
5. 编译后查看 PDF 的中文、公式、引用、目录和页面裁切。保留可编辑源码；缺少环境时明确报告没有完成编译验证。

原始包 SHA-256：36ceef0dd7e42a4fd778c32d792a988f9a40758c9f08d157beef3b1375b6ff00。

用户提供新版模板时优先使用新版。不要把笔记模板自动用于期刊论文；期刊论文模板由用户指定。
