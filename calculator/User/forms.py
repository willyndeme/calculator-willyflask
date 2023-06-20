from calculator.models import users
from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Length,ValidationError

class RegistrationForm(FlaskForm):
    def validate_username(self,username):
        user=users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username taken..Please try a different one')
    
    def validate_email(self,email):
        user=users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email taken..Please try a different one')
    
    
    username=StringField('username',validators=[DataRequired(),Length(min=3,max=20)])
    email=EmailField('email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    password1=PasswordField('confirm password',validators=[EqualTo('password')])
    submit=SubmitField('register')
    

        
class LoginForm(FlaskForm):
    email=EmailField('email',validators=[DataRequired()])
    password=PasswordField('password',validators=[DataRequired()])
    submit=SubmitField('login')
    