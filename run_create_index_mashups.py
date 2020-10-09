# run_create_index_mashups.py

import glob  # finding all the path names matching a specified pattern
from bs4 import BeautifulSoup  # pulling data out of HTML
import json  # dump the data into json file
import pandas as pd  # store the data into DataFrame

indices = glob.glob('data/01-raw/mashups-page-*.html')
local_files = list()

for fname in glob.glob('data/01-raw-mashups/*.html'):
    local_files.append(fname.split('/')[-1])

mashups = list()
for fname in indices:
    print(fname)
    with open(fname) as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    # print soup.select('div.content')
    table = soup.find('table')

    headers = list()
    for header in table.select('thead tr th'):
        headers.append(header.text.strip().lower().replace(' ', '_'))
    # print headers
    for row in table.select('tbody tr'):
        data = dict()
        for index, cell in enumerate(row.find_all('td')):
            data[headers[index]] = cell.text.strip()
            if index == 0:
                data['url'] = 'http://programmableweb.com%s' % cell.a['href']
                # print data['url']
                keepcharacters = ('_', '-')
                filestring = data['url'].split('/')[-1]
                filestring = ''.join(c for c in filestring if c.isalnum() or c in keepcharacters).rstrip()
                data['id'] = data['url'].split('/')[-1]
                data['filename'] = '%s.html' % data['url'].split('/')[-1]
        # Finally, checking whether such a file already exists
        data['available'] = data['filename'] in local_files
        # print data
        mashups.append(data)

print('In total %s mashups extracted, serializing' % len(mashups))

with open('data/02-refined/mashup_index.json', 'w') as f:
    json.dump(mashups, f, indent=1)

print('Status:')
df_mashups = pd.DataFrame.from_dict(mashups)
print(df_mashups.available.value_counts())

print('Files not available:')
print(df_mashups[df_mashups.available == False].mashups_name)
