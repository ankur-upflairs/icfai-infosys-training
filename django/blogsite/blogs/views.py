from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from .data import blogs
from .forms import BlogForm,UserForm
from .models import Blog,Users
# Create your views here.

def home(request):
    return HttpResponse('this is home page')
def signup(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blogs/manage')
    else:
        form=UserForm()
    return render(request,'blogs/login.html',{"login":False,
                    "form":form})
def login(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            try:
                user=Users.objects.get(username=username)
                print('find')
                if user.password != password:
                    return render(request,'blogs/login.html',{"login":True,
                    "form":form,"err":2})
                # print(user)
                request.session['user']=user.username
                return HttpResponseRedirect('/blogs/manage')
            except:
                print('error')
                return render(request,'blogs/login.html',{"login":True,
                    "form":form,"err":1}) 
    else:
        form=UserForm()
    return render(request,'blogs/login.html',{"login":True,
            "form":form,"err":0})

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
    if 'user' not in request.session:
        return HttpResponseRedirect('/login') 
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