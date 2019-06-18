"""
nginx-access-log-parser/exceptions.py
"""


class NginxLogParseException(Exception):
    pass


class DateNotFound(NginxLogParseException):

    def __init__(self, log_entry):

        msg = "The date was not found in the following log entry: {}".format(log_entry)

        super(DateNotFound, self).__init__(msg)


class URLNotFound(NginxLogParseException):

    def __init__(self, log_entry):

        msg = "The URI was not found in the following log entry: {}".format(log_entry)

        super(URLNotFound, self).__init__(msg)
