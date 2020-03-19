import json

with open("sorted_brooch_projections.json") as json_file:
  data = json.load(json_file)
  mylist = []
  for item in data:
    num = item['image'][14:-4]
    mylist.append(num)
  print(len(mylist))



  i = 0
  j = 1
  found = 0

 # outfile = open("USE_ME_Atlas_Flist_1.txt", "w")
 # for JCODE in mylist:
 #   i += 1
 #   outfile.write("BROOCH_" + str(JCODE) + ".jpg\n")
 #   if i == 1024:
 #     i = 0
 #     j += 1
 #     outfile.close()
 #     outfile = open("USE_ME_Atlas_Flist_" + str(j) + ".txt", "w")

  #outfile.close()
  fme = []
  for i in range(1, 26):
    infile = open("USE_ME_Atlas_Flist_" + str(i) + ".txt")
    x = (infile.read()).split("\n")
    for item in x:
      if item != "":
        fme.append(item)
    infile.close()
  print(len(fme))

  trues = 0
  falses = 0
  for i in range(0, 25075):
    print(str(fme[i]) + " == " + str(mylist[i]))
    if int(fme[i][7:-4]) == int(mylist[i]):
      trues += 1
    else:
      falses +=1
  print("Trues: " + str(trues))
  print("Falses: " + str(falses))

  #infile = open("USE_ME_Atlas_Flist_1.txt")
  #print(infile.read())
  #for JCODE in mylist:
   # i += 1
    #supposed_to_be_num = infile.readline()[7:-4]
    #found +=1
   # if i == 1024:
  #    infile.close()
  #    j += 1
  #    infile = open("Brooch_Atlas_FList_" + str(j) + ".txt")
  #    i = 0
  #  print(str(JCODE) + " = " + str(supposed_to_be_num))
  #
json_file.close()
