from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Follow
from django.contrib import messages


def films_list(request):
    query = request.GET.get('query', '')
    films = Film.objects.all()

    if query:
        films = films.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(keywords__icontains=query))

    paginator = Paginator(films, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'menu/films.html', context={'films': films,
                                                       'query': query,
                                                       'page_obj': page_obj})


def film_info(request, pk):
    film = get_object_or_404(Film, pk=pk)

    return render(request, 'menu/film_info.html', {'film': film})


@login_required
def add_follow(request, pk):
    film = get_object_or_404(Film, pk=pk)

    if Follow.objects.filter(user=request.user, film=film).exists():
        messages.warning(request, 'Этот фильм уже в вашем избранном.')
    else:
        Follow.objects.get_or_create(user=request.user, film=film)
        messages.success(request, 'Фильм успешно добавлен в избранное.')

    return redirect(request.META.get('HTTP_REFERER', 'fallback_url'))


@login_required
def remove_follow(request, pk):
    film = get_object_or_404(Film, pk=pk)
    Follow.objects.filter(user=request.user, film=film).delete()
    return redirect(request.META.get('HTTP_REFERER', 'fallback_url'))


@login_required
def follow(request):
    follow_film = Follow.objects.filter(user=request.user)

    paginator = Paginator(follow_film, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'menu/follow.html', {
        'follow_film': follow_film,
        'page_obj': page_obj
    })
