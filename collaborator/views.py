from flask import request, jsonify, make_response
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
from PIL import Image
from io import BytesIO
import base64

def load_image(data):
    try:
        if data is None:
            raise ValueError
        f = open(data, "r")
        d = f.read()
        f.close()
        return d
    except (ValueError, OSError):
        return data


URL = 'http://192.168.1.188:443/api/collaborator/'
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
    on_key_parse=[{'key': 'image', 'loader': load_image}],
    db=db,
    on_before_call=authorize,
    keys_to_delete=[{"key": 'image', "replacement": lambda x: URL + x + '/image'}]
)


@app.route('/api/collaborator/<e_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/api/collaborator', methods=['POST'])
def collaborator(e_id=None):
    if request.method == 'GET':
        return api.get(entity_id=e_id, query=request.args.to_dict())
    elif request.method == 'POST':
        return api.post(package=request.json)
    elif request.method == 'PUT':
        return api.put(entity_id=e_id, package=request.json, use_self_update=True)
    elif request.method == 'DELETE':
        return api.delete(entity_id=e_id)


@app.route('/api/collaborator/<e_id>/image', methods=['GET'])
def img_collaborator(e_id=None):
    collab = Collaborator.query.get(e_id)
    if collab is not None and collab.image is not None:
        split = collab.image.replace("data:image/png;base64,", '')
        im = base64.b64decode(split.encode('ascii'))
        response = make_response(im, 200)
        response.mimetype = 'image/png'
        return response
    return 404


@app.route('/api/list/collaborator', methods=['GET'])
def list_collaborator():
    return api.list(data=request.args, require_call=False)
