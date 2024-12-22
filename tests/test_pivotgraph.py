import graspgraph as gg

def figure_set_title_text(figure):
  figure.LayoutTitleText = "<b>[pivotgraph]</b>"
  figure.XTitleText = "金額(百万円)"
  figure.YTitleText = "月次"

def test_pivotgraph():
  pivotTable = gg.PivotTable(
    ["1月", "2月", "3月"],
    ["収入", "支出", "利益"],
    [[1, 2, 3], [-1, -2.5, -2], [0, -0.5, 1]]
  )
  pivotTableArray = [
    ["", "収入", "支出", "利益"],
    ["1月", 1, 2, 3],
    ["2月", -1, -2.5, -2],
    ["3月", 0, -0.5, 1],
  ]
  assert(pivotTable.to_array() == pivotTableArray)

  pivotgraph = gg.Pivotgraph(gg.PivotgraphAxis(gg.PivotTable()))
  figure = pivotgraph.to_figure()
  figure_set_title_text(figure)
  figure.Write("./images/pivot/sample_empty.png")

  pivotgraph = gg.Pivotgraph(gg.PivotgraphAxis(pivotTable), colors = gg.PivotgraphColors(layoutTitle = "red", xTitle = "blue", yTitle = "green", grid = "white", background = "gray", bars = ["skyblue", "pink", "purple"]))
  figure = pivotgraph.to_figure()
  figure_set_title_text(figure)
  figure.Write("./images/pivot/sample_coloring.png")

def test_pivotgraph_usage():
  pivotTable = gg.PivotTable.from_array([
    ["", "収入", "支出", "利益"],
    ["1月", 1, 2, 3],
    ["2月", -1, -2.5, -2],
    ["3月", 0, -0.5, 1],
  ])
  pivotgraph = gg.Pivotgraph(gg.PivotgraphAxis(pivotTable, gg.FigureTick(2)), gg.PivotgraphColors(bars = ["blue", "red", "green"]))
  figure = pivotgraph.to_figure()
  figure_set_title_text(figure)
  figure.Write("./images/pivot/usage.png")
