"""
Utilities to parse nginx logs.
"""

from dateutil import parser
import re

from exceptions import DateNotFound


def extract_timestamp(log_entry):
    """Given a log entry, return a Python object
    (datetime.datetime) from the timestamp."""

    pattern = r"\[(.+)\]\s"
    match = re.search(pattern, log_entry)

    if not match:
        msg = "The date was not found in the following log entry: {}".format(log_entry)
        raise DateNotFound(msg)

    timestamp_str = match.group().replace('[', '').replace(']', '').strip()
    timestamp = parser.parse(timestamp_str, fuzzy=True)

    return timestamp


class NginxEvent(object):

    def __init__(self, log_string):

        self.timestamp = extract_timestamp(log_string)
