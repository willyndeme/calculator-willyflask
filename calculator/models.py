from calculator import db,login
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return users.query.get(int(id))

class users(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,nullable=False,unique=True)
    email=db.Column(db.String,nullable=False,unique=True)
    password_hash=db.Column(db.String(12))
    
    def __init__(self,username,email,password_hash):
        self.username=username
        self.email=email
        self.password_hash=password_hash  