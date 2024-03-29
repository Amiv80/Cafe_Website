from django.urls import path
from cafe.views import home, calculate_cost, display_cost

urlpatterns = [
    path("", home, name="home"),
    path("calculate_cost/", calculate_cost, name="calculate_cost"),
    path("display_cost/", display_cost, name="display_cost"),
]
