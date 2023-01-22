from random import randint
from typing import Callable
import click


class OurPizza:
    def __init__(self, name: str, size: str):
        if name not in ['Margherita', 'Pepperoni', 'Hawaiian']:
            raise ValueError('This pizza in not in menu!')
        if size not in ['L', 'XL']:
            raise ValueError('This size in not available!')

        self.size = size
        self.name = name

        if name == 'Margherita':
            self.name += ' 🧀'
            self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']

        if name == 'Pepperoni':
            self.name += ' 🍕'
            self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']

        if name == 'Hawaiian':
            self.name += ' 🍍'
            self.ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __str__(self):
        """магический метод для отображения информации об объекте класса для пользователей"""
        return f'{self.name} ({self.size})'

    def dict(self):
        """метод dict() - выводит рецепт в виде словаря"""
        recipe = {self.name: ', '.join(ingredient for ingredient in self.ingredients)}
        return recipe

    def __eq__(self, other):
        """реализуйте __eq__() для сравнения пицц
        (object.__eq__ в Python позволяет реализовать проверку на равенство для экземпляров пользовательских типов)"""
        if self.name == other.name and self.size == other.size:
            return True
        else:
            return False


def order(pizza: str, size: str, delivery_flag: bool):
    """Команда готовит пиццу, флаг –—delivery передает ее с курьером."""
    if delivery_flag not in [True, False]:
        raise ValueError('Delivery included, true or false')
    ordered_pizza = OurPizza(pizza, size)
    print(ordered_pizza)
    if delivery_flag == True:
        return ordered_pizza.__str__() + bake(pizza).__str__() + delivery(pizza).__str__()
    else:
        return ordered_pizza.__str__() + bake(pizza).__str__() + pickup(pizza).__str__()


def log(example: str):
    """декоратор, который выводит имя функции и время выполнения """

    def outer_wrapper(function: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs):
            print(example.replace('{}', f'{randint(10, 1000)}'))
            function(*args, **kwargs)

        return inner_wrapper

    return outer_wrapper


"""шаблоны, в которые подставляется время"""


@log('👨‍🍳 Приготовили за {} с!')
def bake(pizza: OurPizza):
    """Готовит пиццу"""


@log('🛵 Доставили за {} с!')
def delivery(pizza: OurPizza):
    """Доставляет пиццу"""


@log('🏠 Забрали за {} с!')
def pickup(pizza: OurPizza):
    """Самовывоз пиццы"""


