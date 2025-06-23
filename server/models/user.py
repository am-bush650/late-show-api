from server.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)#unique identifier for each user
    username = db.Column(db.String(80), unique=True, nullable=False)#username must be unique and not null
    _password_hash = db.Column(db.Text, nullable=False)#stores the hashed password(not the raw password)


    #prevent password from being read directly
    @property
    def password(self):
        raise AttributeError("Password is write only.")
    
    #hash the password and store it
    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password)

    #check if the provided password matches the stored hash
    def verify_password(self, password):
        return check_password_hash(self._password_hash, password)