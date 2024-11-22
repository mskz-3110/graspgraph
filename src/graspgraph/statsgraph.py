import numpy as np
import plotly.graph_objects as pgo
from .color import *
from .array import *
from .figure import *

class SimpleStats:
  def __init__(self, values):
    self.__Values = tuple(values)
    if 0 < len(values):
      self.__Avg = sum(values) / len(values)
      self.__Min = min(values)
      self.__Max = max(values)
    else:
      self.__Avg = self.__Min = self.__Max = 0

  @property
  def Values(self):
    return self.__Values

  @property
  def Avg(self):
    return self.__Avg

  @property
  def Min(self):
    return self.__Min

  @property
  def Max(self):
    return self.__Max

class MultipleStats:
  def __init__(self, values, maxCount = 0):
    self.__Values = tuple(values)
    self.__Avg = []
    self.__Min = []
    self.__Max = []
    count = len(values)
    maxCount = min(max(maxCount, 0), count)
    if count <= maxCount:
      self.__Avg = values
    else:
      for splitedValues in np.array_split(values, maxCount):
        stats = SimpleStats(splitedValues)
        self.__Avg.append(stats.Avg)
        self.__Min.append(stats.Min)
        self.__Max.append(stats.Max)
    self.__Avg = tuple(self.__Avg)
    self.__Min = tuple(self.__Min)
    self.__Max = tuple(self.__Max)

  @property
  def Values(self):
    return self.__Values

  @property
  def Avg(self):
    return self.__Avg

  @property
  def Min(self):
    return self.__Min

  @property
  def Max(self):
    return self.__Max

class StatsgraphInputAxis:
  def __init__(self, values, maxCount = 0, tick = 1, tickFormat = "d"):
    self.__Values = tuple(values)
    self.MaxCount = maxCount
    self.Tick = tick
    self.TickFormat = tickFormat

  @property
  def Values(self):
    return self.__Values

  @property
  def MaxCount(self):
    return self.__MaxCount

  @MaxCount.setter
  def MaxCount(self, value):
    if value <= 0:
      value = max(len(self.__Values), 1)
    self.__MaxCount = value

class Statsgraph:
  def __init__(self, xInputAxis, yInputAxis, lineRGB = RGB()):
    self.__XInputAxis = xInputAxis
    self.__YInputAxis = yInputAxis
    self.__LineRGB = lineRGB
    yMultipleStats = MultipleStats(yInputAxis.Values, xInputAxis.MaxCount)
    scale = len(yInputAxis.Values) / xInputAxis.MaxCount
    if len(yMultipleStats.Avg) == len(yInputAxis.Values):
      xValues = xInputAxis.Values
      figure = pgo.Figure(data = [pgo.Scatter(mode = "lines", x = xInputAxis.Values, y = yInputAxis.Values, line = dict(color = lineRGB.HexCode, width = 5))])
      xDtick = xInputAxis.Tick
    else:
      xStep = xInputAxis.Values[1] - xInputAxis.Values[0]
      xValues = np.delete(Array.arange(xInputAxis.Values[0], xInputAxis.Values[-1], xStep * scale), 0)
      for i in range(len(xValues) - 1):
        xValues[i] -= xStep
      xValues[-1] = xInputAxis.Values[-1]
      fillColor = """rgba({}, {}, {}, 0.15)""".format(*lineRGB.Array)
      figure = pgo.Figure(data = [
        pgo.Scatter(showlegend = False, mode = "lines", x = xValues, y = yMultipleStats.Min, line = dict(color = lineRGB.HexCode, width = 0)),
        pgo.Scatter(showlegend = False, mode = "lines", x = xValues, y = yMultipleStats.Avg, line = dict(color = lineRGB.HexCode, width = 5), fillcolor = fillColor, fill = "tonexty"),
        pgo.Scatter(showlegend = False, mode = "lines", x = xValues, y = yMultipleStats.Max, line = dict(color = lineRGB.HexCode, width = 0), fillcolor = fillColor, fill = "tonexty")])
      xDtick = max(scale, xInputAxis.Tick)
      if xValues[-1] <= xDtick:
        xDtick = xValues[1] - xValues[0]
    ySimpleStats = SimpleStats(yInputAxis.Values)
    figure.update_xaxes(zeroline = True, zerolinecolor = "black", zerolinewidth = 0.5, tickformat = xInputAxis.TickFormat, dtick = xDtick, linecolor = "black", linewidth = 3, gridcolor = "black", griddash = "dot", mirror = True)
    figure.update_yaxes(zeroline = True, zerolinecolor = "black", zerolinewidth = 0.5, tickformat = yInputAxis.TickFormat, dtick = yInputAxis.Tick, linecolor = "black", linewidth = 3, gridcolor = "black", griddash = "dot", mirror = True)
    figure.update_layout(title = dict(text = "", font = dict(color = "black", size = 26), x = 0.5),
      xaxis = dict(title = "", color = "black"),
      yaxis = dict(title = "", color = "black", range = [ySimpleStats.Min, min(yInputAxis.Tick * yInputAxis.MaxCount + ySimpleStats.Min, ySimpleStats.Max)]),
      font = dict(size = 14),
      paper_bgcolor = "white", plot_bgcolor = "white")
    self.__Figure = figure

  @property
  def XInputAxis(self):
    return self.__XInputAxis

  @property
  def YInputAxis(self):
    return self.__YInputAxis

  @property
  def LineRGB(self):
    return self.__LineRGB

  @property
  def Args(self):
    return [self.__XInputAxis, self.__YInputAxis, self.__LineRGB]

  @property
  def Figure(self):
    return self.__Figure

  def to_figure_helper(self):
    return FigureHelper(self.__Figure)
