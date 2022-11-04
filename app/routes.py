from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models import planet
from app.models.planet import Planet


# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description

     
planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

# Helper function:
def get_one_planet_or_abort(planet_name):    
    # incomplete: validate planet function
    planet = validate_planet(planet_name)

    matching_planet = Planet.query.get(planet_name)

    if not matching_planet:
        response_str = f"Planet with name `{planet_name}` was not found in the database."
        abort(make_response(jsonify({"message":response_str}), 404))
    
    return matching_planet


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

@planet_bp.route("/<planet_name>", methods=["PATCH"])
def update_planet_info(planet_name):
    planet = call_a_planet(planet_name)

    request_body = request.get_json()

    # need to test if this works if not all info is given, 
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_sun = request_body["distance_from_sun"]

    db.session.commit()
    # 
    return make_response(f"{planet_name} is successfully updated")
    

#delete function here 
@planet_bp.route("/<planet_name>", methods=["DELETE"])
def delete_one_planet(planet_name):
    chosen_planet = get_one_planet_or_abort(planet_name)

    db.session.delete(chosen_planet)
    db.session.commit()

    return jsonify({"message": f"Successfully deleted planet with id `{planet_name}`"}), 200


@planet_bp.route("/all", methods=["GET"])
def get_all_planets():
    planet_list = Planet.query.all()
    response = [planet.to_dict() for planet in planet_list]
    return jsonify(response), 200
    
@planet_bp.route("/<planet_name>", methods=["GET"])
def call_a_planet(planet_name):
    planet_list = Planet.query.all()

    #refactor GET route to use a helper function

    # if planet_name.isalpha() == False or planet_name.islower() == False:
    #     return jsonify({"message" : "Planet plathways will be lowercase with no special characters or numbers"}), 400
    # else:    


        
        response = [planet.to_dict() for planet in planet_list]
        return jsonify(response), 200

    
    return jsonify({"message": f"{planet_name} not found."}),404
    



    