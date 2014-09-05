DEBUG = True

MANDRILL_API_KEY = '<your mandrill key here>'
MAILGUN_API_KEY = '<your mailgun key here>'
MAILGUN_DOMAIN = '<your mailgun domain here>'

DEFAULT_MAILER = 'mandrill'

MAILER_SETTINGS = {
    'mandrill': {
        'auth': MANDRILL_API_KEY,
        'url': 'https://mandrillapp.com/api/1.0/messages/send.json'
    },
    'mailgun': {
        'auth': MAILGUN_API_KEY,
        'url': 'https://api.mailgun.net/v2/{0}/messages'.format(MAILGUN_DOMAIN)
    }
}