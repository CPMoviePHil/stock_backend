from django.urls import path

from . import views

urlpatterns = [
    path('date', views.list_of_stock_by_date, name="search_by_date"),
    path('name', views.stock_by_name, name="search_by_name_and_date"),
    path('search', views.search_stock_by_condition, name="search_stock"),
]
