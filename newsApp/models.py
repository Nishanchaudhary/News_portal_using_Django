from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(("1",'Active'), ("2",'Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    title = models.TextField()
    short_description = models.TextField()
    content = models.TextField()
    banner_path = models.ImageField(upload_to='news_bannner')
    status = models.CharField(max_length=2, choices=(("1",'Published'), ("2",'Unpublished')), default=2)
    meta_keywords = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,default="")
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.name} - {self.post.title}"