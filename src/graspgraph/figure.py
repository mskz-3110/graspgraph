from collections import Counter

class FigureHelper:
  def __init__(self, figure):
    self.Figure = figure

  @property
  def LayoutTitleText(self):
    return self.Figure.layout.title.text

  @LayoutTitleText.setter
  def LayoutTitleText(self, value):
    self.Figure.layout.title.text = value

  @property
  def LayoutTitleColor(self):
    return self.Figure.layout.title.font.color

  @LayoutTitleColor.setter
  def LayoutTitleColor(self, value):
    self.Figure.layout.title.font.color = value

  @property
  def BackgroundColor(self):
    return Counter([self.Figure.layout.paper_bgcolor, self.Figure.layout.plot_bgcolor]).most_common(1)[0][0]

  @BackgroundColor.setter
  def BackgroundColor(self, value):
    self.Figure.layout.paper_bgcolor = self.Figure.layout.plot_bgcolor = value

  @property
  def XTitleText(self):
    return self.Figure.layout.xaxis.title.text

  @XTitleText.setter
  def XTitleText(self, value):
    self.Figure.layout.xaxis.title.text = value

  @property
  def XTitleColor(self):
    return self.Figure.layout.xaxis.color

  @XTitleColor.setter
  def XTitleColor(self, value):
    self.Figure.layout.xaxis.color = value

  @property
  def YTitleText(self):
    return self.Figure.layout.yaxis.title.text

  @YTitleText.setter
  def YTitleText(self, value):
    self.Figure.layout.yaxis.title.text = value

  @property
  def YTitleColor(self):
    return self.Figure.layout.yaxis.color

  @YTitleColor.setter
  def YTitleColor(self, value):
    self.Figure.layout.yaxis.color = value

  @property
  def GridColor(self):
    return Counter([
      self.Figure.layout.xaxis.linecolor, self.Figure.layout.xaxis.gridcolor, self.Figure.layout.xaxis.zerolinecolor,
      self.Figure.layout.yaxis.linecolor, self.Figure.layout.yaxis.gridcolor, self.Figure.layout.yaxis.zerolinecolor]).most_common(1)[0][0]

  @GridColor.setter
  def GridColor(self, value):
    self.Figure.layout.xaxis.linecolor = self.Figure.layout.xaxis.gridcolor = self.Figure.layout.xaxis.zerolinecolor = value
    self.Figure.layout.yaxis.linecolor = self.Figure.layout.yaxis.gridcolor = self.Figure.layout.yaxis.zerolinecolor = value

  @property
  def XDtick(self):
    return self.Figure.layout.xaxis.dtick

  @property
  def YDtick(self):
    return self.Figure.layout.yaxis.dtick

  @property
  def Dticks(self):
    return [self.XDtick, self.YDtick]

  def set_texts(self, layoutTitle = None, xTitle = None, yTitle = None):
    if layoutTitle is not None:
      self.LayoutTitleText = layoutTitle
    if xTitle is not None:
      self.XTitleText = xTitle
    if yTitle is not None:
      self.YTitleText = yTitle

  def set_colors(self, layoutTitle = None, xTitle = None, yTitle = None, grid = None, background = None):
    if layoutTitle is not None:
      self.LayoutTitleColor = layoutTitle
    if xTitle is not None:
      self.XTitleColor = xTitle
    if yTitle is not None:
      self.YTitleColor = yTitle
    if grid is not None:
      self.GridColor = grid
    if background is not None:
      self.BackgroundColor = background

  def write_image(self, filePath = None, width = 1600, height = 900):
    if filePath is None:
      self.Figure.show()
    else:
      self.Figure.write_image(filePath, width = width, height = height)
