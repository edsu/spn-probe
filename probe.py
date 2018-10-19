#!/usr/bin/env python

import json
import requests

from datetime import datetime as dt

url = 'https://mith.umd.edu/research/'
t = dt.now().strftime('%Y%m%d%H%M%S')

try:
    spn_url = 'https://web.archive.org/save/' + url
    resp = requests.get(spn_url, headers={'User-Agent': 'spn-probe'})
    with open('data/%s.txt' % t, "w") as out:
        out.write(json.dumps(dict(resp.headers), indent=2) + "\n\n")
        out.write(resp.text)
        out.write("finished: %s" % dt.now().strftime('%Y%m%d%H%M%S'))

except Exception as e:
    with open('data/%s.txt' % t, "wt") as out:
        out.write(str(e) + "\n\n")
        out.write("finished: %s" % dt.now().strftime('%Y%m%d%H%M%S'))
