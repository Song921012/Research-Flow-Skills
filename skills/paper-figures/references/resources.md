# 资料使用索引

构思或遇到具体绘图问题时读本页，再打开有关来源的具体章节、范图或代码。
先复用项目中已检查过的相似案例；新的问题再补充查找，不必每次通读全部网站。
每次取用留下简短的“参考什么、改变什么、检查什么”，无法取得正文时不要声称已经阅读。

| 遇到的问题 | 优先来源 | 转成什么动作，怎样检查 |
| --- | --- | --- |
| 多条轨线重叠，难以比较 | Data-to-Viz 的 [spaghetti.Rmd](https://github.com/holtzy/data_to_viz/blob/master/caveat/spaghetti.Rmd)；R Graph Gallery 的[分面示例](https://github.com/holtzy/R-graph-gallery/blob/master/web-line-chart-small-multiple-all-group-greyed-out.Rmd) | 按比较目的选择叠加、分面或重点突出，必要时直接标注线尾；核对曲线身份、尺度和未被隐藏的背景信息。 |
| 局部结构在主图中难以辨认 | Rougier 的 [annotation-zoom.py](https://github.com/rougier/scientific-visualization-book/blob/master/code/ornaments/annotation-zoom.py) | 对有科学意义的区域设置放大图，标出范围与连接关系；检查原数据、坐标和主图一致，没有局部分析需求时省略。 |
| 多面板布局或色条占位不协调 | Matplotlib 的 [layouts.py](https://github.com/matplotlib/cheatsheets/blob/main/scripts/layouts.py)；[figures4papers 示例入口](https://github.com/ChenLiu-1996/figures4papers/blob/main/scientific-figure-making/references/demos.md) | 先确定阅读顺序，再安排面板、图例和色条；检查最终尺寸、对齐与各面板所需的比较关系，外部示例按其许可使用。 |
| 解场、预测场、误差场的颜色难以比较 | Matplotlib [颜色选择](https://matplotlib.org/stable/users/explain/colors/colormaps.html)与[数值映射](https://matplotlib.org/stable/users/explain/colors/colormapnorms.html) | 按顺序量、正负差异或周期量选择映射；可比解场共享数值映射，误差场按定义设置并标明色标；核对极值、单位和不同尺度。 |
| 收敛、精度与计算成本比较 | [SciML 的公平比较规则](https://docs.sciml.ai/SciMLBenchmarksOutput/dev/#Rules:-Optimal,-Fair,-and-Reproducible) | 用实际误差与网格尺度或耗时作图；核对误差定义、计时范围、软硬件条件和失败结果，必要时比较达到相同精度的成本。 |
| 多次实验、配对或不确定性 | Seaborn 的[误差区间说明](https://seaborn.pydata.org/tutorial/error_bars.html)与[分类数据说明](https://seaborn.pydata.org/tutorial/categorical.html) | 按真实重复单位选择原始点、配对连线、分布或区间；写明样本量、聚合方式与区间含义，不把相关观测数当独立样本量。 |
| 字体、线宽、导出样式需要整理 | [SciencePlots 样式源文件](https://github.com/garrettj403/SciencePlots/blob/master/src/scienceplots/styles/science.mplstyle) | 只采用适用设置，核实字体、TeX 依赖、裁切与实际输出尺寸；打开导出文件检查，不能把套用样式当作质量证明。 |
| 论文图需适应最终版面 | [Nature Research Figure Guide](https://research-figure-guide.nature.com/figures/)及目标期刊当前官方要求 | 核对信息层次、标注、尺寸和导出条件；按最终排版检查文字和线条，Nature 资料不替代其他期刊要求。 |

## 学论文图时看什么

选择研究问题、数据形态和比较任务相近的论文，阅读图注与必要正文。
记录具体借鉴的表达、标注或布局；图的好看程度和刊物名称不能替代适用性判断。
不得复制他人结果或把数值参考解称为精确解；复制代码、素材时核对来源和许可。
Vivid、Nature Figure、figures4papers 等技能的入口和许可边界，按主说明直接链接的其他技能文件核对。

本页是原创使用索引，外部内容保持各自许可。访问日期和实际阅读范围随具体任务记录。
