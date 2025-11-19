from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from .data import blogs
# Create your views here.

def home(request):
    return HttpResponse('this is home page')

def all_blogs(request):
    return render(request,'blogs/all-blogs.html',{"blogs":blogs})

def find_blog_by_id(request,id):
    for blog in blogs:
        if blog['id'] == id:
            return render(request,'blogs/single-blog.html',{"blog":blog}) 
    return HttpResponseNotFound('blog not found')

# def find_blog_by_slug(request,slug):
#     return HttpResponse(f"{slug}")

def create_blog(request):
    return render(request,'blogs/create-blog.html')

def manage_blogs(request):
    return render(request,'blogs/manage.html')
# def home(request):
#     return HttpResponse('this is home page')

# def all_blogs(request):
#     return HttpResponse('this is all blog page')

# def find_blog_by_id(request,id):
#     return HttpResponse(f"{id}")

# def find_blog_by_slug(request,slug):
#     return HttpResponse(f"{slug}")

# def create_blog(request):
#     return HttpResponse('this create blog page')