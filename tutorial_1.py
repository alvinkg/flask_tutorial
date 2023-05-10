from flask import Flask, redirect, url_for

# create instance of Flask
app = Flask(__name__)

# define pages on website
@app.route('/')
def home():
    return "Hello! This is the main page <h1>Hello<h1>"

# how to get variables passed in url as parameters
@app.route("/<firstname>,<lastname>")
def user(firstname, lastname):
    return f'Hello {firstname} {lastname}!'

# how to redirect users
@app.route('/admin/')
def admin():
    return redirect(url_for('user', firstname='alvin', lastname='lim'))

if __name__ == "__main__":
    app.run()