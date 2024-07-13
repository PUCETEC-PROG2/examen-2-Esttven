from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, null=False)
    genre = models.CharField(null=False)
    director_name = models.CharField(null=False)
    release_year = models.IntegerField(null=False)
    sinopsis = models.TextField(null=False)

    def __str__(self) -> str:
        return self.title