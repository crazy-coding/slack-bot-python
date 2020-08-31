# from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime

import random

class SlackTeam(db.Model):
    __tablename__ = 'slack_team'

    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(128), index=True)
    domain = db.Column(db.String(128), index=True)
    email_domain = db.Column(db.String(128), index=True)
    icon = db.Column(db.Text)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}