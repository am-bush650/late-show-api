from flask import Blueprint, request, jsonify
from server.models.user import User
from server.app import db
from flask_jwt_extended import create_access_token

#create blueprint for authentification routes
auth_bp = Blueprint("auth", __name__)

# POST / register - create new user
@auth_bp.route('/register', methods=["POST"])
def register():
    data = request.get_json()

    #check if username already exists
    if user.query.filter_by(username=data["username"]).first():
        return jsonify(message="Username already taken"), 400

    #create user and hash password via the property setter
    user = User(username=data["username"])
    user.password = data["password"] #this triggers the @password.setter

    #save to database
    db.session.add(user)
    db.session.commit()


    return jsonify(message="User created"), 201


# POST / lgin - authenticate and return JWT access token
@auth_bp.route('/login', methods=["POST"])
def login():
    data = request.get_json()

    #look for user by name
    user = User.query.filter_by(username=data["username"]).first()

    #verify password and return token if valid
    if user and user.verify_password(data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token), 200
    
    # invalid username or password
    return jsonify(message="Invalid credentials"), 401