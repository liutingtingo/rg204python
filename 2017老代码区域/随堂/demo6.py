class Lv(object):
    def eat(self):
        print("驴在吼")

class Ma(object):
    def eat(self):
        print("马在叫")

class Luozi(Ma,Lv):
    def eat(self):
        super().eat()
        print("骡子在咆哮")
        super().eat()
luozi = Luozi()
luozi.eat()

