from flask import Flask, redirect, url_for

# create instance of Flask
app = Flask(__name__)

# define pages on website
@app.route('/')
def home():
    return "Hello! This is the main page <h1>Hello<h1>"

# how to get variables passed in url as parameters
@app.route("/<name>")
def user(name):
    return f'Hello {name}!'

# how to redirect users
@app.route('/admin')
def admin():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()