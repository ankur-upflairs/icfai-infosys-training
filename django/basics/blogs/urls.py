from django.urls import path
from .views import all_blogs,find_blog_by_id,find_blog_by_slug


urlpatterns=[
    path('',all_blogs),
    path('<int:id>',find_blog_by_id),
    path('<slug:slug>',find_blog_by_slug,name='blog_id')
]
