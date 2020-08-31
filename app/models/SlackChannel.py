# from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime

import random

class SlackChannel(db.Model):
    __tablename__ = 'slack_channel'

    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), index=True)
    is_channel = db.Column(db.Boolean)
    is_group = db.Column(db.Boolean)
    is_im = db.Column(db.Boolean)
    created = db.Column(db.DateTime)
    is_archived = db.Column(db.Boolean)
    is_general = db.Column(db.Boolean)
    name_normalized = db.Column(db.String(128))
    creator = db.Column(db.String(128))
    topic = db.Column(db.Text)
    purpose = db.Column(db.Text)
    num_members = db.Column(db.Integer)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}