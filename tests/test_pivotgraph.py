import graspgraph as gg

def figure_set_title_text(figure):
  figure.LayoutTitleText = "<b>[pivotgraph]</b>"
  figure.XTitleText = "金額(百万円)"
  figure.YTitleText = "月次"

def test_pivotgraph():
  pivotTable = gg.PivotTable([
    gg.PivotBar("収入", [1, 2, 3], ["1月", "2月", "3月"]),
    gg.PivotBar("支出", [-1, -2.5, -2], ["1月", "2月", "3月"]),
    gg.PivotBar("利益", [0, -0.5, 1], ["1月", "2月", "3月"]),
  ])
  pivotTableArray = [
    ["", "収入", "支出", "利益"],
    ["1月", 1, -1, 0],
    ["2月", 2, -2.5, -0.5],
    ["3月", 3, -2, 1],
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
    ["1月", 1, -1, 0],
    ["2月", 2, -2.5, -0.5],
    ["3月", 3, -2, 1],
  ])
  pivotgraph = gg.Pivotgraph(gg.PivotgraphAxis(pivotTable, gg.FigureTick(2)), gg.PivotgraphColors(bars = ["blue", "red", "green"]))
  figure = pivotgraph.to_figure()
  figure_set_title_text(figure)
  figure.Write("./images/pivot/usage.png")
