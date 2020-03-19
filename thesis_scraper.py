import requests
import urllib.request
import time
import multiprocessing
from bs4 import BeautifulSoup

# PLANNED OUTFILE NAMES
# 0. Pages1-800
# 1. Pages801-1600
# 2. Pages1601-2400
# 3. Pages2401-3200
# 4. Pages3200-3386



def jsonify_item(url):
  # example input: https://finds.org.uk/database/artefacts/record/id/954990
  json_page = requests.get(str(url + "/format/json"))
  return json_page.text

# Total Roman-period records = 337,326
# At 100 results a page, that's 3,374 pages to scrape
# Example page url:
# https://finds.org.uk/database/search/results/broadperiod/ROMAN/show/100/page/1

# Get a list of all the pages to scrape, with 100 items per page
def fill_url_list(output_list, page_start, page_end):
  base_url = "https://finds.org.uk/database/search/results/broadperiod/IRON+AGE/show/100/page/"
  total_pages = 549 # range(1, 3386)
  for p in range(page_start,(page_end + 1)):
    output_list.append(base_url + str(p))
  return output_list

# Function to scrape the items on a page
def scrape_page(url, file):
  stem = "https://finds.org.uk"
  soup = BeautifulSoup((requests.get(url)).text, "html.parser")
  i = 0
  for item in soup.find_all("a"):
    if item.has_attr('href'):
      href = item['href']
      if href[0:30] == "/database/artefacts/record/id/":
        i += 1
        print(i)
        new_url = stem + href
        json = jsonify_item(str(stem + href))
        file.write(url + '\n' + json + '\n\n\n')

def scrape_pages(links, outfile):
  for link in links:
    scrape_page(link, outfile)

def split_list(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def main_program(p_start, p_end, fnamelist):
  # Create text file for output
  outfile = open("outputted_jsons.txt", 'w')
  print("Gathering page urls...")
  list_of_page_urls = fill_url_list([], p_start, p_end)
  progress = 0


  procs = 4
  chunks = split_list(list_of_page_urls, procs)
  outfiles = [open(fnamelist[0], 'w'), open(fnamelist[1], 'w'), open(fnamelist[2], 'w'), open(fnamelist[3], 'w')]

  #first_half = A[:len(A)//2]
  #second_half = A[len(A)//2:]
  #print(len(first_half))
  #print(len(second_half))
  #S1 =

  print("Scraping...")

  # Start two simultaneous processes
  #procs = 2
  jobs = []

  for i in range(procs):
    jobs.append(multiprocessing.Process(target=scrape_pages,
                                        args=(chunks[i], outfiles[i])))

  for j in jobs:
    j.start()

  for j in jobs:
    j.join(1000)

  outfile.close()

def check_fidelity(file):
  #serial_jsons = []
  #multip_jsons = []
  #sf = open("first_two_page_fidelity_check.txt", "r")
  #s = sf.read()
  mf = open(file)
  m = mf.read()
  #sf.close()
  mf.close()
  print(m.count("\"record\":["))



SKIP_TO_PAGE = 425 # last fully completed page was ___
CONTINUE_UNTIL_PAGE = 550 # last page is 549, but non-inclusive so write 550
FNAMELIST = ["11. IRON Pages UGH.txt", "12. IRON Pages UGH.txt", "13. IRON Pages UGH.txt", "14. IRON Pages UGH.txt"]
main_program(SKIP_TO_PAGE, CONTINUE_UNTIL_PAGE, FNAMELIST)


for file in FNAMELIST:
  check_fidelity(file)






