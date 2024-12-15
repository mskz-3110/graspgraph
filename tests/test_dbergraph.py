import graspgraph as gg

def test_dbergraph():
  assert(gg.Color(1, 2, 3).to_string() == "#010203")

  assert(gg.Path.join("file", "") == "file")
  assert(gg.Path.join("file", "ext") == "file.ext")
  assert(gg.Path.join("file", "ext", "directory") == "directory/file.ext")
  filePath = "./directory/file.ext"
  directory, file, ext = gg.Path.split(filePath)
  assert(gg.Path.join(file, ext, directory) == filePath)
  directory, file, ext = gg.Path.split(filePath)
  path = gg.Path(directory, file, ext)
  assert(path.Directory == "./directory")
  assert(path.File == "file")
  assert(path.Ext == "ext")
  assert(path.to_string() == filePath)

  with open("./images/dber/database_input.yaml", "r", encoding = "utf-8") as file:
    dbergraph = gg.Dbergraph(
      gg.Database.from_yaml(file),
      gg.DotColors("orange", "blue", "white", "green", "red", "gray"))
    dbergraph.Database.update().save("./images/dber/database_output.yaml")
    prefix = "./images/dber/sample_coloring"
    pdfFilePath = gg.Path.join(prefix, "pdf")
    pngFilePath = gg.Path.join(prefix, "png")
    dot = dbergraph.to_dot()
    dot.TitleText = "<b>[dbergraph]</b>"
    dot.Save(pdfFilePath)
    gg.Pdf.convert(pdfFilePath, pngFilePath)

def test_dbergraph_usage():
  dbergraph = gg.Dbergraph(gg.Database.from_file_path("./images/dber/database_input.yaml"))
  dbergraph.Database.update()
  dot = dbergraph.to_dot()
  dot.TitleText = "<b>[dbergraph]</b>"
  prefix = "./images/dber/usage"
  pdfFilePath = gg.Path.join(prefix, "pdf")
  pngFilePath = gg.Path.join(prefix, "png")
  dot.Save(pdfFilePath)
  gg.Pdf.convert(pdfFilePath, pngFilePath)
