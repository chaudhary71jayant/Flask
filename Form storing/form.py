from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db' #Here we have named our data users.db

db = SQLAlchemy(app)

#Defining the database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(200), nullable = False)
    address = db.Column(db.String(400), nullable = False)


@app.route("/", methods = ['GET','POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        new_user = User(name=name,email=email,address = address)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('index.html')

if __name__  == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)