from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def home(request):
    contect_dict = {'welcome':"Welcome to Riddlr"}
    return render(request, 'Riddlr/home.html', context_dict)

