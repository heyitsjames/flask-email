import json

def prepare_mandrill_payload(data, settings):
    auth = ('key', settings['auth'])
    payload = {
        'key': settings['auth'],
        'message': {
            'to': [
                {
                    'email': data['to'],
                    'name': data['to_name'],
                    'type': 'to'
                }
            ],
            'from_email': data['from'],
            'from_name': data['from_name'],
            'subject': data['subject'],
            'text': data['body']
        }
    }

    return auth, json.dumps(payload)


def prepare_mailgun_payload(data, settings):
    auth = ('api', settings['auth'])
    payload = {
        'to': data['to'],
        'from': data['from'],
        'subject': data['subject'],
        'text': data['body']
    }

    return auth, payload