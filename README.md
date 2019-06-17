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

## Timestamp

Get the timestamp from a log entry. Having extracted
one entry line from an nginx log, do the following:

```
>>> from nginxparser import entryparse

>>> entry = entryparse(log_string)
>>> entry.timestamp
datetime.datetime(2019, 6, 16, 23, 54, 5, 624139)
```

## URL

Get the URL from a log entry:

```
>>> from nginxparser import entryparse

>>> entry = entryparse(log_string)
>>> entry.url
ParseResult(scheme='https', netloc='3000-98358490.staging-avl.appsembler.com', path='', params='', query='', fragment='')
```


