from player import *
from perceptron import perceptron


class smartPlayer(player):
    def __init__(self, position, nInputs, id = 'none'):
        player.__init__(self, position, id)

        self.nInputs = nInputs
        self.brain  = perceptron(nInputs,.1)
        self.target = list()
        self.error  = vector(0,0,)

    def chase(self): ##Seek(ArrayList targets)
        desired = vector(self.position - self.target[0])
        desired = norm(desired)*self.maxSpeed
        steer   = vector(desired - self.velocity)
        if steer.mag > self.maxSpeed:
            steer.mag = self.maxSpeed
        return steer

    def steer(self):

            if len(self.target) != 0:
                forces = list()
                for n in range(0, self.nInputs):
                    forces.append(self.chase())
                result = vector(self.brain.feedForward(forces))## Brain calculates 1 new force
                self.setForce(result)
                self.error = vector(self.target[0]- self.position)
                self.brain.train(forces, self.error)
            else:
                print('No target Set')

            ##if( ) steering procedures for other tasks

    def setTarget(self, targetPos):
        self.target.append(targetPos)


    def printStats(self):
        print('PlayerID: ' , self.id )
        print(' Position', self.getPosition() )
        print('velocity', self.getVelocity() )
        print('accelertaion', self.getAcceleration())
        print('Player Bottom', self.getBottom())
        print('weight', self.brain.weights)
        print('error', self.error)