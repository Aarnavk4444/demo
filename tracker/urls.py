from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('add/', views.add_item, name='add_item'),
]