import pyglet
import math
batch = pyglet.graphics.Batch()


# int((x+(-(y**2)+2*(x+r)*y+r**2-(x+r)**2))**0.5), int((x+(-(y**2)+2*x*y+r**2-x**2))**0.5)
def draw_corner(x, y, z, numberOfSides, r=20, navn='A', grad=0):

    vertices = numberOfSides + 2

    circleVX = [None]*vertices
    circleVY = [None]*vertices
    circleVZ = [None]*vertices

    circleVX[0] = x
    circleVY[0] = y
    circleVZ[0] = z

    for i in range(1, vertices):
        circleVX[i] = x + (r*math.cos(2*i*math.pi / numberOfSides))
        circleVY[i] = y + (r*math.sin(2*i*math.pi / numberOfSides))
        circleVZ[i] = z
    allVertices = [None]*vertices*3
    for i in range(0, vertices):
        allVertices[(i*3)] = circleVX[i]
        allVertices[(i*3 +1)] = circleVY[i]
        allVertices[(i*3 + 2)] = circleVZ[i]

    pyglet.graphics.draw(vertices, pyglet.gl.GL_TRIANGLE_FAN, (('v3f', tuple(allVertices))))
    label = pyglet.text.Label(f'{navn}',
                              font_name='Gill Sans',
                              font_size=14,
                              x=x, y=y+21,
                              anchor_x='center', anchor_y='center',
                              color=(0,0,0, 255))

    label2 = pyglet.text.Label(f'{grad}',
                              font_name='Gill Sans',
                              font_size=14,
                              x=x,y=y,
                              anchor_x='center', anchor_y='center',
                              color=(0,0,0,255))
    label.draw()
    label2.draw()
def draw_kant(x1,y1,x2,y2, len,color):
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                         ('v2i', (x1, y1, x2, y2)),
                         ('c3B', color*2)
                         )
    label = pyglet.text.Label(f'{len}',
                              font_name='Gill Sans',
                              font_size=10,
                              x=(x1+(x2-x1)/2), y=(y1+(y2-y1)/2),
                              anchor_x='center', anchor_y='center',
                              color=(0,0,255, 255))
    label.draw()
