from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt 
from flask_cors import CORS, cross_origin
from models import db, User
 
app = Flask(__name__)
 
app.config['SECRET_KEY'] = 'login-api'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'
 
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
  
bcrypt = Bcrypt(app) 
CORS(app, supports_credentials=True)
db.init_app(app)
  
with app.app_context():
    db.create_all()
 
@app.route("/")
def hello_world():
    return "Login API"
 
@app.route("/signup", methods=["POST"])
def signup():
    user_id = request.json["id"]
    firstName = request.json["firstName"]
    lastName = request.json["lastName"]
    phoneNumber = request.json["phoneNumber"]
    email = request.json["email"]
 
    user_exists = User.query.filter_by(email=email).first() is not None
 
    if user_exists:
        return jsonify({"error": "Email already exists"}), 409
     
    new_user = User(id=user_id,firstName=firstName,lastName=lastName,phoneNumber=phoneNumber,email=email)
    db.session.add(new_user)
    db.session.commit()
 
 
    return jsonify({
        "id": new_user.id,
        "firstName": new_user.firstName,
        "lastName": new_user.lastName,
        "phoneNumber": new_user.phoneNumber,
        "email": new_user.email
    })
 
if __name__ == "__main__":
    app.run(debug=True)