from flask import Flask, redirect, url_for, render_template

# create instance of Flask
app = Flask(__name__)

# render templated pages on website
@app.route('/<name>/')
def home(name):
    
    return render_template('index2.html', content=name, r=2, list=['bill','john','tim'])


@app.route('/')
def test():
    return render_template('index2a.html', content='Tim', i = 5, table = ['Tom', 'Dick', 'Harry'])

if __name__ == "__main__":
    app.run(debug=True)
