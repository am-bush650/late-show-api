from flask import Blueprint, jsonify
from server.models.guest import Guest
from server.app import db


#create a blueprint for guest related routes
guest_bp = Blueprint("guests", __name__)


# GET / guests - return all guest records
@guest_bp.route('/guests', methods=["GET"])
def get_guests():

    #query all guest records from the database
    guests = Guest.query.all()

    #serialize and return each guest as a dictionary
    return jsonify([
        {"id": g.id, "name": g.name, "occupation": g.occupation}
        for g in guests
    ]), 200