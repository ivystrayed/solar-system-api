from app import db
from flask import Blueprint, jsonify, request

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    distance_from_sun = db.Column(db.Integer)

    def to_dict(self):
        planet_dict = {
            "id": self.id,
            "name": self.id,
            "description": self.description,
            "distance_from_sun": self.distance_from_sun
        }
        return planet_dict
    
    def validate_planet(self):
        if self.isalpha() == False or self.islower() == False:
            return jsonify({"message" : "Planet plathways will be lowercase with no special characters or numbers"}), 400

