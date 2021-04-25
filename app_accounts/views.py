from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# Create your views here.

def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('app_boards:home')
    else:
        form = SignUpForm()
    return render(request, 'app_accounts/signup_page.html', {'form' : form})