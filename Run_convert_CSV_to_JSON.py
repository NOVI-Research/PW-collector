# Run_convert_CSV_to_JSON.py

"""convert the CSV file of crunchbase into JSON"""

import csv  # read the CSV file
import json  # dump the data from CSV (CSVReader variable) into organizations.json

data = list()
with open('data/02-crunchbase/organizations.csv') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        data.append(rows)

with open('data/02-crunchbase/organizations.json', 'w') as jsonFile:
    json.dump(data, jsonFile, indent=1)
