from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form, 'error': 'Invalid form data'})
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form})

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')  
    return wrapper

def login(request):
    logger.info("Entering")

    if request.user.is_authenticated:
        logger.info("is_authenticate")
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            logger.info("No username or password provided!")
            return render(
                request=request, 
                template_name="login.html", 
                context={}
            )
        
        logger.info("Authenticating")
        user = authenticate(request, username=username, password=password)

        logger.info(user)

        if user:
            auth_login(user=user, request=request)
            return redirect("files:index")
        
        return redirect("login")

    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
