from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User 

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email is already taken")
            return render(request, 'signup.html')

        User.objects.create_user(email, email, password)
        messages.success(request, "User created")
        return redirect('/auth/login/')
    
    return render(request, 'signup.html')

def handlelogin(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['pass1']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect('/')  # Change 'home' to the URL for your home page

        messages.error(request, "Invalid credentials")
        return redirect('/auth/login/')

    return render(request, 'login.html')

def handlelogout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/auth/login/')
