import shutil, os
for i in range(2, 26):
  infile = open("USE_ME_Atlas_Flist_" + str(i) + ".txt", "r")

  files = []
  x = (infile.read()).split("\n")
  for item in x:
    if item != "":
      files.append(item)

  #check = os.listdir("Brooch_atlas_1")
  #check.sort()
  #check = check[1:]

  #for i in range(0,1024):
  #  print(files[i] + "  " + check[i])

  for f in files:
      shutil.move("Brooch Images/" + str(f), 'Brooch_atlas_' + str(i))
  print("Moved " + str(i))
