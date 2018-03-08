from django.contrib import admin

from riddlr.models import Riddle
from riddlr.models import UserProfile

admin.site.register(Riddle)
admin.site.register(UserProfile)
