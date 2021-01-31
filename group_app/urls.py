from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('login_user', views.login_user),
    path('register_user', views.register_user),
    path('logout', views.logout),
    path('register', views.register),
    path('main', views.main, name="main"),
    path('game_page', views.game_page, name="game_page"),
    path('user_choice', views.user_choice),
]
