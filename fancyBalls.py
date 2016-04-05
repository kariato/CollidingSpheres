from visual import *
from player import *
from particle import *

class fancyBall(player):

    def __init__(m_, position = 'none', id = 'none'):
        player.__init__(m_,position,id)
        m_.width = 10 # of wood table
        m_.thick = 0.5 # thickness of wood
        m_.depth = 7 # of wood table
        m_.height = 2 # of side bars of table
        m_.xhit = m_.height-m_.thick # x distance of center of ball from side bar when it hits
        m_.R = 2 # radius of ball
        m_.H = 10 # height of underside of ceiling above floor
        m_.L = 5 # length of pendulum to center of hanging lamp


        m_.bands = zeros([16,16,4], float)
        for i in range(len(m_.bands)):
            for j in range(len(m_.bands[0])):
                op = 1
                if i % 2 == 0: # every other band is partially transparent
                    op = 0.3
                    col = color.cyan
                else:
                    # choose a color for an opaque band of the beach ball:
                    col = [color.blue, color.green, color.red,
                           color.yellow, color.cyan][i//2 % 5]
                m_.bands[i][j] = (col[0], col[1], col[2], op)
        stripes = materials.texture(data = m_.bands,
                               mapping = "spherical",
                           interpolate = False)



        m_.addComponent(sphere(pos=(m_.width/4,m_.R,0), radius=m_.R, up=(0,1,1), material=stripes),vector(0,-6,0) )