from django.db import models

# Create your models here.
class Content(models.Model):
    title   = models.CharField(max_length=220)
    content = models.CharField(max_length=250)
    time    = models.IntegerField(max_length=10)







