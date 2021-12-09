from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiak>/', views.get_sign_zodiak_number),
    path('<str:sign_zodiak>/', views.get_sign_zodiak, name='horoscope_name'),
]
