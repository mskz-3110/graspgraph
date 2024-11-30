import graspgraph as gg
import numpy as np

def figure_set_title_text(figure, statsgraph):
  figure.LayoutTitleText = """<b>[graspgraph]<br>X(Dtick:{:.3f} MaxCount:{}) Y(Dtick:{:.3f} MaxCount:{})</b>""".format(
    figure.Figure.layout.xaxis.dtick, statsgraph.XAxis.MaxCount,
    figure.Figure.layout.yaxis.dtick, statsgraph.YAxis.MaxCount)
  figure.XTitleText = "X"
  figure.YTitleText = "Y"

def test_statsgraph():
  stats = gg.SimpleStats([1, 2, 3, 4, 5])
  assert stats.Avg == 3
  assert stats.Min == 1
  assert stats.Max == 5

  stats = gg.MultipleStats([1, 2, 3, 4, 5, 6], 3)
  assert(stats.Avg == (1.5, 3.5, 5.5))
  assert(stats.Min == (1, 3, 5))
  assert(stats.Max == (2, 4, 6))

  statsgraph = gg.Statsgraph(
    gg.StatsgraphAxis([]),
    gg.StatsgraphAxis([]))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./images/stats/sample_empty.png")

  statsgraph = gg.Statsgraph(
    gg.StatsgraphAxis([1, 2, 3, 4, 5]),
    gg.StatsgraphAxis([1, 2, 1000, 4, 5]),
    gg.FigureColors(layoutTitle = "red", line = "red"))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./images/stats/sample_over.png")

  green = gg.Color.from_hex_code("#00FF00")
  rgbGreen = green.to_string("""rgb({R}, {G}, {B})""")
  rgbaGreen = green.to_string("""rgba({R}, {G}, {B}, 0.15)""")
  statsgraph = gg.Statsgraph(
    gg.StatsgraphAxis(gg.Array.arange(10, 30, 5), tick = gg.FigureTick(5)),
    gg.StatsgraphAxis(gg.Array.arange(100, 300, 50), tick = gg.FigureTick(50)),
    gg.FigureColors(layoutTitle = "red", xTitle = "blue", yTitle = "blue", grid = "white", background = "gray", line = rgbGreen, fill = rgbaGreen))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./images/stats/sample_coloring.png")

  yValues = []
  for value in np.sin(np.linspace(0, 2 * np.pi, 60)):
    yValues.append(value * 10 + 20)
  statsgraph = gg.Statsgraph(
    gg.StatsgraphAxis(gg.Array.arange(1, len(yValues), 1)),
    gg.StatsgraphAxis(yValues),
    gg.FigureColors(layoutTitle = rgbGreen, line = rgbGreen, fill = rgbaGreen))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./images/stats/sample_sin_simple.png")

  statsgraph.XAxis.Tick.Dtick = 5
  statsgraph.XAxis.MaxCount = 10
  statsgraph.YAxis.Tick.Dtick = 6
  statsgraph.YAxis.MaxCount = 5
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./images/stats/sample_sin_multiple.png")

  statsgraph.XAxis = gg.StatsgraphAxis(gg.Array.arange(-0.9, 0.9, 0.2), tick = gg.FigureTick(0.2, ".1f"))
  statsgraph.YAxis = gg.StatsgraphAxis(gg.Array.arange(-2.25, 2.25, 0.5), tick = gg.FigureTick(0.5, ".1f"))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./images/stats/sample_float_simple.png")

  statsgraph.XAxis.MaxCount = 5
  statsgraph.YAxis.Tick.Dtick = 1
  statsgraph.YAxis.MaxCount = 5
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./images/stats/sample_float_multiple.png")

def test_statsgraph_usage():
  statsgraph = gg.Statsgraph(
    gg.StatsgraphAxis([1, 2, 3, 4, 5]),
    gg.StatsgraphAxis([11, 12, 13, 14, 15]),
    gg.FigureColors(line = "blue"))
  figure = statsgraph.to_figure_helper()
  figure.LayoutTitleText = "<b>[statsgraph]<br>タイトル</b>"
  figure.XTitleText = "X軸"
  figure.YTitleText = "Y軸"
  figure.write_image("./images/stats/usage.png")
