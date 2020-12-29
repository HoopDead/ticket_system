from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from accounts.forms import SignUpForm
import json

def login_page(request):
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