from . import views
from django.urls import path

app_name = "files"

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('upload/', views.UploadFileView.as_view(), name='upload'),
    path('download/<pk>/', views.DownloadFileView.as_view(), name='download'),
    path('create_folder/', views.CreateFolderView.as_view(), name='create_folder'),
    path('delete_file/<pk>/', views.DeleteFileView.as_view(), name='delete_file'),
    path('delete_folder/<pk>/', views.DeleteFolderView.as_view(), name='delete_folder'),
    # path('share_folder/<pk>/', views.ShareFolderView, name='share_folder'),
]