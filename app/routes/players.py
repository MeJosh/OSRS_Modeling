import os
from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from flasgger import swag_from

bp = Blueprint('players', __name__)
mongo_url = os.environ['MONGO_URI']
client = MongoClient(mongo_url)
db = client.mydatabase

@bp.route('/', methods=['POST'])
@swag_from('swagger/add_player.yml')
def add_player():
    player = request.get_json()
    db.players.insert_one(player)
    return jsonify(player), 201

@bp.route('/<name>', methods=['GET'])
@swag_from('swagger/get_player.yml')
def get_player(name):
    player = db.players.find_one({'name': name})
    if player:
        return jsonify(player), 200
    else:
        return jsonify({'error': 'Player not found'}), 404

@bp.route('/<name>', methods=['PUT'])
@swag_from('swagger/update_player.yml')
def update_player(name):
    player = db.players.find_one({'name': name})
    if player:
        new_data = request.get_json()
        db.players.update_one({'name': name}, {'$set': new_data})
        return jsonify(new_data), 200
    else:
        return jsonify({'error': 'Player not found'}), 404

@bp.route('/<name>', methods=['DELETE'])
@swag_from('swagger/delete_player.yml')
def delete_player(name):
    result = db.players.delete_one({'name': name})
    if result.deleted_count == 1:
        return jsonify({'message': 'Player deleted'}), 200
    else:
        return jsonify({'error': 'Player not found'}), 404
