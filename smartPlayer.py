from player import *
from fullANN import *

class smartPlayer (player):

    def __init__(self, position, id):
        player.__init__(self, position, id)
        self.brain = neuralNetwork()


