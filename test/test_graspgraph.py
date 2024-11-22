import graspgraph as gg
import numpy as np
import pytest

def test_color():
  assert gg.RGB.from_hex_code("#010203").HexCode == "#010203"

def create_layout_title(statsgraph, figure):
  return """<b>[graspgraph]<br>X(Tick:{} MaxCount:{} Dtick:{:.3f}) Y(Tick:{} MaxCount:{} Dtick:{:.3f})</b>""".format(
    statsgraph.XInputAxis.Tick, statsgraph.XInputAxis.MaxCount, figure.XDtick,
    statsgraph.YInputAxis.Tick, statsgraph.YInputAxis.MaxCount, figure.YDtick)

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
    gg.StatsgraphInputAxis(gg.Array.arange(10, 30, 5), tick = 5),
    gg.StatsgraphInputAxis(gg.Array.arange(100, 300, 50), tick = 50),
    gg.RGB(0, 255, 0))
  figure = statsgraph.to_figure_helper()
  figure.set_texts(layoutTitle = create_layout_title(statsgraph, figure), xTitle = "X", yTitle = "Y")
  figure.set_colors(layoutTitle = "red", xTitle = "blue", yTitle = "blue", grid = "white", background = "gray")
  figure.write_image("./image/sample_coloring.png")

  yValues = []
  for value in np.sin(np.linspace(0, 2 * np.pi, 60)):
    yValues.append(value * 10 + 20)
  statsgraph = gg.Statsgraph(
    gg.StatsgraphInputAxis(gg.Array.arange(1, len(yValues), 1)),
    gg.StatsgraphInputAxis(yValues),
    gg.RGB(0, 255, 0))
  figure = statsgraph.to_figure_helper()
  figure.set_texts(layoutTitle = create_layout_title(statsgraph, figure), xTitle = "X", yTitle = "Y")
  figure.LayoutTitleColor = statsgraph.LineRGB.HexCode
  figure.write_image("./image/sample_sin_simple.png")

  statsgraph.XInputAxis.Tick = 5
  statsgraph.XInputAxis.MaxCount = 10
  statsgraph.YInputAxis.Tick = 6
  statsgraph.YInputAxis.MaxCount = 5
  statsgraph = gg.Statsgraph(*statsgraph.Args)
  figure = statsgraph.to_figure_helper()
  figure.set_texts(layoutTitle = create_layout_title(statsgraph, figure), xTitle = "X", yTitle = "Y")
  figure.LayoutTitleColor = statsgraph.LineRGB.HexCode
  figure.write_image("./image/sample_sin_multiple.png")

  statsgraph = gg.Statsgraph(
    gg.StatsgraphInputAxis(gg.Array.arange(-0.9, 0.9, 0.2), tick = 0.2, tickFormat = ".1f"),
    gg.StatsgraphInputAxis(gg.Array.arange(-2.25, 2.25, 0.5), tick = 0.5, tickFormat = ".1f"),
    gg.RGB(0, 255, 0))
  figure = statsgraph.to_figure_helper()
  figure.set_texts(layoutTitle = create_layout_title(statsgraph, figure), xTitle = "X", yTitle = "Y")
  figure.LayoutTitleColor = statsgraph.LineRGB.HexCode
  figure.write_image("./image/sample_float_simple.png")

  statsgraph.XInputAxis.MaxCount = 5
  statsgraph.YInputAxis.Tick = 1
  statsgraph.YInputAxis.MaxCount = 5
  statsgraph = gg.Statsgraph(*statsgraph.Args)
  figure = statsgraph.to_figure_helper()
  figure.set_texts(layoutTitle = create_layout_title(statsgraph, figure), xTitle = "X", yTitle = "Y")
  figure.LayoutTitleColor = statsgraph.LineRGB.HexCode
  figure.write_image("./image/sample_float_multiple.png")
