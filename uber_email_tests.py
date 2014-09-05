import os
import uber_email
import unittest
import tempfile

class UberEmailTestCase(unittest.TestCase):

    def setUp(self):
        uber_email.app.config['TESTING'] = True
        self.app = uber_email.app.test_client()

    def tearDown(self):
        pass

    # test model creation, inits with data

    # test validation of email model works

    # test validation fails with bad input

    # test the clean() method strips tags

    # test post_message recieves a 200

    # test post_message receives a 400 using bad data

        # test last two with both mandrill and mailgun



if __name__ == '__main__':
    unittest.main()