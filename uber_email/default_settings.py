DEBUG = True

MANDRILL_API_KEY = '5SGhFGKPpCk7cx8qhp3j-w'
MAILGUN_API_KEY = 'key-b6e6468eeca7f25c18f26c7beaf81ec3'
DEFAULT_MAILER = 'mandrill'
MAILGUN_SUBDOMAIN = 'sandbox668fc0038bf6476881a90d1ffb5e437c.mailgun.org'

MAILER_SETTINGS = {
    'mandrill': {
        'auth': MANDRILL_API_KEY,
        'url': 'https://mandrillapp.com/api/1.0/messages/send.json'
    },
    'mailgun': {
        'auth': MAILGUN_API_KEY,
        'url': 'https://api.mailgun.net/v2/{0}/messages'.format(MAILGUN_URL)
    }
}