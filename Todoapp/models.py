from django.db import models

# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField() 
    
class Form(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
      