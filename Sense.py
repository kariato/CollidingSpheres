from __future__ import division
from collision import *
from visual import floor
import numpy as np


class sense:

    def __init__(self, player_id ,current_position, scope):
        self.scope = scope
        self.scope_boundary = aabb(player_id, scope, current_position)
        #self.net = self.formNet(scope)
        #self.NET_KEY = CollisionMonitor.addSet(self.net)
        self.dt  = 1

    def formNet(self, scope):
        # This is a guess for now, V_MIN can be smaller as a result of collisions
        V_MIN = 1
        mesh_unit_size = V_MIN * self.dt
        mesh_dim_x = floor(self.scope[0]/mesh_unit_size)
        mesh_dim_y = floor(self.scope[1]/mesh_unit_size)
        mesh_dim_z = floor(self.scope[2]/mesh_unit_size)
        # setting mesh_dim_y to 1 will effectively ignore vertical attacks but will reduce computation
        mesh_dim_y = 1
        # mesh_size will be the total length of list returned as "detected"
        mesh_size = mesh_dim_x * mesh_dim_y * mesh_dim_z
        detected = np.zeros(1,mesh_size)


    def look(self, current_position):

            threat_count = self.scope_boundary.check_for_players_in_scope(current_position)

            if threat_count == 0:
                print('No threats detected')

            ## if threats detected we will need to check all bounding boxes
            elif threat_count > 0:

                print('Threats Detected')
                detected = 0
                # detected = some function I havent made yet thre returns a NumpyArray
                return detected
