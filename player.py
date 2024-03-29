from visual import *
from particle import *
from random import randint

class player(particle):


    def __init__(self, position = 'none', id = 'none'):

        self.dt = .05
        particle.__init__(self, position, id )
        self.playerComponents = []
        self.jumpCharge   = vector(0, 1,  0)
        self.jumpStrength = vector(0, 10, 0)
        self.bottom = -2
        self.rollEnable = True
        self.boundaryList = []
        self.maxSpeed     = 15

    def fullRender(self):
        self.dr = self.velocity * self.dt
        self.position += self.dr
        for component in self.playerComponents:
            component.pos = self.position + component.posRel

    def roll(self):
        if self.rollEnable :
            dthetaX = -self.dr.x / self.body.radius
            dthetaZ =  self.dr.z / self.body.radius
            if dthetaX != 0:
                self.body.rotate(axis=(0,0,1), angle = dthetaX )
            if dthetaZ != 0:
                self.body.rotate(axis=(1,0,0), angle = dthetaZ )

    def chargeJump(self):
        if self.jumpCharge.y < 15:
            self.jumpCharge.y += self.jumpStrength.y/self.jumpCharge.y

    def addComponent(self, shape, relativePosition = 0):
        shape.posRel = relativePosition
        self.playerComponents.append(shape)
        self.body = self.playerComponents[0]
        self.body.pos = self.position + shape.posRel

    def getBottom(self):
        return self.position.y + self.bottom


    def printStats(self):
        print( 'PlayerID: ' , self.id )
        print( ' Position', self.getPosition() )
        print(  'velocity', self.getVelocity() )
        print( 'Player Bottom', self.getBottom() )


    def setTimeResolution(self, newDt):
        self.dt = newDt

    def addBoundingSphere(self, boundingSphere):
        self.boundaryList.append(boundingSphere)

    def getSpeed(self):
        return self.velocity.mag

    def walk(self):
        dv = vector(randint(-3,3), 0, randint(-3,3))
        self.changeVelocity(dv)

    def jump(self):
        jumpCharge = vector(0,randint(5,15),0)
        jumpWindow_lower = 55
        jumpWindow_upper = 65
        jump       = randint(0,100)

        if jumpWindow_lower < jump and jump < jumpWindow_upper:
            self.jumpCharge = jumpCharge
            return jumpCharge.y
        else:
            return 0





