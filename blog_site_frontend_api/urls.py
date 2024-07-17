from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='blog_site_frontend_api.dashboard'),
]
