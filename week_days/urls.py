from django.urls import path
from week_days import views as views_week_days

urlpatterns = [
    path('<int:day>', views_week_days.get_day_week_number),
    path('<str:day>', views_week_days.get_day_week),
]
