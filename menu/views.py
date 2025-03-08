from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Film


def films_list(request):
    query = request.GET.get('query', '')
    films = Film.objects.all()

    if query:
        films = films.filter(Q(title__icontains=query) | Q(description__icontains=query))

    paginator = Paginator(films, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'menu/films.html', context={'films': films,
                                                       'query': query,
                                                       'page_obj': page_obj})


def film_info(request, pk):
    film = get_object_or_404(Film, pk=pk)

    return render(request, 'menu/film_info.html', {'film': film})