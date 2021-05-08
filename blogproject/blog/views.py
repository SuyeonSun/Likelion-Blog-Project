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
    blogs=Blog.objects.all().order_by('-pk') # 최신순으로 글 보여주기
    return render(request, 'blog/index.html', {'blogs': blogs})

def single_post_page(request, pk):
    blog=Blog.objects.get(pk=pk)
    return render(request, 'blog/single_post_page.html', {'blog':blog})

