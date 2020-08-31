# from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime

import random

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    uuid = db.Column(db.String(128), index=True, unique=True)
    email = db.Column(db.String(128), index=True)
    first_name = db.Column(db.String(128), index=True)
    last_name = db.Column(db.String(128), index=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}