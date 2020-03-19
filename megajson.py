import csv
import json
import re
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
"URL Page"]

start_char = ("\"record\":")

outfile = open("TESTING.csv", "w")
writer = csv.writer(outfile)
writer.writerow(fields)
infile = open("testable.json", "r")
temp = infile.read()
#print(temp.find(start_char))
#print(temp[:4])

# pass in json['record'][0]
def json_to_csv(json, writ):
  new_row = []
  for item in fields:
    new_row.append(json[item])
  writ.writerow(new_row)

print(temp)
#temp = json.loads(temp)
#json_to_csv(temp['record'][0], writer)

