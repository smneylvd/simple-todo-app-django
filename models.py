from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('task', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
