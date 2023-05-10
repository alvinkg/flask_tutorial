from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
# Session data is encrypted on the server and needs a secret key
app.secret_key = 'hello'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['name']
        session["user"] = user    
        if user:
            return redirect(url_for('user'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    
@app.route('/user/')
def user():
    if "user" in session:
        user = session['user']
        return f'<h1>{user}</h1>'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)