# run_crawl_mashups.py

""" go through mashup_index.json to check the availability of the file in the local if available set it to True if
not tries to crawl it """

import simplejson as json  # dump the data into json file
import requests  # sending HTTP request
import time  # adding sleep time between each calls
import random  # random number generator for time
from requests.exceptions import TooManyRedirects  # handle exceptions of  redirects

with open('data/02-refined/mashup_index.json') as f:
    mashups = json.load(f)

datadir = 'data/01-raw-mashups/'

# Checking whether local copies of pages exist.
# And creating file names while going through the list
# for mashup in mashups:
#   page = requests.get(mashup['url'])
#   fname = '%s.html' % mashup['url'].split('/')[-1]
#   mashup['filename'] = fname

# with open('data/02-refined/mashup_index.json','w') as f:
#   json.dump(f,mashups,indent=1)

for index, mashup in enumerate(mashups):
    if not mashup['available']:
        try:
            page = requests.get(mashup['url'])
        except TooManyRedirects:
            print('Too many redirects when reading %s' % mashup['url'])
            continue
        fname = '%s.html' % mashup['url'].split('/')[-1]
        fpath = 'data/01-raw-mashups/%s' % fname
        print(index, len(mashups), fpath)
        with open(fpath, 'wb') as f:
            f.write(page.content)
        time.sleep(10 + random.random() * 10)
