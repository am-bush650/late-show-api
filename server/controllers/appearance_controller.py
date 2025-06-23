from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from server.app import db

#blueprint for all appearance realated routes
appearance_bp = Blueprint("appearances", __name__)


# POST / appearances - create a new appearance
@appearance_bp.route('/appearances', methods=["POST"])
@jwt_required()
def create_appearance():

    #parse json data from the request body
    data = request.get_json()

    #look up guest and episode by ID
    guest = Guest.query.get(data.get("guest_id"))
    episode = Episode.query.get(data.get("episode_id"))

    #return error if either guest or episode does not exist
    if not guest or not episode:
        return jsonify(message="Guest or episode not found."), 404
    
    #validate rating
    rating = data.get("rating")
    if rating is None or not (1 <= int(rating) <= 5):
        return jsonify(meesage="Rating mustbe between 1 and 5"), 400
    
    #create the appearnace
    appearance = Appearance(
        guest_id = guest.id,
        episode_id = episode.id,
        rating = rating
    )
    #save to database
    db.session.add(appearance)
    db.session.commit()

    #return the newly created appearance data
    return jsonify({
        "id": appearance.id,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id,
        "rating": appearance.rating
    }), 201
