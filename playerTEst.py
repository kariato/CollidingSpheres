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
#
#
#
# ## Known Bugs, if more than 1 player jumps the first jumper will fall through the floor because, the player 1 id is
# ## removed from association with key value
# ## consider making id value a list of ids and restructure forces
#
#
#
# ################################### Create Course ################################
#
#
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
        m_.activePlayers       = list()
        m_.centerOfMass        = vector()


        m_.scene1 = display(x=0, y=0, width=1200, height = 600)
        m_.scene1.autoscale = False
        m_.scene1.title = 'SphereLand Lab Frame'
        m_.scene1.range = (30,10,5)

        m_.uFric = .5

        m_.p1 = player   (vector(-10, 0,  0), 1)
        m_.p2 = player   (vector(  0, 0, -3), 2)
        m_.p3 = player   (vector(  7, 0, .2), 3)
        m_.p4 = fancyBall(vector(  0, 0,  3), 4)

        m_.p1.mass = 80
        m_.p2.mass = 40
        m_.p3.mass = 25
        m_.p4.mass = 40

## Other Player Attributes
## make_trail = True, trail_type = 'points', interval = 20, retain = 400

        m_.p1.addComponent(sphere(radius = 2, color = color.red ), vector(0,-6,0))
        m_.p1.body.material = materials.wood
        m_.p1.bottom = -8


        m_.activePlayers.append(m_.p1)

        m_.p2.addComponent(sphere(radius = 2, color = color.red),vector(0,-6,0))
        m_.p2.body.color = color.green
        m_.p2.body.material = materials.marble
        m_.p2.bottom = 2
        m_.activePlayers.append(m_.p2)

        m_.p3.addComponent(sphere(radius = 2, color = color.orange),vector(0,-6,0))
        m_.p3.body.color = color.orange
        m_.p3.body.material = materials.marble
        m_.p3.bottom = 4
        m_.activePlayers.append(m_.p3)

        m_.activePlayers.append(m_.p4)
## Other Player Attributes

        m_.floor1    = flr(m_.p1.bottom)
        print(m_.floor1.getFloorTop())
        m_.frontWall = obstacle((0,     -6.75, -23),(110, 0,  0),2.5, 3)
        m_.backWall = obstacle ((0,     -6.75,  23),(110, 0,  0),2.5, 3)
        m_.leftWall = obstacle ((-53.5, -6.75,    0),(0,   0, 44),2.5, 3)
        m_.rightWall = obstacle((53.5,  -6.75,     0),(0,   0, 44),2.5, 3)


        m_.collisionTest1 = collisionMonitor( m_.activePlayers )


    def run(m_):

        while True:
            rate(m_.rate)
            while m_.notPaused:
                rate(m_.rate)

                for player in m_.activePlayers:
                    player.fullRender()
                    player.updateVelocity()
                    player.roll()                   ## Assumes player is a sphere, need to add player flag 'rollEnabled'

                if len(m_.activeForcesList) != 0:    ##Call all active Forces
                    for f in range (0, len(m_.activeForcesList)):
                        getattr(m_, m_.activeForcesList[f])()

                m_.collisionTest1.check()
                m_.walls()

            if m_.pauseCount == 0:
                print('Paused')
                print('Active Forces List: ', m_.activeForcesList)
                print('Active Forces Dict: ', m_.activeForcesDict)
                m_.pauseCount = 1


    def floor(m_):
        if 'floor' in m_.activeForcesList:
            for player in m_.activePlayers:
                if player.id == m_.activeForcesDict['floor']:
                    if player.getPosition().y < .05:
                        player.velocity.y = 0
                        player.setAcceleration( vector(0,0,0) )
                        player.position.y = 0
                        player.jumpCharge = vector(0,1,0)
                        m_.activeForcesList.remove('floor')
                        del m_.activeForcesDict['floor']
                        return

    def friction(m_):
        for player in m_.activePlayers:
            if player.position.y == 0:            ## Only frictino on floor
                player.velocity.x -=  (m_.globalDt * m_.uFric * player.velocity.norm().x)
                if mag(vector(player.velocity.x, 0, 0)) < player.restThreshold:
                    player.velocity.x = 0
                player.velocity.z -=  (m_.globalDt * m_.uFric * player.velocity.norm().z)
                if mag(vector(player.velocity.z, 0, 0)) < player.restThreshold:
                    player.velocity.z = 0

    def walls(m_):
        for player in m_.activePlayers:
            if player.getPosition().x <= -50 or player.getPosition().x >= 50:
                vx = player.getVelocity().x
                player.changeVelocity(vector(-2*vx,0,0 ))

            if player.getPosition().z <= -20 or player.getPosition().z >= 20:
                vz = player.getVelocity().z
                player.changeVelocity(vector(0,0,-2*vz))

    def createPlayer(m_, position):

        newPlayerPosition   = vector()
        newPlayerPosition   = position
##        newPlayerPosition.y = 0


        if newPlayerPosition.x < -50:
            newPlayerPosition.x = -50
        if newPlayerPosition.x > 50:
            newPlayerPosition.x = 50

        if newPlayerPosition.z < -19:
            newPlayerPosition.z = -19
        if newPlayerPosition.z > 19:
            newPlayerPosition.z = 19

        newPlayer = player   ( newPlayerPosition, len(m_.activePlayers) + 1)
        newPlayer.updatePosition()
        newPlayer.setAcceleration(vector(0,-9.81,0))
        m_.activeForcesList.append('floor')
        m_.activeForcesDict.update({'floor':newPlayer.getID()})


        id = newPlayer.getID()      ## Use PlayerID to generate a new color
        colorID = id  - 3              ## StartGenerating colors from ID 1

        newColor   =  [int(x) for x in bin(colorID)[2:]]

        if( len(newColor) <= 3):
            while len(newColor) < 3:
                newColor.append(0)

            print(newColor)
            newPlayer.mass = 80
            newPlayer.addComponent(sphere(radius = 2, color = newColor ), vector(0,-6,0))
            m_.activePlayers.append(newPlayer)
            m_.rollEnable = False


    def playerSelect(m_, player, psBox ):

        n_steps = 20
        psBox.pos = player.getPosition()
        psBox.pos.y -= 6
        psBox.opacity = .2
        psBox.color = color.red

        m_.scene1.center = psBox.pos

        # center_begin = vector()
        # center_end   = vector()

        # center_begin = m_.scene1.center
        # center_end   = psBox.pos
        # scroll_Increment = (center_end - center_begin)/n_steps

        # while m_.scene1.center != center_end:
        #     rate (20)
        #     m_.scene1.center += scroll_Increment

############################### Main Program #############################################
env1 = enviornment()
env1.handler = eventHandler(env1)
env1.run()
############################### Main program #############################################


