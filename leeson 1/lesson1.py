# #высота потокдлв и праписать медоды которое принянимет этоой комнаты
# #128кв метр
# #количест комнат
# #высот потодка
# #сколько этаж
#
# #
# #
# #
# class onefloorhouse:
#         total_square = 100  #
#
#         def __init__(self, room_count_param,room_vysota_param):#магический метод
#             self.room_count = room_count_param #атрибут эгземпляра
#             self.room_vysota = room_vysota_param
#
#         def get_volume(self):
#             total_volume= self.total_square* self.room_vysota
#             return total_volume
#
#
# class twofloorhouse(onefloorhouse):
#     total_square = 165
#
# house1 = onefloorhouse(room_count_param=5, room_vysota_param=2.80) #создаем эгземпляр класса посредсвом конструктора
# house2 = onefloorhouse
# # print(house1.total_square) #обращяемся к значению атрибута
# # print(house1.room_count)
# # print(house1.room_vysota)
#
#
# #twofloorhouse1 = twofloorhouse(room_count_param=8,room_vysota_param=3)
# #pr создаем класс ректенгил
# #принимает двва паремтры длину и ширину
# #наследуемся от данного класса паралепипет которое принимают длину и  ширну и имее
#
# class Rectangle:
#
#     def __init__(self,dlina,shirina):
#         self.dlina= dlina
#         self.shirina = shirina
#
#     def get_square(self):
#         return self.dlina*self.shirina
#
# square1 = Rectangle(dlina=10,shirina=5)
# # print(square1.dlina)
# # print(square1.shirina)
# # print(square1.get_square())
#
# class Paralelpiped(Rectangle):
#
#     def __init__(self,dlina,shirina,vysata):
#         self.dlina= dlina
#         self.shirina = shirina
#         self.vysata = vysata
#
#     def get_volume(self):
#         return self.dlina *self.shirina+self.vysata
#
# square2= Paralelpiped(dlina=10,shirina=5,vysata=15)
# print(square2.get_volume())


#single responsibilyti = ринцип единой отвественнности


class Person:

      def __init__(self,name1,age):
          self.name = name1
          self.age = age

      def get_info(self):
          info = f'имя {self.name}.возраст: {self.age}' #функция
          return  info

      def show_info(self):
          info= f'имя: {self.name}.возраст:{self.age}'  #процедура
          print(info)

      def get_age(self):
          return self.age



person2 = Person(name1='daiyr',age=17)
person2.show_info()



class Product:
      magazine_name= 'bishkek'
      def __init__(self, name,priсe):
          self.name=name
          if priсe < 0:
              raise ValueError('цена не может быть отрицательным')


      def get_price(self):
          price= f'цена {self.__price}'
          return price


























