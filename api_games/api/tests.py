from django.test import TestCase, Client
from django.urls import reverse
from .models import Player, Category, OnlineGame

class PlayerTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_player_url = reverse('create_player')

    def test_create_player(self):
        response = self.client.post(self.create_player_url, {
            'name': 'John',
            'age': 30
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Player.objects.count(), 1)
        self.assertEqual(Player.objects.first().name, 'John')
        self.assertEqual(Player.objects.first().age, 30)


class CategoryTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_category_url = reverse('create_category')

    def test_create_category(self):
        response = self.client.post(self.create_category_url, {
            'name': 'Action',
            'description': 'Action games'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().name, 'Action')
        self.assertEqual(Category.objects.first().description, 'Action games')


class OnlineGameTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_game_url = reverse('create_game')

    def test_create_game(self):
        category = Category.objects.create(name='Action', description='Action games')
        response = self.client.post(self.create_game_url, {
            'name': 'Game1',
            'description': 'Game description',
            'categories': [category.id]
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(OnlineGame.objects.count(), 1)
        self.assertEqual(OnlineGame.objects.first().name, 'Game1')
        self.assertEqual(OnlineGame.objects.first().description, 'Game description')
        self.assertEqual(OnlineGame.objects.first().categories.first(), category)