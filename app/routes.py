from flask import Blueprint, jsonify, request, make_response
from app import db
from app.models.planet import Planet


# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description

     
# planets_list = [
#     Planet(1, 'Mercury', "Mercury is the smallest planet in the Solar System and the closest to the Sun. It's orbit around the Sun takes 87.97 Earth days, the shortest of all the Sun's planets"),
#     Planet(2, 'Venus', "Venus is the second planet from the Sun. It is sometimes called Earth's 'sister' or 'twin' planet as it is almost as large and has a similar composition. Venus, like Mercury, appears in Earth's sky never far from the Sun, either as morning star or evening star with a synodic period of 1.6 years."),
#     Planet(3, 'Earth', "Earth is the third planet from the Sun and the only astronomical object known to harbor life. While large volumes of water can be found throughout the Solar System, only Earth sustains liquid surface water. About 71% of Earth's surface is made up of the ocean, dwarfing Earth's polar ice, lakes, and rivers."),
#     Planet(4, 'Mars', "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury. In the English language, Mars is named for the Roman god of war."),
#     Planet(5, 'Jupiter', "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, but slightly less than one-thousandth the mass of the Sun."),
#     Planet(6, 'Saturn', "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth. It has only one-eighth the average density of Earth; however, with its larger volume, Saturn is over 95 times more massive."),
#     Planet(7, 'Uranus', "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, but slightly less than one-thousandth the mass of the Sun."),
#     Planet(8, 'Neptune', "Neptune is the eighth planet from the Sun and the farthest known solar planet. In the Solar System, it is the fourth-largest planet by diameter, the third-most-massive planet, and the densest giant planet. It is 17 times the mass of Earth, and slightly more massive than its near-twin Uranus"),
# ]

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
    
    return make_response(f"{new_planet} was added", 201)



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
         

  

    