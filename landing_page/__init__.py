from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 's3cr3t'
db = SQLAlchemy(app)
