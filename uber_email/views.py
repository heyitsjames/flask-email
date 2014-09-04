import re
from uber_email import app
from flask import jsonify, request, abort
from .models import Email

@app.errorhandler(400)
def uber_email_400(error):
    response = jsonify(message=error.description, code=error.code)
    return response

@app.route('/api/emails', methods=['POST'])
def send_email():
    data = {} if request.json == None else request.json
    model = Email(data=data)

    if model.is_valid():
        return jsonify({ 'message': 'Email sent'}), 201
    else:
        abort(400, model.field_errors)
