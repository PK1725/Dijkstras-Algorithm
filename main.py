import pyglet
from pyglet.window import key, mouse
import graphics, UI
import graphGenerator, eventHandler, constants
window = pyglet.window.Window(vsync=True, resizable=True, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, caption="Dijkstras Algoritme")
constants.SCREEN_WIDTH = window.width
constants.SCREEN_HEIGHT = window.height

handler = eventHandler.Handler()
button1 = UI.Button('Generate',window.width-275, window.height-200,180,50,(79,77,73))
button2 = UI.Button2('Dijkstra', constants.SCREEN_WIDTH- 275, constants.SCREEN_HEIGHT- 600, 180,50,(79,77,73),button1=button1)
text = UI.Start("",constants.SCREEN_WIDTH-205, constants.SCREEN_HEIGHT-300,25,"Start:")
text2 = UI.Start("",constants.SCREEN_WIDTH-205, constants.SCREEN_HEIGHT-400,25,"Stop:")

handler.add(button1)
handler.add(button2)
handler.add(text)
handler.add(text2)


def set_focus(focus2):
    if constants.focus:
        constants.focus.caret.visible = False
        constants.focus.caret.mark = constants.focus.caret.position = 0

    constants.focus = focus2
    if constants.focus:
        constants.focus.caret.visible = True
        constants.focus.caret.mark = 0
        constants.focus.caret.position = len(constants.focus.document.text)
set_focus(text)

text_cursor = window.get_system_mouse_cursor('text')


@window.event
def on_mouse_press(x, y, button, modifiers):

    handler.handle(x,y,button=button,mouseObj=mouse,start=text.document.text.upper(),stop=text2.document.text.upper())
    if text.hit_test(x,y):
        set_focus(text)
    elif text2.hit_test(x, y):
        set_focus(text2)
    else:
        set_focus(None)
    if constants.focus:
        constants.focus.caret.on_mouse_press(x,y,button,modifiers)

@window.event
def on_mouse_motion(x, y, dx, dy):
    if text.hit_test(x, y):
        window.set_mouse_cursor(text_cursor)
    if text2.hit_test(x, y):
        window.set_mouse_cursor(text_cursor)

    else:
        window.set_mouse_cursor(None)
@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):

    if constants.focus:
        constants.focus.caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)
@window.event
def on_mouse_release(x, y, button, modifiers):
    handler.update(button=button,mouseObj=mouse)
@window.event
def on_text(text):

    if constants.focus:
        constants.focus.caret.on_text(text)
@window.event

def on_text_motion( motion):

    if constants.focus:
        constants.focus.caret.on_text_motion(motion)
@window.event
def on_text_motion_select( motion):

    if constants.focus:
        constants.focus.caret.on_text_motion_select(motion)
@window.event
def on_resize(width, height):
    constants.SCREEN_WIDTH = width
    constants.SCREEN_HEIGHT = height
    handler.draw()
@window.event
def on_draw():

    window.clear()
    pyglet.graphics.draw(4, pyglet.graphics.GL_QUADS,
                         ('v2f', (0,0,window.width,0,window.width,window.height,0,window.height)),
                         ('c3B', (177,176,175)*4))
    pyglet.graphics.draw(4, pyglet.graphics.GL_QUADS,
                         ('v2f', (window.width-300, 0, window.width, 0, window.width, window.height, window.width-300, window.height)),
                         ('c3B', (146, 145, 143) * 4))


    handler.draw()

    pyglet.clock.tick()
@window.event

def on_key_press( symbol, modifiers):
    if symbol == pyglet.window.key.TAB:
        if modifiers & pyglet.window.key.MOD_SHIFT:
            dir = -1
        else:
            dir = 1



        set_focus(text)

    elif symbol == pyglet.window.key.ESCAPE:

        pyglet.app.exit()

pyglet.app.run()