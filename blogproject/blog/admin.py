from django.contrib import admin
from .models import Blog
from .models import People


# Register your models here.

# 블로그 사이트 글 등록
admin.site.register(Blog)
admin.site.register(People)