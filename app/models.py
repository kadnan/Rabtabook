from app import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), index=True, unique=True)
    lastname = db.Column(db.String(30), index=True, unique=True)
    phone = db.Column(db.String(15), index=True, unique=True)
    mobile = db.Column(db.String(15), index=True, unique=True)
    address = db.Column(db.String(100), index=True, unique=True)
    city = db.Column(db.String(50), index=True, unique=True)
    country = db.Column(db.String(20), index=True, unique=True)

    def __repr__(self):
        return '<Contact %r>' % (self.firstname)

