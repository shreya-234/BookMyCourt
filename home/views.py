from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .models import (Amenities, Hotel, HotelBooking)

# Create your views here.


def home(request):
    return render(request, 'home.html')


def hotel_detail(request):
    return render(request, 'hotel-detail.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Account not found')
            return redirect('login_page')

    else:
        return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password');

        user_obj = User.objects.filter(username=username)
        if user_obj.exists():
            messages.warning(request, 'Username already exist')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        user = User.objects.create(username == username)
        user.set_password(user)
        user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'register.html')

# if request.method == 'POST':
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#
#     user_obj = User.objects.filter(username=username)
#     if not user_obj.exists():
#         messages.warning(request, 'Account not found')
#         return redirect('/')
#
#     user_obj = authenticate(username=username, password=password)
#
#     if not user_obj:
#         messages.warning(request, 'Invalid credentials')
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#
#     login(request, user_obj)
#     return redirect('/')

# return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# return render(request, 'login.html')
