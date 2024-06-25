from django.db import models
from django.contrib.auth.models import User


class Folder(models.Model):
    app_label = "files"
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class File(models.Model):
    app_label = "files"
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploaded_files/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)

class Share(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)