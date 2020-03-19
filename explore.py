import csv



shipwrecks = open("romanshipwrecks.csv","r")
reader = csv.reader(shipwrecks, 'excel')

print(reader.__next__())







shipwrecks.close()
