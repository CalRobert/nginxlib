"""
nginx-access-logs-parser/
"""

from dateutil import parser
from nginxutils import NginxEvent


EVENT_STRING = """
    (127.0.0.1 - - [19/Jun/2012:09:16:22 +0100] "GET /GO.jpg HTTP/1.1" 499 0 "http://8000-987547.domain.com/htm_data/7/1206/758536.html" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; SE 2.X MetaSr 1.0)"  # noqa E501
    """


def test_get_event_time():
    """Given a log event string, I can get the time of the log event."""

    event_time = parser.parse("19/Jun/2012:09:16:22 +0100", fuzzy=True)

    event = NginxEvent(EVENT_STRING)

    assert event.timestamp == event_time


def test_get_domain():
    """Given a log event string, I can get the domain."""

    domain = "http://8000-987547.domain.com/htm_data/7/1206/758536.html"

    event = NginxEvent(EVENT_STRING)

    assert domain == event.domain


def test_get_deploy_id():
    """Given a log event string, I can get the deployment ID."""

    deploy_id = '987547'

    event = NginxEvent(EVENT_STRING)

    assert deploy_id == event.deploy_id
