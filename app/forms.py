from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class add_contact(Form):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])
    mobile = StringField('mobile', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    country = StringField('country', validators=[DataRequired()])
    #remember_me = BooleanField('remember_me', default=False)
