import json

x = {
  "record":[
    {
      "id":"961866",
      "old_findID":"NMS-4794B8",
      "uniqueID":"PAS5D24794B0017F9",
      "objecttype":"COIN"
    }
  ]
}

url1 = "https://finds.org.uk/database/search/results/broadperiod/ROMAN/show/100/page/1"
url2 = "https://finds.org.uk/database/search/results/broadperiod/ROMAN/show/100/page/15"
url3 = "https://finds.org.uk/database/search/results/broadperiod/ROMAN/show/100/page/100"
url4 = "https://finds.org.uk/database/search/results/broadperiod/ROMAN/show/100/page/2000"

urls = [url1, url2, url3, url4]

def pnum(url):
  end = url[-5:]
  new = ""
  for c in end:
    if not c.isalpha():
      new += c
  return (new.replace("/", ""))

x["record"][0]["URL Page"] = pnum(url1)
print(x)
