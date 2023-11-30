from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, blank=False, unique=False)
    year = models.PositiveSmallIntegerField(default=2023)

    class Task(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title