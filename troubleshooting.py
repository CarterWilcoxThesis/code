import csv
import json
import re
infile = open("84. Pages3201-3396.json", "r")

re_start = "{\"record\":"
re_end = "}]}"
RE_S = re.compile(re_start)
RE_E = re.compile(re_end)

#end_of_json = "}]}"
#temp = infile.read()
#temp = "[" + temp[:-1] + "]"
#print(temp[:5000])
#infile.close()
fields = ["id",
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
"parishID",
"fourFigure",
"map25k",
"map10k",
"fourFigureLat",
"fourFigureLon",
"woeid",
"geonamesID",
"what3words",
"centreLat",
"centreLon",
"parish",
"URL Page"]

def get_jsons(text):
  list_of_jsons = []
  # check to make sure we have an equal number of starts and ends
  start_list = RE_S.findall(text)
  end_list = RE_E.findall(text)
  print("---------")
  print("JSONS to find: " + str(len(start_list)))
  if len(start_list) != len(end_list):
    return ("ERROR: POTENTIALLY INCOMPLETE JSON")
  else:
    # start the iterators
    start_iterator = RE_S.finditer(text)
    end_iterator = RE_E.finditer(text)
    i = 0
    # while there are still jsons to find...
    while i < len(start_list):
      i += 1
      # go to the next start and end
      next_start = next(start_iterator).span()
      next_end = next(end_iterator).span()
      nj = [int(next_start[0]), int(next_end[1])]
      list_of_jsons.append(text[nj[0]:nj[1]])
      #print(text[next_start.span()[0], next_end.span()[1]]
      #print(next_start)
      #print(next_end)
  print("JSONS found: " + str(len(list_of_jsons)) + "\n")
  return list_of_jsons

x = get_jsons(infile.read())
y = json.loads(x[0])
print(y)
z = (y['record'][0].keys())
for key in z:
  if key not in fields:
    print("\"" + str(key) + "\",")
