#!/usr/bin/env python3

import re
import sys
import glob
import json

if len(sys.argv) > 1:
    dir = sys.argv[1]
else:
    dir = "pois/"

ficheros = glob.glob(dir+"/*.md")
ficheros.append("intro.md")

for f in ficheros:
    file_content = open(f, "r").read()
    file_content = re.sub(r'\[([^\]]+)\]\(http[^\(]+\)', r'\1', file_content)
    split_refs = re.split(r'## Referencias\s+', file_content)
    file_content = split_refs[0]

    f = f.replace('.md', '-nolinks.md')
    with open(f, "w") as links_file:
        links_file.write(file_content)
