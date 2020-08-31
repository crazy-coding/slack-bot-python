# from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime

import random

class SlackUser(db.Model):
    __tablename__ = 'slack_user'

    id = db.Column(db.String(128), primary_key=True)
    team_id = db.Column(db.String(128), index=True)
    name = db.Column(db.String(128), index=True)
    deleted = db.Column(db.Boolean)
    color = db.Column(db.String(128))
    real_name = db.Column(db.String(128), index=True)
    tz = db.Column(db.String(128))
    profile = db.Column(db.Text)
    is_admin = db.Column(db.Boolean)
    is_owner = db.Column(db.Boolean)
    is_primary_owner = db.Column(db.Boolean)
    is_bot = db.Column(db.Boolean)
    updated = db.Column(db.DateTime)
    is_app_user = db.Column(db.Boolean)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}