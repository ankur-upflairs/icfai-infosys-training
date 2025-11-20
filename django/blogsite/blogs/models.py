from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=55)
    category=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True,null=False)
    featured=models.BooleanField()
    content=models.TextField()

class Users(models.Model):
    username=models.CharField()
    password=models.CharField()
    