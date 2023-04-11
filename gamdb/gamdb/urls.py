from django.contrib import admin
from django.urls import path
from films.views import homepage, movies, directors

urlpatterns = [
    path("", homepage, name="homepage"),
    path("movies/", movies, name="movies"),
    path("directors/", directors, name="directors"),
    path("admin/", admin.site.urls),
]
