# from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.now)
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

	# Which user this belongs to 
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), index=True)

	# The todo as decribed by the user
	description = db.Column(db.UnicodeText)


	def to_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}