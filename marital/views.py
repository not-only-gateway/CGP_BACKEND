from flask import request

from api.api import ApiView
from app import app, authorize
from app import db
from marital.models import MaritalStatus

api = ApiView(
    class_instance=MaritalStatus,
    identifier_attr='id',
    relationships=[],
    db=db,
    on_before_call=authorize
)

@app.route('/api/marital_status/<e_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/api/marital_status', methods=['POST'])
def marital_status(e_id=None):
    if request.method == 'GET':
        return api.get(entity_id=e_id)
    elif request.method == 'POST':
        return api.post(package=request.json)
    elif request.method == 'PUT':
        return api.put(entity_id=e_id, package=request.json)
    elif request.method == 'DELETE':
        return api.delete(entity_id=e_id)


@app.route('/api/list/marital_status', methods=['GET'])
def list_marital_status():
    return api.list(request.args)
