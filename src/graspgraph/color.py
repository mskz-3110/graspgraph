class RGB:
  def __init__(self, r = 0, g = 0, b = 0):
    self.__R = min(max(r, 0), 255)
    self.__G = min(max(g, 0), 255)
    self.__B = min(max(b, 0), 255)
    self.__Array = tuple([self.__R, self.__G, self.__B])
    self.__HexCode = """#{:02X}{:02X}{:02X}""".format(r, g, b)

  @property
  def R(self):
    return self.__R

  @property
  def G(self):
    return self.__G

  @property
  def B(self):
    return self.__B

  @property
  def Array(self):
    return self.__Array

  @property
  def HexCode(self):
    return self.__HexCode

  @classmethod
  def from_hex_code(cls, hexCode):
    return RGB(*[int(hexCode[i: i + 2], 16) for i in range(1, 7, 2)])
