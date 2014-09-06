## Uber Email

This is a simple app that exposes a REST endpoint and allows one to send an email via that endpoint. Mandrill and Mailgun are used as the transport backends.

### To install:

First, clone this repo and cd into the folder that git creates.  
Then, create your environment and activate:  

    virtualenv .
    source bin/activate
    
Next, pip install from the requirements.txt in the project root:  

    pip install -r requirements.txt
    
Everything should be installed by now. Now, open up `uber_email/default_settings.py` and add your Mandrill and Mailgun configs in these variables:  

    MANDRILL_API_KEY = '<your mandrill key here>'
    MAILGUN_API_KEY = '<your mailgun key here>'
    MAILGUN_DOMAIN = '<your mailgun domain here>'

You can run the application via runserver.py:  

    python runserver.py
  
By default, the server is running with production settings. To run in development mode, simply open up `uber_email/__init__.py` and change the following line:

    app.config.from_object('uber_email.production_settings')

To be

    app.config.from_object('uber_email.default_settings')
    
    
The test suite can be run by calling

    python uber_email_tests.py
    

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

    
    
### Design decisions
  
I chose Python/Flask as my language and framework for a few reasons. Firstly, I know Python and am fairly productive in it. Secondly, I had never used Flask in my life, but I heard that's what a good portion of Uber is built upon, so I decided to learn it. I can say I fully enjoyed myself.

One decision I made was to use as few non-standard frameworks and libraries as possible, for learning purposes. With the exception of the requests module and Flask, I stuck rather stringently to that end. I ended up creating my own Email Model, complete with field validators and other helper methods. This ended up cleaning up the actual views quite nicely, and provided a good decoupling of logic. And it was pretty fun to write.

### Things I could have done better

1. The model `clean()` method in my `EmailModel` is in a strange spot. I would have liked to rework how the overall validation flow goes so that it was in a more obvious and sane place
2. The post_message function inside my EmailModel is rather brittle; I'm not doing much error handling if the response completely blows up.
3. It would have been cool to add optional fields in the Model, right now the 'required' value for each field key is superfluous; It is never used. I had it in my mind to build in logic to handle optional paramaters, but never got around to it.
4. My testing suite could really use some work. I desperately desire to learn how to test well. My current job and employer don't hold testing or the time it takes in much regard, so I'm not 100% sure what I'm doing. I'd love to be part of a company where testing is more of a first-class citizen so I can learn how to do it, and do it well.
5. There is very high coupling between the `fields` in the Model and the `payload_handlers.py` methods. It would have been better to make a few "rules" concerning how the JSON structure is supposed to be laid out. The current approach makes the app much less DRY.

