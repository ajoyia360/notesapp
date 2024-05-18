from django.urls import path
from . import  views
from django.contrib.auth.decorators import login_required

#pip lines for the project
urlpatterns = [
    path('create_note/', login_required(views.create_note), name='create_note'),
    path('read_notes/', login_required(views.read_notes), name='read_notes'),
    path('detail_note/<int:id>/', login_required(views.detail_note), name='detail_note'),
    path('delete_note/<int:id>/', login_required(views.delete_note), name='delete_note'),
    path('edit_note/<int:id>/', login_required(views.edit_note), name='edit_note'),
    path('search/', login_required(views.search_notes), name='search_notes'),
]