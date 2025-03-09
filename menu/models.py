from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):

    title = models.CharField(max_length=52)
    description = models.TextField()
    generes = models.TextField()
    keywords = models.TextField()
    image_url = models.URLField()
    rating = models.FloatField(default=0)
    rating_count = models.PositiveIntegerField(default=0)
    total_ratings = models.PositiveIntegerField(default=0)

    def update_rating(self, new_rating):
        self.rating_count += 1
        self.total_ratings += new_rating
        self.rating = self.total_ratings / self.rating_count
        self.save()

    def __str__(self):
        return self.title


class Follow(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.film}'


class Generes(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name="Фильм", related_name="ratings")
    stars = models.PositiveIntegerField(verbose_name="Оценка")

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        unique_together = ('user', 'film')

    def __str__(self):
        return f"{self.user.username} - {self.film.title}"
