import csv

infile = open("FULL_PAS_DATA_IRON.csv", "r")
reader = csv.reader(infile)

outfile = open("FULL_PAS_DATA_IRON_CLEAN.csv", "w")
writer = csv.writer(outfile)

seen_ids = []

for row in reader:
  if row[0] not in seen_ids:
    seen_ids.append(row[0])
    writer.writerow(row)
  else:
    pass

infile.close()
outfile.close()

