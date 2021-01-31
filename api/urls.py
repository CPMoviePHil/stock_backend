from django.urls import path

from . import views

urlpatterns = [
    path('date', views.list_of_stock_by_date),
]
