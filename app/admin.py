from flask import redirect 
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth

from . import app
from .models import db, User

admin = Admin(app)

basic_auth = BasicAuth(app)

@app.route('/admin/login')
@basic_auth.required
def secret_view():
	return redirect('/admin')

# Setup a backend Admin
# First overide accesabliety 
class ProtectedModelView(ModelView):
	def is_accessible(self):
		return basic_auth.authenticate()

	def inaccessible_callback(self, name, **kwargs):
		return redirect('/admin/login')

class UserModelView(ProtectedModelView):
	column_searchable_list = ('email', 'first_name','last_name')

admin.add_view(UserModelView(User, db.session))
