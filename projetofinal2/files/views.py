from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from.forms import FileForm, FolderForm
from.models import Folder, File
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class HomePageView(LoginRequiredMixin, View):
    def get(self, request):
        folders = Folder.objects.filter(owner=request.user)
        files = File.objects.filter(owner=request.user)
        return render(request, 'index.html', {"files": files, "folders": folders})

class UploadFileView(LoginRequiredMixin, View):
    def get(self, request):
        form = FileForm()
        return render(request, 'upload.html', {'form': form})

    def post(self, request):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.owner = request.user
            file.save()
            return redirect('files:index')
        return render(request, 'upload.html', {'form': form})

class DownloadFileView(LoginRequiredMixin, View):
    def get(self, request, pk):
        uploaded_file = get_object_or_404(File, owner=request.user)
        response = HttpResponse(uploaded_file.file, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
        return response

class CreateFolderView(LoginRequiredMixin, View):
    def get(self, request):
        form = FolderForm()
        return render(request, 'create_folder.html', {'form': form})
    
    def post(self, request):
        parent_folder = None
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.parent = parent_folder
            folder.owner = request.user
            folder.save()
            return redirect('files:index')
        return render(request, 'create_folder.html', {'form': form})

class DeleteFileView(LoginRequiredMixin, View):
    def get(self, request, pk):
        file = File.objects.get(pk=pk)
        file.delete()
        return redirect('files:index')

class DeleteFolderView(LoginRequiredMixin, View):
    def get(self, request, pk):
        folder = Folder.objects.get(pk=pk)
        folder.delete()
        return redirect('files:index')

