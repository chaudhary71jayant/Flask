from db.index import db

#Defining the database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    firstName = db.Column(db.String(100), nullable = False)
    lastName = db.Column(db.String(100), nullable = False)
    userName = db.Column(db.String(200), nullable = False)
    city = db.Column(db.String(200), nullable = False)
    zip = db.Column(db.String(100), nullable = False)