from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    games = models.ManyToManyField('OnlineGame', through='Statistic', related_name='players')

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class OnlineGame(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='online_games')

    class Meta:
        verbose_name = 'Онлайн игра'
        verbose_name_plural = 'Онлайн игры'

class Statistic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(OnlineGame, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    time_played = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
