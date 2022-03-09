from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import Note
from .forms import UserAuthenticationForm, NotesForm, UserRegisterForm


def index(request):
    if request.user.is_authenticated:
        length = len(Note.objects.filter(author_id=int(request.session['_auth_user_id'])))
        return render(request, 'notes/index.html', {'length': length})
    return render(request, 'notes/index.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'notes/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserAuthenticationForm()
    return render(request, 'notes/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def add_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.cleaned_data['author_id'] = int(request.session['_auth_user_id'])
            note = Note.objects.create(**form.cleaned_data)
            note.save()
            return redirect('add_note')
    else:
        form = NotesForm()
    return render(request, 'notes/add_note.html', {'form': form})


def view_notes(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(author_id=int(request.session['_auth_user_id']))
        return render(request, 'notes/list_of_notes.html', {'notes': notes})
    return render(request, 'notes/list_of_notes.html')
