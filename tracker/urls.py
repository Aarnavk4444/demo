from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('financials/', views.financial_metrics_view, name='financial_metrics'),
    path('health-report/', views.health_report_view, name='health_report'),
    path('registry/', views.inventory_registry_view, name='inventory_registry'),
    path('item/<int:item_id>/', views.item_detail_view, name='item_detail'),
]