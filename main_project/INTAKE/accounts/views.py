from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as logedin, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.conf import settings


# Create your views here.
def signup(request):
    form = SignupForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            logedin(request, user)
            # return redirect(settings.LOGIN_URL)
            return redirect('main_app:main_page')
        else:
            form = SignupForm()
    ctx = {
        'form': form,
    }
    return render(request, 'accounts/signup_form.html', ctx)


def login(request):
    form = AuthenticationForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            logedin(request, user)
            # return redirect(request.path)
            return redirect('main_app:main_page')
        else:
            form = AuthenticationForm()
    ctx = {
        'form': form,
    }
    return render(request, 'accounts/login_form.html', ctx)


def view_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main_app:main_page')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')