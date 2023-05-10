from flask import Flask, redirect, url_for, render_template

# create instance of Flask
app = Flask(__name__)

# render templated pages on website
@app.route('/<name>/')
def home(name):
    
    return render_template('index.html', content=name, r=2, list=['bill','john','tim'])

if __name__ == "__main__":
    # Add debug=True to auto restart upon changes
    app.run(debug=True)