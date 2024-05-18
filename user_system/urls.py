from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

# pip lines for the project
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]