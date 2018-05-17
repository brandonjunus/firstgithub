# external imports 
from flask import render_template, url_for, request, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user

# internal imports 
from kanyemadness import app, db
from models import Choices

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        username = current_user.username
        choice1 = request.form['choice1']
        choice2 = request.form['choice2']
        choice3 = request.form['choice3']
        choice4 = request.form['choice4']
        selections = Choices(username, choice1, choice2, choice3, choice4)
        db.session.add(selections)
        db.session.commit()
        return redirect(url_for('bracketcreated'))
    return render_template("create.html")


# imports related to login 
from forms import LoginForm
from werkzeug.security import check_password_hash

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('create'))
        flash("Username or Password is incorrect")
        return render_template('login.html', form = form)
    return render_template('login.html', form = form)


# imports related to registration
from forms import RegisterForm
from models import User
from werkzeug.security import generate_password_hash

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method = 'sha256')
        new_user = User(username = form.username.data, email=form.email.data, password= hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Your account has been created!")
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.route('/bracketcreated')
@login_required
def bracketcreated():
    return render_template("bracketcreated.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)