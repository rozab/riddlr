"""riddlr_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from riddlr import views

urlpatterns = [
    path('',
         views.home,
         name='home'),

    path('about/',
         views.about,
         name='about'),

    path('riddles/',
         views.riddles,
         name='riddles'),

    path('add_riddle/',
         views.add_riddle,
         name='add_riddle'),

    path('riddle/<id>/',
         views.riddle,
         name='riddle'),

    path('user/<username>/',
         views.user,
         name='user'),

    path('users/',
         views.users,
         name='users'),

    path('login/',
         views.user_login,
         name='login'),

    path('logout/',
         views.user_logout,
         name='logout'),

    path('register/',
         views.register,
         name='register'),

    path('help/',
         views.help,
         name='help'),

    path('admin/',
         admin.site.urls),

    # url(r'^accounts/', include('registration.backends.simple.urls')),
    # reference to registration package

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'riddlr.views.error_404'
