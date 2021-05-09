from django.shortcuts import render, get_object_or_404 # import 해주기!
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects # 쿼리셋
    return render(request, 'home.html', {'blogs': blogs}) # home.html에서 blogs를 보여주는 것이 목적

def detail(request, blog_id):
    details=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs}) # index.html 파일 찾아서 방문자에게 보내줌

def about_me(request):
    return render(request, 'about_me.html')
