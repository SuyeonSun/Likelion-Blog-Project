from django.contrib import admin
from django.urls import path, include
from .views import *
#from django.conf import settings
#from django.conf.urls.static import static


urlpatterns = [
    path('', index, name="index"),
    path('blog/<int:blog_id>/', detail, name="detail"),
    path('about_me/', about_me, name="about_me"),
    path('new/', new, name="new"), 
    path('create/', create, name = "create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]