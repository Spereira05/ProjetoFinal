from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from.forms import FileForm, FolderForm, ShareForm
from.models import Folder, File, Share
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

class CreateFolderView(LoginRequiredMixin, View):
    def get(self, request):
        form = FolderForm()
        return render(request, 'create_folder.html', {'form': form})
    
    def post(self, request):
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.owner = request.user
            folder.save()
            return redirect('files:index')
        return render(request, 'create_folder.html', {'form': form})

class DeleteFileView(LoginRequiredMixin, View):
    def get(self, request, pk):
        file = File.objects.get(pk=pk)
        file.delete()
        return redirect('files:index')

#     # def delete_folder(request, pk):
#     #     folder = Folder.objects.get(pk=pk)
#     #     folder.delete()
#     #     return redirect('index')

#     # def share_folder(request, pk):
#     #     folder = Folder.objects.get(pk=pk)
#     #     if request.method == 'POST':
#     #         form = ShareForm(request.POST)
#     #         if form.is_valid():
#     #             share = form.save(commit=False)
#     #             share.folder = folder
#     #             share.save()
#     #             return redirect('index')
#     #     else:
#     #         form = ShareForm()
#     #     return render(request, 'share.html', {'form': form, 'folder': folder})