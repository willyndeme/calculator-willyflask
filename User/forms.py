from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Length 

class RegistrationForm(FlaskForm):
    username=StringField('username',validators=[DataRequired(),Length(min=3,max=20)])
    email=EmailField('email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    password1=PasswordField('confirm password',validators=[EqualTo('password')])
    submit=SubmitField('register')
    
class LoginForm(FlaskForm):
    email=EmailField('email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('login')
    