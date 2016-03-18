from __future__ import print_function
from __future__ import division
from visual import *
from eventHandler import *
from player import *
from eventHandler import *
from collision import *
from math import *
from CourseObjects import *
from fancyBalls import *
from playerManager import*
import threading
import time

class enviornment:

    def __init__(m_):
        pass

        m_.rate       = 200
        m_.globalTime = 0
        m_.globalDt   = 10/m_.rate

        m_.notPaused = True
        m_.pauseCount = 0
        m_.activeForcesDict    = dict()
        m_.activeForcesList    = list()
        m_.forceFuncDict       = {'floor':m_.floor, 'friction':m_.friction}

        m_.centerOfMass        = vector()
        m_.playerMgr           = playerManager()


        m_.scene1 = display(x=0, y=0, width=1200, height = 600)
        m_.scene1.autoscale = False
        m_.scene1.title = 'SphereLand Lab Frame'
        m_.scene1.range = (30,10,5)
        m_.playerMgr.scene( m_.scene1)
        m_.uFric = .05

        m_.Walker0 = m_.playerMgr.createPlayer(vector(-10, 0,  0))
        m_.Walker1 = m_.playerMgr.createPlayer(vector(5, 0,  0))
        m_.Walker2 = m_.playerMgr.createPlayer(vector(5, 0,  5))
        m_.playerMgr.setPlayerBottom(-8)


        m_.playerMgr.setAsWalker(m_.Walker0)
        m_.playerMgr.setAsWalker(m_.Walker1)
        m_.playerMgr.setAsWalker(m_.Walker2)




## Other Player Attributes
        m_.playerMgr.buildPlayers(sphere(radius = 2, color = (.996,.616,.016) ), vector(0,-6,0), materials.wood, 0)
        m_.playerMgr.buildPlayers(sphere(radius = 2, color = color.blue ), vector(0,-6,0), materials.wood, 1)
        m_.playerMgr.buildPlayers(sphere(radius = 2, color = color.green ), vector(0,-6,0), materials.wood, 2)
        m_.playerMgr.setPlayerMass(20)



## Other Player Attributes

        m_.floor1    = flr(m_.playerMgr.getPlayerBottom(0))
        print(m_.floor1.getFloorTop())
        m_.frontWall = obstacle((0,     -6.75, -23)  ,(110, 0,  0),2.5, 3)
        m_.backWall = obstacle ((0,     -6.75,  23)  ,(110, 0,  0),2.5, 3)
        m_.leftWall = obstacle ((-53.5, -6.75,    0) ,(0,   0, 44),2.5, 3)
        m_.rightWall = obstacle((53.5,  -6.75,     0),(0,   0, 44),2.5, 3)

        m_.collisionTest1 = collisionMonitor( m_.playerMgr.activePlayers )

        m_.randomWalk = randomWalk(1,m_, m_.playerMgr,.5)

    def run(m_):

        m_.randomWalk.start()
        while True:
            rate(m_.rate)
            while m_.notPaused:
                rate(m_.rate)
                m_.playerMgr.updatePlayers()
                m_.playerMgr.applyForces(m_)
                m_.collisionTest1.check()
                m_.walls()


            if m_.pauseCount == 0:
                print('Paused')
                print('Active Forces List: ', m_.activeForcesList)
                print('Active Forces Dict: ', m_.activeForcesDict)
                m_.pauseCount = 1
                m_.playerMgr.playerSelect()

    def floor(m_, player):

                if 'floor' in m_.activeForcesList:
                    if player.getPosition().y < .05:
                        player.velocity.y = 0
                        player.setAcceleration( vector(0,0,0) )
                        player.position.y = 0
                        player.jumpCharge = vector(0,1,0)
                        m_.activeForcesList.remove('floor')

#                        del m_.activeForcesDict['floor']
                        m_.playerMgr.unsetForce(player.getID(),'floor')
                        return

    def friction(m_, player):
        if player.position.y == 0:            ## Only frictino on floor
            player.velocity.x -=  (m_.globalDt * m_.uFric * player.velocity.norm().x)
            if mag(vector(player.velocity.x, 0, 0)) < player.restThreshold:
                player.velocity.x = 0
            player.velocity.z -=  (m_.globalDt * m_.uFric * player.velocity.norm().z)
            if mag(vector(player.velocity.z, 0, 0)) < player.restThreshold:
                player.velocity.z = 0

    def walls(m_):
        for player in m_.playerMgr.activePlayers:
            if player.getPosition().x <= -50 or player.getPosition().x >= 50:
                vx = player.getVelocity().x
                player.changeVelocity(vector(-2*vx,0,0 ))

            if player.getPosition().z <= -20 or player.getPosition().z >= 20:
                vz = player.getVelocity().z
                player.changeVelocity(vector(0,0,-2*vz))

    def addForce(m_, newForce , newPlayerID ):
        m_.activeForcesList.append(newForce)
        m_.activeForcesDict.update({newForce: newPlayerID})

class randomWalk (threading.Thread):
    def __init__(self, threadID, envObj, manager, sleep):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.SLEEP = sleep
        self.manager = manager
        self.envObj = envObj

    def run(self):
        while true:
            for walker in self.manager.listOfWalkers:
                walker.walk()
                y = walker.jump()
                if y != 0:
                    print(walker.getID(), ' is jumping :', y)
                    self.manager.jump(self.envObj, walker)
            time.sleep(self.SLEEP)


############################### Main Program #############################################
env1 = enviornment()
env1.handler = eventHandler(env1)
env1.run()
############################### Main program #############################################


