from __future__ import print_function
from __future__ import division
from visual import *
import math

class aabb:

    playerManager = 0
    def __init__(self, id, scope, pos_Rel_Center = vector(0,0,0) ):

        self.type = 'aabb'
        if id >= 0:
            self.id = id
        else:
            return
        length = scope[0]
        width  = scope[1]
        height = scope[2]
        self.location = vector(pos_Rel_Center)
        self.Upper = self.location + .5*vector(length, width, height)
        self.Lower = self.location - .5*vector(length, width, height)

    def contains(self, incoming):


        print('Checking to see if: ', incoming, ' is between ', self.Upper, ' and ', self.Lower)
        Upper_x = self.Upper.x
        Upper_y = self.Upper.y
        Upper_z = self.Upper.z

        Lower_x = self.Lower.x
        Lower_y = self.Lower.y
        Lower_z = self.Lower.z

        x = incoming.x
        y = incoming.y
        z = incoming.z

        if Lower_x < x and  x < Upper_x and Lower_y < y and  y < Upper_y and Lower_z < z and  z < Upper_z:
            return 1
        else:
            return 0

    def registerManager(self, mgr):
        playerManager = mgr





        ## Define Boudnary Planes from box


# Bounding Sphere Class
class bs:
    def __init__(self, interactingSets):
        pass

class CollisionMonitor:
    def __init__ (self):
        self.interactingSets = dict()
        self.time = 0

        # should sort through objectList, caclute, then assign bounding sphere, bound box etc
        # or a superpostion of bounding structures

    def check_player_player_collision(self, setID):
        if len(self.interactingSets) == 0:
            print("Add interacting Set with 'addSet'")
            return

        test_set = self.interactingSets[setID]
        length = len(test_set)
        for j in range(0, length):
            objX = test_set[j]
            for i in range(j+1, length):
                objY = test_set[i]
                distance = objX.getPosition() - objY.getPosition()
                min_distance = objX.body.radius + objY.body.radius
                if distance.mag <= min_distance:
                    self.handleCollision(objX, objY)

    def handleCollision(self,objX, objY):
        
        scale            = 5
        vPlaneOffset     = vector(0,3,0)
        rNorselfvec        = vector()
        r1Norselfvec       = vector()
        r2Norselfvec       = vector()
        vRel_vec         = vector()
        u1_vec           = vector()
        u2_vec           = vector()
        v1_vec           = vector()
        v2_vec           = vector()

        m1               = objX.mass
        m2               = objY.mass
        r1Norm           = objX.position
        r2Norm           = objY.position
        u1_vec           = objX.velocity
        u2_vec           = objY.velocity

        u                = m1*m2/(m1+m2)

        rNorselfvec        = r1Norm - r2Norm
        vRel_vec         = u1_vec - u2_vec

        v1_vec           = u1_vec - 2*(u/m1)*vRel_vec.proj(rNorselfvec)
        v2_vec           = u2_vec + 2*(u/m2)*vRel_vec.proj(rNorselfvec)

        objX.setVelocity(v1_vec)
        objY.setVelocity(v2_vec)


    def addSet(self, newSet):
        newKey = len(self.interactingSets) + 1
        self.interactingSets.update({newKey: newSet})
        return newKey
