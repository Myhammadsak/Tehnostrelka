from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Follow, Generes, Rating
from django.contrib import messages
from .forms import RatingForm


def films_list(request):
    query = request.GET.get('query', '')
    films = Film.objects.all()

    genres = Generes.objects.all()

    if query:
        films = films.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(keywords__icontains=query))

    paginator = Paginator(films, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'menu/films.html', context={'films': films,
                                                       'query': query,
                                                       'page_obj': page_obj,
                                                       'genres': genres})


def film_info(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Войдите, чтобы оценить фильм.")
        return redirect('/register/login/')

    film = get_object_or_404(Film, pk=pk)
    user = request.user
    user_rating = Rating.objects.filter(user=user, film=film).first()

    if request.method == 'POST':

        form = RatingForm(request.POST)
        if form.is_valid():
            new_rating = int(form.cleaned_data['stars'])

            if user_rating:
                old_rating = user_rating.stars
                user_rating.stars = new_rating
                user_rating.save()

                film.total_ratings += new_rating - old_rating
                film.rating = film.total_ratings / film.rating_count
                film.save()
            else:
                Rating.objects.create(user=user, film=film, stars=new_rating)
                film.update_rating(new_rating)

            return redirect(request.META.get('HTTP_REFERER', 'fallback_url'))
    else:
        form = RatingForm()

    return render(request, 'menu/film_info.html', {
        'film': film,
        'form': form,
        'user_rating': user_rating.stars if user_rating else None
    })


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


def genre_films(request, pk):
    genre = get_object_or_404(Generes, pk=pk)
    films = Film.objects.filter(generes__contains=genre.name)

    return render(request, 'menu/films_by_genre.html', {'genre': genre, 'films': films})


@login_required
def rating_user(request):
    user = request.user
    rating = Rating.objects.filter(user=user)

    paginator = Paginator(rating, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'menu/rating.html', {'rating': rating, 'page_obj': page_obj})


@login_required
def remove_rating(request, pk):
    film = get_object_or_404(Film, pk=pk)
    Rating.objects.filter(user=request.user, film=film).delete()

    return redirect(request.META.get('HTTP_REFERER', 'fallback_url'))