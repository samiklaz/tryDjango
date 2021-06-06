from django.urls import path
from .views import *

app_name = 'posts'
urlpatterns = [
    path('', posts_list, name='list'),
    path('create/', posts_create, name='create'),
    path('<str:slug>/', posts_detail, name='detail'),
    path('<str:slug>/update/', post_update, name='update'),
    path('<str:slug>/delete/', posts_delete, name='delete'),
]