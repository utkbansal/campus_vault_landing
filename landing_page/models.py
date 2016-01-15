from landing_page import db


class UserDetail(db.Model):
    id = db.Column(db.Integer, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, primary_key=True, nullable=False)
    phone_no = db.Column(db.String)

    def __init__(self, first_name, last_name, email, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
