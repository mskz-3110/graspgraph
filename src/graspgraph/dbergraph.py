from .dot import *
from .font import *
from .database import *

class Dbergraph:
  def __init__(self, database = None, colors = None, fontName = None):
    if database is None:
      database = Database()
    if colors is None:
      colors = DotColors()
    if fontName is None:
      fontName = Font.instance().Name
    self.Database = database
    self.Colors = colors
    self.FontName = fontName

  def to_dot(self):
    return DotFactory.dber(self.Database, self.Colors, self.FontName)

  def to_dot_helper(self):
    return DotHelper(self.to_dot())
