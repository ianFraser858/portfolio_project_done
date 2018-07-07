from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000)

    def __str__(self):
        return self.title

