from __future__ import division
from __future__ import print_function
from random import *
from visual import *


class perceptron:
    def __init__(self, numInputs, lk):
        self.nInputs = numInputs
        self.inputs      = list()
        self.weights     = list()
        self.learningConstant = lk

        for i in range(0, self.nInputs):
            self.weights.append(uniform(-1,1))

    def feedForward(self, forces):
        self.inputs = forces
        self.sum = vector(0,0,0)
        for i in range(0, self.nInputs):
            self.sum += forces[i] * self.weights[i]
        return self.sum



    def train(self, forces, error):
        for i in range(0, len(forces)):
            self.weights[i] = self.learningConstant * error.x * forces[i].x      ## Calculate the change for each input
            self.weights[i] = self.learningConstant * error.y * forces[i].y      ## Calculate the change for each input
            self.weights[i]= self.learningConstant * error.z * forces[i].z      ## Calculate the change for each input



class trainer:
    def __init__(self, m, b):
        self.slope     = m
        self.intercept = b
        self.trainee   = 0
        self.yLine     = 0
        self.answer    = 0

    def giveSolution(self, testPoint):
        xTest = testPoint[0]
        yTest = testPoint[1]
        self.yLine  = self.slope * xTest + self.intercept
        if yTest > self.yLine:
            self.aboveLine = True
            return 1
        else:
            self.aboveLine = -1
            return -1




