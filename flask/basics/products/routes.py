from flask import Blueprint,render_template

products=Blueprint('product',__name__)

@products.route('/')
def all_products():
    return render_template('products.html')

@products.route('/<int:id>')
def single_product(id):
    return f"product id is {id}"




