from django import forms
from.models import File, Folder, Share

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'file')

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('name',)

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ('user',)