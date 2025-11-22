from extensions import db

class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    price=db.Column(db.Integer,default=1)
    imageUrl=db.Column(db.String(200),default='')
    
    def __str__(self):
        return f"{self.title}"
    def to_dict(self):
        return { "id":self.id,
                "title":self.title,
                "price":self.price,
                "imageUrl":self.imageUrl}