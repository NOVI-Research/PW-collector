# run_crawl_apis.py
""" go through api_index.json to check the availability of the file in the local if available set it to True if not tries to crawl it """

import simplejson as json  # dump the data into json file
import requests  # sending HTTP request
from requests.exceptions import TooManyRedirects  # handle exceptions of  redirects
import time  # adding sleep time between each calls
import random  # random number generator for time

with open('data/02-refined/api_index.json') as f:
    apis = json.load(f)

datadir = 'data/01-raw-apis/'

for index, api in enumerate(apis):
    if not api['available']:
        try:
            page = requests.get(api['url'])
        except TooManyRedirects:
            print('Too many redirects when reading %s' % api['url'])
            continue
        # fname = '%s.html' % api['url'].split('/')[-1]
        fpath = 'data/01-raw-apis/%s' % api['filename']
        print(index, len(apis), fpath)
        with open(fpath, 'wb') as f:
            f.write(page.content)
        time.sleep(10 + random.random() * 10)
