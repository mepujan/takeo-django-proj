from django.db import models
from datetime import datetime

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField("Descriptions of the Task")
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.title
