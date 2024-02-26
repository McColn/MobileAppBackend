from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(null=True,blank=True,upload_to='covers/')
    pdf_file = models.FileField(upload_to='pdfs/')
    


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, null=True,blank=True)