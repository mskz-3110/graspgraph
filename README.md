# graspgraph
Create easy-to-understand graphs

## Concept
Make it easier to understand with graphs

### Stats
![](./images/stats/usage.png)

### Database ER diagram-like
![](./images/dber/usage.png)

### Pivot table
![](./images/pivot/usage.png)

## What is possible
### statsgraph
1. Graphing statistics

### dbergraph
1. Graphing database table definition information

### pivotgraph
1. Graphing a pivot table

## Reason for development
- I want to make things that are difficult to understand through text alone easier to understand by creating graphs

## Versions

|Version|Summary|
|:--|:--|
|0.3.4|Add pivotgraph|
|0.2.5|Refactoring|
|0.2.4|Add dbergraph|
|0.1.0|Release graspgraph(statsgraph)|

## Installation
### [graspgraph](https://pypi.org/project/graspgraph/)
`pip install graspgraph`

### [Graphviz](https://graphviz.org/download/)
Required for PDF output

### [Poppler](https://github.com/Belval/pdf2image?tab=readme-ov-file)
Required for PDF image conversion

## Usage
### statsgraph
![](./images/stats/usage.png)
```python
import graspgraph as gg

statsgraph = gg.Statsgraph(
  gg.StatsgraphAxis([1, 2, 3, 4, 5]),
  gg.StatsgraphAxis([11, 12, 13, 14, 15]),
  gg.FigureColors(line = "blue"))
figure = statsgraph.to_figure()
figure.LayoutTitleText = "<b>[statsgraph]<br>タイトル</b>"
figure.XTitleText = "X軸"
figure.YTitleText = "Y軸"
figure.Write("./statsgraph.png")
```

### dbergraph
![](./images/dber/usage.png)
```python
import graspgraph as gg

prefix = "./database"
dbergraph = gg.Dbergraph(gg.Database.from_file_path(gg.Path.join(prefix, "yaml")))
dbergraph.Database.update()
dot = dbergraph.to_dot()
dot.TitleText = "<b>[dbergraph]</b>"
pdfFilePath = gg.Path.join(prefix, "pdf")
pngFilePath = gg.Path.join(prefix, "png")
dot.Write(pdfFilePath)
gg.Pdf.convert(pdfFilePath, pngFilePath)
```

### pivotgraph
![](./images/pivot/usage.png)
```python
import graspgraph as gg

pivotTable = gg.PivotTable.from_array([
  ["", "収入", "支出", "利益"],
  ["1月", 1, 2, 3],
  ["2月", -1, -2.5, -2],
  ["3月", 0, -0.5, 1],
])
pivotgraph = gg.Pivotgraph(gg.PivotgraphAxis(pivotTable, gg.FigureTick(2)), gg.PivotgraphColors(bars = ["blue", "red", "green"]))
figure = pivotgraph.to_figure()
figure.LayoutTitleText = "<b>[pivotgraph]</b>"
figure.XTitleText = "金額(百万円)"
figure.YTitleText = "月次"
figure.Write("./images/pivot/usage.png")
```

## CLI
### pdf.convert
Convert PDF to image

#### 1. Image(PNG) conversion by CLI execution

```
pdf.convert # <pdf file path> <image file path>
```
`graspgraph pdf.convert graph.pdf graph.png`
```
graph.png is done.
```
