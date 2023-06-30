# class Lamp():
#     status = True
#     Bright = 3
#
#
# Lamp1 = Lamp()
# print(Lamp1.status)

# class lamp():
#     def __init__(self, manu, volt):
#         self.manu = manu
#         self.volt = volt
#
#     bright = 10
#     status = True
#
#     def info(self):
#         print(self.volt, self.manu, self.status, self.bright)
#
#
# hall_lamp = lamp(11, 12)
# hall_lamp.info()

# наследование

# class Dev():
#     def __init__(self, volt, name):
#         self.volt = volt
#         self.name = name
#
#     status = False
#
#     def On(self):
#         self.status = True
#         print(self.status)
#
#     def Off(self):
#         self.status = False
#
#
# class Lamp(Dev):
#     bright = 0
#
#     def info(self):
#         print(self.status)
#         print(self.bright)
#
#
# class Cleaner(Dev):
#     type = 0
#
#     def cleaning(self):
#         if self.type == 0:
#             print('0', self.status)
#         else:
#             print('1', self.status)
#
#
# cleaner1 = Cleaner(220, 'Cleaner')
# lamp1 = Lamp(110, 'Lamp')
# cleaner1.type = 1
# cleaner1.On()
# cleaner1.cleaning()
# print('-----')
# lamp1.bright = 100
# lamp1.On()
# lamp1.info()

# полиморфизм

# class Hero:
#     def __init__(self):
#         self.np = 100
#         self.atack = 15
#         self.speed = 1
#
#     def Say(self, a):
#         print("Герой говорит: " + a)
#
#
# class Enemy:
#     def __init__(self):
#         self.hp = 20
#         self.atack = 5
#         self.speed = 20
#
#     def Say(self):
#         print("Непонятное ворчание")
#
#
# character1 = Hero()
#
# character1.Say("я тебя спасу")
#
# antagonist1 = Enemy()
#
# antagonist1.Say()

# class Enemy():
#     def __init__(self, hp, atack, speed):
#         self.hp = hp
#         self.atack = atack
#         self.speed = speed
#
#         def Say(self):
#             self.speed += 30
#             print("Непонятное ворчание", self.speed)
#
#
# class Epick_Enemy(Enemy):
#
#     def Fly(self):
#         self.speed += 30
#
#     def Say(self):
#         self.speed += 30
#         print("Попробуй догони!", self.speed)
#
#
# Small_Dragon = Epick_Enemy(20, 39, 28)
# Small_Dragon.Say()

# инкапсуляция
# class Some:
#     def printWords(self):
#         __status = False
#         print(__status)
#     def __res(self):
#         print(1)
#
#
#
# obj = Some()
# obj.printWords() # Вызов функции ничего не даст
# obj.__res()



# class Simple_Class():
#   def __init__(self):
#     print("Я родился")
#   def __del__(self):
#     print("Мой час пришел")
#
# new_class = Simple_Class()


# class Simple_Class():
#   def __add__(self,n):
#     print(1 + n)
#
# res = Simple_Class()
# b = res + 1