from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse 
from .data import blogs
# Create your views here.

def create_blog(request):
    return render(request,'blogs/create.html')

def all_blogs(request):
    return render(request,'blogs/allblogs.html',{
        "title":'All Blogs' ,"blogs":blogs
    })
def find_blog_by_id(request,id):
    try:
        for obj in blogs:
            if obj['id']==id:
                slug=obj['slug']
                break
        slug_path=reverse('blogs.slug',args=[slug])
        return HttpResponseRedirect(slug_path)
    except:
        return HttpResponseNotFound('<h1>id not found</h1>')
    
def find_blog_by_slug(request,slug):
     for obj in blogs:
            if obj['slug']==slug:                
               return render(request,'blogs/single-blog.html', {"blog":obj})