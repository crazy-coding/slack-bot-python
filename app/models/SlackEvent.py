# from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime

import random

class SlackEvent(db.Model):
    __tablename__ = 'slack_event'

    id = db.Column(db.String(128), primary_key=True)
    token = db.Column(db.String(128))
    team_id = db.Column(db.String(128))
    event_time = db.Column(db.DateTime)

    event_type = db.Column(db.String(128), index=True)
    event_user = db.Column(db.String(128))
    event_json = db.Column(db.Text, index=True)
    event_ts = db.Column(db.Float)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}