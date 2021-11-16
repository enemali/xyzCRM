from django.db import models
from django.contrib.auth.models import AbstractUser
from .Allchoise import*

class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 #   email = models.EmailField(max_length=100, unique=True)
 #   phone = models.CharField(max_length=100, unique=True)
 #   profile_pic = models.ImageField(upload_to='images/', blank=True)
 #   special_file = models.FileField(upload_to='files/', blank=True)
 #   created_at = models.DateTimeField(auto_now_add=True)
 #   updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
        
class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    source = models.CharField(choices=(SOURCE_CHOICES), max_length=100)
    message = models.CharField(max_length=500, blank=True)
   # profile_pic = models.ImageField(upload_to='images/', blank=True)
    special_file = models.FileField(upload_to='files/', blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name





