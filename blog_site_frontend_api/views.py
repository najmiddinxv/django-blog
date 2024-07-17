from django.shortcuts import render
from django.http import JsonResponse

def dashboard(request):
    return JsonResponse({
        'status':'ok',
        'message':'dashboard blog_site_frontend_api'
    })

