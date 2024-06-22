from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired
import datetime

class ExpensesForm(FlaskForm):
    type = SelectField('Típus', validators=[DataRequired()],
                       choices= [('Bevétel', 'Bevétel'), 
                                  ('Kiadás', 'Kiadás')])
    category = SelectField('Kategória', validators=[DataRequired()],
                       choices = [('Bér', 'Bér'), 
                                  ('Autó', 'Autó'),
                                  ('Befektetés', 'Befektetés'),
                                  ('Mellékállás', 'Mellékállás'),
                                  ('Bevásárlás', 'Bevásárlás'),
                                  ('Rezsi', 'Rezsi'),
                                  ('Szórakozás', 'Szórakozás'),
                                  ('Egészség', 'Egészség'),
                                  ('Sport', 'Sport'),
                                  ('Oktatás', 'Oktatás'),
                                  ('Egyéb', 'Egyéb'),])
    amount = IntegerField('Összeg', validators=[DataRequired()], default=0)
    date = DateField('Dátum', validators=[DataRequired()], default=datetime.date.today(), format='%Y-%m-%d')
    submit = SubmitField('Hozzáadás')
    