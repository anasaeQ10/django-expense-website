from django.shortcuts import redirect, render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
#from django.core.mail import EmailMessage 
#from django.contrib.sites.shortcuts import get_current_site
#from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError 
#from django.core.mail import send_mail 
#from django.contrib.sites.shortcuts import get_current_site 
#from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
#from django.template.loader import render_to_string 
#from .utils import account_activation_token 
#from django.urls import reverse
from django.contrib import auth

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authentification/home.html')


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry, email is used. Choose another one'}, status=409)
        return JsonResponse({'email_valid': True})

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry, username is used. Choose another one'}, status=409)
        return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password should be at least 6 characters')
                    return render(request, 'authentication/register.html', context)
                
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = True  # Activer l'utilisateur par défaut
                user.save()
                messages.success(request, 'Account created successfully')
                return render(request, 'authentication/register.html')

        messages.error(request, 'Account creation failed. Please try again.')
        return render(request, 'authentication/register.html', context)

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']


        if username and password :

            user=auth.authenticate(username=username, password=password)

            if user :
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome '+ user.username +' ,you are now logged in')
                    return redirect('expenses')

                messages.error(request, 'Account is not activate , please check your email')
                return render(request, 'Authentication/login.html')    
            messages.error(request, 'Invalid credentials , try again')
            return render(request, 'Authentication/login.html')
        
        messages.error(request, 'please fill all fields')
        return render(request, 'Authentication/login.html')
    

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')