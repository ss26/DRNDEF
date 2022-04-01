# This is for Stanley
from collections import namedtuple
from scene.config.infer.is10_all_t6 import ADD_PROPS
import carla
import sys
import numpy as np

sys.path.append('../../../')

SCENE_NAME = "s3_all_t3"
TOWN = 'Town03_opt'


TRAFFIC = False
SCENE_NUMBER = 2
#####
FILTER_VEHICLES = True
USE_RL = True
PLOT = False
#####

# x = 227, 580,   np.linspace(227, 580, 20)
# y = 240, 250, 2 np.linspace(240, 250, 5)
# theta = 0, 10, 20, ... np.linspace(0, 350, 36)

X_RANGE = np.linspace(0, 80, 641) # Difference is exactly 0.125
Y_RANGE = np.linspace(-3, 3, 5)
TH_RANGE = None

# EGOLOC = carla.Transform(carla.Location(x=300.002968, y=125.089096, z=1.001809),
#                          carla.Rotation(pitch=-0.016358, yaw=720.0, roll=0.000000))
EGOLOC = carla.Transform(carla.Location(x=210.187241, y=7.577184, z=0.542399), carla.Rotation(pitch=0.004583, yaw=-179.265320, roll=0.000000)) 

TR_LOC = []
S = [2.5] * len(TR_LOC)

TR_VEL = []
for s in S:
    TR_VEL.append(carla.Vector3D(s, 0, 0))

assert len(TR_VEL) == len(TR_LOC), 'Different Vel and Pos shapes!'

EGO_VEL = carla.Vector3D(-1.2, 0, 0)

LAYERS = [
    # carla.MapLayer.Walls,
    # carla.MapLayer.StreetLights,
    # carla.MapLayer.Props,
    # carla.MapLayer.Foliage,
    # carla.MapLayer.Buildings,
    # carla.MapLayer.ParkedVehicles
]


LIDAR_RANGES_LIST = [55, 50, 45]

######
LIDAR_RANGE = LIDAR_RANGES_LIST[2]
######

FPS = 10
LANE_L = 6
LANE_R = 0.5
ROAD_WIDTH = LANE_L + LANE_R
RUN_LENGTH = 100

ADD_PROPS = False

# Not being used
def cons_vel(traffic):
    for itr, vehicle in enumerate(traffic):
        # vehicle.set_target_velocity(TR_VEL[itr])
        vehicle.enable_constant_velocity(TR_VEL[itr])


def traffic_runner(traffic):
    for itr, vehicle in enumerate(traffic):
        vehicle.set_target_velocity(TR_VEL[itr])
        # vehicle.enable_constant_velocity(TR_VEL[itr])


FILTER_PCD_CLASSES = [
    # Reference: https://carla.readthedocs.io/en/0.9.11/ref_sensors/
   
    # # 10, # Vehicles
   
    # # The following set collectively represents ground
    # 22,  # Terrain
    # 14,   # Ground
    # 6,  # Road Line
    # 7,    # Road
    # 8,  # Side Walk

    # 0,  # Unlabelled
    # 3,  # Other

    # 11,   # Wall
    # # 17,   # Ground Rail
    # # # 1,  # Building
    # # 9, # Vegetation

]
