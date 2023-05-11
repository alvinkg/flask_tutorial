# Flask Tutorial

## Basics

### Install using the requirements.txt

pip install -r requirements.txt

### Using grep to build requirements.txt

pip freeze | grep -i flask >> requirements.txt

### Tutorial 1

- How to build a flask app
- How to do a redirect with flask mtd redirect
- How to use url_for in redirect
- How to pass parameters encoded to your redirect

### Tutorial 2

- How to use render_template
  - create templates directory
  - create template html file
  - call render_template mtd to render html file
- How to pass parameters to template
  - add placeholders inside {{}} in html file
  - hard code param values in backend
- How to run pythonic logic in html
  - use {% %} to wrap code

## Tutorial 5

Sessions

- 'permanent' sessions
  - Your data can last as long as your browser's page is open by default
  - If you are redirected to another page all your data will need to be redirected by code
  - The alternative is to store data on the server for the duration of your session, that is as long as your browser is open
  - To keep your session data after the browser is closed, define the session lifetime
- permanent sessions lifetime
  - We can define the session lifetime to make them last longer than the browser lifetime
- secret key
  - We need to define a secret key if when we store session data on the server
  - app.secretkey

- Steps
  - import session from flask
  - set up session data when method = 'POST' from form
  - check if there is data is the session under the key

## Tutorial 6: Flashing a message

Steps

- import flash
- add to base.html messages
- add flash to locations where a message is required.

## Tutorial 7: Using SQLAlchemy dB

## Tutorial 9: Static Files

This includes css stylesheets and images.
We create a directory 'static' and store our static files inside, using sub-directories like images.

### CSS

- We first add a style.css stylesheet to the static folder.
- Add bootstrap script inside style.css
  - body {color:aqua;}
- Link to style.css inside the html file
- We can add our default bootstrap cdn link above to allow our style.css stylesheet to overwrite it. See below.
  
```bash
<link rel="stylesheet" type="text/css" href="{{url_for('static',filename='style.css')}}">
```

## Tutorial 10 Blueprints

Blueprints allow us to organize our code better, either functionally or into apps (referred to as divisions in exploreflask.com).  If the code is really meant to be together then blueprints are a collection of views.  Should we expect them to work as standalone apps, then divisions is the way to go.  Each app or division will have its own templates and static directories, making it easy to pass along to someone.

Steps

- import Blueprint into the new app's python file.

```bash
from flask import Blueprint
```

- register the blueprint variable in the main view python file.

```bash
second = Blueprint('second', __name__, static_folder='static', template_folder='templates')
```

- import the blueprint variable from the other view file and register it.

```bash
from second import second

then...
app.register_blueprint(second, url_prefix="")
```

### Resources

[exploreflask.com](https://exploreflask.com/en/latest/blueprints.html)

## Tutorial #11 How to deploy Flask to a Linux server

Tim recommended a few apps:

- PuTTY
- Bitvise SSH Client
- Bitvise SSH Server
He uploads his Flask app into a linode server.
Since I am using DigitalOcean I will place the page link below

[How to deploy a Flask app to Digital Ocean's app platform](https://dev.to/ajot/how-to-deploy-a-flask-app-to-digital-oceans-app-platform-goc)

[Deploy a Flask App Using Gunicorn to App Platform](https://docs.digitalocean.com/tutorials/app-deploy-flask-app/)

```bash
https://docs.digitalocean.com/tutorials/app-deploy-flask-app/

https://dev.to/ajot/how-to-deploy-a-flask-app-to-digital-oceans-app-platform-goc
```

## References

[video](https://www.youtube.com/watch?v=mqhxxeeTbu0)
