from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255)
    due_date = models.DateField(null=False, blank=False)
    status = models.CharField(max_length=20)