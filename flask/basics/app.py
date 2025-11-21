from flask import Flask,render_template 
from products import routes
from users.routes import user
app=Flask(__name__)


app.register_blueprint(user,url_prefix='')

app.register_blueprint(routes.products,url_prefix='/products')

if __name__=='__main__':
    app.run(debug=True,port=5000)





