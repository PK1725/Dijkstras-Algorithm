import pyglet
import random, hjørne_kant, constants

class Generator:


    data = []
    hjørner = hjørne_kant.Hjørner
    antalKanter = 0
    def generate(self, width, height):

        self.hjørner.generate(self=self.hjørner, width=width, height=height)

    def draw(self):
        for kant in self.hjørner.kanter:
            kant.draw()
        self.hjørner.draw(self.hjørner)

    def clear(self):
        self.hjørner.positioner = []
        self.hjørner.antalhjørner = random.randint(4,constants.NUM_OF_VERTICES)
        self.hjørner.kanter =[]
        self.antalKanter = 0
        self.hjørner.connections = []

