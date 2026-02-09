from flask import  Blueprint,request, redirect, render_template
from models.users import User
from db.index import db

add_user_bp = Blueprint('add_user_bp',__name__)

@add_user_bp.route("/", methods =  ['GET','POST'])
def add_user():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        userName = request.form['Username']
        city = request.form['city']
        zip = request.form['zip']

        new_user = User(firstName = firstName,lastName = lastName,userName = userName, city= city, zip = zip)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    
    return render_template('index.html')





