from django.db import models

# Create your models here.

class Task(models.Model):
    t_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=300)