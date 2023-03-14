from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year"]
    list_display_links = ["name"]


admin.site.register(Movie, MovieAdmin)
