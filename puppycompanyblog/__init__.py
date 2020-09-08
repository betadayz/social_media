import os
from flask import Flask
from flask_sqlalchemy import  import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)
login_Manager.login_view = 'users.login'

from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)