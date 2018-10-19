A little utility to run from cron to save a given page in Internet Archive's
Save Page Now for use as trace data.

A sample crontab to that will run every 12 hours, and save the response to the
data subdirectory:

    0 0,12 * * * * /hom/ed/Projects/spn-probe/probe.py

