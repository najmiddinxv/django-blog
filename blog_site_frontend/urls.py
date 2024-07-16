from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_site_frontend.index'),
]
