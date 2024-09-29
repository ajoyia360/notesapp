# views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in.')
        return redirect('read_notes')  # Adjust this to your actual redirect after login
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect('read_notes')  # Adjust this to your desired URL
            else:
                return render(request, 'user_system/login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'user_system/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been registered successfully.')
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'user_system/register.html', {'form': form})
