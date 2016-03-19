from __future__ import print_function
from __future__ import division
from visual import *
import math

class aabb:
    def __init__(self, objList, relativeCenter, length, width, height ):
        self.id = 'box'

        ## Define Boudnary Planes from box



class bs:           ## Bounding Sphere Class
    def __init__(self, objList):
        pass

class collisionMonitor:
    def __init__ (self, objList):
        self.objList = objList
        self.time = 0

        ## should sort through objectList, caclute, then assign bounding sphere, bound box etc
        ## or a superpostion of bounding structures


    def check(self):
         length = len(self.objList)
         for j in range(0, length):
            objX = self.objList[j]
            for i in range(j+1, length):
                objY = self.objList[i]
                distance = objX.getPosition() - objY.getPosition()
                minDistance = objX.body.radius + objY.body.radius
                if distance.mag <= minDistance:
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

