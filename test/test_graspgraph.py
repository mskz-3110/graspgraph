import graspgraph as gg
import numpy as np
import pytest

def figure_set_title_text(figure, statsgraph):
  figure.LayoutTitleText = """<b>[graspgraph]<br>X(Dtick:{:.3f} MaxCount:{}) Y(Dtick:{:.3f} MaxCount:{})</b>""".format(
    figure.Figure.layout.xaxis.dtick, statsgraph.XInputAxis.MaxCount,
    figure.Figure.layout.yaxis.dtick, statsgraph.YInputAxis.MaxCount)
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
    gg.StatsgraphInputAxis([]),
    gg.StatsgraphInputAxis([]))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./image/sample_none.png")

  statsgraph = gg.Statsgraph(
    gg.StatsgraphInputAxis([1, 2, 3, 4, 5]),
    gg.StatsgraphInputAxis([1, 2, 1000, 4, 5]),
    gg.FigureColors(layoutTitle = "red", line = "red"))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./image/sample_over.png")

  green = gg.Color.from_hex_code("#00FF00")
  rgbGreen = green.to_string("""rgb({R}, {G}, {B})""")
  rgbaGreen = green.to_string("""rgba({R}, {G}, {B}, 0.15)""")
  statsgraph = gg.Statsgraph(
    gg.StatsgraphInputAxis(gg.Array.arange(10, 30, 5), tick = gg.FigureTick(5)),
    gg.StatsgraphInputAxis(gg.Array.arange(100, 300, 50), tick = gg.FigureTick(50)),
    gg.FigureColors(layoutTitle = "red", xTitle = "blue", yTitle = "blue", grid = "white", background = "gray", line = rgbGreen, fill = rgbaGreen))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./image/sample_coloring.png")

  yValues = []
  for value in np.sin(np.linspace(0, 2 * np.pi, 60)):
    yValues.append(value * 10 + 20)
  statsgraph = gg.Statsgraph(
    gg.StatsgraphInputAxis(gg.Array.arange(1, len(yValues), 1)),
    gg.StatsgraphInputAxis(yValues),
    gg.FigureColors(layoutTitle = rgbGreen, line = rgbGreen, fill = rgbaGreen))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./image/sample_sin_simple.png")

  statsgraph.XInputAxis.Tick.Dtick = 5
  statsgraph.XInputAxis.MaxCount = 10
  statsgraph.YInputAxis.Tick.Dtick = 6
  statsgraph.YInputAxis.MaxCount = 5
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./image/sample_sin_multiple.png")

  statsgraph.XInputAxis = gg.StatsgraphInputAxis(gg.Array.arange(-0.9, 0.9, 0.2), tick = gg.FigureTick(0.2, ".1f"))
  statsgraph.YInputAxis = gg.StatsgraphInputAxis(gg.Array.arange(-2.25, 2.25, 0.5), tick = gg.FigureTick(0.5, ".1f"))
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./image/sample_float_simple.png")

  statsgraph.XInputAxis.MaxCount = 5
  statsgraph.YInputAxis.Tick.Dtick = 1
  statsgraph.YInputAxis.MaxCount = 5
  figure = statsgraph.to_figure_helper()
  figure_set_title_text(figure, statsgraph)
  figure.write_image("./image/sample_float_multiple.png")
