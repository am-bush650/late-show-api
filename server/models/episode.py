from server.app import db

#episode model representing a single late night tv episode
class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)#a unique identifier for each episode
    date = db.Column(db.String, nullable=False)#the date the episode will air stored as a string
    number = db.Column(db.Integer, nullable=False)# the episode number ie episode 1,2,3


    #one to many relationship => one episode can have many appearances
    #backref='episode' => lets you access episode from an appearance (apperance.episode)
    #cascade='all, delete' => delete an episode and its appearances
    appearances = db.relationship("Appearance", backref="episode", cascade="all, delete")

    