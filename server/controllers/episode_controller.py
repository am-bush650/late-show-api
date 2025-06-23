from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode 
from server.models.appearance import Appearance
from server.app import db


#a blueprint for episode routes
episode_bp = Blueprint("episode", __name__)


#GET / episode to return all episodes
@episode_bp.route('/episode', methods=["GET"])
def get_episodes():

    #query all episode records from database
    episodes = Episode.query.all()

    #serialize and return a list of episodes as json
    return jsonify([
        {"id": e.id, "date": e.date, "number": e.number}
        for e in episodes
    ]), 200


# GET / episodes / <id> return a specific episode with appearances
@episode_bp.route('/episodes/<int:id>', methods=["GET"])
def get_episode(id):

    #retrieve episode by id or return 404 if not found
    episode = Episode.query.get_or_404(id)

    #gather all guests and their details for appearances of this episode
    appearances = [
        {
            "id": a.id,
            "rating": a.rating,
            "guest": {
                "id": a.guest.id,
                "name": a.guest.name,
                "occupation": a.guest.occupation
            }
        }
        # access related apperances vis sqlalchemy relationship
        for a in episode.appearances
    ]
    #return episode info and all appearances
    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": appearances
    }), 200

# DELETE / episodes / <id> delete an episode jwt protected
@episode_bp.route('/episodes/<int:id>', methods=["DELETE"])
@jwt_required() #requires a valid jwt access token to access this route

def delete_episode(id):
    #find the episode or return 404 if it doesnt exist
    episode = Episode.query.get_or_404(id)

    #delete the episode and commit the change to the database
    db.session.delete(episode)
    db.session.commit()

    #return a sucess message
    return jsonify(message="Episode deleted"), 200
