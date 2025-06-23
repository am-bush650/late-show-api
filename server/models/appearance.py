from server.app import db

# apperance model representing a guest appearing in an episode
class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)#unique identifier for each appearance
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guest.id'))#foreign key linking to a specific guest who appeared
    episode_id = db.Column(db.Integer, db.ForeignKey('episode.id'))#foreign key linking to a specific episode where the guest appeared
