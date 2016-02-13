from __future__ import print_function
from __future__ import division
from visual import *
import math

class aabb:
    def __init__(m_, objList, relativeCenter, length, width, height ):
        m_.id = 'box'

        ## Define Boudnary Planes from box



class bs:           ## Bounding Sphere Class
    def __init__(m_, objList):
        pass

class collisionMonitor:
    def __init__ (m_, objList):
        m_.objList = objList
        m_.time = 0

        ## should sort through objectList, caclute, then assign bounding sphere, bound box etc
        ## or a superpostion of bounding structures


    def check(m_):
         length = len(m_.objList)
         for j in range(0, length):
            objX = m_.objList[j]
            for i in range(j+1, length):
                objY = m_.objList[i]
                distance = objX.getPosition() - objY.getPosition()
                minDistance = objX.body.radius + objY.body.radius
                if distance.mag <= minDistance:
                    m_.handleCollision(objX, objY)

    def handleCollision(m_,objX, objY):
        
        scale            = 5
        vPlaneOffset     = vector(0,3,0)
        rNorm_vec        = vector()
        r1Norm_vec       = vector()
        r2Norm_vec       = vector()
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

        rNorm_vec        = r1Norm - r2Norm
        vRel_vec         = u1_vec - u2_vec

        v1_vec           = u1_vec - 2*(u/m1)*vRel_vec.proj(rNorm_vec)
        v2_vec           = u2_vec + 2*(u/m2)*vRel_vec.proj(rNorm_vec)

        objX.setVelocity(v1_vec)
        objY.setVelocity(v2_vec)

