import click
from pip._internal import cli

from pizza_project import OurPizza
from pizza_project import bake, pickup, delivery


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery_flag', default=False, is_flag=True)
@click.option('--size', default='L', type=str)
@click.argument('pizza', nargs=1)
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


@cli.command()
def menu():
    """Команда отображает доступное меню"""
    answer = ''
    for pizza in all_pizza:
        answer += f'- {pizza.name}: ' + ', '.join(ingredient for ingredient in pizza.ingredients) + '\n'
    print (answer)


if __name__ == '__main__':
    all_pizza = [OurPizza('Margherita', 'L'), OurPizza('Pepperoni', 'L'), OurPizza('Hawaiian', 'L')]
    cli()