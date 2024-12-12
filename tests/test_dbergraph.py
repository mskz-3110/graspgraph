import graspgraph as gg

def test_dbergraph():
  filePath = "./directory/file.ext"
  path = gg.Path.from_file_path(filePath)
  assert(path.Directory == "./directory")
  assert(path.File == "file")
  assert(path.Ext == "ext")
  assert(path.to_string() == filePath)

  dbergraph = gg.Dbergraph(
    gg.Database().load("./images/dber/database_input.yaml"),
    gg.DotColors("blue", "white", "green", "red", "gray"))
  dbergraph.Database.update().save("./images/dber/database_output.yaml")
  prefix = "./images/dber/sample_coloring"
  pdfFilePath = gg.Path.join(prefix, "pdf")
  pngFilePath = gg.Path.join(prefix, "png")
  dbergraph.to_dot_helper().write_image(pdfFilePath)
  gg.Pdf.convert(pdfFilePath, pngFilePath)

def test_dbergraph_usage():
  with open("./images/dber/database_input.yaml", "r", encoding = "utf-8") as file:
    dbergraph = gg.Dbergraph(gg.Database.from_yaml(file))
    dbergraph.Database.update()
    prefix = "./images/dber/usage"
    pdfFilePath = gg.Path.join(prefix, "pdf")
    pngFilePath = gg.Path.join(prefix, "png")
    dbergraph.to_dot_helper().write_image(pdfFilePath)
    gg.Pdf.convert(pdfFilePath, pngFilePath)
