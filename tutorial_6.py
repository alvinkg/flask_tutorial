from flask import Flask, render_template, redirect, request, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)

# session
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    if "user" in session:
        user = session['user']
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')
    
@app.route("/login/", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['name']
        session['user'] = user
        flash(f"Login for {user} is successful!")
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            user = session['user']
            flash(f'{user} already logged in!')
            return redirect(url_for('user'))
        
        return render_template('login.html')
        
@app.route('/user/')
def user():
    if 'user' in session:
        user = session['user']
        # return f"<h1>{user}</h1>"
        # replace above code with below render_template of 'user.html'
        return render_template('user.html', user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for('login'))
        # return render_template('login') ###
    
@app.route('/logout/')
def logout():
    if 'user' in session:
        user = session['user']
        flash(f"   You, {user} have been logged out!", "info")
        session.pop('user', None)
    else:
        flash(f"You are not logged in!", "info")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)