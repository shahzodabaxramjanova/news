from django.urls import path
from .views import *

urlpatterns = [
    path('', news_list, name='news-list'),
    path('create/', news_create, name='news-create'),
    path('detail/<int:pk>/', news_detail, name='news-detail'),
    path('update/<int:pk>/', news_update, name='news-update'),
    path('delete/<int:pk>/', news_delete, name='news-delete'),
]