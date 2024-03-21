from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("chat")
        else:
            return HttpResponse("Invalid Login, check your credentials")
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        firstName= request.POST['firstName']
        lastName= request.POST['lastName']
        address = request.POST['address']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        userType = request.POST['userType']
        if userType=="Customer":
            userType = 1 
        else:
            userType = 2
        print(username, email, password)
        user = User.objects.create_user(username, email, password, first_name=firstName, last_name=lastName, address=address, user_type=userType)
        user.save()
        auth.login(request, user)
        if userType==1:
            return redirect("customer")
        elif userType==2:
            return redirect("rentals")
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')