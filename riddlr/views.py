from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from riddlr.models import Riddle, UserProfile, UserAnswer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from riddlr.forms import RiddleForm, UserForm, UserProfileForm, AnswerForm
from riddlr import forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from riddlr.filters import UserProfileFilter,RiddleFilter


def home(request):
    context_dict = {}
    context_dict['top_riddles'] = Riddle.objects.order_by('-rating')[:5]
    context_dict['recent_riddles'] = Riddle.objects.order_by(
        '-date_posted')[:5]
    context_dict['top_riddlrs'] = UserProfile.objects.order_by('-score')[:5]
    return render(request, 'riddlr/home.html', context_dict)

def error_404(request):
    return render(request, 'riddlr/404.html')

def about(request):
    context_dict = {}
    return render(request, 'riddlr/about.html', context_dict)


def riddles(request):
    riddle_list = Riddle.objects.order_by('-rating')
    riddle_filter = RiddleFilter(request.GET, queryset=riddle_list)

    return render(request, 'riddlr/riddles.html', {'filter':riddle_filter})


@login_required(login_url='/login/')
def add_riddle(request):
    form = RiddleForm()
    if request.method == 'POST':
        form = RiddleForm(request.POST)
        if form.is_valid():
            riddle = form.save(commit=False)
            riddle.author = request.user
            riddle.save()
            return redirect('riddle', riddle.id)
        else:
            print(form.errors)

    return render(request, 'riddlr/add_riddle.html', {'form': form})

def riddle(request, id):
    context_dict = {'riddle': Riddle.objects.get(id=id)}
    if request.user.is_authenticated:
        useranswer = UserAnswer.objects.get_or_create(riddle=Riddle.objects.get(id=id), user=request.user.userprofile)[0]
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                useranswer.answer = form.data['answer']
                useranswer.num_tries += 1

                answer_list = useranswer.riddle.answers.split(",")
                for a in answer_list:
                    if useranswer.answer == a.strip():
                        useranswer.correct = True
                        break
                useranswer.save()
            else:
                print(form.errors)
        else:
            form = AnswerForm()
        context_dict['form'] = form
        context_dict['useranswer'] = useranswer

    return render(request, 'riddlr/riddle.html', context_dict)

def upvote(request, id):
    useranswer = UserAnswer.objects.get(id=id)
    if useranswer.rating == 1:
        useranswer.rating = 0
    else:
        useranswer.rating = 1
    useranswer.save()
    return redirect('riddle', useranswer.riddle.id)

def downvote(request, id):
    useranswer = UserAnswer.objects.get(id=id)
    if useranswer.rating == -1:
        useranswer.rating = 0
    else:
        useranswer.rating = -1
    useranswer.save()
    return redirect('riddle', useranswer.riddle.id)


def user(request, username):
    context_dict = {}
    try:
        user = User.objects.get(username=username)
        userprofile = user.userprofile
    except ObjectDoesNotExist:
        context_dict['error'] = "User Not Found"
        return render(request, 'riddlr/404.html', context_dict)

    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('user', user.username)
        else:
            print(form.errors)
            context_dict['errors'] = form.errors
            # TODO display errors properly

    context_dict = {'username': username}
    context_dict['userprofile'] = userprofile
    riddles = user.riddle_set.all()
    context_dict['top_riddles'] = riddles.order_by('-rating')
    context_dict['recent_riddles'] = riddles.order_by('-date_posted')
    context_dict['solved_answers'] = userprofile.useranswer_set.filter(
        correct=True).order_by('-riddle__date_posted')

    return render(request, 'riddlr/user.html', context_dict)


def users(request):
    up_list = UserProfile.objects.order_by('-score')
    up_filter = UserProfileFilter(request.GET, queryset=up_list)

    return render(request, 'riddlr/users.html', {'filter':up_filter})


def user_login(request):
    # TODO return errors properly with form
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
            user.set_password(user.password)
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


def help(request):
    return render(request, 'riddlr/help.html')