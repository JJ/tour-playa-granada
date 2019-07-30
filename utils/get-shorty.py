#!/usr/bin/env python3

import re
import sys
import glob
import json
import bitly
import os

if len(sys.argv) > 1:
    urls_json = sys.argv[1]
else:
    urls_json = "enlaces.json"

with open( urls_json ) as data_file:
    urls = json.load(data_file)

print(os.environ["BITLY_USER"], os.environ["BITLY_TOKEN"])

b = bitly.Connection(os.environ["BITLY_USER"], os.environ["BITLY_TOKEN"])

shortened_links = []
for u in urls:
#    print(u)
    if (re.search("amzn.to",u[1])):
        shortened_links.append( [ u[0], u[1], u[1] ] )
    else:
        response = b.shorten( uri=u[1] )
        print(response)
#        shortened_links.append( [ u[0], u[1], my_id['id'] ] )

#print(json.dumps( shortened_links ))
