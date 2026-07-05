from django.shortcuts import render

from .models import Director


def movie_catalog(request):
    directors = Director.objects.prefetch_related('movies').all()
    return render(request, 'catalog/catalog.html', {'directors': directors})
