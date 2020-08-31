import os

from flask import Blueprint, jsonify, request
from flask_restx import Resource
from ..models import db, SlackTeam, SlackUser, SlackChannel

from . import api_rest
from app.services.slack import update_team, update_channels, update_users

route_base = '/slack'

@api_rest.route(route_base+'/teams', methods=['GET', 'POST'])
class Teams(Resource):

	def get(self):
		slackteams = SlackTeam.query.all()
		arr = []
		for slackteam in slackteams:
			arr.append(slackteam.to_dict())
		return jsonify(arr)

	def post(self):
		res = update_team()
		return jsonify(res)


@api_rest.route(route_base+'/channels', methods=['GET', 'POST'])
class Channels(Resource):
	def get(self):
		slackchannels = SlackChannel.query.all()
		arr = []
		for slackchannel in slackchannels:
			arr.append(slackchannel.to_dict())
		return jsonify(arr)

	def post(self):
		res = update_channels()
		return jsonify(res)


@api_rest.route(route_base+'/users', methods=['GET', 'POST'])
class Users(Resource):
	def get(self):
		slackusers = SlackUser.query.all()
		arr = []
		for slackuser in slackusers:
			arr.append(slackuser.to_dict())
		return jsonify(arr)

	def post(self):
		res = update_users()
		return jsonify(res)