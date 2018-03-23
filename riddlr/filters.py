from django.contrib.auth.models import User
from riddlr.models import UserProfile, Riddle
import django_filters

class UserProfileFilter(django_filters.FilterSet):
    user__username = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = UserProfile
        fields = ['user__username',]

class RiddleFilter(django_filters.FilterSet):


    class Meta:
        model = Riddle
        fields = ['difficulty_pt','rating']