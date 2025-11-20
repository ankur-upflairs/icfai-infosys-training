from django.urls import path
from .views import *
urlpatterns=[
    path('sessions/',learn_sessions),
    path('create/',create_blog)
    # path('blogs/',all_blogs),
    # path('blogs/<int:id>',find_blog_by_id,name='blogs.id'),
    # path('blogs/<slug:slug>',find_blog_by_slug,name='blogs.slug')
]

