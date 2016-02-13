from visual import *
from particle import *

class player(particle):


    def __init__(m_, position = 'none', id = 'none'):

        m_.dt = .05
        particle.__init__(m_, position, id )
        m_.playerComponents = []
        m_.jumpCharge   = vector(0, 1,  0)
        m_.jumpStrength = vector(0, 10, 0)
        m_.bottom = -2
        m_.rollEnable = True
        m_.boundaryList = []
        m_.maxSpeed     = 15

    def fullRender(m_):
        m_.dr = m_.velocity * m_.dt
        m_.position += m_.dr
        for component in m_.playerComponents:
            component.pos = m_.position + component.posRel

    def roll(m_):
        if m_.rollEnable :
            dthetaX = -m_.dr.x / m_.body.radius
            dthetaZ =  m_.dr.z / m_.body.radius
            if dthetaX != 0:
                m_.body.rotate(axis=(0,0,1), angle = dthetaX )
            if dthetaZ != 0:
                m_.body.rotate(axis=(1,0,0), angle = dthetaZ )

    def chargeJump(m_):
        if m_.jumpCharge.y < 15:
            m_.jumpCharge.y += m_.jumpStrength.y/m_.jumpCharge.y

    def addComponent(m_, shape, relativePosition = 0):
        shape.posRel = relativePosition
        m_.playerComponents.append(shape)
        m_.body = m_.playerComponents[0]
        m_.body.pos = m_.position + shape.posRel

    def getBottom(m_):
        return m_.position.y + m_.bottom


    def printStats(m_):
        print( 'PlayerID: ' , m_.id )
        print( ' Position', m_.getPosition() )
        print(  'velocity', m_.getVelocity() )
        print( 'Player Bottom', m_.getBottom() )


    def setTimeResolution(m_, newDt):
        m_.dt = newDt

    def addBoundingSphere(m_, boundingSphere):
        m_.boundaryList.append(boundingSphere)\

    def getSpeed(m_):
        return m_.velocity.mag