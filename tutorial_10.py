from flask import Flask, render_template
from tenth import tenth

# instantiate Flask app
app = Flask(__name__)

# register blueprint 'second'
app.register_blueprint(tenth, url_prefix="/tenth/")

# define route
@app.route("/")
def main():
    return "<h1>Welcome to Tutorial #10</h1>" 

# run app
if __name__ == "__main__":
    app.run(debug=True)