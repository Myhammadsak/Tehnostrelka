from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
from django.urls import path, reverse_lazy
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView,
                                       PasswordResetConfirmView)

app_name = 'register'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html', authentication_form=LoginForm),
         name='login'),
    path('logout/', views.logout_v, name='logout'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='register/password_reset_form.html',
                                                                 email_template_name='register/password_reset_email.html',
                                                                 success_url=reverse_lazy('register:password_reset_done')),
         name='password_reset'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='register/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='register/password_reset_confirm.html',
                                                     success_url=reverse_lazy('register:password_reset_complete')),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'),
         name='password_reset_complete'),
]
