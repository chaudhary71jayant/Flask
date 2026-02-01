from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' #Here we have named our data users.db

db = SQLAlchemy(app)

#Defining the database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    firstName = db.Column(db.String(100), nullable = False)
    lastName = db.Column(db.String(100), nullable = False)
    userName = db.Column(db.String(200), nullable = False)
    city = db.Column(db.String(200), nullable = False)
    zip = db.Column(db.String(100), nullable = False)


@app.route("/", methods = ['GET','POST'])
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

@app.route("/delete/<int:id>", methods =['GET','POST'])
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect('/')

if __name__  == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)