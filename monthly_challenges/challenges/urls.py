from django.urls import path

from . import views

urlpatterns = [
    path("", views.index), # triggers for /challenges/
    path("<int:month>", views.monthly_challenges_by_num),
    path("<str:month>", views.monthly_challenges, name = "month-challenge")
]
