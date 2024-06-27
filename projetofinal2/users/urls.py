from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('password_reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]