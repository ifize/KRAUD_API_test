from django.urls import path

from . import views


urlpatterns = [
    path('players/create/', views.create_player, name='create_player'),
    path('categories/create/', views.create_category, name='create_category'),
    path('games/create/', views.create_online_game, name='create_online_game'),
    path('players/', views.get_players, name='get_players'),
    path('categories/', views.get_categories, name='get_categories'),
    path('games/', views.get_games, name='get_games'),
    path('statistic/', views.get_statistic, name='get_statistic'),
    path('statistic/update/', views.update_statistic, name='update_statistic'),
    path('top-players/', views.top_players, name='top_players'),
    path(
        'user_games/<int:player_id>/',
        views.get_user_games,
        name='get_user_games'
        ),
]
