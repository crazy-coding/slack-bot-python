import os

from flask import Blueprint, jsonify, request
from flask_restx import Resource
from ..models import db, Todo

from . import api_rest

route_base = '/todos'

@api_rest.route(route_base, methods=['GET'])
class Base(Resource):

	def get(self):
		todos = Todo.query.all()
		arr = []
		for todo in todos:
			arr.append(todo.to_dict())
		return jsonify(arr)
