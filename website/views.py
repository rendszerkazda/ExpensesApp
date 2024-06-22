from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from website.form import ExpensesForm
from website import db
from website.models import Expenses
import datetime as dt
import json

views = Blueprint('views', __name__) # Create a blueprint object, which is a python object that is used to organize the code in a flask application

@views.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.userName = request.form.get('userName')
        current_user.email = request.form.get('email')
        db.session.commit()
        flash("Profil frissítve!", category='success')
    count = Expenses.query.filter_by(user_id=current_user.id).count()
    return render_template("profile.html", user=current_user, count=count)

@views.route('/')
@login_required
def home():
    expenses = Expenses.query.filter_by(user_id=current_user.id).all()
    
    income_expense = db.session.query(db.func.sum(Expenses.amount), Expenses.type).filter_by(user_id=current_user.id).group_by(Expenses.type).all()
    ie_labels = [income_expense[1] for income_expense in income_expense]
    ie_values = [income_expense[0] for income_expense in income_expense]

    
    
    category_comparison = db.session.query(db.func.sum(Expenses.amount), Expenses.category).filter(Expenses.type == "Bevétel", Expenses.user_id == current_user.id).group_by(Expenses.category).order_by(Expenses.category).all()
    ic_labels = [category[1] for category in category_comparison]
    ic_values = [category[0] for category in category_comparison]

    category_comparison = db.session.query(db.func.sum(Expenses.amount), Expenses.category).filter(Expenses.type == "Kiadás", Expenses.user_id == current_user.id).group_by(Expenses.category).order_by(Expenses.category).all()
    ec_labels = [category[1] for category in category_comparison]
    ec_values = [category[0] for category in category_comparison]
    
    dates = db.session.query(db.func.sum(Expenses.amount), Expenses.date).filter(Expenses.type == "Kiadás", Expenses.user_id == current_user.id).group_by(Expenses.date).order_by(Expenses.date).all()

    over_time_expenditure = []
    date_labels = []
    for amount, date in dates:
        date_labels.append(date.strftime("%m-%d-%y"))
        over_time_expenditure.append(amount)

    return render_template('home.html',
                            user=current_user,
                            expenses=expenses,
                            ie_labels=ie_labels,
                            ie_values=ie_values,
                            ic_labels=ic_labels,
                            ic_values=ic_values,
                            ec_labels=ec_labels,
                            ec_values=ec_values,
                            over_time_expenditure=over_time_expenditure,
                            date_labels=date_labels
                        )

@views.route('/add', methods=['GET','POST'])
@login_required
def add():
    form = ExpensesForm()
    if request.method == 'POST':
        type = form.type.data
        category = form.category.data
        amount = form.amount.data
        date = form.date.data
        new_expense = Expenses(type=type, category=category, amount=amount, date=date, user_id=current_user.id)
        db.session.add(new_expense)
        db.session.commit()
        flash("Hozzáadás sikeres!", category='success')
    return render_template("add.html", title='Bejegyzés hozzáadása',user=current_user, form=form,btn=['outline-primary','Hozzáadás'])

@views.route('/delete/<int:id>')
@login_required
def delete(id):
    expense = Expenses.query.get(id)
    if expense.user_id == current_user.id:
        db.session.delete(expense)
        db.session.commit()
        flash("Törlés sikeres!", category='success')
    return redirect(url_for('views.home'))

@views.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def update(id):
    if request.method == 'POST':
        expense = Expenses.query.get(id)
        expense.type = request.form.get('type')
        expense.category = request.form.get('category')
        expense.amount = request.form.get('amount')
        expense.date = dt.datetime.strptime(request.form.get('date'), '%Y-%m-%d') # Convert the string to a datetime object
        db.session.commit()
        flash("Módosítás sikeres!", category='success')
        return redirect(url_for('views.home'))
    else:
        form = ExpensesForm()
        form.type.data = Expenses.query.get(id).type
        form.category.data = Expenses.query.get(id).category
        form.amount.data = Expenses.query.get(id).amount
        form.date.data = Expenses.query.get(id).date
    return render_template("add.html", title='Bejegyzés módosítása', user=current_user, form=form, btn=['warning','Módosítás'])