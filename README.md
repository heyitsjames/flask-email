## Flask Email

This is a simple app (for learning purposes) that exposes a REST endpoint and allows one to send an email via that endpoint. Mandrill and Mailgun are used as the transport backends.

### To install:

First, clone this repo and cd into the folder that git creates.  
Then, create your environment and activate:  

    virtualenv .
    source bin/activate
    
Next, pip install from the requirements.txt in the project root:  

    pip install -r requirements.txt
    
Everything should be installed by now. Now, open up `flask_email/default_settings.py` and add your Mandrill and Mailgun configs in these variables:  

    MANDRILL_API_KEY = '<your mandrill key here>'
    MAILGUN_API_KEY = '<your mailgun key here>'
    MAILGUN_DOMAIN = '<your mailgun domain here>'

You can run the application via runserver.py:  

    python runserver.py
  
By default, the server is running with production settings. To run in development mode, simply open up `flask_email/__init__.py` and change the following line:

    app.config.from_object('flask_email.production_settings')

To be

    app.config.from_object('flask_email.default_settings')
    
    
The test suite can be run by calling

    python flask_email_tests.py
    

### How to use

Once your server is running by executing the `runserver.py` script, it should be running on `http://localhost:5000`.
You may then hit the api endpoint `/api/emails` via POST. The following fields, are required:

- ‘to’ ­ The email address to send to
- ‘to_name’ ­ The name to accompany the email
- ‘from’ ­ The email address in the from and reply fields
- ‘from_name’ ­ the name to accompany the from/reply emails
- ‘subject’ ­ The subject line of the email
- ‘body’ ­ the HTML body of the email

Currently, all HTML will be stripped out of the `body` field. Only plain text is supported.

An example cURL to the `/api/emails` endpoint:

    curl -H "Content-Type: application/json" \
    http://localhost:5000/api/emails \
    -d '{"to": "email@email.com", "from": "email@another.email.com", "body": "<h1> Body</h1><span> This is a message.</span>", "from_name": "Alice", "to_name": "Bob", "subject": "Did you hear about Eve?"}'
