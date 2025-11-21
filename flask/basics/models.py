
from app import db 

class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    price=db.Column(db.Integer,default=1)
    imageUrl=db.Column(db.String(200),default='')
    
    def __str__(self):
        return f"{self.title}"