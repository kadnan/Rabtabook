from flask import (
    Flask,
    #abort,
    #flash,
    redirect,
    render_template,
    request,
    url_for,
)
import os
from flask.ext.sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'it is as simple as Flask App'
app.config['WTF_CSRF_ENABLED'] = True
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'dd632bba519f4d94ba9f3be32f5d90ed'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'database/migrations/')
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def index():
    contacts = [
        {
            'id':'1',
            'first_name':'Adnan',
            'last_name': 'Siddiqi',
            'phone': '9302020',
            'mobile': '9230012344',
            'address': 'A-X Block-X',
            'city': 'Karachi',
            'country': 'Pakistan',
        },
        {
            'id':'2',
            'first_name':'Ahmad',
            'last_name': 'Adnan',
            'phone': '9221-939393',
            'mobile': '923001234',
            'address': 'A-Z Block-Z',
            'city': 'Karachi',
            'country': 'Pakistan',
        }
    ]
    return render_template(
                'index.html',
                contacts=contacts)

@app.route('/view/<int:id>')
def view(id):
    contacts =  [
        {
            'id':'1',
            'first_name':'Adnan',
            'last_name': 'Siddiqi',
            'phone': '92213415041',
            'mobile': '923009290538',
            'address': 'A-270 Block-H',
            'city': 'Karachi',
            'country': 'Pakistan'
        }
    ]
    return render_template(
                'view.html',
                contacts=contacts)

if __name__ == '__main__':
    app.run()
