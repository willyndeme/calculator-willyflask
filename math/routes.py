from flask import Blueprint,request,render_template
from calculator.math.forms import AdditionForm,SubtractForm,DivideForm,MultiplyForm
from flask_login import login_required

math=Blueprint('math',__name__)

@math.route('/')
@login_required
def home():
    return render_template('home.html')

@math.route('/Add',methods=['POST','GET'])
def add():
    form=AdditionForm()
    if request.method=='POST':
        number1=int(request.form.get('number1'))
        number2=int(request.form.get('number2'))
        add=number1+number2
        return render_template('add.html',add=add,form=form)
    return render_template('add.html',form=form)

@math.route('/Subtract',methods=['POST','GET'])
def subtract():
    form=SubtractForm()
    if request.method=='POST':
        number1=int(request.form.get('number1'))
        number2=int(request.form.get('number2'))
        subtract=number1-number2
        return render_template('subtract.html',subtract=subtract,form=form)
    return render_template('subtract.html',form=form)

@math.route('/Divide',methods=['POST','GET'])
def divide():
    form=DivideForm()
    if request.method=='POST':
        number1=int(request.form.get('number1'))
        number2=int(request.form.get('number2'))
        divide=number1/number2
        return render_template('divide.html',divide=divide,form=form)
    return render_template('divide.html',form=form)

@math.route('/Multiply',methods=['POST','GET'])
def multiply():
    form=MultiplyForm()
    if request.method=='POST':
        number1=int(request.form.get('number1'))
        number2=int(request.form.get('number2'))
        multiply=number1*number2
        return render_template('multiply.html',multiply=multiply,form=form)
    return render_template('multiply.html',form=form)