NGINX log parser
================================

Parse nginx logs with Python.

Inspired by: https://code.richard.do/explore/projects.

This python script parses an NGINX access log and counts the total occurrences of a chosen item within the logs and outputs a dictionary.

In the example.log it processes the "requested file/page" segment, this can be changed to any other segment of the log.

The output is useful when serving media assets as you can serve assets from source and calculate view counts periodically from the NGINX logs using this parser.

Note: if you log files are not in standard format the find() function will need editing accordingly.


Usage 
======= 
Given this nginx log entry: 

```
96.49.212.83 - - [16/Jun/2019:22:52:21 +0000] "GET /vs/editor/editor.main.nls.js HTTP/1.1" 200 34027 "https://3000-98358490.staging-avl.appsembler.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0" "-"  # noqa E503
```

the `entryparse` object will behave as follows:

```
>>> from nginxparser import entryparse

>>> entry = entryparse(log_string)
>>> entry.timestamp
datetime.datetime(2019, 6, 16, 23, 54, 5, 624139)
>>> entry.url
ParseResult(scheme='https', netloc='3000-98358490.staging-avl.appsembler.com', path='', params='', query='', fragment='')
>>> entry.deploy_id
'98358490'
```
