from flask import Flask,redirect,url_for,render_template,request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# session
app.secret_key = 'hello'
# setup dB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def home():
    if "user" in session:
        user = session['user']
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')

@app.route('/login/', methods=["POST","GET"])
def login():
    # if not logged in
    if request.method == "POST":
        session.permanent=True
        user = request.form['name']
        session['user'] = user
        
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
            
        flash(f"Login of {user} Successful!")
        return render_template("user.html", user=user)
        
    else:
        #if logged in already, since key in the dict 'session'
        if "user" in session:
            user = session['user']
            flash(f"User {user} already logged in session!")
            # return redirect(url_for("user"))
            return render_template("user.html", user=user)
    return render_template("login.html")


@app.route('/user/', methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form['email']
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash(f"Email {email} was saved.")
        else:
            if "email" in session:
                email = session["email"]
                flash(f"{email} has already logged in.")
        
        return render_template("user.html", email=email, user=user)
    else:
        flash(f"You are not logged in.")
        return redirect(url_for('login'))
    

@app.route('/logout/')
def logout():
    flash(f"You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)