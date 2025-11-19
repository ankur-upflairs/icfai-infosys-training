from django.urls import path
from .views import *
urlpatterns=[
    path('',home),
    path('blogs/',all_blogs,name='all-blogs'),
    path('blogs/create',create_blog,name='create-blog'),
    path('blogs/manage',manage_blogs,name='manage'),
    path('blogs/<int:id>',find_blog_by_id,name='blog-id'),
    # path('blogs/<slug:slug>',find_blog_by_slug)
]

