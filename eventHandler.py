from visual import*
from player import*
class eventHandler:

    def __init__(self , envObj):
        self.env          =  envObj
        self.playerManager = envObj.playerMgr
        self.activePlayer = self.playerManager.getActivePlayer()
        self.mode         = 0

        self.env.scene1.bind('keydown', self.handleKeyDown )
        self.env.scene1.bind('keyup'  , self.handleKeyUp   )
        self.env.scene1.bind('click'  , self.handleClick   )

    def handleKeyDown(self, evt ):
        if evt.key == 'left':
            self.leftKeyDown()

        if evt.key == 'right':
            self.rightKeyDown()

        if evt.key == 'up':
            self.upKeyDown()

        if evt.key == 'down':
            self.downKeyDown()

        if evt.key == " ":
            self.spaceKeyDown()

        if evt.key == 's':
            self.sKeyDown()

        if evt.key == 'f':
            self.fKeyDown()

        if evt.key == 'r':
            self.rKeyDown()

        if evt.key == 'p':
            self.pKeyDown()

        if evt.key == '1':
            self.oneKeyDown()

        if evt.key == '2':
            self.twoKeyDown()

        if evt.key == '3':
            self.threeKeyDown()

        if evt.key == 'f1':
            self.f1KeyDown()

    def leftKeyDown(self):

        if self.mode == 1:
            self.activePlayer = self.playerManager.changePlayer(-1)
            return

        initialSpeed = self.activePlayer.getSpeed()
        finalSpeed   = mag(self.activePlayer.getVelocity() + vector(-2,0,0))
        if (self.activePlayer.position.y == 0 and self.env.notPaused and
        (self.activePlayer.getSpeed() < self.activePlayer.maxSpeed or finalSpeed < initialSpeed)):
            self.activePlayer.changeVelocity( (-2,0,0 ) )


    def rightKeyDown(self):

        if self.mode == 1:
            self.activePlayer = self.playerManager.changePlayer(1)
            return

        initialSpeed = self.activePlayer.getSpeed()
        finalSpeed   =  mag(self.activePlayer.getVelocity() + vector(2,0,0))
        if (self.activePlayer.position.y == 0 and self.env.notPaused and
        (self.activePlayer.getSpeed() < self.activePlayer.maxSpeed or finalSpeed < initialSpeed)):
          self.activePlayer.changeVelocity( (2,0,0 ) )



    def upKeyDown(self):

        if self.mode == 1:
            return

        initialSpeed = self.activePlayer.getSpeed()
        finalSpeed   = mag(self.activePlayer.getVelocity() + vector(0,0,-2))
        if (self.activePlayer.position.y == 0 and
        (self.activePlayer.getSpeed() < self.activePlayer.maxSpeed or finalSpeed < initialSpeed)):
            self.activePlayer.changeVelocity( (0,0,-2 ) )

    def downKeyDown(self):

        if self.mode == 1:
            return

        initialSpeed = self.activePlayer.getSpeed()
        finalSpeed   = mag(self.activePlayer.getVelocity() + vector(0,0,2))
        if (self.activePlayer.position.y == 0  and
        (self.activePlayer.getSpeed() < self.activePlayer.maxSpeed or finalSpeed < initialSpeed)):
            self.activePlayer.changeVelocity( (0,0,2 ) )

    def spaceKeyDown(self):


        if self.activePlayer.position.y == 0:
            self.activePlayer = self.playerManager.getActivePlayer()
            self.activePlayer.chargeJump()

    def fKeyDown(self):
        if 'friction' in self.env.activeForcesList:
            self.env.activeForcesList.remove('friction')
            del self.env.activeForcesDict['friction']
            self.playerManager.unsetForce(-1,'friction')
            print('turning Friction off')

        else:
            self.env.activeForcesList.append('friction')
            self.env.activeForcesDict.update({'friction':self.activePlayer.id})
            self.playerManager.setForce(-1,'friction')
            print('turning Friction On')

        print(self.env.activeForcesDict)

    def sKeyDown(self):
#        if self.activePlayer.position.y == 0:
            self.activePlayer.setVelocity(vector(0,0,0))

    def rKeyDown(self):
##       if self.activePlayer.position.y == 0:
            self.activePlayer.setPosition(vector(-5,0,0))

    def pKeyDown(self):
        self.activePlayer.printStats()

    def oneKeyDown(self):
        self.activePlayer = self.env.p1

    def twoKeyDown(self):
        self.activePlayer = self.env.p2
        print('Player 2 is active')

    def threeKeyDown(self):
        self.activePlayer = self.env.p3
        print('Player 3 is active')


    def f1KeyDown(self):
        self.env.notPaused = not(self.env.notPaused)
        self.mode = not(self.mode)
        self.env.pauseCount = 0
        if self.env.notPaused == True:
            self.playerManager.unpause()



    def leftKeyDown_Paused(self):
            id = self.activePlayer.getID()
            self.activePlayer = self.env.activePlayers[ id - 2]
            print('new active player: ', self.activePlayer.getID())
            self.env.playerSelect(self.activePlayer, self.psBox)

    def rightKeyDown_Paused(self):
            id = self.activePlayer.getID()
            self.activePlayer = self.env.activePlayers[ id ]
            print('new active player: ', self.activePlayer.getID())
            self.env.playerSelect(self.activePlayer, self.psBox)
## Key Up Functions ##

    def handleKeyUp(self, evt ):

        if evt.key == " ":
            self.spaceKeyUp()

    def spaceKeyUp(self):
        self.playerManager.jump(self.env)


    def handleClick(self,evt):
        print ('click @', evt.pos)
        self.playerManager.createPlayer_Click(evt.pos, self.env)


           
