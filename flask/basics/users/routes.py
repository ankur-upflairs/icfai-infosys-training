from flask import Blueprint

user=Blueprint('user',__name__)

@user.route('/')
def home():
    return 'this is the home page'

@user.route('/about/')
def about():
    return 'this is about page'

@user.route('/users/<name>')
def users(name):
    return f"name is {name}"
