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
  dbergraph.to_dot_helper().write_image("./images/dber/sample_coloring.pdf")

def test_dbergraph_usage():
  with open("./images/dber/database_input.yaml", "r", encoding = "utf-8") as file:
    dbergraph = gg.Dbergraph(gg.Database.from_yaml(file))
    dbergraph.Database.update()
    dbergraph.to_dot_helper().write_image("./images/dber/usage.pdf")
