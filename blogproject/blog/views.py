from django.shortcuts import render, redirect, get_object_or_404 # import 해주기!
from django.utils import timezone
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

def new(request): # new.html 보여줌
    return render(request, 'new.html')

def create(request):
    new_blog=Blog()
    new_blog.title = request.POST.get('title', False)
    new_blog.writer = request.POST.get('writer', False)
    new_blog.body = request.POST.get('body', False)
    new_blog.pub_date=timezone.now()
    # new_blog.image=request.FILES['image']
    new_blog.image=request.POST.get('image', '')
    new_blog.save()
    return redirect('/blog/' + str(new_blog.id))

def edit(request, id): # 글 수정
    edit_blog=Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id): # 수정내역 데이터베이스에 적용
    update_blog = Blog.objects.get(id = id)
    new_blog.title = request.POST.get('title', False)
    new_blog.writer = request.POST.get('writer', False)
    new_blog.body = request.POST.get('body', False)
    update_blog.pub_date=timezone.now()
    new_blog.image=request.POST.get('image', '')
    update_blog.save() # 꼭 save!
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect('index')

