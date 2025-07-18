from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.user

class note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title