from flask import Blueprint,render_template,request,redirect,url_for
from models import Products,db

products=Blueprint('product',__name__)

@products.route('/')
def all_products():
    items=Products.query.all()
    # print(items)
    return render_template('products.html',items=items)

@products.route('/create',methods=['GET','POST'])
def create():
    if request.method=='POST':
        title= request.form['title']
        price= request.form['price']
        imageUrl= request.form['imageUrl']

        p=Products(title=title,price=price,imageUrl=imageUrl)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('all_Products'))    
    return render_template('create.html')

@products.route('/<int:id>')
def single_product(id):
    return f"product id is {id}"




