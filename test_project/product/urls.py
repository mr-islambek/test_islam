from django.urls import path
from rest_framework import serializers
from  .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user_profiles/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
             name='user_profile_list'),
    path('user_profiles/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_profile_detail'),

    path('post/', PostViewSets.as_view({'get': 'list', 'post': 'create'}),
             name='post_list'),
    path('post/<int:pk>/', PostViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='post_detail'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)