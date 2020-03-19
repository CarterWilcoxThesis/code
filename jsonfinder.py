import re
import csv
import json

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

re_start = "{\n\t\"record\":"
re_end = "}\n\t]\n}"
RE_S = re.compile(re_start)
RE_E = re.compile(re_end)


def get_jsons(text):
  list_of_jsons = []
  # check to make sure we have an equal number of starts and ends
  start_list = RE_S.findall(text)
  end_list = RE_E.findall(text)
  print("--------------")
  print("JSONS to find: " + str(len(start_list)) + "   " + str(len(end_list)))
  if len(start_list) != len(end_list):
    print("ERROR: POTENTIALLY INCOMPLETE JSON")
    i=0
    start_iterator = RE_S.finditer(text)
    end_iterator = RE_E.finditer(text)

    k = 0
    while i < len(start_list):
      i += 1
      next_start = next(start_iterator).span()
      next_end = next(end_iterator).span()
      nj = [int(next_start[0]), int(next_end[1])]
      #print("Total Length: " + str(next_end[1] - next_start[0]) + "  at  " + str(next_start[0]))
      valid_test = RE_S.findall(text[(nj[0] - 1):(nj[1] + 1)])
      print("Total Start Matches " + str(len(valid_test)))
      if len(valid_test) != 1:
        if k == 0:
          print(text[nj[0]:nj[0]+300])
          k+=1

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

def json_to_csv(json, writ):
  new_row = []
  for item in fields:
    try:
      new_row.append(json[item])
    except:
      new_row.append("Not Found")
  writ.writerow(new_row)

def main():
  outfile = open("FULL_PAS_DATA_IRON.csv", "w")
  writer = csv.writer(outfile)
  writer.writerow(fields)

  list_of_infiles = ["01. IRON Pages1-549.json",
  "02. IRON Pages1-549.json",
  "03. IRON Pages1-549.json",
  "04. IRON Pages1-549.json",
  "11. IRON Pages UGH.json",
  "12. IRON Pages UGH.json",
  "13. IRON Pages UGH.json",
  "14. IRON Pages UGH.json"]

  i = 0
  errs = 0
  for file in list_of_infiles:
    infile = open(file, "r")
    temp = infile.read()
    #print(temp[:8000])

    json_list = get_jsons(temp)
    for item in json_list:
      #print(item)
      #print(json.loads(item))
      try:
        json_to_csv(json.loads(item)['record'][0], writer)
      except:
        errs += 1
        print("Errors: " + str(errs))
        print(item)
    i += 1
    print("Files Complete: " + str(i) + "/8")
    infile.close()
  print("Done!")
  outfile.close()

main()
