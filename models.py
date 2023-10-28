from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(11), primary_key=True, unique=True)
    firstName = db.Column(db.String(150), unique=True)
    lastName = db.Column(db.String(150), unique=True)
    phoneNumber= db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
