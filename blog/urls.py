from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('item/<int:pk>/', views.item_page, name='item_detail'),
    path('item/new/', views.item_new, name='item_new'),
]
