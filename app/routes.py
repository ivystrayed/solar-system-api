from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models import planet
from app.models.planet import Planet


# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description

     
planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

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

# need to add a patch function here 
@planet_bp.route("/<planet_name>", methods=["PATCH"])
def update_planet_info():
    pass 

    # if or try to create the 404

    #update info

    # response


#delete function here 
@planet_bp.route("/<planet_name>", methods=["DELETE"])
def delete_planet():
    # 404 if planet doesnt exist

    # delete command

    # response
    pass 



@planet_bp.route("/all", methods=["GET"])
def get_all_planets():
    planet_list = Planet.query.all()

    response = []
    for planet in planet_list:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance from sun" : planet.distant_from_sun        
        }
        response.append(planet_dict)
    
    return jsonify(response), 200
    
@planet_bp.route("/<planet_name>", methods=["GET"])
def call_a_planet(planet_name):
    planet_list = Planet.query.all()

    if planet_name.isalpha() == False or planet_name.islower() == False:
        return jsonify({"message" : "Planet plathways will be lowercase with no special characters or numbers"}), 400

    for planet in planet_list:
        if planet.name.lower() == planet_name:
            response =  {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description        
             }
            return jsonify(response), 200
     
     
    return jsonify({"message": f"{planet_name} not found."}),404
         

  

    