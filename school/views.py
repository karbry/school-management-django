from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User

def dashboardView(request):
    context = {'user': request.user,
               'groups': request.user.groups.all()}
    return render(request, 'index.html')          

def logoutView(request):
    return render(request, 'logout.html')