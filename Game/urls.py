from django.urls import path
from . import views

app_name = 'Game'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('game/<int:num>', views.game_view, name='game'),
    path('result/', views.result_view, name='result'),
    path('table/', views.table_view, name='table'),
    path('leave/<int:num>', views.leave_game, name='leave'),
]
