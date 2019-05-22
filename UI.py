import pyglet, graphGenerator, constants, algorithm

class Button:
    isGenerate = False
    generator  = 0
    dijkstra = algorithm.Dijkstra()
    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.orColor = color

    def checkIfClicked(self,mouseX,mouseY, button, mouseObj,start,stop):
        if mouseX > self.x and mouseX < (self.x + self.width) and  mouseY > self.y and mouseY < (self.y + self.height) and button == mouseObj.LEFT:
            self.color = (197,196,193)
            self.generator = graphGenerator.Generator()

            if self.generator.hjørner.positioner:
                self.generator.clear()
            self.generator.generate(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
            if self.dijkstra.table:
                self.dijkstra.clear()

    def draw(self):
        if self.generator:
            self.generator.draw()
        pyglet.graphics.draw(4, pyglet.graphics.GL_QUADS,
                             ('v2f', (self.x,self.y,self.x+self.width,self.y,self.x+self.width,self.y+self.height,self.x,self.y+self.height)),
                             ('c3B', self.color * 4))
        label = pyglet.text.Label(self.text,
                                  font_name='Gill Sans',
                                  font_size=18,
                                  x=self.x+(self.width//2), y=self.y+(self.height//2),
                                  anchor_x='center', anchor_y='center')
        label.draw()

    def update(self, button, mouseObj):

        if button == mouseObj.LEFT:
            self.color = self.orColor


class Button2:
    isGenerate = False
    generator = None

    def __init__(self, text, x, y, width, height, color, button1):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.orColor = color
        self.button1 = button1


    def checkIfClicked(self,mouseX,mouseY, button, mouseObj,start,stop):
        if mouseX > self.x and mouseX < (self.x + self.width) and  mouseY > self.y and mouseY < (self.y + self.height) and button == mouseObj.LEFT:
            self.color = (197,196,193)
            self.button1.dijkstra.run(generator=self.button1.generator, start=start, stop=stop)








    def draw(self):

        pyglet.graphics.draw(4, pyglet.graphics.GL_QUADS,
                             ('v2f', (self.x,self.y,self.x+self.width,self.y,self.x+self.width,self.y+self.height,self.x,self.y+self.height)),
                             ('c3B', self.color * 4))
        label = pyglet.text.Label(self.text,
                                  font_name='Gill Sans',
                                  font_size=18,
                                  x=self.x+(self.width//2), y=self.y+(self.height//2),
                                  anchor_x='center', anchor_y='center')
        label.draw()

    def update(self, button, mouseObj):

        if button == mouseObj.LEFT:
            self.color = self.orColor

class Rectangle(object):
    def __init__(self, x1, y1, x2, y2,color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
    def draw(self):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', [self.x1, self.y1, self.x2, self.y1, self.x2, self.y2, self.x1, self.y2]),
                             ('c4B', self.color * 4)
                             )
class Start(object):
    isGenerate = False
    generator = None

    def __init__(self, text, x, y, width):
        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text),
                                dict(color=(0, 0, 0, 255),font_size=20)
                                )
        font = self.document.get_font()

        self.height = font.ascent - font.descent
        self.width = width
        self.layout = pyglet.text.layout.IncrementalTextLayout(
            self.document, width, self.height, multiline=False)

        self.caret = pyglet.text.caret.Caret(self.layout)
        self.layout.x = x
        self.layout.y = y
        self.rectangle = Rectangle(x - 2, y -2, x+width +2, y + self.height+2,[200, 200, 220, 255])
    def hit_test(self, x, y):
        return (0 < x - self.layout.x < self.layout.width and
                0 < y - self.layout.y < self.layout.height)



    def draw(self):
        self.rectangle.draw()
        self.layout.draw()
        #pyglet.graphics.draw(4, pyglet.graphics.GL_QUADS,
        #                    ('v2f', (self.layout.x,self.layout.y,self.layout.x+self.width,self.layout.y,self.layout.x+self.width,self.layout.y+self.height,self.layout.x,self.layout.y+self.height)),
        #                     ('c3B', self.color * 4))
        label = pyglet.text.Label("Start:",
                                  font_name='Gill Sans',
                                  font_size=18,
                                  x=self.layout.x -40, y=self.layout.y+self.layout.height//2+2,
                                  anchor_x='center', anchor_y='center')
        label.draw()

    def update(self, button, mouseObj):
        pass


class Start(object):
    isGenerate = False
    generator = None

    def __init__(self, text, x, y, width, label):
        self.label = label
        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text),
                                dict(color=(0, 0, 0, 255),font_size=20)
                                )
        font = self.document.get_font()

        self.height = font.ascent - font.descent
        self.width = width
        self.layout = pyglet.text.layout.IncrementalTextLayout(
            self.document, width, self.height, multiline=False)

        self.caret = pyglet.text.caret.Caret(self.layout)
        self.layout.x = x
        self.layout.y = y
        self.rectangle = Rectangle(x - 2, y -2, x+width +2, y + self.height+2,[200, 200, 220, 255])
    def hit_test(self, x, y):
        return (0 < x - self.layout.x < self.layout.width and
                0 < y - self.layout.y < self.layout.height)



    def draw(self):
        self.rectangle.draw()
        self.layout.draw()
        #pyglet.graphics.draw(4, pyglet.graphics.GL_QUADS,
        #                    ('v2f', (self.layout.x,self.layout.y,self.layout.x+self.width,self.layout.y,self.layout.x+self.width,self.layout.y+self.height,self.layout.x,self.layout.y+self.height)),
        #                     ('c3B', self.color * 4))
        label = pyglet.text.Label(self.label,
                                  font_name='Gill Sans',
                                  font_size=18,
                                  x=self.layout.x -40, y=self.layout.y+self.layout.height//2+2,
                                  anchor_x='center', anchor_y='center')
        label.draw()

    def update(self, button, mouseObj):
        pass

