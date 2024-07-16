from django.shortcuts import render, redirect, get_object_or_404
from .models import Tag

def dashboard(request):
    tags = Tag.objects.all()
    return render(request, 'dashboard.html', {'tags': tags})
