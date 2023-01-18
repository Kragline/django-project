from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return str(self.name)


    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    image = models.ImageField(null = True, blank = True,upload_to = "images/", verbose_name='Image')
    category = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=True, blank=True, verbose_name='Description')
    likes = models.ManyToManyField(User, related_name = 'blog_posts')
    

    def __str__(self):
        return str(self.author)


    def get_absolute_url(self):
        return reverse('home')


    def total_likes(self):
        return self.likes.count()


    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-id']