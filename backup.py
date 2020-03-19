import requests
import urllib.request
import time
from bs4 import BeautifulSoup


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
  base_url = "https://finds.org.uk/database/search/results/broadperiod/ROMAN/show/100/page/"
  total_pages = 3374 # range(1, 3375)
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
        file.write(json + '\n\n')


def main_program(p_start, p_end):
  # Create text file for output
  outfile = open("outputted_jsons.txt", 'w')
  print("Gathering page urls...")
  list_of_page_urls = fill_url_list([], p_start, p_end)
  progress = 0
  print("Scraping...")
  for link in list_of_page_urls:
    scrape_page(link, outfile)
    progress += 1
    print("Pages Completed: " + str(progress))
  outfile.close()


SKIP_TO_PAGE = 1 # last fully completed page was ___
CONTINUE_UNTIL_PAGE = 2 # last page is 3374, but non-inclusive so write 3375
#main_program(SKIP_TO_PAGE, CONTINUE_UNTIL_PAGE)






