from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from riddlr.models import Riddle, UserProfile, UserAnswer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from riddlr.forms import UserForm, UserProfileForm
from riddlr import forms

def home(request):
    context_dict = {}
    context_dict['top_riddles'] = Riddle.objects.order_by('-rating')[:5]
    context_dict['recent_riddles'] = Riddle.objects.order_by('-date_posted')[:5]
    context_dict['top_riddlrs'] = UserProfile.objects.order_by('-score')[:5]
    return render(request, 'riddlr/home.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'riddlr/about.html', context_dict)

def riddles(request):
    context_dict = {}
    top_riddles = Riddle.objects.order_by('-rating')[:]
    hard_riddles = Riddle.objects.filter(difficulty__gt=100)
    medium_riddles = Riddle.objects.filter(difficulty__gt=50).filter(difficulty__lt=101)
    easy_riddles = Riddle.objects.filter(difficulty__lt=51)
    context_dict['top_riddles'] = top_riddles
    return render(request, 'riddlr/riddles.html', context_dict)

def add_riddle(request):
    context_dict = {}
    return render(request, 'riddlr/add_riddle.html', context_dict)

def riddle(request, id):
    context_dict = {}
    return render(request, 'riddlr/riddle.html', context_dict)

def user(request, username):
    context_dict = {'username':username}
    try:
        user = UserProfile.objects.get(user__username=username)
        riddles = user.riddle_set
        context_dict['top_riddles'] = riddles.order_by('-rating')
        context_dict['recent_riddles'] = riddles.order_by('-date_posted')
        #context_dict['solved_riddles'] = user.useranswer_set.filter(correct=True).riddle_set.order_by('-date_posted')
        
    except User.DoesNotExist:
        context_dict['top_riddles'] = None
        context_dict['recent_riddles'] = None
        context_dict['solved_riddles'] = None

    return render(request, 'riddlr/user.html', context_dict)

def users(request):
    context_dict = {}
    context_dict['top_riddlrs'] = UserProfile.objects.order_by('-score')[:]
    return render(request, 'riddlr/users.html', context_dict)

def user_login(request):
    context_dict = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request, 'riddlr/login.html')

def user_logout(request):
    context_dict = {}
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    context_dict = {}
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.set_password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'riddlr/register.html', {'user_form': user_form, 'profile_form': profile_form,
                                                    'registered': registered})

