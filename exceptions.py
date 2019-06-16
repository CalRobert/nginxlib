"""
nginx-access-log-parser/exceptions.py
"""


class NginxLogParseException(Exception):
    pass


class DateNotFound(NginxLogParseException):

    def __init__(self, message, log_entry):

        msg = "The date was not found in the following log entry: {}".format(log_entry)

        super(DateNotFound, self).__init__(msg)
