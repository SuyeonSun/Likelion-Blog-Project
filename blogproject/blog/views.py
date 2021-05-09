from django.shortcuts import render, redirect, get_object_or_404 # import 해주기!
from django.utils import timezone
from .models import Blog
from .models import People

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

def new(request): # new.html 보여줌
    return render(request, 'new.html')

def create(request):
    new_blog=Blog()
    # new_blog.title = request.POST.get('title')
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date=timezone.now()
    new_blog.save()
    return redirect('detail.html', new_blog.id)


