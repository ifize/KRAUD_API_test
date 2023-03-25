from django.contrib import admin
from .models import Player, Category, OnlineGame, Statistic

admin.site.register(Player)
admin.site.register(Category)
admin.site.register(OnlineGame)
admin.site.register(Statistic)
