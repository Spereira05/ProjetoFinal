from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
]