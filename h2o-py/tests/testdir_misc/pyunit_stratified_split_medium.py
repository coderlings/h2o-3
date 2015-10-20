




def stratified_split():
  fr = h2o.import_file(pyunit_utils.locate("bigdata/laptop/covtype/covtype.data"))
  stratified = fr[54].stratified_split()
  train = fr[stratified=="train"]
  test  = fr[stratified=="test"]
  print (fr[54].table()["Count"] / fr[54].table()["Count"].sum()).show()
  print (train[54].table()["Count"] / train[54].table()["Count"].sum()).show()
  print (test[54].table()["Count"] / test[54].table()["Count"].sum()).show()


stratified_split()