from market import app
from flask import render_template, url_for, redirect
from market.models import Item, User, User
from market.forms import RegisterForm
from market import db

@app.route('/')
@app.route('/home')   # farklı 2 dizinde aynı sayfa
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():

    items = Item.query.all()

    return render_template('market.html', items=items)


@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address = form.email_address.data,
                              password_hash = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors != {}: 
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}')
        
    return render_template('register.html', form = form)
