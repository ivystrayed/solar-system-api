from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models import planet
from app.models.planet import Planet

     
planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

def validate_input(input):
    if input.isalpha() == False or input.islower() == False:
        return jsonify({"message" : "Planet plathways will be lowercase with no special characters or numbers"}), 400
    else:
        return True


@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()

    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        distance_from_sun = request_body["distance from sun"]
    )

    db.session.add(new_planet)
    db.session.commit()
    
    return make_response(f"{new_planet.name} was added", 201)

@planet_bp.route("/<planet_name>", methods=["DELETE"])
def delete_one_planet(planet_name):
    input_check = validate_input(planet_name)
    if input_check == True:
        db.session.delete(planet_name)
        db.session.commit()

        return jsonify({"message": f"Successfully deleted planet with id `{planet_name}`"}), 200
    else:
        return input_check


@planet_bp.route("/all", methods=["GET"])
def get_all_planets():
    planet_list = Planet.query.all()
    response = [planet.to_dict() for planet in planet_list]
    return jsonify(response), 200
    
@planet_bp.route("/<planet_name>", methods=["GET"])
def call_a_planet(planet_name):

    input_check = validate_input(planet_name)

    if input_check == True:
        try:
            planet = Planet.query.get(planet_name)
            return jsonify(planet.to_dict())

        except:
            response_str = f"Planet with name `{planet_name}` was not found in the database."
            abort(make_response(jsonify({"message":response_str}), 404))
    else:
        return input_check

@planet_bp.route("/<planet_name>", methods=["PATCH"])
def update_planet_info(planet_name):
    planet = call_a_planet(planet_name)

    request_body = request.get_json()

    # need to test if this works if not all info is given, 
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_sun = request_body["distance_from_sun"]

    db.session.commit()
    return make_response(f"{planet_name} is successfully updated")
    



    