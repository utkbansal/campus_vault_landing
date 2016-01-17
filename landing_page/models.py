from landing_page import db


class UserDetail(db.Model):
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), primary_key=True, nullable=False)
    phone_no = db.Column(db.String(255))

    def __init__(self, first_name, last_name, email, phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no

    def __repr__(self):
        return self.email