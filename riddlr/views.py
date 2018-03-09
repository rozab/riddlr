from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def home(request):
    context_dict = {}
    top_riddles = Riddle.objects.order_by('-rating')[:5]
    recent_riddles = Riddle.objects.order_by('-date_posted')[:5]
    top_riddlrs = UserProfile.objects.order_by('-score')[:5]
    context_dict = {'top_riddles': top_riddles, 'recent_riddles': recent_riddles, 'top_riddlrs':top_riddlrs}
    return render(request, 'riddle/home.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'riddle/about.html', context_dict)


def top_riddles(request):
    context_dict = {}
    return render(request, 'riddle/top_riddles.html', context_dict)


def recent_riddles(request):
    context_dict = {}
    return render(request, 'riddle/recent_riddles.html', context_dict)


def add_riddle(request):
    context_dict = {}
    return render(request, 'riddle/add_riddle.html', context_dict)


def riddle(request):
    context_dict = {}
    return render(request, 'riddle/riddle.html', context_dict)


def user(request):
    context_dict = {}
    return render(request, 'riddle/home.html', context_dict)


def login(request):
    context_dict = {}
    return render(request, 'riddle/login.html', context_dict)


def logout(request):
    context_dict = {}
    return render(request, 'riddle/logout.html', context_dict)


def register(request):
    context_dict = {}
    return render(request, 'riddle/register.html', context_dict)
