from django.contrib import admin
from django.urls import path
from films.views import homepage, directors

urlpatterns = [
    path("", homepage, name="homepage"),
    path("directors/", directors, name="directors"),
    path("admin/", admin.site.urls),
]
