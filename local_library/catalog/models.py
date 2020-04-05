from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text='Title')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    checkout_date = models.DateTimeField(blank=True,null=True)

# Create your models here.
class Magazine(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text='Name of magazine')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    checkout_date = models.DateTimeField(blank=True,null=True)
