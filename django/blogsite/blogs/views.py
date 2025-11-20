from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from .data import blogs
from .forms import BlogForm
from .models import Blog
# Create your views here.

def home(request):
    return HttpResponse('this is home page')

def all_blogs(request):
    blogs=Blog.objects.all()
    return render(request,'blogs/all-blogs.html',{"blogs":blogs})

def find_blog_by_id(request,id):
    blog=Blog.objects.get(id=id)
    return render(request,'blogs/single-blog.html',{"blog":blog}) 
   
    # for blog in blogs:
    #     if blog['id'] == id:
    #         return render(request,'blogs/single-blog.html',{"blog":blog}) 
    return HttpResponseNotFound('blog not found')

# def find_blog_by_slug(request,slug):
#     return HttpResponse(f"{slug}")

def create_blog(request):
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blogs')
    else:
        form=BlogForm()
    return render(request,'blogs/create-blog.html',{
        "form":form
    })
def update_blog(request,id):
    instance=Blog.objects.get(pk=id)
    if request.method=='POST':
        form=BlogForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blogs')
    else:
        form=BlogForm(instance=instance)
    return render(request,'blogs/update.html',{
        "form":form
    })
def manage_blogs(request):
    blogs=Blog.objects.all()
    return render(request,'blogs/manage.html',{
        "blogs":blogs 
    })
def delete_blog(request,id):
    if request.method=='POST':
        blogs=Blog.objects.get(pk=id)
        blogs.delete()
    return HttpResponseRedirect('/blogs/manage')
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