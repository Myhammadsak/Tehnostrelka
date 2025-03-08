from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):

    title = models.CharField(max_length=52)
    description = models.TextField()
    generes = models.TextField()
    keywords = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title


class Follow(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.film}'
