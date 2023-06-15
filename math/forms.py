from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class AdditionForm(FlaskForm):
    number1=IntegerField('number1',validators=[DataRequired()])
    number2=IntegerField('number2',validators=[DataRequired()])
    submit=SubmitField('Add')
    
class SubtractForm(FlaskForm):
    number1=IntegerField('number1',validators=[DataRequired()])
    number2=IntegerField('number2',validators=[DataRequired()])
    submit=SubmitField('subtract')
    
class DivideForm(FlaskForm):
    number1=IntegerField('number1',validators=[DataRequired()])
    number2=IntegerField('number2',validators=[DataRequired()])
    submit=SubmitField('divide')
    
class MultiplyForm(FlaskForm):
    number1=IntegerField('number1',validators=[DataRequired()])
    number2=IntegerField('number2',validators=[DataRequired()])
    submit=SubmitField('multiply')