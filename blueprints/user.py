from flask import Blueprint
import moudels.user

app=Blueprint("user ", __name__)


@app.route('/user ')
def user():  # put application's code here
    return 'This Is user Page '




