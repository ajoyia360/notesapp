from django.shortcuts import render
from mainapp.forms import NoteForm
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NoteForm  # Import your NoteForm
from .models import NoteModel


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)  # Need to include request.FILES for file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'Note submitted successfully!')
            return redirect('read_notes')
    else:
        form = NoteForm()

    # Pass the form to the template context in both cases
    context = {'form': form}
    return render(request, 'mainapp/create_notes.html', context)


#read all the notes


def read_notes(request):
    notes=NoteModel.objects.all()
    context = {'notes':notes}
    return render(request, 'mainapp/read_notes.html', context)
#detail of notes
def detail_note(request,id):
    note=NoteModel.objects.get(pk=id)
    context = {'note':note}
    return render(request,'mainapp/detail_note.html',context)

def delete_note(request,id):
    if request.method == 'POST':
        note = NoteModel.objects.get(pk=id)
        note.delete()
        messages.success(request, 'note has been deleted..')
        return redirect('read_notes')
    else:
        note = NoteModel.objects.get(pk=id)
        context = {'note':note}
        return render(request, 'mainapp/delete_note.html')

    #edit notes
def edit_note(request, id):
    if request.method == 'POST':
        note = NoteModel.objects.get(pk=id)
        messages.success(request, 'note has been edited..')
        return redirect('read_notes')
    else:
        note = NoteModel.objects.get(pk=id)
        context = {'note': note}
        return render(request, 'mainapp/edite_note.html', context)


def search_notes(request):
    query = request.GET.get('query')
    if query:
        notes = NoteModel.objects.filter(title__icontains=query)
    else:
        notes = []
    return render(request, 'mainapp/search_notes.html', {'notes': notes, 'query': query})