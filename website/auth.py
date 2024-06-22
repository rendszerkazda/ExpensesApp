from flask import Blueprint, render_template, request, flash, redirect, url_for
from website.models import User
from website import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userName = request.form.get('userName')
        password = request.form.get('password')
        
        user = User.query.filter_by(userName=userName).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Sikeres bejelentkezés!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Hibás jelszó, próbáld újra.", category='danger')
        else:
            flash("A felhasználónév nem létezik", category='danger')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST': # if the form is submitted
        email = request.form.get('email')
        userName = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash("Az email cím túl rövid, adj meg egy hosszabb email címet.", category='danger')
        elif len(userName) < 2:
           flash("A felhasználónév túl rövid, adj meg egy hosszabb felhasználónevet.", category='danger')
        elif password1 != password2:
           flash("A jelszavak nem egyeznek", category='danger')
        elif len(password1) < 4:
           flash("A jelszó legalább 4 karakter hosszú kell legyen", category='danger')
        else:
            new_user = User(email=email, userName=userName, password=generate_password_hash(password1, method='pbkdf2:sha256', salt_length=8))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Fiók sikeresen létrehozva!", category="success")
            return redirect(url_for('views.home'))
           
    return render_template("sign_up.html", user=current_user)