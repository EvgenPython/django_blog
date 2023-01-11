from django.db import models

class BlogProject(models.Model):
    title = models.CharField(max_length=200, blank=True)
    data = models.DateField()
    description = models.CharField(max_length=150)
    post = models.TextField(default='')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title