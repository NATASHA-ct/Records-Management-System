from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def login_user(request):
    pass

def logout_user(request):
    pass

def home(request):
    # first check if user is logged in
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = authenticate(request, username=username, password=password)     

       if user is not None:
           login(request, user)
           messages.success(request, "You are logged in!")
           return redirect('home')
       else:
           messages.success(request, "There was an error logging in!")
           return redirect('home')
    else:       
       return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')