# -*- coding: utf-8 -*-
"""
Utilities to parse nginx logs.
"""

from dateutil import parser
import re
from urllib.parse import urlparse

from .exceptions import DateNotFound, URLNotFound

URL_PATTERN = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
TIMESTAMP_PATTERN = r"\[(.+)\]\s"


def extract_timestamp(log_entry):
    """Given a log entry, return a Python object
    (datetime.datetime) from the timestamp."""
    match = re.search(TIMESTAMP_PATTERN, log_entry)

    if not match:
        msg = "The date was not found in the following log entry: {}".format(log_entry)
        raise DateNotFound(msg)

    timestamp_str = match.group().replace('[', '').replace(']', '').strip()
    timestamp = parser.parse(timestamp_str, fuzzy=True)

    return timestamp


def extract_url(log_entry):
    """Given a log entry, return a Python object representing the string."""

    url = re.findall(URL_PATTERN, log_entry)

    if not url:
        raise URLNotFound(log_entry)

    return urlparse(url[-1])


def extract_deploy_id(log_entry):
    """Given a log entry, return the 'deploy ID'.

    (A deploy ID is specific to Appsembler, the maintainer of this package.
    If you are not an Appsembler employee, or don't for another reason
    care about the zeroth element of the subdomain, fork this package
    and submit a PR :) Otherwise, ignore the deploy_id attribute.)
    """
    url = extract_url(log_entry)

    subdomain = url.netloc.split('.')[0]
    parts = subdomain.split('-')
    # A subdomin with no hyphen is not of interest.
    if not len(parts) > 1:
        return None
    else:
        return parts[-1]


class LogEntry(object):

    def __init__(self, log_string):
        self.timestamp = extract_timestamp(log_string)

        try:
            self.url = extract_url(log_string)
        except URLNotFound:
            self.url = None

        if self.url:
            self.deploy_id = extract_deploy_id(log_string)
        else:
            self.deploy_id = None

    def __str__(self):
        "LogEntry(timestamp={}, url={}, deploy_id={})".format(self.timestamp,
                                                              self.url,
                                                              self.deploy_id
                                                              )


def entryparse(log_entry):

    return LogEntry(log_entry)
