from django.db import models

# Create your models here.
class wishes(models.Model):
    wish=models.CharField(max_length=800)
    to=models.CharField(max_length=60)
