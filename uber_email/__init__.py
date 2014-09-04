from flask import Flask

app = Flask(__name__)
app.config.from_object('default_settings')

import uber_email.views