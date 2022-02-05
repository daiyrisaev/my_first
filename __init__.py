# # # # # модуль это файл с расширением
# # # #  дироктория это простая попка
# # # #  пакет - папка внутри есть файл
# # # #
# # # #
# # # number = 0
# # # while number<=50:
# # #
# # #     number += 1
# # #     if (number % 1) !=0:
# # #
# # #      continue;
# # #
# # #     print('четные число'+ str(number))
# #
# #
#
#
# class Animal:
#       def __init__(self,lion,elephant,):
#           self.lion=lion
#           self.elephant=elephant
#
#       def get_count(self):
#        return self.lion+self.elephant
# Animal1=Animal(lion=10,elephant=10)
# print(Animal1.lion)
# print(Animal1.elephant)
# print(Animal1.get_count())
#
# class Snake(Animal):
#
#
#
#
#
#
# stroka1=int(2)
# stroka2=int(3)
#
# def compare_stroka(s1,s2):
#
#
#
#   if(s1==s2):
#     result='='
#   elif(s1>s2):
#     result='>'
#   elif(s1<s2):
#      result='<'
#   return result
#
# result=compare_stroka(stroka1,stroka2)
# print(result)
#
#
# months = {

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
try:
    date = int(input('введите порядок месяца: '))
    print(months[date])
    if date > 12:
        print('у нас есть только 12 месяцев')
except:
    print('найдена ошибка... ')
    date = int(input('введите порядок месяца: '))
    print(months[date])
