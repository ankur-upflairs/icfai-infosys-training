from flask import Blueprint,render_template ,request

user=Blueprint('user',__name__,template_folder='templates/')

@user.route('/')
def home():
    return 'this is the home page'

@user.route('/about/')
def about():
    return 'this is about page'

@user.route('/user/create',methods=['GET','POST'])
def create_user():
    if request.method == 'POST':
        return 'form data submitted'
    return render_template('create-user.html')


@user.route('/users/<name>')
def users(name):
    return f"name is {name}"
