from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notebook
import json
from django.contrib import messages
# Create your views here.
@login_required
def home(request):
    posts = [{'title': 'Sample Post 01', 'content': '01 This is a sample post content.'},
             {'title': 'Sample Post 02', 'content': '02 This is a sample post content.'},
             {'title': 'Sample Post 03', 'content': '03 This is a sample post content.'},
             {'title': 'Sample Post 04', 'content': '04 This is a sample post content.'},
             {'title': 'Sample Post 05', 'content': '05 This is a sample post content.'},]
    """ 01
    Render the home page of the notebook application.
    """
    return render(request, 'notebook/home.html',context={'posts': posts})

@login_required
def index(request):
    notes = Notebook.objects.filter(author=request.user).order_by('-updated_at')
    return render(request, 'notebook/index.html',context={'notes': notes})

@login_required
def delete_notebook(request):
    """Delete a notebook entry."""
    if request.method == 'POST':
        data = json.loads(request.body)
        notebook_id = data.get('note_id')
        try:
            notebook = Notebook.objects.get(id=notebook_id, author=request.user)
            notebook.delete()
            messages.success(request, f'Notebook deleted successfully.')
        except Notebook.DoesNotExist:
            messages.error(request, f'Notebook not found.')
    notes = Notebook.objects.all().order_by('-updated_at')
    return render(request, 'notebook/index.html',context={'notes': notes})


@login_required
def update_notebook(request, note_id):
    """Update a notebook entry."""
    note = get_object_or_404(Notebook, id=note_id, author=request.user)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('notebook:home')

    return render(request, 'notebook/update.html', {'note': note})

@login_required
def save_notebook(request, note_id):
    note = get_object_or_404(Notebook, id=note_id, author=request.user)

    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('notebook:home')  # Redirect after saving

    return render(request, 'notebook/update.html', {'note': note})
    
@login_required
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Notebook.objects.create(title=title, content=content, author=request.user)
        return redirect('notebook:home')
    return render(request, 'notebook/create.html')