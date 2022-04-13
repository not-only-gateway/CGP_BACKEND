from flask import request

from api.api import ApiView
from app import app, authorize
from app import db
from effective.models import Effective

api = ApiView(
    class_instance=Effective,
    identifier_attr='id',
    relationships=[],

    db=db,
    on_before_call=authorize
)


@app.route('/api/effective/<e_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/api/effective', methods=['POST'])
def effective(e_id=None):
    if request.method == 'GET':
        return api.get(entity_id=e_id)
    elif request.method == 'POST':
        return api.post(package=request.json)
    elif request.method == 'PUT':
        return api.put(entity_id=e_id, package=request.json)
    elif request.method == 'DELETE':
        return api.delete(entity_id=e_id)



@app.route('/api/list/effective', methods=['GET'])
def list_effective():
    return api.list(request.args)
