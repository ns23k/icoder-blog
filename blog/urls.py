from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name="bloghome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
]
