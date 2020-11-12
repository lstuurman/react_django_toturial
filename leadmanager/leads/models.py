from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50,unique=True)
    message = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)