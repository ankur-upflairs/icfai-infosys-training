from flask import Blueprint, request, jsonify

from models import Products
from extensions import db

products_api = Blueprint("products_api", __name__)

# ---------------------------
# Get all products
# ---------------------------
@products_api.route("/products", methods=["GET"])
def get_products():
    products = Products.query.all()
    return jsonify([p.to_dict() for p in products]), 200


# ---------------------------
# Get single product by id
# ---------------------------
@products_api.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = Products.query.get(id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    return jsonify(product.to_dict()), 200


# ---------------------------
# Create product
# ---------------------------
@products_api.route("/products", methods=["POST"])
def create_product():
    data = request.json

    new_product = Products(
        title=data.get("title"),
        price=data.get("price", 1),
        imageUrl=data.get("imageUrl", "")
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product created", "product": new_product.to_dict()}), 201


# ---------------------------
# Update product
# ---------------------------
@products_api.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = Products.query.get(id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.json
    product.title = data.get("title", product.title)
    product.price = data.get("price", product.price)
    product.imageUrl = data.get("imageUrl", product.imageUrl)

    db.session.commit()

    return jsonify({"message": "Product updated", "product": product.to_dict()}), 200


# ---------------------------
# Delete product
# ---------------------------
@products_api.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Products.query.get(id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted"}), 200
