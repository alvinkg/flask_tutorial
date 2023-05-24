from flask import Flask, session, render_template, url_for, redirect, flash, request
from datetime import timedelta

app = Flask(__name__)
app.secret_key='hello'
app.permanent_session_lifetime = timedelta(seconds=80)

@app.route('/')
def home():
    return render_template('index6.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        if user:
            session['user'] = user
            session['login'] = True
            
            session.permanent = True
            return redirect(url_for('user'))
    else:
        if 'user' in session:
            redirect(url_for('user'))

    return render_template('login6.html')

@app.route('/logout/')
def logout():
    if 'user' in session:
        user = session['user']
        session.pop("user", None)
        flash(f"User '{user}' has been logged out.", "info")
    return redirect(url_for('login'))

@app.route('/user/')
def user():
    if 'user' in session:
        user = session['user']
        if session['login'] == True:
            flash(f"User '{user}' has been logged in successfully.", "info")
            session['login'] = False
        else:
            flash(f"Welcome back User '{user}'.", "info")
        return render_template('user6.html', user=user)
    else:
        flash('You are not logged in', 'info')
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)