from player import *
from perceptron import perceptron


class smartPlayer(player):
    def __init__(self, position, nInputs, id = 'none'):
        player.__init__(self, position, id)

        self.brain = perceptron(3,.001)


