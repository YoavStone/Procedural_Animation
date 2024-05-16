import math
from py_2d_prototype_leg.settings import *


class legPart:
    def __init__(self, start_loc, end_loc):
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.len = math.dist(self.start_loc, self.end_loc)
        self.angle = angle(self.start_loc, self.end_loc)

    def part_to_string(self):
        print("pos: ", self.start_loc, " , ", self.end_loc)
        print("len: ", self.len)
        print("angle: ", self.angle)
