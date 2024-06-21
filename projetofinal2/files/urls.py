from . import views
from django.urls import path

app_name = "files"

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('create_folder/', views.create_folder, name='create_folder'),
    path('delete_file/<pk>/', views.delete_file, name='delete_file'),
    path('delete_folder/<pk>/', views.delete_folder, name='delete_folder'),
    path('share_folder/<pk>/', views.share_folder, name='share_folder'),
]