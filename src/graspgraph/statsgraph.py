import numpy as np
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
      self.__Avg = self.__Min = self.__Max = self.__Values
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
  def __init__(self, values, maxCount = 0, tick = FigureTick()):
    self.__Values = tuple(values)
    self.MaxCount = maxCount
    self.Tick = tick

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
  def __init__(self, xInputAxis, yInputAxis, colors = FigureColors()):
    self.XInputAxis = xInputAxis
    self.YInputAxis = yInputAxis
    self.Colors = colors

  def to_figure(self):
    if len(self.YInputAxis.Values) <= self.XInputAxis.MaxCount:
      xValues = self.XInputAxis.Values
      xDtick = self.XInputAxis.Tick.Dtick
    else:
      tick = self.XInputAxis.Values[1] - self.XInputAxis.Values[0]
      step = (self.XInputAxis.Values[-1] - self.XInputAxis.Values[0] + tick) / self.XInputAxis.MaxCount
      xValues = Array.arange(self.XInputAxis.Values[0] + step - tick, self.XInputAxis.Values[-1], step)
      xDtick = max(step, self.XInputAxis.Tick.Dtick)
      if xValues[-1] <= xDtick:
        xDtick = step
    ySimpleStats = SimpleStats(self.YInputAxis.Values)
    yMultipleStats = MultipleStats(self.YInputAxis.Values, self.XInputAxis.MaxCount)
    return FigureFactory.stats(
      xValues,
      [yMultipleStats.Min, yMultipleStats.Avg, yMultipleStats.Max],
      [ySimpleStats.Min, min(self.YInputAxis.Tick.Dtick * self.YInputAxis.MaxCount + ySimpleStats.Min, ySimpleStats.Max)],
      [FigureTick(xDtick, self.XInputAxis.Tick.Format), self.YInputAxis.Tick],
      self.Colors)

  def to_figure_helper(self):
    return FigureHelper(self.to_figure())
