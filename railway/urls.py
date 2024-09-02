from django.urls import path
from railway import views

urlpatterns = [
    path("",views.home, name="home"),
    path("search_trains",views.search_trains, name="search_trains"),
]
