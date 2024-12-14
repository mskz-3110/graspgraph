import graspgraph as gg

def test_dbergraph():
  filePath = "./directory/file.ext"
  path = gg.Path.from_file_path(filePath)
  assert(path.Directory == "./directory")
  assert(path.File == "file")
  assert(path.Ext == "ext")
  assert(path.to_string() == filePath)

  dbergraph = gg.Dbergraph(
    gg.Database.from_file_path("./images/dber/database_input.yaml"),
    gg.DotColors("orange", "blue", "white", "green", "red", "gray"))
  dbergraph.Database.update().save("./images/dber/database_output.yaml")
  prefix = "./images/dber/sample_coloring"
  pdfFilePath = gg.Path.join(prefix, "pdf")
  pngFilePath = gg.Path.join(prefix, "png")
  dot = dbergraph.to_dot_helper()
  dot.TitleText = "<b>[dbergraph]</b>"
  dot.write_image(pdfFilePath)
  gg.Pdf.convert(pdfFilePath, pngFilePath)

def test_dbergraph_usage():
  with open("./images/dber/database_input.yaml", "r", encoding = "utf-8") as file:
    dbergraph = gg.Dbergraph(gg.Database.from_yaml(file))
    dbergraph.Database.update()
    dot = dbergraph.to_dot_helper()
    dot.TitleText = "<b>[dbergraph]</b>"
    prefix = "./images/dber/usage"
    pdfFilePath = gg.Path.join(prefix, "pdf")
    pngFilePath = gg.Path.join(prefix, "png")
    dot.write_image(pdfFilePath)
    gg.Pdf.convert(pdfFilePath, pngFilePath)
