from django.db import models
from datetime import datetime
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField("Descriptions of the Task")
    due_date = models.DateField(default=datetime.now())

    def __str__(self) -> str:
        return self.title