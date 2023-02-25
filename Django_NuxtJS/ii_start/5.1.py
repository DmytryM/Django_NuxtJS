# class Lamp():
#     status = True
#     Bright = 3
#
#
# Lamp1 = Lamp()
# print(Lamp1.status)

class lamp():
    def __init__(self, manu, volt):
        self.manu = manu
        self.volt = volt

    bright = 10
    status = True

    def info(self):
        print(self.volt, self.manu, self.status, self.bright)


hall_lamp = lamp(11, 12)
hall_lamp.info()
