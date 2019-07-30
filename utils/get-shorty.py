#!/usr/bin/env python3

import re
import sys
import glob
import os
import requests
import json
from pprint import pprint

if len(sys.argv) > 1:
    urls_json = sys.argv[1]
else:
    urls_json = "enlaces.json"

with open( urls_json ) as data_file:
    urls = json.load(data_file)

api_key = os.environ["BITLY_TOKEN"]
group_guid = os.environ["BITLY_USER"]

shortened_links = []
for u in urls:
    payload = {'long_url': u[1], "domain": "bit.ly" }
    response = requests.post( "https://api-ssl.bitly.com/v4/shorten",
                              json=payload,
                              headers={'Authorization': f"Bearer {api_key}" } )
    short_url = json.loads( response.text )
    shortened_links.append( [ u[0], u[1], short_url['id'] ] )

print(json.dumps( shortened_links ))
