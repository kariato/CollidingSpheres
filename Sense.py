from __future__ import division
from collision import *
from visual import *
import numpy as np


class sense:

    def __init__(self, player_id ,current_position, scope):
        self.scope = scope
        self.current_position = current_position
        self.scope_boundary = aabb(player_id, scope, current_position)
        self.dt = 1
        self.net = self.formNet(scope)


        #self.NET_KEY = CollisionMonitor.addSet(self.net)

    def formNet(self, scope):

        net = list()
        # This is a guess for now, V_MIN can be smaller as a result of collisions
        V_MIN = 1
        mesh_unit_size = V_MIN * self.dt
        # mesh_dim refers to the dimensions of a single quadrant or octant
        mesh_dim_x = floor(self.scope[0]/mesh_unit_size)
        mesh_dim_y = floor(self.scope[1]/mesh_unit_size)
        mesh_dim_z = floor(self.scope[2]/mesh_unit_size)
        # setting mesh_dim_y to 1 will effectively ignore vertical attacks but will reduce computation
        mesh_dim_y = 1
        quadrant_octant_factor = 4 # Set to 4 for Quadrant, 8 for octant
        # mesh_size will be the number of elements the "detected" numpy array fed to brain
        mesh_size = quadrant_octant_factor*mesh_dim_x * mesh_dim_y * mesh_dim_z
        mesh_center = self.current_position


        mesh_front_left_x  = mesh_center.x - (mesh_dim_x - 1/2)*mesh_unit_size
        mesh_front_left_y  = mesh_center.y
        mesh_front_left_z  = mesh_center.z - (mesh_dim_z - 1/2)*mesh_unit_size
        mesh_front_left_id = self.scope_boundary.id + 1
        mesh_front_left_position = vector(mesh_front_left_x, mesh_front_left_y , mesh_front_left_z)
        u = mesh_unit_size

        mesh_front_left = aabb(mesh_front_left_id, (u, u, u), mesh_front_left_position)
        sphere(pos = mesh_front_left_position, radius = u, color = color.red)

        # Populate mesh with bounding boxes
        # for x in range():
        #     for z in range():
        net.append(aabb(mesh_front_left_id, (u, u, u), mesh_front_left_position))


        print('mesh_size', mesh_size)



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
