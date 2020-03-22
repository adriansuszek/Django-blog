from django.db import models
from django.contrib.auth import get_user_model
#get user model?

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
    overview = models.TextField()
    #dokumentacja - zapytać przemasa
    #dokumentacja - zapytać przemasa
    #dokumentacja - zapytać przemasa
    #dokumentacja - zapyt   ać przemasa
    #dokumentacja - zapytać przemasa
    #dokumentacja - zapytać przemasa
    #dokumentacja - zapytać przemasa
    timestamp = models.DateTimeField(auto_now_add = True)
    comment_count = models.IntegerField(default = 0)
    views_number = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
