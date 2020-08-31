import json
import hashlib
import hmac
import pytest
from slackeventsapi import SlackEventAdapter
from app import app

def create_signature(secret, timestamp, data):
    req = str.encode('v0:' + str(timestamp) + ':') + str.encode(data)
    request_signature= 'v0='+hmac.new(
        str.encode(secret),
        req, hashlib.sha256
    ).hexdigest()
    return request_signature


def load_event_fixture(event, as_string=True):
    filename = "tests/data/{}.json".format(event)
    with open(filename) as json_data:
        event_data = json.load(json_data)
        if not as_string:
            return event_data
        else:
            return json.dumps(event_data)


def pytest_configure():
    pytest.reaction_event_fixture = load_event_fixture('reaction_added')
    pytest.create_signature = create_signature

@pytest.fixture
def adapter():
    return SlackEventAdapter(app.config["SLACK_SIGNING_SECRET"])
