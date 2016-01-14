from landing_page import db


class UserDetail(db.Model):
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    phone_no = db.Column(db.String)

    def __init__(self, first_name, last_name, email, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
