from flask import Flask, request, session, render_template, url_for, redirect
from datetime import timedelta

app = Flask(__name__)

# Session data is encrypted on the server and needs a secret key
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(seconds=30)

@app.route('/')
def home():
    return render_template('index5.html')

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        session.permanent = False
        # pass 'name' to session
        session["user"] = name
        if name:
            return redirect(url_for('user'))
    else:
        if "user" in session:
            return redirect(url_for('user'))
        return render_template('login5.html')
        
@app.route('/logout/')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))
                           
@app.route('/user/')
def user():
    # if this parameter is not empty => there is a session ongoing
    if "user" in session:
        # pass session user data to var user
        user = session["user"]
        print("session user: ", user)
        return f'<h1>{user}</h1>'
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)