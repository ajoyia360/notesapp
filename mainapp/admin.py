# mainapp/admin.py
from django.contrib import admin
from .models import NoteModel

@admin.register(NoteModel)
class NoteAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/custom_unfold_admin.css',)  # Path to your custom CSS
        }
