from flask import Blueprint,request,redirect,url_for,render_template
from calculator.User.forms import RegistrationForm, LoginForm
from calculator import db,bcrypt
from flask_login import login_user,logout_user,login_required
from calculator.models import users

use=Blueprint('use',__name__)

@use.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        password_hash=bcrypt.generate_password_hash(password).decode('utf-8')
        user=users(username=username,email=email,password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('math.home'))
    return render_template('register.html',form=form)

@use.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash,form.password.data):
            login_user(user)
            return redirect(url_for('math.home'))
    return render_template('login.html',form=form)

@use.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('use.login'))