
from data import Pizza
from data import Drink

def generate_pizzas():
    pizzas = [Pizza(name_pm='Маргарита', price_pm=300, size_pm=25, consist_pm='сыр, томаты'),
              Pizza(name_pm='Гавайская', price_pm=550, size_pm=35, consist_pm='сыр, ананас'),
              Pizza(name_pm='Пепперони', price_pm=495, size_pm=30, consist_pm='сыр, ветчина'),]
    return pizzas

def generate_drinks():
    drinks = [Drink(name_pm='coco-cola',price_pm=50, volume_pm=0.5,is_gas_pm=True),
              Drink(name_pm='fanta', price_pm=55, volume_pm=0.7, is_gas_pm=False),
              Drink(name_pm='asu', price_pm=20, volume_pm=0.4, is_gas_pm=True),]
    return drinks


