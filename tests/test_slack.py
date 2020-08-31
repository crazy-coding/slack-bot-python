""" pytests for Flask """

import pytest, time
from app import app

from app.services.slack import update_channels, update_team, update_users
from slackeventsapi.server import SlackEventAdapterException

@pytest.fixture(scope="module")
def client(request):
    return app.test_client()

def test_update_channels(client):
    resp = update_channels()
    assert resp['ok'] == True

def test_update_team(client):
    resp = update_team()
    assert resp['ok'] == True

def test_update_users(client):
    resp = update_users()
    assert resp['ok'] == True

def test_event_emission(adapter):
    test_event_emission.event_handled = False

    # Events should trigger an event
    @adapter.on('reaction_added')
    def event_handler(event_data):
        test_event_emission.event_handled = True

        event = event_data['event']
        assert event["reaction"] == 'grinning'

    data = pytest.reaction_event_fixture
    timestamp = int(time.time())
    signature = pytest.create_signature(adapter.signing_secret, timestamp, data)

    with adapter.server.test_client() as client:
        res = client.post(
            '/slack/events',
            data=data,
            content_type='application/json',
            headers={
                'X-Slack-Request-Timestamp': timestamp,
                'X-Slack-Signature': signature
            }
        )
        assert res.status_code == 200

    assert test_event_emission.event_handled

# TODO: Get this test running
# def test_slack_events_handler_challenge(client):
#     response = client.post(
#         '/api/slack/events',
#         data=json.dumps({
#             "token": "VEbshB9n8XywOj2jmcdrc6Ys",
#             "challenge": "4Me1ZHUwvVZKaMClPWn6hm79DTD6RyfowgOCEEQLtNIPiFc1aw9C",
#             "type": "url_verification"
#         }),
#         content_type='application/json',
#     )
#     # data = json.loads(response.get_data(as_text=True))
#     assert response.status_code == 200

    