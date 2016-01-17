from flask.ext.wtf import Form
from wtforms_html5 import TextField, EmailField, IntegerField
from wtforms.validators import DataRequired, Email, Length

from .models import UserDetail
from landing_page import db


class SubscribeForm(Form):
    first_name = TextField(validators=[DataRequired()])
    last_name = TextField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired(), Email()])
    phone_number = TextField(validators=[])

    def save(self):
        obj = UserDetail(self.first_name.data, self.last_name.data, self.email.data,
                         self.phone_number.data)
        db.session.add(obj)
        db.session.commit()
        return obj
