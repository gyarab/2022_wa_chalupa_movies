from django.contrib import admin
from django.urls import path
from films.views import homepage, movies, movie, directors, director, actors, actor

urlpatterns = [
    path("", homepage, name="homepage"),
    path("admin/", admin.site.urls),
    path("movies/", movies, name="movies"),
    path('movie/<int:id>', movie, name="movie"),
    path("directors/", directors, name="directors"),
    path('director/<int:id>', director, name="director"),
    path('actors/', actors, name="actors"),
    path('actor/<int:id>', actor, name="actor"),
]
