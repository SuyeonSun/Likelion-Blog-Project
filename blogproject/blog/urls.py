from django.urls import path
from .import views # views.py 가져오기

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
]