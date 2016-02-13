from __future__ import print_function
from __future__ import division
from visual import *


class flr:

    def __init__(m_, position):
        m_.rect1 = box(length=110, height=.5, width = 50, material = materials.wood)
        m_.rect1.pos = (0, position, 0)
        m_.rect1.opacity = .2
        m_.rect1.pos = (0, position - .25, 0)


    def getFloorTop(m_):
        return m_.rect1.pos.y + m_.rect1.height/2
        print (m_.rect1.pos.y + m_.rect1.height/2)


    def friction(m_, speed):
        speed.x -=  (m_.dt * m_.uFric * speed.norm().x)
        if( mag( vector(speed.x,0,0) ) < m_.restThreshold ):
            speed.x = 0
        speed.z -=  (m_.dt * m_.uFric * speed.norm().z)
        if( mag( vector(speed.z,0,0) ) < m_.restThreshold ):
            speed.z = 0

        return speed
              

class obstacle:

    def __init__(m_, position, ax, h, w ):
        m_.rect1 = box(axis = ax, height = h , width = w, material = materials.bricks)
        m_.rect1.pos = position


    def addBoundingSphere(m_, boundingSphere):
        m_.boundaryList.append(boundingSphere)


    def addBoundingBox(m_, boundingBox):
        m_.boundaryList.append(boundingBox)