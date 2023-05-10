from flask import Flask, redirect, url_for, render_template

# create instance of Flask
app = Flask(__name__)

# render templated pages on website
@app.route('/')
def home():
    
    return render_template('index.html' )

if __name__ == "__main__":
    # Add debug=True to auto restart upon changes
    app.run(debug=True)