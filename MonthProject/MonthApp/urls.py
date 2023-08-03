from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<int:month_id>/', views.redirect_to, name='redirect_to'),
    path('<str:month_name>/', views.month_view, name='month_view'),
    path('not_found/', views.not_found, name='not_found'),
]
