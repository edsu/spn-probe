#!/usr/bin/env python

import json
import time
import datetime
import optparse
import requests

now = datetime.datetime.now


def main():
    p = optparse.OptionParser()
    p.add_option("--repeat", type="int", default=0)
    p.add_option("--sleep", type="int", default=10)
    opts, args = p.parse_args()

    if len(args) == 0:
        p.error("You must supply a URL to save")
    url = args[0]

    started = now()

    if opts.repeat > 0:
        tries = 0
        while tries < opts.repeat:
            tries += 1
            probe(url, started, tries)
            if opts.sleep > 0:
                time.sleep(opts.sleep)
    else:
        probe(url, started)


def probe(url, dt=None, try_num=None):
    if dt is None:
        dt = now()

    t = dt.strftime('%Y%m%d%H%M%S')

    spn_url = 'https://web.archive.org/save/' + url + '?ua=spn-probe&t=%s' % t

    msg = {
        "started": t,
        "url": spn_url
    }

    try:
        resp = requests.get(spn_url, 
            timeout=300,
            headers={'User-Agent': 'spn-probe'})
        msg["status_code"] = resp.status_code
        msg["headers"] = dict(resp.headers)
        msg["text"] = resp.text

    except Exception as e:
        msg["error"] = str(e)

    msg["finished"] = now().strftime('%Y%m%d%H%M%S')

    if try_num is None:
        file_path = "data/%s.json" % t
    else:
        file_path = "data/%s-%02i.json" % (t, try_num)

    open(file_path, "w").write(json.dumps(msg, indent=2))


if __name__ == "__main__":
    main()
