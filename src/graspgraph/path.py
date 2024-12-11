import os

class Path:
  def __init__(self, directory = ".", file = "", ext = ""):
    self.Directory = directory
    self.File = file
    self.Ext = ext

  def makedirs(self):
    os.makedirs(self.Directory, exist_ok = True)

  def to_string(self):
    return """{}/{}.{}""".format(self.Directory, self.File, self.Ext)

  @classmethod
  def from_file_path(cls, filePath):
    directory, fileAndExt = os.path.split(filePath)
    file, ext = os.path.splitext(fileAndExt)
    return Path(directory, file, ext[1:])
