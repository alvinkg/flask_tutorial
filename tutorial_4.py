from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index4.html')

# login page exposing a list of two mtd 'get, post'
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['name']
        if user:
            return redirect(url_for('user', usr=user))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

# user page
@app.route("/<usr>/")
def user(usr):
    return f"<h1> {usr} </h1>"

if __name__ == '__main__':
    app.run(debug=True)