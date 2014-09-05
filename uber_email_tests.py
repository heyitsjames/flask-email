import os
import uber_email
import unittest
import tempfile

from uber_email import models, views

class UberEmailTestCase(unittest.TestCase):

    def setUp(self):
        uber_email.app.config['TESTING'] = True
        self.app = uber_email.app.test_client()

        self.good_data =  {
            'to': 'email@mail.com',
            'to_name': 'name',
            'from': 'from@from.com',
            'from_name': 'other name',
            'subject': 'hello',
            'body': '<h1>world</h1>',
        }

        self.missing_data =  {
            # 'to' is missing
            'to_name': 'name',
            'from': 'from@from.com',
            'from_name': 'other name',
            'subject': 'hello',
            'body': '<h1>world</h1>',
        }

        self.bad_email_data =  {
            'to': 'email@mail@.com',
            'to_name': 'name',
            'from': 'from@from.com',
            'from_name': 'other name',
            'subject': 'hello',
            'body': '<h1>world</h1>',
        }

    def tearDown(self):
        pass

    # test model creation, inits with data
    def test_model_create(self):
        model = models.EmailModel(self.good_data)
        assert 'to' in model.data

    # test validation of email model works
    def test_validate_model(self):
        model = models.EmailModel(self.good_data)
        assert model.is_valid()

    # test validation fails with bad input
    def test_validate_model_fails(self):
        model = models.EmailModel(self.missing_data)
        assert model.is_valid() == False

    # test the clean() method strips tags
    def test_strip_tags(self):
        model = models.EmailModel(self.good_data)
        model.clean()
        assert model.data['body'] == 'world'

    # test post_message receives a 200
    def test_post_message_success_mandrill(self):
        uber_email.app.config['DEFAULT_MAILER'] = 'mandrill'
        model = models.EmailModel(self.good_data)
        
        assert model.is_valid()

        r = model.post_message()
        assert r.status_code == 200

    def test_post_message_success_mailgun(self):
        uber_email.app.config['DEFAULT_MAILER'] = 'mailgun'
        model = models.EmailModel(self.good_data)
        
        assert model.is_valid()

        r = model.post_message()
        assert r.status_code == 200

    # test post_message fails with bad data
    def test_post_message_failure_mandrill(self):
        uber_email.app.config['DEFAULT_MAILER'] = 'mandrill'
        model = models.EmailModel(self.good_data)
        
        assert model.is_valid()
        auth = ('key', uber_email.app.config['MANDRILL_API_KEY'])
        payload = {'nothing': 'here'}
        r = model.post_message(auth=auth, payload=payload)
        assert not r.ok

    def test_post_message_failure_mailgun(self):
        uber_email.app.config['DEFAULT_MAILER'] = 'mailgun'
        model = models.EmailModel(self.good_data)
        
        assert model.is_valid()
        auth = ('key', uber_email.app.config['MAILGUN_API_KEY'])
        payload = {'nothing': 'here'}
        r = model.post_message(auth=auth, payload=payload)
        assert not r.ok

if __name__ == '__main__':
    unittest.main()