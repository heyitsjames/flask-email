import re
from .utils import strip_tags

class Model(object):
    # Model base class

    def __init__(self, data, *args, **kwargs):
        self.data = data

    FIELD_REQUIRED_MSG = 'This field is required'
    field_errors = {}
    fields = {}
    
    def validate(self):
        _field_errors = {}

        # this is a dumb place to put this
        self.clean()

        print(self.data['body'])
        for key, value in self.fields.iteritems():
            if key not in self.data and value == 'required':
                _field_errors[key] = self.FIELD_REQUIRED_MSG

            validator = 'validate_{0}'.format(key)
            if hasattr(self, validator) and callable(getattr(self, validator)):
                msg = getattr(self, validator)(self.data[key])
                if msg:
                    _field_errors[key] = msg

        return _field_errors if len(_field_errors.keys()) > 0 else None

    def clean(self):
        # to be overridden
        pass

    def is_valid(self):
        errors = self.validate()
        if errors:
            self.field_errors = errors
            return False
        return True

class EmailModel(Model):

    def __init__(self, *args, **kwargs):
        super(Email, self).__init__(*args, **kwargs)

    # There's really no good way to completely validate an e-mail, but
    # this simple regex check does the trick for most obvious scenarios
    VALID_EMAIL = re.compile('[^@]+@[^@]+\.[^@]+')

    fields = {
        'to': 'required',
        'to_name': 'required',
        'from': 'required',
        'from_name': 'required',
        'subject': 'required',
        'body': 'required',
    }

    def clean(self):
        # strip the tags from the body in self.data
        self.data['body'] = strip_tags(self.data['body'])

    def validate_to(self, field):
        valid_email = re.match(self.VALID_EMAIL, field)
        if not valid_email:
            return 'Please enter a valid email address'
        return ''

    def validate_from(self, field):
        valid_email = re.match(self.VALID_EMAIL, field)
        if not valid_email:
            return 'Please enter a valid email address'
        return ''
