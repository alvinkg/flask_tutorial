# Flask Tutorial

## Basics

### Install using the requirements.txt

pip install -r requirements.txt

### Using grep to build requirements.txt

pip freeze | grep -i flask >> requirements.txt

## Tutorial 1 How to Make Websites with Python

### What is Flask

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

Add the following javascript code via the script just before the  body tag.

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

GET is to request for info from the server  transparently for example via the url.  
POST is to make a request for info securely via encrypted channels.

We first create index4.html to extend from base.html.
Next we define method 'login' in tutorial_4.py that render_template 'index4.html'.

We add in index4.html inside the block 'content' the following items:  a label 'Names', a text field and a submit button.

```bash
{%block content%}

<form action="#" method="POST">
    <p>Names:</p>
    <p><input type="text" name="name"/></p> 
    <p><input type="submit" submit="submit"/></p>

</form>

{%endblock%}
```

### Using the request method to determine what methods are being used

## Tutorial 5

### Sessions

Sessions are a way to store  information (user name, etc.) about a website visit between pages. The session data may be removed once the visitor logs out or leaves.

To use sessions we do the following:

```bash
from flask import Flask, request, session, render_template, url_for
from datetime import timedelta

app = Flask(__name__)

# Session data is encrypted on the server and needs a secret key
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=5)
```

With session activated, data is stored for as long the browswr window is maintained open.  During this time data about the user can be stored in a dictionary under 'session'.  There is no need to pass around variables.
Alternatively we can determine exactly how long the data is kept in the server irrespective of the browser status.  app.permanent_session_lifetime defines how long session data should be kept, even after logout or browser closure.  After that we need to define the value of session.permanent to be true.

Now, whenever data is posted, it can be stored in the dictionary of session.

```bash
@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        # pass 'name' to session
        session["user"] = name
```

## Tutorial 6: Message Flashing

Flask allows sending of text messages to give status info.

import flash

```bash
from flask import flash
```

Add flash messages to your python code to reflect an event or status

```bash
flash('You have been logged out successfully.', 'info')
```

To display the messages add the code below to the page to for loop through the flashed messages and flash them.

### with statement

By using the with statement we achieve neat code that ensures proper acquistion and release of resources in the background.  Otherwise these resources remaining may constitute a memory leak or loss data sitting in a buffer.

```bash
{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for message in messages %}
      <p>{{message}}</p>
    {% endfor %}
  {% endif %}
```

One issue remains, the message needs some conditional statements.  When logging out, code logic so that it is flashed when the user is logged in a a session.  I personalized the code by getting the user name from the session and adding it to the message.

```bash
@app.route('/logout/')
def logout():
    if 'user' in session:
        user = session['user']
        session.pop("user", None)
        flash(f"User '{user}' has been logged out.", "info")
    return redirect(url_for('login'))
```

## Tutorial 7: Using SQLAlchemy dB

### clean up session

When logging out we need to empty the session dictionary of variables, 'user' and 'email' with the method 'session.pop'.

```bash
@app.route('/logout/')
def logout():
    if 'user' in session:
        user = session['user']
        session.pop('user', None)
        session.pop('email', None)
        flash(f'User {user} has logged out.', 'info')
```

### Install flask-sqlalchemy


To showcase sqlalchemy we store the user supplied email address inside a sqlite dB.
First install flask-sqlalchemy
In the commmand line type:

  ```bash
  % pip install flask-sqlalchemy
  ```

Then import sqlalchemy as required in your python file.

```bash
from flask-sqlalchemy import SQLAlchemy
```



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
