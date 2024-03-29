# spn-probe

<a href="https://doi.org/10.5281/zenodo.5529700"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.5529700.svg" alt="DOI"></a>

*spn-probe* is a utility to run from cron to save a given timestamped URL in
Internet Archive's Save Page Now for use as trace data in the generated WARC
files created at the Internet Archive. Here is a sample crontab to that will
run every 12 hours, and save the response to the data subdirectory:

    0 0,12 * * * * /hom/ed/Projects/spn-probe/probe.py https://mith.umd.edu/research/ 

The resulting file for each run will look something like below. Note how the URL
that is archived has additional query parameters to identify the time of the
request and the user agent. This is so the exact request can be identified in
the saved WARC data without making any assumptions of how HTTP headers and the
like will end up in the WARC data. If the URL you are testing with has query
parameters this could interfere with the experiment. So it's best to use a URL
that does not have query parameters, and will not malfunction when query
parameters are used.

```json
{
  "started": "20181019212930",
  "url": "https://web.archive.org/save/https://mith.umd.edu/research/?t=20181019212930",
  "status_code": 200,
  "headers": {
    "Server": "nginx/1.13.11",
    "Date": "Fri, 19 Oct 2018 21:29:31 GMT",
    "Content-Type": "text/html;charset=utf-8",
    "Transfer-Encoding": "chunked",
    "Connection": "keep-alive",
    "Content-Location": "/web/20181019212509/https://mith.umd.edu/research/",
    "Set-Cookie": "JSESSIONID=8B6FB1CCAAADE85523BA8CCF7A0C97AE; Path=/; HttpOnly",
    "X-Archive-Orig-Vary": "Accept-Encoding",
    "X-Archive-Guessed-Charset": "UTF-8",
    "X-Archive-Orig-Server": "Apache/2.4.29 (Ubuntu)",
    "X-Archive-Orig-Connection": "close",
    "X-Archive-Orig-Age": "29068",
    "X-Archive-Orig-Date": "Fri, 19 Oct 2018 13:20:41 GMT",
    "X-Archive-Orig-Accept-Ranges": "bytes",
    "X-Archive-Orig-X-Varnish": "633637 234936",
    "X-Archive-Orig-Link": "<https://mith.umd.edu/wp-json/>; rel=\"https://api.w.org/\"",
    "X-Archive-Orig-Content-Type": "text/html; charset=UTF-8",
    "X-Archive-Orig-Via": "1.1 varnish (Varnish/5.2)",
    "X-App-Server": "wwwb-app14",
    "X-ts": "----",
    "X-location": "save-get",
    "Content-Encoding": "gzip"
  },
  "text": "<!DOCTYPE html>\n<html class=\"avada-html-layout-boxed\" lang=\"en-US\" prefix=\"og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# og: http://ogp.me/ns#\">\n<head>\n\n\n<script type=\"text/javascript\" src=\"/static/js/analytics.js\"></script>\n<script type=\"text/javascript\">archive_analytics.values.server_name=\"wwwb-app14.us.archive.org\";archive_analytics.values.server_ms=0;</script>\n<link type=\"text/css\" rel=\"stylesheet\" href=\"/static/css/banner-styles.css\"/>\n\n\n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\" />\n\t<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n\t<title>Research Archive &ndash; Maryland Institute for Technology in the Humanities</title>\n\n<!-- This site is optimized with the Yoast SEO plugin v8.4 - /save/https://yoast.com/wordpress/plugins/seo/ -->\n<meta name=\"robots\" content=\"noindex,follow\"/>\n<link rel=\"next\" href=\"https://mith.umd.edu/research/page/2/\" />\n<meta property=\"og:locale\" content=\"en_US\" />\n<meta property=\"og:type\" content=\"object\" />\n<meta property=\"og:title\" content=\"Research Archive &ndash; Maryland Institute for Technology in the Humanities\" />\n<meta property=\"og:url\" content=\"https://mith.umd.edu/research/\" />\n<meta property=\"og:site_name\" content=\"Maryland Institute for Technology in the Humanities\" />\n<meta name=\"twitter:card\" content=\"summary\" />\n<meta name=\"twitter:title\" content=\"Research Archive &ndash; Maryland Institute for Technology in the Humanities\" />\n<!-- / Yoast SEO plugin. -->\n\n<link rel='dns-prefetch' href='//s3.amazonaws.com' />\n<link rel='dns-prefetch' href='//s.w.org' />\n<link rel=\"alternate\" type=\"application/rss+xml\" title=\"Maryland Institute for Technology in the Humanities &raquo; Feed\" href=\"https://mith.umd.edu/feed/\" />\n<link rel=\"alternate\" type=\"application/rss+xml\" title=\"Maryland Institute for Technology in the Humanities &raquo; Comments Feed\" href=\"https://mith.umd.edu/comments/feed/\" />\n\t\t\t\t\t<link rel=\"shortcut icon\" href=\"/save/_embed/https://mith.umd.edu/wp-content/uploads/2018/07/favicon.png\" type=\"image/x-icon\" />\n\t\t\n\t\t\n\t\t\n\t\t\n\t\t\t\t<link rel=\"alternate\" type=\"application/rss+xml\" title=\"Maryland Institute for Technology in the Humanities &raquo; Research Feed\" href=\"https://mith.umd.edu/research/feed/\" />\n\t\t<script type=\"text/javascript\">\n\t\t\twindow._wpemojiSettings = {\"baseUrl\":\"/save/https://s.w.org\\/images\\/core\\/emoji\\/11\\/72x72\\/\",\"ext\":\".png\",\"svgUrl\":\"/save/https://s.w.org\\/images\\/core\\/emoji\\/11\\/svg\\/\",\"svgExt\":\".svg\",\"source\":{\"concatemoji\":\"/save/https://mith.umd.edu\\/wp-includes\\/js\\/wp-emoji-release.min.js?ver=4.9.8\"}};\n\t\t\t!function(a,b,c){function d(a,b){var c=String.fromCharCode;l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,a),0,0);var d=k.toDataURL();l.clearRect(0,0,k.width,k.height),l.fillText(c.apply(this,b),0,0);var e=k.toDataURL();return d===e}function e(a){var b;if(!l||!l.fillText)return!1;switch(l.textBaseline=\"top\",l.font=\"600 32px Arial\",a){case\"flag\":return!(b=d([55356,56826,55356,56819],[55356,56826,8203,55356,56819]))&&(b=d([55356,57332,56128..."
  "finished": "20181019212932"
}
```

In addition to the SPN response also recorded here are the web server access log messages that were generated as a result of the website in question (mith.umd.edu) being crawled. These can be found in data/varnish.tar.gz

Finally we conducted a series of manual SavePageNow requests using the Internet
Archive's web form as well as the Firefox browser extension. Each request URL
identified a page on a web server that we had access logs for (mith.umd.edu).
The URL also included query parameters for a unique timetamp (t) and the
user-agent (ua). The experiment was designed to look on and around our sample
day in question: September 25, 2018. You can see the plan, including the URLs
used in `spn-experiment.csv` which is a CSV for the Google Sheet that was used
to log the tests.

The results of these probes showed that:

1. The User-Agent of the requesting client is used by SPN to request the resources from the server: so spn-probe and the Firefox User-Agent in our case.
2. The Accept header of the requesting client is used by SPN to request the resources from the server: e.g. `*/*` for spn-probe and `text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8` for Firefox
3. Using the web form in a browser to fetch a page resulted in 107 requests to the web server, the initial HTML and all the JavaScript, CSS and image files that it referenced. See `data/firefox.log`
4. Using the spn-probe to programmatically request the page be archived only archived the HTML file. See `data/spn-probe.log`
5. Both modes resulted in SPN identifying itself with the Via HTTP Header, e.g. `Via: HTTP/1.0 web.archive.org (Wayback Save Page)`
6. All the requests came from 10 IP addresses in a block of addresses owned by the Internet Archive: 207.241.224.0 - 207.241.239.255


