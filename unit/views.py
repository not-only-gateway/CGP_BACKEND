from flask import request

from api.api import ApiView
from app import app, authorize
from app import db
from unit.models import Unit

api = ApiView(
    class_instance=Unit,
    identifier_attr='acronym',
    relationships=[
        {'key': 'parent_unit', 'instance': Unit},
        {'key': 'root', 'instance': Unit}
    ],

    db=db,
    on_before_call=authorize
)


@app.route('/api/unit/<e_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/api/unit', methods=['POST'])
def unit(e_id=None):
    if request.method == 'GET':
        return api.get(entity_id=e_id)
    elif request.method == 'POST':
        return api.post(package=request.json)
    elif request.method == 'PUT':
        return api.put(entity_id=e_id, package=request.json)
    elif request.method == 'DELETE':
        return api.delete(entity_id=e_id)


@app.route('/api/list/unit', methods=['GET'])
def list_unit():

    return api.list(request.args)
