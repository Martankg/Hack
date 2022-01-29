
from django.db import models
from django.shortcuts import render


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    adress = models.CharField(max_length=150)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

