class Man:
    weight = 70
    height = 175
    iq = 130
    def __init__(self,weight,height,iq):
        self.weight = weight
        self.height = height
        self.iq = iq

    def eat(self):
        self.weight = self.weight+10
        self.height = self.height+10
        self.iq = self.iq-10

    def study(self):
        self.weight = self.weight-10
        self.height = self.height-10
        self.iq = self.iq+10

    def sleep(self):
        self.weight = self.weight-10
        self.height = self.height+10
        self.iq = self.iq+10

    def sta(self):
        print(self.weight,self.height,self.iq)

class Woman:
    weight = 50
    height =160
    iq = 120

    def __init__(self, weight, height, iq):
        self.weight = weight
        self.height = height
        self.iq = iq

    def eat(self):
        self.weight = self.weight + 10
        self.height = self.height + 10
        self.iq = self.iq - 10

    def study(self):
        self.weight = self.weight - 10
        self.height = self.height - 10
        self.iq = self.iq + 10

    def sleep(self):
        self.weight = self.weight - 10
        self.height = self.height + 10
        self.iq = self.iq + 10

    def sta(self):
        print(self.weight, self.height, self.iq)

mys = Man(80,170,120)
mys.eat()
mys.sta()
mys.study()
mys.sta()
mys.sleep()
mys.sta()