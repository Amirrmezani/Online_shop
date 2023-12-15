from flask import Blueprint

app=Blueprint("general ", __name__)


@app.route('/')
def general():  # put application's code here
    return 'This Is Main Page '


@app.route('/about')
def general_about():  # put application's code here
    return 'about us'



