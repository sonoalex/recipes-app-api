
from decimal import Decimal
from core.models import Recipe, User


class RecipeBuilder():
    def __init__(self):

        self.defaults = {
            'title': 'Sample recipe title',
            'time_minutes': 22,
            'price': Decimal('5.25'),
            'link': 'http://example.com/recipe.pdf',
        }

    def with_title(self, title: str):

        self.defaults.update({'title': title })

    def with_user(self, user: User):
        self.defaults.update({'user': user })

    def build(self):

        return Recipe.objects.create(**self.defaults)

