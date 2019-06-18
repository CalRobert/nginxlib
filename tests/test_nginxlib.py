#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `nginxlib` package."""

from dateutil import parser
from urllib.parse import urlparse
from os import path
import re

import pytest  # noqa F401

from nginxlib import LogEntry, entryparse, URL_PATTERN


LOG_ENTRY = """
    96.49.212.83 - - [16/Jun/2019:22:52:21 +0000] "GET /vs/editor/editor.main.nls.js HTTP/1.1" 200 34027 "https://3000-98358490.staging-avl.appsembler.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0" "-"  # noqa E503
    """
LOG_ENTRY_NO_SUBSUBDOMAIN = LOG_ENTRY.replace("3000-98358490.", "")  # staging-avl.appsembler.com
LOG_ENTRY_NO_HYPHEN = LOG_ENTRY.replace("3000-98358490.staging-avl.", "foo.")  # foo.appsembler.com
LOGFILE = 'appsembler_example.log'


def test_get_event_time():
    """Given a log event string, I can get the time of the log event."""
    event_time = parser.parse("16/Jun/2019:22:52:21 +0000", fuzzy=True)

    event = LogEntry(LOG_ENTRY)

    assert event.timestamp == event_time


def test_get_url():
    """Given a log event string, I can get the url."""
    url_string = "https://3000-98358490.staging-avl.appsembler.com"
    url = urlparse(url_string)

    event = LogEntry(LOG_ENTRY)

    assert url == event.url


def test_get_deploy_id():
    """Given a log event string, I can get the deployment ID."""

    deploy_id = '98358490'

    event = LogEntry(LOG_ENTRY)

    assert deploy_id == event.deploy_id


def test_parse_many():
    """The LogEntry object can properly extract urls amidst
    various entry types."""

    logfile = '/'.join((path.abspath(path.curdir), 'tests', LOGFILE))

    with open(logfile) as f:
        for line in f:
            entry = entryparse(line)

            # Every entry must have a timestamp.
            assert entry.timestamp

            # An entry with no referrer (url) is okay, but this line must
            # indeed not have a url.
            if not entry.url:
                assert not re.findall(URL_PATTERN, line)

            # An entry with no deploy_id is okay, but this line must
            # indeed not have a deploy_id.
            elif entry.url and not entry.deploy_id:
                segments = entry.url.netloc.split('.')
                parts = segments[0].split('-')
                assert len(parts) == 1


def test_no_url():
    """An entry without a referrer does not raise an exception."""

    log_entry = '35.196.122.33 - - [17/Jun/2019:06:25:02 +0000] "GET / HTTP/1.1" 302 0 "-" "Go-http-client/1.1" "-"\n'  # noqa E501

    entry = entryparse(log_entry)

    assert entry.url is None


def test_no_subsubdomain():
    """An entry with no sub-subdomain should not raise."""

    entryparse(LOG_ENTRY_NO_SUBSUBDOMAIN)


def test_no_hyphen():
    """An entry with no hyphen in the subdomain should return no deploy_id."""

    entry = entryparse(LOG_ENTRY_NO_HYPHEN)

    assert not entry.deploy_id


def test_two_urls():
    """If the entry contains a full domain in the location, we should still
    get the referrer."""

    LOG_ENTRY = '5.188.210.101 - - [17/Jun/2019:07:56:52 +0000] "GET http://5.188.210.101/echo.php HTTP/1.1" 400 666 "https://www.google.com/" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" "-"\n'  # noqa E501
    referrer = 'https://www.google.com'

    entry = entryparse(LOG_ENTRY)
    assert entry.url == urlparse(referrer)
