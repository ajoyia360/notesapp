from django.urls import path
from user_system.views import custom_login,user_logout,register
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', login_required(custom_login), name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
