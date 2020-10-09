# run_crawl_listing.py

""" Crawl through pages of APIs and Mashup at programmableweb to restore the contents """

import requests  # sending HTTP request
import time  # adding sleep time between each calls
import random  # random number generator for time

# page = requests.get('http://www.programmableweb.com/mashup/getsentiment-restaurant-reviews')

# print page.content

""" Crawl through pages of APIs - page numbers are hard-coded """
for listing_index in range(0, 875):
    print(listing_index)
    url = 'http://www.programmableweb.com/category/all/apis?page=%s' % listing_index
    print(url)
    page = requests.get(url)
    fname = 'data/01-raw-api-listings/api-listing-%03d.html' % listing_index
    print(fname)
    with open(fname, 'wb') as f:
        f.write(page.content)
    time.sleep(5 + random.random() * 3)

""" Crawl through pages of Mashups - page numbers are hard-coded """
for listing_index in range(0, 258):
    print(listing_index)
    url = 'http://www.programmableweb.com/category/all/mashups?page=%s' % listing_index
    print(url)
    page = requests.get(url)
    fname = 'data/01-raw-mashup-listings/mashups-listing-%03d.html' % listing_index
    print(fname)
    with open(fname, 'wb') as f:
        f.write(page.content)
    time.sleep(10 + random.random() * 10)
