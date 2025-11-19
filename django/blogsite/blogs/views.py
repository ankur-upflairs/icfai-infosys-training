from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('this is home page')

def all_blogs(request):
    return render(request,'blogs/all-blogs.html')

def find_blog_by_id(request,id):
    return HttpResponse(f"{id}")

def find_blog_by_slug(request,slug):
    return HttpResponse(f"{slug}")

def create_blog(request):
    return HttpResponse('this create blog page')

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