from django.urls import path
from . import views

urlpatterns = [
    path('', views.vote_view, name='vote'),
    path('result/', views.vote_result, name='vote_result'),
]
