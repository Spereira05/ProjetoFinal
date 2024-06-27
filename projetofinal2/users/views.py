from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
import logging
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from django.views import View


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('files:index')
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('files:index')
            else:
                return render(request, 'register.html', {'form': form, 'error': 'Invalid form data'})
        else:
            form = RegisterForm()
        logger.info(request.user)
        return render(request, 'register.html', {'form': form})

class LogInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('files:index')
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('files:index')
        
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user:
                auth_login(user=user, request=request)
                return redirect("files:index")
            
            form = LoginForm()

        return render(request, 'login.html', {'form': form})

class LogOutView(View):
    def get(self, request):
        return render(request, "logout.html")

    def post(self, request):
        auth_logout(request)
        return redirect("users:login")
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users:login')
