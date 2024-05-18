import math
import numpy as np


# py game
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
SCREEN_CENTER = [WINDOW_WIDTH/2, WINDOW_HEIGHT/2]
REFRESH_RATE = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# legs
MAX_LEG_LEN = 300
NUM_OF_LEG_PARTS = 3
LEG_PART_LEN = MAX_LEG_LEN / NUM_OF_LEG_PARTS
FIXED_JOINT = [0, 0]

# body
BODY_SIZE = 10
LEG_AMOUNT = 2
MAX_ACC = np.array([1, 1])
MAX_SPEED = np.array([3, 3])


# functions
def angle_from_location(loc1, loc2):
    rad = math.atan2((loc2[1] - loc1[1]), (loc2[0] - loc1[0]))
    deg = math.degrees(rad)
    if deg < 0:
        deg = 360 + deg
    return deg


def angle_to_location(loc1, length, angle):
    rad = angle*math.pi/180
    loc2 = [loc1[0] + length * math.cos(rad), loc1[1] + length * math.sin(rad)]
    return loc2


def angle_between_3_points(a, b, c):
    deg = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return deg + 360 if deg < 0 else deg
