from . import views
from django.urls import path

app_name = 'menu'

urlpatterns = [
    path('', views.films_list, name='films'),
    path('film/<int:pk>/', views.film_info, name='film_info'),
    path('following/<int:pk>/', views.add_follow, name='add_follow'),
    path('follow/', views.follow, name='follow'),
    path('follow/remove/<int:pk>/', views.remove_follow, name='remove_follow')
]
