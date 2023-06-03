from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=126)
    last_name = models.CharField(max_length=126)
    email = models.CharField(max_length=126, unique=True)
