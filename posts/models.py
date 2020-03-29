from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse


from datetime import datetime


User = get_user_model()


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length = 150)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length = 150)
    overview = RichTextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    comment_count = models.IntegerField(default = 0)
    slug = models.SlugField(unique=True)
    views_number = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)


    #str zmienia reprezentacje typu string tej klasy -> print() automatycznie konwertuje to co w nawiasie, na string
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'slug': self.slug
        })
