from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Player, Category, OnlineGame, Statistic
from django.db.models import Sum
import json


@csrf_exempt
def create_player(request):
    """
    Создание игрока с заданным именем и возрастом.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        player = Player.objects.create(name=name, age=age)
        return JsonResponse({'status': 'success', 'player_id': player.id})


@csrf_exempt
def create_category(request):
    """
    Создание категории с заданным именем и описанием.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        category = Category.objects.create(name=name, description=description)
        return JsonResponse({'status': 'success', 'category_id': category.id})


@csrf_exempt
def create_online_game(request):
    """
    Создание онлайн-игры с заданным именем, описанием и категориями.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        category_ids = data.get('categories')
        categories = Category.objects.filter(id__in=category_ids)
        game = OnlineGame.objects.create(name=name, description=description)
        game.categories.set(categories)
        return JsonResponse({'status': 'success', 'game_id': game.id})


def get_players(request):
    """
    Получение списка всех игроков.
    """
    players = Player.objects.all().values('id', 'name', 'age')
    return JsonResponse({'players': list(players)})


def get_categories(request):
    """
    Получение списка всех категорий.
    """
    categories = Category.objects.all().values('id', 'name', 'description')
    return JsonResponse({'categories': list(categories)})


def get_games(request):
    """
    Получение списка всех онлайн-игр.
    """
    games = OnlineGame.objects.all().values('id', 'name', 'description')
    return JsonResponse({'games': list(games)})


def get_statistic(request):
    """
    Получение статистики всех игроков.
    """
    stats = Statistic.objects.all().values(
        'id', 'player_id', 'score', 'time_played', 'game_id'
        )
    return JsonResponse({'statistic': list(stats)})


@csrf_exempt
def update_statistic(request):
    """
    Обновление статистики игрока для заданной игры.
    """
    if request.method == 'PUT':
        data = json.loads(request.body)
        player_id = data.get('player_id')
        game_id = data.get('game_id')
        score = data.get('score')
        time_played = data.get('time_played')
        statistic, created = Statistic.objects.get_or_create(
            player_id=player_id,
            game_id=game_id
            )
        statistic.score = score
        statistic.time_played = time_played
        statistic.save()
        return JsonResponse({'status': 'success'})


def top_players(request):
    """
    Получение списка топ-5 игроков по общему времени игры.
    """
    top_players = Statistic.objects.values('player__name').annotate(
        total_time_played=Sum('time_played')
        ).order_by('-total_time_played')[:5]
    return JsonResponse({'top_players': list(top_players)})


def get_user_games(request, player_id):
    """
    Получение списка игр, в которые играл заданный игрок.
    """
    user_statistics = Statistic.objects.filter(player_id=player_id)
    user_games = []
    for statistic in user_statistics:
        game = OnlineGame.objects.get(id=statistic.game_id)
        user_games.append({
            'id': game.id,
            'name': game.name,
            'description': game.description,
        })
    return JsonResponse({'games': user_games})
