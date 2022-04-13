from flask import request, jsonify
import requests
import env
from api.api import ApiView
from app import app
from app import authorize
from app import db
from commissioned.models import Commissioned
from effective.models import Effective
from instruction.models import Instruction
from linkage.models import Linkage
from marital.models import MaritalStatus
from collaborator.models import Collaborator
from unit.models import Unit

api = ApiView(
    class_instance=Collaborator,
    identifier_attr='id',
    relationships=[
        {'key': 'unit', 'instance': Unit},
        {'key': 'effective', 'instance': Effective},
        {'key': 'commissioned', 'instance': Commissioned},
        {'key': 'marital_status', 'instance': MaritalStatus},
        {'key': 'linkage', 'instance': Linkage},
        {'key': 'instruction', 'instance': Instruction}
    ],
    db=db,
    on_before_call=authorize
)

@app.route('/api/collaborator/<e_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/api/collaborator', methods=['POST'])
def collaborator(e_id=None):
    if request.method == 'GET':
        return api.get(entity_id=e_id)
    elif request.method == 'POST':
        return api.post(package=request.json)
    elif request.method == 'PUT':
        return api.put(entity_id=e_id, package=request.json)
    elif request.method == 'DELETE':
        return api.delete(entity_id=e_id)



@app.route('/api/list/collaborator', methods=['GET'])
def list_collaborator():
    return api.list(request.args)



