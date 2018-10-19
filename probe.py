#!/usr/bin/env python

import json
import requests

from datetime import datetime as dt

url = 'https://mith.umd.edu/research/'
t = dt.now().strftime('%Y%m%d%H%M%S')
spn_url = 'https://web.archive.org/save/' + url + '?t=%s' % t

msg = {
    "started": t,
    "url": spn_url
}

try:
    resp = requests.get(spn_url, headers={'User-Agent': 'spn-probe'})
    msg["status_code"] = resp.status_code
    msg["headers"] = dict(resp.headers)
    msg["text"] = resp.text

except Exception as e:
    msg["error"] = str(e)

msg["finished"] = dt.now().strftime('%Y%m%d%H%M%S')

open("data/%s.json" % t, "w").write(json.dumps(msg, indent=2))

