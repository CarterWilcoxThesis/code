import requests
import urllib.request
import csv

infile = open("Brooch Thumbnails.csv", "r")
reader = csv.reader(infile)
url = "https://finds.org.uk/database/ajax/download/id/"

def setup():
  thumbnails = []
  for row in reader:
    thumbnails.append(row[0])
  chunked_thumbnails = [thumbnails[0:5000],
                        thumbnails[5000:10000],
                        thumbnails[10000:15000],
                        thumbnails[15000:20000],
                        thumbnails[20000:]]
  #x = 0
  #check_list = []
  #for item in chunked_thumbnails:
  #  x += len(item)
  #  for num in item:
  #    if num not in check_list:
  #      check_list.append(num)
  #    else:
  #      print("ERROR!!!!")
  #print("Length of checklist: " + str(len(check_list)))
  #print(x)
  return chunked_thumbnails

# I have done 0, 1, 2, 3
def main(inpt):
  i = 0
  for num in inpt:
    img_data = requests.get(str(url + str(num))).content
    with open(str("BROOCH_" + str(num) + ".jpg"), 'wb') as handler:
        handler.write(img_data)
    i+=1
    print(i)
  print("Rows: " + str(i))

main(setup()[4])
infile.close()
