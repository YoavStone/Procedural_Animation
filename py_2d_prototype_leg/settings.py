import math


# py game
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900
REFRESH_RATE = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# legs
MAX_LEG_LEN = 300
NUM_OF_LEG_PARTS = 3
LEG_PART_LEN = MAX_LEG_LEN / NUM_OF_LEG_PARTS
FIXED_JOINT = [WINDOW_WIDTH/2, WINDOW_HEIGHT/2]

# body
BODY_SIZE = 10
LEG_AMOUNT = 2


# functions
def angle_from_location(loc1, loc2):
    rad = math.atan2((loc2[1] - loc1[1]), (loc2[0] - loc1[0]))
    deg = math.degrees(rad)
    if deg < 0:
        deg -= 360
    return deg


def angle_to_location(loc1, length, angle):
    rad = angle*math.pi/180
    loc2 = [loc1[0] + length * math.cos(rad), loc1[1] + length * math.sin(rad)]
    return loc2
