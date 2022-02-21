from market import app
from flask import render_template
from market.models import Item

@app.route('/')
@app.route('/home')   # farklı 2 dizinde aynı sayfa
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():

    items = Item.query.all()

    return render_template('market.html', items=items)
