from django import forms
from django.contrib.auth.models import User
from riddlr.models import Riddle, UserProfile, UserAnswer

class RiddleForm(forms.ModelForm):
    question = forms.CharField(max_length=400,
                               help_text="Please enter the riddle.")
    answers = forms.CharField(max_length=128,
                             help_text="Enter accepted answers in a comma separated list")
    difficulty = forms.IntegerField()
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    num_answers = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Riddle
        fields = ('question', 'answers')

class AnswerForm(forms.Form):
    answer = forms.CharField(max_length=30,help_text="Answer here.", initial="")

    class Meta:
        model = UserAnswer
        fields = ('answer',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    
    class Meta:
        model = UserProfile
        fields = ('picture',)
