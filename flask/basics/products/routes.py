from flask import Blueprint,render_template,request

products=Blueprint('product',__name__)

@products.route('/')
def all_products():
    return render_template('products.html')

@products.route('/create',methods=['GET','POST'])
def create():
    if request.method=='POST':
        title= request.form['title']
        
        return f"title = {title}"
    
    return render_template('create.html')

@products.route('/<int:id>')
def single_product(id):
    return f"product id is {id}"




