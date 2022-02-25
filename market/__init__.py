from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #app'imizin database tanıması için config
app.config['SECRET_KEY'] = '6d44279c7aa12a146ee1af62'
db = SQLAlchemy(app) #Python Class yapısı ile Database oluşturmak için kullanıyoruz

from market import routes