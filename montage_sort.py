# open up the montage file
# open an outfile called Brooch_Atlas_Files_(i).txt
# for every 1024 files,
import os

all_files = os.listdir("Brooch Images")

# Now we want to organize them in ascending order
all_files.sort()


#infile = open("brooch_files_for_montages.txt", "r")
#text = infile.read()

stem = "Brooch_Atlas_FList_"

outfile = open((stem + "1.txt"), "w")

total_files_seen = 0
temp_files = 0
outf_num = 1

for line in all_files:
  total_files_seen += 1
  temp_files += 1
  outfile.write(str(line) + "\n")
  if temp_files == 1024:
    outfile.close()
    outf_num += 1
    outfile = open((stem + str(outf_num) + ".txt"), "w")
    temp_files = 0


outfile.close()
print("Total files seen: " + str(total_files_seen))
print("Final temp file count: " + str(temp_files))
print("Total outfiles: " + str(outf_num))



