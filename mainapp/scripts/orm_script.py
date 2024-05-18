from mainapp.models import NoteModel
from django.db import connection


def run():
    notes=NoteModel.objects.all()
    #returning all the instances of the database ,
    #now want ot ieterate to each model instance
    for note in notes:
        print(f'note{note.id},{note.title},{note.content},{note.screen_shoot}')