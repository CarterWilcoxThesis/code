import json
import csv

STEM = "01. Pages1-400"

file = STEM + ".txt"
fh = open(file, 'r')
data = fh.read()

data = data.split('\n')

start_pts = list()
end_pts = list()

for i in range(len(data)):
  if data[i] == '{':
    start_pts.append(i)
  if data[i] == '}':
    end_pts.append(i)

pairs = list()

for i in range(len(start_pts)):
  try:
    pairs.append((start_pts[i], end_pts[i]))
  except:
    pass

def pnum(url):
  end = url[-5:]
  new = ""
  for c in end:
    if not c.isalpha():
      new += c
  return (new.replace("/", ""))


class WeirdThingy:
  def __init__(self, url, json):
    self.url = url
    self.json = json

  def __repr__(self):
    return self.url + '\n' + self.json


thingies = list()

for start, end in pairs:
  json_data = '\n'.join([data[j] for j in range(start, end+1)])
  url = data[start-1]
  thingies.append(WeirdThingy(url, json_data))

outfile = open((STEM + "ABC.csv"), "w+")
writer = csv.writer(outfile)

jsonfields = ["id",
"old_findID",
"uniqueID",
"objecttype",
"classification",
"subclass",
"length",
"height",
"width",
"weight",
"thickness",
"diameter",
"quantity",
"otherRef",
"curr_loc",
"discoveryMethod",
"treasureID",
"broadperiod",
"numdate1",
"numdate2",
"description",
"notes",
"reuse",
"reusePeriodID",
"created",
"updated",
"secwfstage",
"findofnote",
"objecttypecert",
"datefound1",
"datefound2",
"inscription",
"museumAccession",
"subsequentAction",
"objectCertainty",
"dateFromCertainty",
"dateToCertainty",
"dateFoundFromCertainty",
"dateFoundToCertainty",
"subPeriodFrom",
"subPeriodTo",
"objdate1period",
"objdate2period",
"secuid",
"material1",
"material2",
"manmethod",
"decmethod",
"decstyle",
"complete",
"surface",
"manufactureID",
"culture",
"recorderID",
"identifier1ID",
"identifier2ID",
"smrRef",
"createdBy",
"updatedBy",
"hoardcontainer",
"institution",
"reason",
"fullname",
"primaryMaterial",
"primaryBMmaterial",
"secondaryMaterial",
"secondaryBMmaterial",
"decoration",
"style",
"manufacture",
"surfaceTreatment",
"completeness",
"preservation",
"periodFrom",
"seneschalPeriodFrom",
"bmPeriodFrom",
"periodoPeriodFrom",
"periodTo",
"seneschalPeriodTo",
"bmPeriodTo",
"periodoPeriodTo",
"reusePeriod",
"ascribedCulture",
"culturePeriodo",
"cultureBM",
"discmethod",
"identifier",
"secondaryIdentifier",
"recorder",
"fromCirca",
"toCirca",
"findSpotID",
"countyID",
"districtID",
"regionID",
"knownas",
"gridlen",
"accuracy",
"source",
"coinID",
"obverseDescription",
"obverseInscription",
"reverseDescription",
"reverseInscription",
"cciNumber",
"denominationID",
"degreeOfWear",
"allenType",
"vaType",
"mackType",
"abcType",
"bmcType",
"reeceID",
"dieAxis",
"moneyer",
"revtypeID",
"categoryID",
"typeID",
"tribeID",
"statusID",
"rulerQualifier",
"denominationQualifier",
"mintQualifier",
"dieAxisCertainty",
"initialMark",
"reverseMintMark",
"statusQualifier",
"ruler1",
"ruler2",
"mintID",
"rrcID",
"ricID",
"tribe",
"ironAgeRegion",
"ironAgeArea",
"denomination",
"nomismaDenomination",
"dbpediaDenomination",
"bmDenomination",
"primaryRuler",
"viaf",
"rulerDbpedia",
"nomismaRulerID",
"secondaryRuler",
"periodName",
"dateRange",
"mintName",
"nomismaMintID",
"pleiadesID",
"mintGeonamesID",
"mintWoeid",
"mintOsID",
"mintGettyID",
"mintWoeID",
"mintDbPediaID",
"mintWhat3Words",
"mintBritMuseumID",
"wear",
"nomismaWear",
"dieAxisName",
"category",
"type",
"moneyerID",
"nomismaMoneyer",
"emperorID",
"romanMintID",
"reverseType",
"status",
"jettonClass",
"jettonType",
"jettonGroup",
"thumbnail",
"filename",
"filesize",
"imageLabel",
"imageCopyrightHolder",
"imageLicense",
"imagedir",
"region",
"rallyID",
"rallyName",
"rallyDateFrom",
"rallyDateTo",
"landuse",
"landvalue",
"regionType",
"countyType",
"county",
"districtType",
"district",
"parishType",
"subsequentActionTerm",
"bmThesObject",
"seneschalObject",
"URL Page"]

def json_to_csv(json, writ):
  new_row = []
  for item in fields:
    new_row.append(json[item])
  writ.writerow(new_row)

i = 0
x = 0
for thing in thingies:
  #print(thing.json[0]`)
  #(["record"][0]["URL Page"]) = thing.url
 #print(thing.json)
  i += 1
  try:
    temp = json.loads(thing.json)
    temp["record"][0]["URL Page"] = pnum(thing.url)
    print(i)
    json_to_csv(temp["record"][0])
  except:
    x+=1

print(x)
outfile.close()


