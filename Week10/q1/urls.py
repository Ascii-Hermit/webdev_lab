from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.category_list, name='category_list'),
    path('pages/', views.page_list, name='page_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('pages/create/', views.page_create, name='page_create'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail')
]