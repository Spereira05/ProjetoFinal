from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.forms import FileForm, FolderForm, ShareForm
from.models import Folder, File, Share

@login_required
def index(request):
    folders = Folder.objects.filter(owner=request.user) 
    files = File.objects.filter(owner=request.user)
    return render(request, 'index.html', {'folders': folders, 'files': files})

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = request.user
            file.save()
            return redirect('index')
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.owner = request.user
            folder.save()
            return redirect('index')
    else:
        form = FolderForm()
    return render(request, 'create_folder.html', {'form': form})

@login_required
def delete_file(request, pk):
    file = File.objects.get(pk=pk)
    file.delete()
    return redirect('index')

@login_required
def delete_folder(request, pk):
    folder = Folder.objects.get(pk=pk)
    folder.delete()
    return redirect('index')

@login_required
def share_folder(request, pk):
    folder = Folder.objects.get(pk=pk)
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            share = form.save(commit=False)
            share.folder = folder
            share.save()
            return redirect('index')
    else:
        form = ShareForm()
    return render(request, 'hare.html', {'form': form, 'folder': folder})