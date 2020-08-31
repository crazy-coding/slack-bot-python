from slackeventsapi import SlackEventAdapter
from slack import WebClient

from .IntentHandler import IntentHandler
import json
from datetime import datetime

from .. import app
from app.models import SlackTeam, SlackChannel, SlackUser, SlackEvent
from app import db

# Setup the celery
from app.services.celery import make_celery
celery = make_celery(app)

slack_client = WebClient(app.config["SLACK_BOT_USER_OAUTH_TOKEN"])

def init_slack(app):
	# Bind the Events API route to your existing Flask app by passing the server
	# instance as the last param, or with `server=app`.

	slack_events_adapter = SlackEventAdapter(app.config['SLACK_SIGNING_SECRET'], "/api/slack/events", app)
	handler = IntentHandler(app)

	# Create an event listener for "reaction_added" events and print the emoji name
	@slack_events_adapter.on("reaction_added")
	def reaction_added(event_data):
		# Don't talk to bots... including yourself
		if "bot_id" in event_data["event"].keys():
			return

		resp = update_event(event_data)
		emoji = event_data["event"]["reaction"]
		app.logger.info("Slack - Recieved Reaction: " + emoji)

		response = handler.get_emoji_response(event_data)
		channel = event_data['event']['item']['channel']
		result = send_message.delay(channel, response)
		result.wait()
		return

	# Create an event listener for "message.im"
	@slack_events_adapter.on("message")
	def message(event_data):
		if "bot_id" in event_data["event"].keys():
			return

		resp = update_event(event_data)
		text = event_data["event"]["text"]
		app.logger.info("Slack - Recieved Message: " + text)
		
		response = handler.get_text_response(event_data) 
		channel = event_data['event']['channel']
		result = send_message.delay(channel, response)
		result.wait()
		return


@celery.task()
def send_message(channel, text):
	slack_client.chat_postMessage(channel=channel, text=text)
	return


def update_event(item):
	try:
		event = SlackEvent(
			id = item['event_id'],
			token = item['token'],
			team_id = item['team_id'],
			event_time = datetime.fromtimestamp(item['event_time']),

			event_type = item['event']['type'],
			event_user = item['event']['user'],
			event_json = json.dumps(item['event']),
			event_ts = item['event']['event_ts'],
		)
		db.session.merge(event)
		db.session.commit()
		return {'ok': True, 'event_id': event.id}
	except:
		return {'ok': False}


def update_team():
	call = slack_client.api_call("team.info")
	if call.get('ok'):
		item = call['team']
		try:
			team = SlackTeam(
				id = item['id'],
				name = item['name'],
				domain = item['domain'],
				email_domain = item['email_domain'],
				icon = json.dumps(item['icon']),
			)
			db.session.merge(team)
			db.session.commit()
			return {'ok': True, 'team_id': team.id}
		except:
			return {'ok': False}
	else:
		return {'ok': False}

def update_channels():
	call = slack_client.api_call("conversations.list")
	if call.get('ok'):
		channel_ids = []
		for item in call['channels']:
			try:
				channel = SlackChannel(
					id = item['id'],
					name = item['name'],
					is_channel = item['is_channel'],
					is_group = item['is_group'],
					is_im = item['is_im'],
					created = datetime.fromtimestamp(item['created']),
					is_archived = item['is_archived'],
					is_general = item['is_general'],
					name_normalized = item['name_normalized'],
					creator = item['creator'],
					topic = json.dumps(item['topic']),
					purpose = json.dumps(item['purpose']),
					num_members = item['num_members'],
				)
				db.session.merge(channel)
				db.session.commit()
				channel_ids.append(channel.id)
			except:
				continue
		return {'ok': True, 'channel_ids': channel_ids}
	else:
		return {'ok': False}

def update_users():
	call = slack_client.api_call("users.list")
	if call.get('ok'):
		users_ids = []
		for item in call['members']:
			try:
				user = SlackUser(
					id = item['id'],
					team_id = item['team_id'],
					name = item['name'],
					deleted = item['deleted'],
					color = item['color'],
					real_name = item['real_name'],
					tz = item['tz'],
					profile = json.dumps(item['profile']),
					is_admin = item['is_admin'],
					is_owner = item['is_owner'],
					is_primary_owner = item['is_primary_owner'],
					is_bot = item['is_bot'],
					updated = datetime.fromtimestamp(item['updated']),
					is_app_user = item['is_app_user'],
				)
				db.session.merge(user)
				db.session.commit()
				users_ids.append(user.id)
			except:
				continue
		return {'ok': True, 'users_ids': users_ids}
	else:
		return {'ok': False}