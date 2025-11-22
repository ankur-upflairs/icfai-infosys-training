from flask import Flask
from flask_migrate import Migrate
from extensions import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    # Import blueprints AFTER db.init_app
    from products.routes import products
    from users.routes import user
    from api.routes import products_api

    app.register_blueprint(user, url_prefix='')
    app.register_blueprint(products, url_prefix='/products')
    app.register_blueprint(products_api, url_prefix='/api')

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5000)
