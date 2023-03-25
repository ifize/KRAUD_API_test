from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Player, Category, OnlineGame, Statistic
import json

@csrf_exempt
def create_player(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        player = Player.objects.create(name=name, age=age)
        return JsonResponse({'status': 'success', 'player_id': player.id})

@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        category = Category.objects.create(name=name, description=description)
        return JsonResponse({'status': 'success', 'category_id': category.id})

@csrf_exempt
def create_online_game(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        category_ids = data.getlist('categories')
        categories = Category.objects.filter(id__in=category_ids)
        game = OnlineGame.objects.create(name=name, description=description)
        game.categories.set(categories)
        return JsonResponse({'status': 'success', 'game_id': game.id})

def get_players(request):
    players = Player.objects.all().values('id', 'name', 'age')
    return JsonResponse({'players': list(players)})

def get_categories(request):
    categories = Category.objects.all().values('id', 'name', 'description')
    return JsonResponse({'categories': list(categories)})

def get_games(request):
    player_id = request.GET.get('player_id')
    if player_id:
        player = Player.objects.get(id=player_id)
        games = player.games.all().values('id', 'name', 'description')
    else:
        games = OnlineGame.objects.all().values('id', 'name', 'description')
    return JsonResponse({'games': list(games)})

@csrf_exempt
def update_statistic(request):
    if request.method == 'UPDATE':
        data = json.loads(request.body)
        player_id = data.get('player_id')
        game_id = data.get('game_id')
        score = data.get('score')
        time_played = data.get('time_played')
        statistic, created = Statistic.objects.get_or_create(player_id=player_id, game_id=game_id)
        statistic.score = score
        statistic.time_played = time_played
        statistic.save()
        return JsonResponse({'status': 'success'})

def top_players(request):
    top_players = Statistic.objects.all().values('playerid', 'playername').annotate(total_time_played=models.Sum('time_played')).order_by('-total_time_played')[:5]
    return JsonResponse({'top_players': list(top_players)})

@csrf_exempt
def create_statistic(request):
    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        game_id = request.POST.get('game_id')
        score = request.POST.get('score')
        time_played = request.POST.get('time_played')
        player = Player.objects.get(id=player_id)
        game = OnlineGame.objects.get(id=game_id)
        statistic = Statistic.objects.create(player=player, game=game, score=score, time_played=time_played)
        return JsonResponse({'status': 'success', 'statistic_id': statistic.id})