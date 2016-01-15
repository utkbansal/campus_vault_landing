from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.secret_key = 's3cr3t'
db = SQLAlchemy(app)

from .models import UserDetail

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
