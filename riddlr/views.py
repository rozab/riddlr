from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from riddlr.models import Riddle, UserProfile, UserAnswer
#from riddlr.forms import UserForm, UserProfileForm


def home(request):
    context_dict = {}
    context_dict['top_riddles'] = Riddle.objects.order_by('-rating')[:5]
    context_dict['recent_riddles'] = Riddle.objects.order_by('-date_posted')[:5]
    context_dict['top_riddlrs'] = UserProfile.objects.order_by('-score')[:5]
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
    try:
        user = UserProfile.objects.get(username=username)
        riddles = user.riddle_set
        context_dict['top_riddles'] = riddles.order_by('-rating')
        context_dict['recent_riddles'] = riddles.order_by('-date_posted')
        context_dict['solved_riddles'] = user.useranswer_set.filter(correct=True).order_by('-date_posted')
        
    except User.DoesNotExist:
        context_dict['top_riddles'] = None
        context_dict['recent_riddles'] = None
        context_dict['solved_riddles'] = None

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
    # registered = False
    # if request.method == 'POST':
    #     user_form = UserForm(data=request.POST)
    #     profile_form = UserProfileForm(data=request.POST)
    #
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user = user_form.save()
    #         user.set_password(user.set_password)
    #         user.save()
    #         profile = profile_form.save(commit=False)
    #         profile.user = user
    #         if 'picture' in request.FILES:
    #             profile.picture = request.FILES['picture']
    #         profile.save()
    #         registered = True
    #     else:
    #         print(user_form.errors, profile_form.errors)
    # else:
    #     user_form = UserForm()
    #     profile_form = UserProfileForm()
    #
    # return render(request, 'riddlr/register.html', {'user_form': user_form, 'profile_form': profile_form,
    #                                                 'registered': registered})
    return render(request, context_dict)
