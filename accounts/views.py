from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import User

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            is_trainer=request.POST.get('role') == 'trainer'
        )
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/signup.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')
