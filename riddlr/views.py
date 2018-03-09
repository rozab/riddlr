from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def home(request):
    context_dict = {}
    return render(request, 'Riddlr/home.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'Riddlr/about.html', context_dict)


def top_riddles(request):
    context_dict = {}
    return render(request, 'Riddlr/top_riddles.html', context_dict)


def recent_riddles(request):
    context_dict = {}
    return render(request, 'Riddlr/recent_riddles.html', context_dict)


def add_riddle(request):
    context_dict = {}
    return render(request, 'Riddlr/add_riddle.html', context_dict)


def riddle(request):
    context_dict = {}
    return render(request, 'Riddlr/riddle.html', context_dict)


def user(request):
    context_dict = {}
    return render(request, 'Riddlr/home.html', context_dict)


def login(request):
    context_dict = {}
    return render(request, 'Riddlr/home.html', context_dict)


def logout(request):
    context_dict = {}
    return render(request, 'Riddlr/home.html', context_dict)


def register(request):
    context_dict = {}
    return render(request, 'Riddlr/register.html', context_dict)
