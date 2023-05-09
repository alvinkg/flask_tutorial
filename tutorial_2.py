from flask import Flask, redirect, url_for, render_template

# create instance of Flask
app = Flask(__name__)

# define pages on website
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()