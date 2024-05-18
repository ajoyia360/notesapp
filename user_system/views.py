# myapp/views.py

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.user.is_authenticated:
        messages.success(request,'you are already login.')
        return redirect('read_notes')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'successfully login..')
                return redirect('read_notes')
                # Redirect to home page after login
            else:
                # Handle invalid login
                return render(request, 'user_system/login.html', {'error': 'Invalid username or password'})
        else:
            return render(request,'user_system/login.html')
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,'user has been register successfully.....')
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user_system/register.html', {'form': form})
