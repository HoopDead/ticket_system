from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password) # Django Function check if user exist

        if user is not None:
            login(request, user)
            print("Logged in!")
            #TODO: Add redirect to index page for permitted uesr
            return render(request, 'index.html')
        else:
            messages.error(request, 'User name or password is incorrect!')
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')