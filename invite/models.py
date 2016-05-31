from django.db import models

class EmailAccess(models.Model):
    access_code = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email

class AccessCode(models.Model):
    access_code = models.CharField(max_length=100)

class UserRegister(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
    # Create your models here.
