A little utility to run from cron to save a given page in Internet
Archive's Save Page Now for use as trace data.

A sample crontab that will run 

    0 0,12 * * * * cd /home/ed/Projects/spn-probe ; pipenv run probe


