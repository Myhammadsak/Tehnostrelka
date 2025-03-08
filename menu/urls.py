from . import views
from django.urls import path

app_name = 'menu'

urlpatterns = [
    path('', views.films_list, name='films'),
    path('film/<int:pk>/', views.film_info, name='film_info')
]
