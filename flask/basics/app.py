from flask import Flask,render_template 
from products import routes
from users.routes import user
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
db=SQLAlchemy(app)


class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))



app.register_blueprint(user,url_prefix='') 

app.register_blueprint(routes.products,url_prefix='/products')

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=5000)





