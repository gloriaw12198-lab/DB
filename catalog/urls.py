from django.urls import path

from . import views

urlpatterns = [
    path('', views.movie_catalog, name='movie_catalog'),
]
