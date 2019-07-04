from flask import Flask, json, g, request, jsonify
from app.shop.services.member_service import MemberService as Member
from app.shop.services.store_service import StoreService as Store
from app.shop.schemas.store_schema import StoreSchema
from app.shop.schemas.member_schema import MemberSchema
from flask_cors import CORS
from .middlewares import login_required

app = Flask(__name__)
CORS(app)

@app.route('/stores', methods=['POST'])
@login_required
def create_store():
    store_data = StoreSchema().load(json.loads(request.data))
    
    if store_data.errors:
        return json_response({'error': store_data.errors}, 422)
    
    store = Store().create_store(store_data)
    return json_response(store)

@app.route('/stores', methods=['GET'])
@login_required
def find_stores():
    return json_response(Store().find_all_stores())
    

@app.route('/members', methods=['GET'])
def index():
    return json_response(Member().find_all_members())

@app.route('/members', methods=['POST'])
def create():
    member_data = MemberSchema().load(json.loads(request.data))
    
    if member_data.errors:
        return json_response({'error': member_data.errors}, 422)
    
    member = Member().create_member_for(member_data)
    return json_response(member)


@app.route('/members/<uuid:member_id>', methods=['GET'])
def show(member_id):
    member = Member().find_member(member_id)
    
    if member:
        return json_response(member)
    else:
        return json_response({'error': 'Member not found'}, 404)
    

@app.route('/members/<uuid:member_id>', methods=['PUT'])
def update(member_id):
    member_data = MemberSchema().load(json.loads(request.data))
    
    if member_data.errors:
        return json_response({'error': member_data.errors}, 422)
    else:
        member = Member().update_member_with(member_id, member_data)
    
    if member:
        return json_response(member)
    else:
        return json({'error': 'Member not found'}, 404)
    

@app.route('/members/<uuid:member_id>', methods=['DELETE'])
def delete(member_id):
    if Member().delete_member_for(member_id):
        return json_response({}, 204)
    else:
        return json_response({'error': 'Member not found'}, 404)

def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})