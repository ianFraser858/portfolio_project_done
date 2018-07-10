from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    blurb = models.TextField(max_length=200)
    content = models.TextField(max_length=2000)
    github_link = models.URLField(default='none')

    def __str__(self):
        return self.title

