import os

from flask import Blueprint, jsonify, request
from flask_restx import Resource
from ..models import db, User

from . import api_rest

route_base = '/users'

@api_rest.route(route_base, methods=['GET'])
class Base(Resource):

	def get(self):
		users = User.query.all()
		arr = []
		for user in users:
			arr.append(user.to_dict())
		return jsonify(arr)
