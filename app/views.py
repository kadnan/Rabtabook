from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from .models import Contact

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
