from django.urls import path
from .views import *
urlpatterns=[
    path('',home),
    path('blogs',all_blogs),
    path('blogs/<int:id>',find_blog_by_id),
    path('blogs/create',create_blog),
    path('blogs/<slug:slug>',find_blog_by_slug)
]