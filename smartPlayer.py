from player import *
from fullANN import *

class smartPlayer (player):

    def __init__(self, position, id):
        player.__init__(self, position, id)

        self.training_sets = [
            [[0, 1], [.125]],
            [[-1, 0], [.625]],
            [[0, -1], [.875]],
            [[1, 0], [.375]]
        ]

        self.brain = NeuralNetwork(len(self.training_sets[0][0]), 5, len(self.training_sets[0][1]))

    def train(self):
        for i in range(10000):
            training_inputs, training_outputs = random.choice(self.training_sets)
            self.brain.train(training_inputs, training_outputs)

        print(i, self.brain.calculate_total_error(self.training_sets))


    def chase(self, x, y):
        output = self.brain.feed_forward([x, y])
        return output

