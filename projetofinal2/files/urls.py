from . import views
from django.urls import path

app_name = "files"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('upload/', views.UploadFileView.as_view(), name='upload'),
    path('create_folder/', views.CreateFolderView.as_view(), name='create_folder'),
    path('delete_file/<pk>/', views.DeleteFileView.as_view(), name='delete_file'),
    # path('delete_folder/<pk>/', views.delete_folder, name='delete_folder'),
    # path('share_folder/<pk>/', views.share_folder, name='share_folder'),
]