from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entrepreneurship(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=200)
    header = models.CharField(max_length=350)
    body = models.TextField()
    slug = models.SlugField()
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    Create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug



class Finance(models.Model):
    image = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=200)
    header = models.CharField(max_length=350)
    body = models.TextField()
    slug = models.SlugField()
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    Create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug