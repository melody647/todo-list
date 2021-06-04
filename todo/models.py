from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'<{self.title}>'

    def get_absolute_url(self):
        return reverse('alltodos')