from visual import*
from player import*
class eventHandler:


    def __init__(m_ , envObj):
        m_.env      =  envObj
        m_.activePlayer = envObj.p1

        m_.env.scene1.bind('keydown'      , m_.handleKeyDown )
        m_.env.scene1.bind('keyup'        , m_.handleKeyUp   )
        m_.env.scene1.bind('click'        , m_.handleClick   )

    def handleKeyDown(m_, evt ):
        if evt.key == 'left':
            m_.leftKeyDown()
            

        if evt.key == 'right':
            m_.rightKeyDown()        

        if evt.key == 'up':
            m_.upKeyDown()

        if evt.key == 'down':
            m_.downKeyDown()

        if evt.key == " ":
            m_.spaceKeyDown()
            
        if evt.key == 's':
            m_.sKeyDown()

        if evt.key == 'f':
            m_.fKeyDown()

        if evt.key == 'r':
            m_.rKeyDown()

        if evt.key == 'p':
            m_.pKeyDown()

        if evt.key == '1':
            m_.oneKeyDown()

        if evt.key == '2':
            m_.twoKeyDown()

        if evt.key == '3':
            m_.threeKeyDown()

        if evt.key == 'f1':
            m_.f1KeyDown()

 ##           for f in range (0, len(m_.env.activeForces)):
 ##                   print(m_.env.activeForces[f])
                        


    def leftKeyDown(m_):
        if m_.activePlayer.position.y == 0 and m_.env.notPaused:
            m_.activePlayer.changeVelocity( (-2,0,0 ) )
        elif m_.activePlayer.getID() > 1:
            m_.leftKeyDown_Paused()


    def rightKeyDown(m_):
        if m_.activePlayer.position.y == 0 and m_.env.notPaused:
          m_.activePlayer.changeVelocity( (2,0,0 ) )
        elif m_.activePlayer.getID() < len(m_.env.activePlayers):
            m_.rightKeyDown_Paused()

    def upKeyDown(m_):
       if m_.activePlayer.position.y == 0:
            m_.activePlayer.changeVelocity( (0,0,-2 ) )

    def downKeyDown(m_):
       if m_.activePlayer.position.y == 0:
            m_.activePlayer.changeVelocity( (0,0,2 ) )

    def spaceKeyDown(m_):
        if m_.activePlayer.position.y == 0:
            m_.activePlayer.chargeJump()


    def fKeyDown(m_):
        if 'friction' in m_.env.activeForcesList:
            m_.env.activeForcesList.remove('friction')
            del m_.env.activeForcesDict['friction']
        else:
            m_.env.activeForcesList.append('friction')
            m_.env.activeForcesDict.update({'friction':m_.activePlayer.id})
            print('turning Friction On')

        print(m_.env.activeForcesDict)
        
    def sKeyDown(m_):
#        if m_.activePlayer.position.y == 0:
            m_.activePlayer.setVelocity(vector(0,0,0))

    def rKeyDown(m_):
##       if m_.activePlayer.position.y == 0:
            m_.activePlayer.setPosition(vector(-5,0,0))

    def pKeyDown(m_):
        m_.activePlayer.printStats()

    def oneKeyDown(m_):
        m_.activePlayer = m_.env.p1

        
    def twoKeyDown(m_):
        m_.activePlayer = m_.env.p2
        print('Player 2 is active')

    def threeKeyDown(m_):
        m_.activePlayer = m_.env.p3
        print('Player 3 is active')


    def f1KeyDown(m_):

        m_.env.pauseCount = 0
        if m_.env.notPaused:                    ## Meaning its paused

            m_.env.notPaused = False
            m_.psBox = box(pos = m_.activePlayer.getPosition(),length = 6, height = 6, width = 6)
            m_.psBox.pos.y = -6
            m_.psBox.opacity = .1
            m_.psBox.color = color.red
            m_.env.playerSelect(m_.activePlayer, m_.psBox)
        else:

            m_.env.notPaused = True
            m_.psBox.length  = 0
            m_.psBox.width   = 0
            m_.psBox.height  = 0
            m_.psBox.visble = False
            del m_.psBox



    def leftKeyDown_Paused(m_):
            id = m_.activePlayer.getID()
            m_.activePlayer = m_.env.activePlayers[ id - 2]
            print('new active player: ', m_.activePlayer.getID())
            m_.env.playerSelect(m_.activePlayer, m_.psBox)


    def rightKeyDown_Paused(m_):
            id = m_.activePlayer.getID()
            m_.activePlayer = m_.env.activePlayers[ id ]
            print('new active player: ', m_.activePlayer.getID())
            m_.env.playerSelect(m_.activePlayer, m_.psBox)





## Key Up Functions ##

        
    def handleKeyUp(m_, evt ):

        if evt.key == " ":
            m_.spaceKeyUp()


    def spaceKeyUp(m_):
        if m_.activePlayer.position.y == 0:
            m_.activePlayer.changeVelocity(m_.activePlayer.jumpCharge)
            m_.activePlayer.setAcceleration(vector(0,-9.81,0))
            m_.env.activeForcesList.append('floor')
            m_.env.activeForcesDict.update({'floor':m_.activePlayer.id})
        



    def handleClick(m_,evt):
        print ('click @', evt.pos)
        m_.env.createPlayer(evt.pos)


           
