from visual import *


class particle:
    
    def __init__(m_, position ,id):
        m_.id           = id

        m_.time         = 0 
        m_.dt           = .01
        m_.mass         = 0
        m_.dr           = vector(0,  0, 0)

        m_.position     = position             ## Location of player center
        m_.velocity     = vector(0,0,0)
        m_.acceleration = vector(0,0,0)
        m_.tolerance    = .001
        m_.restThreshold    = .001

        m_.momentum     = vector(0,0,0)
        m_.netForce     = vector(0,0,0)
        m_.energy       = 0
 
        m_.body         = vector(0,0,0)                    ## any simple shape

    def getPosition(m_):
        return m_.position

    def updatePosition(m_):                   
        m_.dr = m_.velocity * m_.dt
        m_.position += m_.dr
        m_.body.pos = m_.position   

    def changePosition(m_, dr):
            m_.position += dr
            m_.updatePosition()
            
    def setPosition(m_, newPosition):
        m_.position = newPosition
    
    def getVelocity(m_):       
        return m_.velocity

    def updateVelocity(m_, limited = 'True'):
        vel = m_.velocity
        m_.velocity += m_.acceleration * m_.dt
        if(limited):
            m_.velocity = vel


    def changeVelocity(m_, dv, limited = 'True'):
        vel = m_.velocity
        m_.velocity += dv
        if(limited):
            m_.velocity = vel


    def setVelocity(m_, newVelocity):
        m_.velocity = newVelocity

    def getAcceleration(m_):
        return m_.acceleration

    def setAcceleration(m_, newAcceleration):
        m_.acceleration = newAcceleration

    def changeAcceleration(m_, newAcceleration):
        m_.acceleration += newAcceleration

    def getForce(m_):
        return m_.netForce

    def changeForce(m_, newForce):
        m_.netForce += newForce

    def setForce(m_, newForce, limit = 'True'):

        force = m_.netForce
        m_.netForce += newForce
        if limit:
            m_.netForce = m_.netForce

        m_.setAcceleration(newForce/m_.mass)

    def getEnergy(m_):
        m_.energy = .5*m_.mass*m_.velocity.mag2
        return  m_.energy

    def calcMomentum(m_):
        m_.momentum = m_.mass * m_.velocity

    def getMomentum(m_):
        return m_.momentum

    def getID(m_):
        return m_.id

    def age(m_):
        m_.time += m_.dt

    def getAge(m_):
        return m_.time

