from django.urls import path
from .views import TagList, TagDetail

urlpatterns = [
    path('tags/', TagList.as_view(), name='tag_list_api'),
    path('tags/<int:pk>/', TagDetail.as_view(), name='tag_detail_api'),
]
