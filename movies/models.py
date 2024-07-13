from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(null=False, primary_key=True)
    title = models.CharField(max_length=100, null=False)
    genre = models.CharField(null=False)
    director_name = models.CharField(null=False)
    release_year = models.IntegerField(null=False)
    sinopsis = models.TextField(null=False)

    def __str__(self) -> str:
        return self.name