from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegisterForm, UpdateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_user(request):
    """User Register Function"""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "You regestrated successfully!")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form' : form})


def login_user(request):
    """User Login Function"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You loged in successfully!")
            return redirect('home')
        else:
            messages.success(request, "Uncorrect username or password, try again please!")
            return redirect('login')
    return render(request, 'registration/login.html', {})


def logout_user(request):
    """User Logout Function"""
    logout(request)
    return redirect('login')


def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated')
            return redirect('home')
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'registration/edit.html', {'form' : form})