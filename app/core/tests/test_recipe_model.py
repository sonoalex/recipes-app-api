"""Test for Models"""
from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class RecipeModelTests(TestCase):
    """Test models"""

    def test_create_recipe(self):
        """Test creating a recipe successfull"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal(5.50),
            description='Sample recipe description'
        )
        self.assertEqual(str(recipe), recipe.title)
