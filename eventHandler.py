

class Handler:

    items = []

    def add(self, item):
        self.items.append(item)

    def handle(self, mouseX, mouseY, button, mouseObj,start,stop):

        if self.items:
            for i in self.items:
                if hasattr(i, 'checkIfClicked'):
                    i.checkIfClicked(mouseX=mouseX, mouseY=mouseY, button=button, mouseObj=mouseObj,start=start,stop=stop)


    def draw(self):
        if self.items:
            for i in self.items:
                i.draw()

    def update(self, button, mouseObj):
        if self.items:
            for i in self.items:
                i.update(button=button,mouseObj=mouseObj)