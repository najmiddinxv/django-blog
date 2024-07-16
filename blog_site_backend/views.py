from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import activate
from .models import Tag
from main.settings import LANGUAGE_COOKIE_NAME

def dashboard(request):
    tags = Tag.objects.all()
    return render(request, 'dashboard.html', {'tags': tags})


def set_language(request):
    user_language = request.GET.get('language', 'en')
    activate(user_language)
    response = redirect('dashboard')
    response.set_cookie(LANGUAGE_COOKIE_NAME, user_language)
    return response