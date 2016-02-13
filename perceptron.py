from __future__ import division
from __future__ import print_function
from random import *
from visual import *


class perceptron:
    def __init__(self, numInputs, lk):
        self.nInputs = numInputs
        self.inputs      = list()
        self.weights     = list()
        self.biasWeight  = 0
        self.output      = 0
        self.guess       = 0
        self.sum         = 0
        self.learningConstant = lk

        for i in range(0, self.nInputs):
            self.weights.append(uniform(-1,1))

    def feedForward(self, inputs):
        self.inputs = inputs
        self.sum = vector(0,0,0)
        for i in range(0, self.nInputs):
            self.sum.x += inputs[i].x * self.weights[i]
            self.sum.y += inputs[i].y * self.weights[i]
            self.sum.z += inputs[i].z * self.weights[i]
        return self.sum

    def activate(self):
        if self.sum > 0:
            self.guess = 1
            return 1
        else:
            self.guess = -1
            return -1

    def train(self, forces, error):
        for i in range(0, len(forces)):
            deltax = self.learningConstant * error.x * forces[i].x      ## Calculate the change for each input
            deltay = self.learningConstant * error.y * forces[i].y      ## Calculate the change for each input
            deltaz = self.learningConstant * error.z * forces[i].z      ## Calculate the change for each input
            delta  = (deltax + deltay + deltaz)
            self.weights[i] += delta

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




