from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home_view(request):
    user = request.user
    text = 'hello world'

    context = {
        'user' : user,
        'text' : text,
    }
    return render(request, 'main/home.html', context)