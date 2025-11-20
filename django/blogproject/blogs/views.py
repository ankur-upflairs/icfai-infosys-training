from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse 
from .data import blogs
from .forms import BlogForm
from .models import Blog
# Create your views here.

def learn_sessions(request):
    # request.session['auth'] = True  
    if 'auth' in request.session :
        print('authentication')
    return render(request,'blogs/thanks.html')

def create_blog(request):
    if request.method == 'POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            # title=form.cleaned_data['title']
            # rating=form.cleaned_data['rating']
            # blog=Blog(title=title,rating=rating)
            # blog.save()
        # print(request.POST['title'])
        # print('post request received')
            return render(request,'blogs/thanks.html')
    else:
        form=BlogForm()
    return render(request,'blogs/create.html',{
        "form":form
    })




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