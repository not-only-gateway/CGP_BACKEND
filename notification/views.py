from flask import request

from app import app
from send_mail import send_email


@app.route('/api/notification', methods=['POST'])
def email_send():
    send_email(request.json)
