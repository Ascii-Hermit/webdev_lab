from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='page1'),  
    path('bill/', views.page2, name='page2'),  
]
