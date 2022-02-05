# # #
# # #
# # # def custom_decarator(function):
# # #     def wrpapper():
# # #         print('начало нашей функции')
# # #         function()
# # #         print('онец нашей функции')
# # #     return wrpapper()
# # #
# # #
# # # def print_triple_hello():
# # #     print('hello')
# # #     print('hello')
# # #     print('hello')
# # #     print('hello')
# #
# # @bot.message_handler(commands=['start'])
# # def start_message(message):
# #     bot.reply_to(message, 'Вас приветствует пиццерия ТоктосунПицца!')
# #
# #
# # .reply_to(message, menu_str)@bot.message_handler(commands=['menu'])
# # def show_menu(message):
# #     menu_str = 'Наше меню\n'
# #     our_pizza_list = generate_pizzas()
# #     for pizza in our_pizza_list:
# #         name_price = pizza.get_name_with_price()
# #         menu_str += f'{name_price}\n'
# #     bot
# #
# #
# # @bot.message_handler(content_types='text')
# # def reply_to_standard_message(message):
# #     msg_text = message.text.lower()
# #     if msg_text in ['привет', 'салам', 'hello', 'hi']:
# #         response_msg = random.choice(['И вам привет!', 'салам!'])
# #         bot.reply_to(message, response_msg)
# #     elif msg_text in ('пока', 'до свидания'):
# #         bot.reply_to(message, 'Прощайте')
# #     elif msg_text in ('спасибо', 'благодарю'):
# #         bot.reply_to(message, 'Вам спасибо.')
# #     else:
# #         bot.reply_to(message, 'Я пока не могу на это ответить.')
# #
# #
# # bot.infinity_polling()
#
#
# import random
# from telebot import TeleBot
# from generate_data import generate_pizzas
#
#
# TELEGRAM_TOKEN = ''
#
#
# bot = TeleBot(TELEGRAM_TOKEN)
#
#
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.reply_to(message, 'Вас приветствует пиццерия ТоктосунПицца!')
#
#
# @bot.message_handler(commands=['menu'])
# def show_menu(message):
#     menu_str = 'Наше меню\n'
#     our_pizza_list = generate_pizzas()
#     for pizza in our_pizza_list:
#         name_price = pizza.get_name_with_price()
#         menu_str += f'{name_price}\n'
#     bot.reply_to(message, menu_str)
#
#
# @bot.message_handler(content_types='text')
# def reply_to_standard_message(message):
#     msg_text = message.text.lower()
#     if msg_text in ['привет', 'салам', 'hello', 'hi']:
#         response_msg = random.choice(['И вам привет!', 'салам!'])
#         bot.reply_to(message, response_msg)
#     elif msg_text in ('пока', 'до свидания'):
#         bot.reply_to(message, 'Прощайте')
#     elif msg_text in ('спасибо', 'благодарю'):
#         bot.reply_to(message, 'Вам спасибо.')
#     else:
#         bot.reply_to(message, 'Я пока не могу на это ответить.')
#
#
# bot.infinity_polling()


months = {
    1: 'январь',
    2: 'февраль',
    3: 'март',
    4: 'апрель',
    5: 'май',
    6: 'июнь',
    7: 'июль',
    8: 'август',
    9: 'сентябрь',
    10: 'октябрь',
    11: 'ноябрь',
    12: 'декабрь',
}
























class Product:
    market_name = "kyrgyz"

    def __init__(self, name_product, price_product , discount_product):
        self.name = name_product
        self.price = price_product
        self.discount = discount_product


    def get_info(self):
        info = f'Имя продукта : {self.name}. Цена продукта : {self.price}.'



    def get_discount_product(self):
        discount = (self.discount * self.price) / 100
        total_price = self.price - discount
        price = f'{self.name} стоит {total_price}сом с учетом скидок'
        return price


cola = Product(name_product = "Кока кола" , price_product = 50 , discount_product = 50 )
print(f'Product: {cola.name}')
print(f'Price: {cola.price}')
print(cola.get_discount_product())


