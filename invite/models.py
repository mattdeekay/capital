from django.db import models

class AccessCode(models.Model):
    access_code = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
# Create your models here.
