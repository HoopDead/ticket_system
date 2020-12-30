from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout # Alias because view defined below was causing recursion max depth error
from django.contrib.auth.decorators import login_required
from accounts.forms import SignUpForm
import json

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password) # Django Function check if user exist

            if user is not None:
                login(request, user)
                return render(request, 'index.html')

            else:
                messages.error(request, 'Username or password is incorrect!')

        return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        sign_up_form = SignUpForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            username = sign_up_form.cleaned_data.get('username')
            raw_password = sign_up_form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return render(request, 'index.html')
        else:
            sign_up_form_errors = json.loads(sign_up_form.errors.as_json())
            for msg in sign_up_form_errors:
                messages.error(request, sign_up_form_errors[msg][0]['message'])
                
    else:
        sign_up_form = SignUpForm(request.POST)

    return render(request, 'register.html', {'form': sign_up_form})

@login_required(redirect_field_name = "")
def logout(request):
    django_logout(request)
    return redirect('login')