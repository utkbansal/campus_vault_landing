from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Email

from .models import UserDetail
from landing_page import db


class SubscribeForm(Form):
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    phone_number = StringField(validators=[])

    def save(self):
        obj = UserDetail(self.first_name, self.last_name, self.email,
                         self.phone_number)
        db.session.add(obj)
        db.session.save()
        return obj
