import os
import pdb

from flask import Flask, redirect, current_app, send_file, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Setup Routes
app = Flask(__name__, static_folder='../dist/static')
# Config the app
from .config import Config
app.config.from_object(Config)
# app.debug = True
app.logger.info('>>> ENV: {}'.format(Config.FLASK_ENV))

# Setup DB and Models
from .models import db
db.init_app(app)
migrate = Migrate(app, db, directory = os.path.join('app','migrations'))

# Setup the API
from .api import api_bp
from .client import client_bp
app.register_blueprint(api_bp)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


from .admin import admin

# Setup the Slack API
from .services.slack import init_slack
init_slack(app)

# Load the root Vue.js index.html file whitch is built in the /dist dir
@app.route('/')
def index_client():
	dist_dir = current_app.config['DIST_DIR']
	entry = os.path.join(dist_dir, 'index.html')
	return send_file(entry)

# Load any other static distribution files
@app.route('/<path:path>')
def send_js(path):
	return send_from_directory(current_app.config['DIST_DIR'], path)

app.logger.info('>>> Up and running.')
