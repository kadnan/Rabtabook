from flask import render_template, flash, redirect, request
from app import app
from .forms import add_contact
from .models import Contact
from app import db
from flask.ext.wtf import Form

@app.route('/')
@app.route('/index')
def index():
    contacts = Contact.query.all()
    return render_template(
        'index.html',
                contacts=contacts)

@app.route('/view/<int:id>')
def view(id):
    contacts = Contact.query.from_statement(("SELECT * FROM contact where id=:id")).params(id=id).all()
    return render_template(
        'view.html',
                contacts=contacts)


@app.route('/add',methods=['GET','POST'])
def add():
    # form = add_contact(request.form)
    if request.method == 'POST':
        firstname = str(request.form['first_name'])
        lastname = str(request.form['last_name'])
        phone = str(request.form['phone'])
        mobile = str(request.form['mobile'])
        address = str(request.form['address'])
        country = str(request.form['country'])
        city = str(request.form['city'])
        contact = Contact(firstname=firstname, lastname=lastname,phone=phone,mobile=mobile,address=address,country=country,city=city)
        db.session.add(contact)
        db.session.commit()
    return render_template(
        'add.html')
    pass
