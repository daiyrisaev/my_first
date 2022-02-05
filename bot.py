import random
from telebot import TeleBot   # это мы импортуруем из скачанай нами библиотеке
from generate_data import generate_pizzas
from generate_data import generate_drinks
TELEGRAM_TOKEN='5028516455:AAF8T5-VfD1quQkqmj2VtEuhFdsbCJwZCko'

bot = TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def react_to_start(message):
    bot.reply_to(message,'приветствую мой Дайыр! Это я ваш первый бот')

@bot.message_handler(commands=['menu'])
def show_menu(message):
    menu_str = 'Наше меню\n'
    our_pizza_list = generate_pizzas()
    for pizza in our_pizza_list:
        name_price = pizza.get_name_with_price()
        menu_str += f'{name_price}\n'
    bot.reply_to(message, menu_str)

@bot.message_handler(commands=['Drink'])
def show_Drink(message):
    Drink_str ='наши напитки\n'
    our_Drink_list = generate_drinks()
    for Drink in our_Drink_list:
        name_price = Drink.get_name_with_price()
        Drink_str+= f'{name_price}\n'
    bot.reply_to(message, Drink_str)


@bot.message_handler(commands=['combo_menu'])
def show_menu(message):
    menu_str = 'комбо меню\n'
    pizzas= generate_pizzas()
    drinks = generate_drinks()
    for i in range(1,4):
        pizza = random.choice(pizzas)
        # pizzas.remove(pizza)
        drink = random.choice(drinks)
        # drink.remove(drink)

        menu_str += f'{pizza.name}+ {drink.name}= {pizza.price+drink.price}сом\n'
    bot.reply_to(message=message, text=menu_str)

@bot.message_handler(func=lambda message: True)
def react_to_message_text(message):
    if message.text == 'привет':
        bot.reply_to(message, 'И тебе привет.')
    elif message.text.lower() == 'пока':
        bot.reply_to(message,'До свидание!!!')

bot.polling()

