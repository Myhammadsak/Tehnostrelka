from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import logout


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/login/')
    else:
        form = SignupForm()

    return render(request, 'register/signup.html', {'form': form})


def logout_v(request):
    logout(request)
    return redirect('/#')