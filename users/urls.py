from django.urls import path
from users import views

urlpatterns = [
    path("register/",views.register, name="register"),
    path("login",views.login, name="login"),
    path("buy_ticket",views.buy_ticket, name="buy_ticket"),
    path("booking_details",views.booking_details, name="booking_details")
]
