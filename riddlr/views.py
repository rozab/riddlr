from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from riddlr.models import Riddle, UserProfile, UserAnswer


def home(request):
    context_dict = {}
    top_riddles = Riddle.objects.order_by('-rating')[:5]
    recent_riddles = Riddle.objects.order_by('-date_posted')[:5]
    top_riddlrs = UserProfile.objects.order_by('-score')[:5]
    context_dict = {'top_riddles': top_riddles, 'recent_riddles': recent_riddles, 'top_riddlrs':top_riddlrs}
    return render(request, 'riddlr/home.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'riddlr/about.html', context_dict)

def top_riddles(request):
    context_dict = {}
    top_riddles = Riddle.objects.order_by('-rating')[:5]
    context_dict['top_riddles'] = top_riddles
    return render(request, 'riddlr/top_riddles.html', context_dict)

def recent_riddles(request):
    context_dict = {}
    recent_riddles = Riddle.objects.order_by('-date_posted')[:5]
    context_dict['recent_riddles'] = recent_riddles
    return render(request, 'riddlr/recent_riddles.html', context_dict)

def add_riddle(request):
    context_dict = {}
    return render(request, 'riddlr/add_riddle.html', context_dict)

def riddle(request, id):
    context_dict = {}
    return render(request, 'riddlr/riddle.html', context_dict)

def user(request, username):
    context_dict = {}
    return render(request, 'riddlr/user.html', context_dict)

def users(request):
    context_dict = {}
    return render(request, 'riddlr/users.html', context_dict)

def login(request):
    context_dict = {}
    return render(request, 'riddlr/login.html', context_dict)

def logout(request):
    context_dict = {}
    return render(request, 'riddlr/logout.html', context_dict)

def register(request):
    context_dict = {}
    return render(request, 'riddlr/register.html', context_dict)
