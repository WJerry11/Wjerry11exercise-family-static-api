"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("jackson")

# create dictionaries (objects) to add to the jackson_family list (aray)


# python a list of dictionaries=js an array of objects
# create 3 disctionaries of the family members in the instructions

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200


@app.route('/member/<int:member_id>', methods=['GET'])
def get_single_family_member(member_id):
    _members = jackson_family.get_member(member_id)
    return jsonify(_members), 200


@app.route('/member', methods=["POST"])
def create_new_member():

    member= request.json
    jackson_family.add_member(member)
    # return f'you successfully added' {member ["first_name"] }, {member ["last_name"] } to the list.,
    return "done"


@app.route('/member', methods=["DELETE"])
def delete_member(member_id):
    jackson_family.delete_member(member_id)
    return "done"


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
