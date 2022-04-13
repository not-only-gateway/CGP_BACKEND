from flask import request

from api.api import ApiView
from app import app, authorize
from app import db
from commissioned.models import Commissioned

api = ApiView(
    class_instance=Commissioned,
    identifier_attr='id',
    relationships=[],
    db=db,
    on_before_call=authorize
)

@app.route('/api/commissioned/<e_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/api/commissioned', methods=['POST'])
def commissioned(e_id=None):
    if request.method == 'GET':
        return api.get(entity_id=e_id)
    elif request.method == 'POST':
        return api.post(package=request.json)
    elif request.method == 'PUT':
        return api.put(entity_id=e_id, package=request.json)
    elif request.method == 'DELETE':
        return api.delete(entity_id=e_id)



@app.route('/api/list/commissioned', methods=['GET'])
def list_commissioned():
    return api.list(request.args)
