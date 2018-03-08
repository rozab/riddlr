from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def home(request):
    context_dict = {}
    return render(request, 'Riddlr/home.html', context_dict)


def about(request):
    return HttpResponse("about page")


def top_riddles(request):
    return HttpResponse("top riddles")


def recent_riddles(request):
    return HttpResponse("recent riddles")


def add_riddle(request):
    return HttpResponse("add riddle")


def riddle(request):
    return HttpResponse("riddle")


def user(request):
    return HttpResponse("user")


def login(request):
    return HttpResponse("login")


def logout(request):
    return HttpResponse("logout")


def register(request):
    return HttpResponse("register")
