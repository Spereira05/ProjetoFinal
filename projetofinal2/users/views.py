from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
import logging

from django.views import View


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class RegisterView(View):
    def post(request):
        if request.user.is_authenticated:
            return redirect('index')
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                return render(request, 'register.html', {'form': form, 'error': 'Invalid form data'})
        else:
            form = UserCreationForm()
        logger.info(request.user)
        return render(request, 'register.html', {'form': form})

class LogInView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('files:index')
        form = AuthenticationForm()
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
            
            if user.is_staff:
                return redirect(reverse('admin:index'))
            return redirect('files:index')
        form = AuthenticationForm()

        return render(request, 'login.html', {'form': form})

class LogOutView(View):
    def get(self, request):
        return render(request, "logout.html")

    def post(self, request):
        auth_logout(request)
        return redirect("users:login")
