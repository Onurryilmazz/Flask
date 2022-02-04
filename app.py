from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #app'imizin database tanıması için config
db = SQLAlchemy(app) #Python Class yapısı ile Database oluşturmak için kullanıyoruz


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


"""@app.route('/')
def index():
    return render_template('index.html')  #klasör adını bildiği için onu belirtmemize gerek yok

@app.route('/about')
def about_page():
    return 'About'

#dinamik rotalar
@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This page about {username}</h1>'
"""

@app.route('/')
@app.route('/home')   # farklı 2 dizinde aynı sayfa
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():

    items = Item.query.all()

    return render_template('market.html', items=items)




if __name__ == '__main__':
    app.run(debug=True)   #debug True : anlık değişiklileri web sitesinde güncelliyor. Deploy ederken False yap.