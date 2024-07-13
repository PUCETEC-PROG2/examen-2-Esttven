from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    pass