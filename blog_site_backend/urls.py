from django.urls import path
from .views import dashboard, set_language
from .views_folder import tag_views

urlpatterns = [
    #views.py
    path('set-language/', set_language, name='set_language'),
    path('dashboard/', dashboard, name='dashboard'),
    #views_folder/tag_views.py
    path('tags/', tag_views.index, name='tags.index'),
    path('tags/<int:pk>/', tag_views.show, name='tags.show'),
    path('tags/create/', tag_views.create, name='tags.create'),
    path('tags/update/<int:pk>/', tag_views.update, name='tags.update'),
    path('tags/delete/<int:pk>/', tag_views.delete, name='tags.delete'),
]
