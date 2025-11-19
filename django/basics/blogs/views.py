from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse

from .data import blogs
# Create your views here.
def all_blogs(request):
    blog_html=''
    for blog in blogs:
        blog_html+= f"<li><a href='/blogs/{blog['id']}' >{blog['title']}</a></li>"
    blog_html=f"<ul>{blog_html}</ul>"
    return HttpResponse(blog_html)

def find_blog_by_id(request,id):
    try:
        for obj in blogs:
            if obj['id']==id:
                slug=obj['slug']
                break    
        slug_path=reverse('blog_id',args=[slug])
        return HttpResponseRedirect(slug_path)
    except:
        return HttpResponseNotFound('<h1>id not found</h1>')
    
def find_blog_by_slug(request,slug):
     for obj in blogs:
            if obj['slug']==slug:                
                return HttpResponse(f"<h3>{obj['title']}</h3><p>{obj['description']}</p>")
 
