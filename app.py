from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import requests
import env
from flask_migrate import Migrate

app = Flask(__name__)

app.config['MEDIA'] = 'media/'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config[
    'SQLALCHEMY_DATABASE_URI'] = env.DATABASE + '://' + env.USER + ':' + env.PASSWORD + '@' + env.HOST_NAME + '/' + env.DATABASE_NAME
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def authorize(method):
    token = request.headers.get('authorization', None)

    if token is not None:
        request_res = requests.get(
            env.AUTH_ENDPOINT,
            headers={'authorization': token},
            params={
                'method': request.method,
                'path': request.path
            })
        if request_res.status_code == 401:
            return jsonify({'status': 'error', 'description': 'unauthorized', 'code': 401}), 401
        return None
    else:
        return jsonify({'status': 'error', 'description': 'unauthorized', 'code': 401}), 401


CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from notification.models import Notification
from vacancy.models import Vacancy
from marital.models import MaritalStatus
from unit.models import Unit
from linkage.models import Linkage
from instruction.models import Instruction
from effective.models import Effective
from commissioned.models import Commissioned
from collaborator.models import Collaborator

import notification.views
import vacancy.views
import marital.views
import unit.views
import linkage.views
import instruction.views
import effective.views
import commissioned.views
import collaborator.views

db.create_all()



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1025)

