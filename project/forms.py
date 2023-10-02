from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class MyForm(FlaskForm):

    go_upstairs = BooleanField('You can go upstairs. Will you?',
                               render_kw={'class': 'form-control-field checkbox-field'})
    go_downstairs = BooleanField('You can go downstairs. Will you?',
                                 render_kw={'class': 'form-control-field checkbox-field'})
    way = SelectField('Choose any side of the world you want to go',
                      coerce=int,
                      choices=[(0, 'North'),
                               (1, 'East'),
                               (2, 'South'),
                               (3, 'West')],
                      render_kw={'class': 'form-control-field'})
    number_steps = IntegerField('How many steps will you do?',
                                validators=[DataRequired(), NumberRange(min=1)],
                                default=1,
                                render_kw={'class': 'form-control-field'})
    submit = SubmitField('go', render_kw={'class': 'form-control-field bot8'})