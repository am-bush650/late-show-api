from server.app import db


#define guest model to represent a guest on the tv show
class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)#unique identifier for each guest
    name = db.Column(db.String, nullable=False)#guest's full name, required
    occupation = db.Column(db.String, nullable=False)#guest's occupation eg, actor, musician(required)


    #one to many relationships => a guest can have many apperances
    #backref='episode' => lets you access guest from an appearance (apperance.guest)
    #cascade='all, delete' => delete a guest and also deletes its appearances
    appearances = db.relationship("Appearance", backref="guest", cascade="all, delete")
    