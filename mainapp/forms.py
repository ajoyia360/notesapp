from django import forms
from mainapp.models import NoteModel

#NOTE FORM
class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ('title','content','screen_shoot')
