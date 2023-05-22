from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

# login page exposing a list of two mtd 'get, post'
@app.route('/login/', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        user = request.form['name']
        # if there is any entry
        if user:
            return redirect(url_for('user', user=user))
    else:
        return render_template('index4.html')

# user page
@app.route("/<user>/")
def user(user):
    return f"<h1> {user} </h1>"

if __name__ == '__main__':
    app.run(debug=True)