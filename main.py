from flask import Flask, render_template
from flask.templating import render_template_string

# Create a flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
# def index():
#     return '<h1>This is the home page!</h1>'

def index():
    return render_template('index.html')


# looks a lot like localhost:5000/user/Molefe
@app.route('/signin')
def sign_in():
    return render_template('signin.html')

# create custom url pages

# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500