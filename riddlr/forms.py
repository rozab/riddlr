from django import forms
from django.contrib.auth.models import User
from riddlr.models import Riddle, UserProfile, UserAnswer  # ,Page

# NOT FINISHED AT ALL DONT USE
# NOT FINISHED AT ALL DONT USE
# NOT FINISHED AT ALL DONT USE
# NOT FINISHED AT ALL DONT USE
# NOT FINISHED AT ALL DONT USE
# NOT FINISHED AT ALL DONT USE
# NOT FINISHED AT ALL DONT USE


class RiddleForm(forms.ModelForm):
    question = forms.CharField(max_length=128,
                               help_text="Please enter the riddle.")
    answer = forms.CharField(max_length=128,
                             help_text="Enter accepted answers in a comma separated list")
    difficulty = forms.IntegerField()
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    num_answers = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Riddle
        fields = ('question', 'answer')

# class PageForm(forms.ModelForm):
#     title = forms.CharField(max_length=128,
#     help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=200,
#     help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         url = cleaned_data.get('url')
#         if url and not url.startswith('http://'):
#             url = 'http://' + url
#             cleaned_data['url'] = url
#
#         return cleaned_data
#
#     class Meta:
#         model = Page
#         exclude = ('category',)

class AnswerForm(forms.ModelForm):
    answer = forms.CharField(max_length=128,help_text="Answer here.")

    num_tries = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    correct = forms.BooleanField(widget=forms.HiddenInput(), initial=False)

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
        fields = ('picture', 'riddles')
