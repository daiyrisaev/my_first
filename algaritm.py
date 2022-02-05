# # # # # i = 0
# # # # # while True:
# # # # #     if i == 5:
# # # # #         break
# # # # #     print(i)
# # # # #     i=i+1
# # # #
# # # # a=int(input('введите первое число'))
# # # # b=int(input('введите второе число'))
# # # # for i in a==b:
# # # #     if a<b:
# # # #       print('это наименьшее число')
# # #
# # # list=[1,2,3,4,5,6,7,8,9,10]
# # # for elem in list:
# # #     if elem < 5:
# # #         # print(elem)
# # #
# # #
# # class Car:
# #     wheels=4
# #     honda=1
# #
# #     def __init__(self,brand,color,honda):
# #         self.brand=brand
# #         self.color=color
# #         self.honda=honda
# #
# #
# #
# # def season(num):
# #
# #      if num == 12 or 1 <= num <= 2:
# #
# # print("Зима")
# #
# # elif 3 <= num <= 5:
# #
# # print("Весна")
# #        elif 6 <= num <= 8:
# #
# #        print("Лето")
# #
# #      elif 9 <= num <= 11:
# #
# # print("Осень")
# #
# #      else:
# #
# #          print("Неверно введён номер месяца!")
# #
# # n = int(input("Введите номер месяца (1-12): "))
# #
# # season(n)
#
#
# class Person:
#
#     def __init__(self,name,age,salary):
#         self.name=name
#         if age in range(1,100):
#             self.__age=age
#         else:
#
#             raise ValueError ('недоступный возраст')
#
#         self.salary=salary
#
#
#     def show_full_info(self):
#         print(f'name:{self.name}')
#         print(f'age:{self.age}')
#         print(f'salary:{self.salary}')
#
#
#
#     @property
#     def age(self):
#         return self.__age
#
# class Employee(Person):
#     '''класс работник'''                                 #ff
#     __boss=None# будет привазан одному начальнику
#
#     super().show_full_info()
#    print(f'__boss:{self.__boss}')
#
#     def boss(self):
#         return self.__boss
#
#     def set_boss(self,boss_pm):
#         if isinstance(boss_pm,Boss):
#             self.__boss=boss_pm
#         raise ValueError('ne ayvlayetsa egzamplara claassa bos')
#
#     def __repr__(self):
#         return f'rabotnik:{self.name}'
#
#     def __str__(self):
#         return f'работник:{self.name}'
#
# class Boss(Person):
#     '''класс работник'''
#     Employeers=[]
#
#     def show_full_info(self):
#         super().show_full_info()
#         print(f'Employeers:{self.Employeers}')
#
#
#     def add_employye(self,emploer_pm):
#         self.emploer=emploer_pm
#         if isinstance(emploer_pm,Employee):
#
#
#
#     def __str__(self):
#         return f'работник:{self.name}'
#
#
# first_worker=Employee(name='работник-1',age=20,salary=3500)
# second_worker=Employee(name='работник-2',age=28,salary=4000)
# first_boss=Boss(name='начальник-2',age=44,salary=5000)
#
#
#
# print('do privaxki:',second_worker.boss)
# second_worker.set_boss(boss_pm=first_boss)
# print('posle privaski:',second_worker.boss)

#
#
# # first_Employee.boss=32232
# # print(first_Employee.boss.age)
# #
# # print(' do привязки:',first_boos.Employeers)
# # first_boos.Employeers=[first_boos.Employeers]
# #print('привязки:',first_boos.Employeers)

# list=[1,2,3,3,3,3,4,4,4,5,5,6,6,7,7]
# my_set=set(list)
# print(my_set)











