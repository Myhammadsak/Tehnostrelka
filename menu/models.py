from django.db import models


class Film(models.Model):

    title = models.CharField(max_length=52)
    description = models.TextField()
    generes = models.TextField()
    keywords = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title