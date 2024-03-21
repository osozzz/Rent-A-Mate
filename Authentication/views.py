from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Data

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("core")
        else:
            return HttpResponse("Invalid Login, check your credentials")
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        fullName = request.POST['fullname']
        address = request.POST['address']
        username = request.POST['username']
        email = request.POST['email']
        phone = int(request.POST['phone'])
        password = request.POST['password']
        savedPost = []
        paymentInfo = []
        orderHistory = []
        saleList = []
        user = User.objects.create_user(username=username, password=password)
        user.save()
        auth.login(request, user)
        data = Data(user=request.user, fullname=fullName, address=address, phone=phone, email=email, saved_posts=savedPost, payment_info=paymentInfo, order_history=orderHistory, sale_list=saleList)
        data.save()
        return redirect("core")
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')