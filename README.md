# Flask Tutorial

## Basics

### Install using the requirements.txt

pip install -r requirements.txt

### Using grep to build requirements.txt

pip freeze | grep -i flask >> requirements.txt

## Tutorial 1 How to Make Websites with Python

- What is Flask
  - microweb framework when compared to Django
    - does not come with user authentication, database connectivity though it is doable
  - used to build websites with python, specifically the backend
  - The frontends connect via RESTFUL API
- How to build a flask app
- How to use it to make websites
- How to do a redirect with flask mtd redirect
- How to use url_for in redirect
- How to pass parameters encoded to your redirect

### Steps

#### install a virtual environment

#### Install flask

```bash
% pip install flask
```

#### import Flask

```bash
% from flask import Flask
```

#### Create instance of Flask inside a python file

```bash
app = Flask(__name__)
if __name__ == "__main__":
  app.run()
```

### Create a home page using a decorator

```bash

# instance of Flask
app = Flask(__name__)

# Home Page
@app.route("/")
def home('/'):
return "Hello! This is the main page <h1>HELLO</h1>"

# Page takes input from url and returns it in html
@app.route("/<name>")
def user(name):
return f'Hello{name}!'

# app runs if main module
if __name__ == "__main__":
# add paramater to auto-restart which code change detected
  app.run(debug=True)
 
```

### How to user redirect and url_for methods

First import redirect and url_for

A request for the page 'admin' will be redirected to 'home'.

```bash
from flask import redirect, url_for

@app.route('/admin')
def admin():
  return redirect(url_for('home'))
```

When redirecting to a page that takes inputs, we can pass default values to the parameters required by the page we are redirecting to.

```bash
@app.route('/admin/')
def admin():
  return redirect(url_for('user', firstname='Tom', lastname='Wong'))
```

## Tutorial 2 HTML Templates

### Build web pages from html files with render_template

Create templates directory to store all the html files
Create template using a html file eg. index.html
Call render_template mtd to render html file index.html

```bash
@app.route('/')
def Home():
  return render_template('index.html')
```

### Pass values to web pages

We can pass values and lists to web pages by enclosing them with {{ }} in the web pages.  The methods define and pass the values in the return statement.

```bash
    <p> Below we run a if loop nested in a for loop</p>
    {% for x in range(10)%}
        {% if x % 2 == 1%}
            <p>{{x}}</p>
        {% endif%}
    {% endfor %}
```

### Add pythonic logic to web pages

Write python in html by enclosing the code with the {% %} and ending with {% %}

```bash
<h1>Home Page!</h1>
{% for _ in range(0,10) %}
  <p> Hello </p>
{% endfor %}
```

## Tutorial 3 Adding Bootstrap and Template Inheritance

### Create a base template to work off with Flask Inheritance

We select a base template or create one from scratch.  We add {% block <block name>>%} that identifies the block, followed by  the {%endblock %}, marking out the locations of the changes.
For each child page, we extend at the top of the file the base with {% extends "path to base template" %}, then we provide the contents by filling in between each block.

We do this to avoid repeating code.  For example most pages need a navbar that is common.  This helps in verson control and ensures our changes are fully implemented.

### Using Bootstrap to add a navbar

First add to the <head> tag just under the <title> tag the link to the css code.

```bash
<title>{% block title %}{%endblock%}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
  ```

Add the following javascript code via the script just before the <body> tag.

```bash
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
  </body>
```

We can make additional modifications to change the navbar color, responsiveness and location.

### Use Bootstrap to create a navbar

We can add components to our web pages.  Here we add a navbar from Bootstrap.  I have changed the color and the search field to dark.  Below is a snippet of what was added in base_3a.html.

```bash
  <body>
    <div class="container">
        <nav class="navbar bg-primary navbar-expand-lg" data-bs-theme="dark">
            <div class="container-fluid">
```

### Tutorial 4: HTTP Methods (GET & POST ) and retrieving form Data

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

Steps

- install flask-sqlalchemy

  ```bash
  % pip install flask-sqlalchemy
  ```

Then just import sqlalchemy as required.


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

## References

[video](https://www.youtube.com/watch?v=mqhxxeeTbu0)
