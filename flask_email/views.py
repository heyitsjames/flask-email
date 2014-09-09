import re, json
from flask_email import app
from flask import jsonify, request, abort
from .models import EmailModel

@app.errorhandler(400)
def flask_email_400(error):
    response = jsonify(message=error.description, code=error.code)
    return response

@app.route('/api/emails', methods=['POST'])
def send_email():
    data = {} if request.json == None else request.json
    model = EmailModel(data)

    if model.is_valid():
        response = model.post_message()
        if response.ok:
            return jsonify({ 'message': 'Message sent'}), 200
        else:
            return jsonify({'message': 'Message failed', 'reason': response.json()}), 400
    else:
        abort(400, model.field_errors)
