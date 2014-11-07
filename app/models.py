from app import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    phone = db.Column(db.String(15))
    mobile = db.Column(db.String(15))
    address = db.Column(db.String(100))
    city = db.Column(db.String(50))
    country = db.Column(db.String(20))

    def __repr__(self):
        return '<Contact %r>' % (self.firstname)

