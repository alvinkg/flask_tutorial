from flask import Flask, render_template
from tenth import tenth
from admin.admin import admin

# instantiate Flask app
app = Flask(__name__)

# register blueprint 'tenth'
app.register_blueprint(tenth, url_prefix="/tenth/")
app.register_blueprint(admin, url_prefix="/admin/")

# define route
@app.route("/")
def main():
    return "<h1>Welcome to Tutorial #10</h1>" 

# run app
if __name__ == "__main__":
    app.run(debug=True)