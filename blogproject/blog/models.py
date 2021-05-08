from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    writer=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()

    def __str__(self): # 클래스 내에 정의
        # return self.title
        return f'{self.title}'

    def summary(self): 
        return self.body[:100] # 100자 이하로 출력

    def get_absolute_url(self):
        return f'/blog/{self.pk}'