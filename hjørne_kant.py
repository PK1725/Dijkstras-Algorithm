import random, graphics, constants

class Kant:
    def __init__(self,x1,y1,x2,y2,connection):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.length = ((x2-x1)**2+(y2-y1)**2)**0.5
        self.connection = connection
        self.color = (0,0,0)

    def draw(self):
        graphics.draw_kant(x1=self.x1,y1=self.y1,x2=self.x2,y2=self.y2,len=round(self.length),color=self.color)
class Hjørner:

    alfa = 'abcdefghijklmnopqrstuvwxyz'.upper()
    antalhjørner = random.randint(4, constants.NUM_OF_VERTICES)
    positioner = []
    kanter = []
    connections = []
    print()

    def generate(self, width, height):

        for i in range(0, self.antalhjørner):

            self.positioner.append(random.randint(15,width-300))
            self.positioner.append(random.randint(15,height-25))
            self.positioner.append(random.choices([1, 2, 3, 4, 5], [0.20, 0.30, 0.20, 0.20, 0.10])[0])
            self.positioner.append(self.alfa[i])
            self.positioner.append(0)
        for i in range(0, self.antalhjørner):
            if self.positioner[i * 5 + 4] >= self.positioner[i * 5 + 2]:
                continue
            else:
                min = self.positioner[i * 5 + 4]
                for j in range(min, self.positioner[i*5+2]):

                    forsøg = 0
                    hjørne = random.randint(0, self.antalhjørner - 1)

                    while self.positioner[hjørne*5+2] <= self.positioner[hjørne*5+4] or hjørne == i or any(x.x1 == (self.positioner[i * 5]) and x.x2 == (self.positioner[hjørne * 5])  for x in self.kanter) or any(x.x1 == (self.positioner[hjørne * 5]) and x.x2 == (self.positioner[i * 5])  for x in self.kanter):

                        forsøg += 1
                        hjørne = random.randint(0, self.antalhjørner - 1)

                        if forsøg >= 50:
                            break
                    if hjørne == i or any(x.x1 == (self.positioner[i * 5]) and x.x2 == (self.positioner[hjørne * 5])  for x in self.kanter) or any(x.x1 == (self.positioner[hjørne * 5]) and x.x2 == (self.positioner[i * 5])  for x in self.kanter):
                        break
                    else:
                        self.kanter.append(Kant(self.positioner[i*5],self.positioner[i*5+1],self.positioner[hjørne*5],self.positioner[hjørne*5+1],[self.positioner[i*5+3].lower(),self.positioner[hjørne*5+3]]))
                        self.connections.append(self.positioner[i*5+3])
                        self.connections.append(self.positioner[hjørne*5+3])

                        self.positioner[i*5+4] += 1
                        self.positioner[hjørne*5+4] += 1

    def draw(self):
        for i in range (0, self.antalhjørner):
            graphics.draw_corner(self.positioner[i*5], self.positioner[i*5+1],0,360,10, self.positioner[i*5+3],self.positioner[i*5+4])

