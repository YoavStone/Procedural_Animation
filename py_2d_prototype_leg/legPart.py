import math
from py_2d_prototype_leg.settings import *


class legPart:
    def __init__(self, start_loc, part_len, is_base=False):
        if type(start_loc) is list:
            self.start_loc = start_loc
            self.len = part_len
            self.angle = 0
            self.end_loc = None
            self.calc_end_loc()
            self.is_base = is_base
        else:
            self.len = part_len
            self.start_loc = [0, 0]
            self.is_base = is_base
            self.follow(start_loc.start_loc)

    def part_to_string(self):
        print("pos: ", self.start_loc, " , ", self.end_loc)
        print("len: ", self.len)
        print("angle: ", self.angle*-1)

    def calc_end_loc(self):
        self.end_loc = angle_to_location(self.start_loc, self.len, self.angle)

    def update(self):
        self.calc_end_loc()

    def follow(self, target):
        self.angle = angle_from_location(self.start_loc, target)
        if not self.is_base:
            self.start_loc = angle_to_location(target, self.len, 180 + self.angle)
        self.update()
