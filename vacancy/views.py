from flask import request

from api.api import ApiView
from app import app, authorize
from app import db
from collaborator.models import Collaborator
from commissioned.models import Commissioned
from vacancy.models import Vacancy
from unit.models import Unit

api = ApiView(
    class_instance=Vacancy,
    identifier_attr='id',
    relationships=[
        {'key': 'commissioned', 'instance': Commissioned},
        {'key': 'unit', 'instance': Unit},
        {'key': 'holder', 'instance': Collaborator},
        {'key': 'substitute', 'instance': Collaborator},
    ],
    db=db,
    on_before_call=authorize
)


@app.route('/api/vacancy/<e_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/api/vacancy', methods=['POST'])
def vacancy(e_id=None):
    if request.method == 'GET':
        return api.get(entity_id=e_id)
    elif request.method == 'POST':
        return api.post(package=request.json)
    elif request.method == 'PUT':
        return api.put(entity_id=e_id, package=request.json)
    elif request.method == 'DELETE':
        return api.delete(entity_id=e_id)


@app.route('/api/list/vacancy', methods=['GET'])
def list_vacancy():
    return api.list(request.args)
