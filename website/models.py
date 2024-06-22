from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    userName = db.Column(db.String(150))
    expensess = db.relationship('Expenses')

class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date(), default=func.now())
    type = db.Column(db.String(30),default='income', nullable=False)
    category = db.Column(db.String(30), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __str__(self):
        return self.id