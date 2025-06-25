from django.shortcuts import render, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import NoteForm


def note_home(request):
    dept = request.GET.get('dept')
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            print('saved file to:' , note.file_upload.path)
            return redirect('note_home')
    else:
        form = NoteForm()
    notes = Note.objects.all().order_by('-created_at')
    if dept:
        notes = notes.filter(author__depertment=dept)
    return render(request, 'notes/notes.html', 
                {
                    'form': form, 
                    'notes': notes,
                    'selected_dept': dept,
                }
            )

@login_required
def note_list(request):
    notes = Note.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes})


# def note_create(request):
#     if request.method == 'POST':
#         form = NoteForm(request.POST, request.FILES)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.author = request.user
#             note.save()
#             return redirect('note_list')
#     else:
#         form = NoteForm()
#     return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id, author=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {'form': form})

@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_delete_confirm.html', {'note': note})
