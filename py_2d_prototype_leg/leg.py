import math
import pygame
from py_2d_prototype_leg.settings import *
from py_2d_prototype_leg.legPart import *


class leg:
    def __init__(self, parts_list, is_right):
        self.parts_list = parts_list
        self.is_right = is_right
        len = 0
        self.part_amount = 0
        for p in parts_list:
            len += p.len
            self.part_amount += 1
        self.max_len = len
        self.start_leg = self.parts_list[0].start_loc  # problem if no parts
        self.paw = self.parts_list[self.part_amount-1].end_loc  # problem if no parts
        self.start_to_end_len = math.dist(self.start_leg, self.paw)
        self.paw_stand_pos = self.paw

    def leg_to_string(self):
        for part in self.parts_list:
            print("---")
            part.part_to_string()
        print("------------")
        if self.is_right:
            print("leg is right leg")
        else:
            print("leg is left leg")
        print("part amount: ", self.part_amount)
        print("max leg len: ", self.max_len)
        print("start leg: ", self.start_leg)
        print("paw: ", self.paw)
        print("start to end len: ", self.start_to_end_len)
        print("#######################")
        print()

    def update_leg(self):
        self.parts_list[0].update()
        self.parts_list[0].angle = angle_from_location(self.parts_list[0].start_loc, self.parts_list[0].end_loc)

        for i in range(1, len(self.parts_list)):
            self.parts_list[i].start_loc = self.parts_list[i-1].end_loc
            self.parts_list[i].angle = angle_from_location(self.parts_list[i].start_loc, self.parts_list[i].end_loc)

            p1 = self.parts_list[i-1].start_loc
            p2 = self.parts_list[i].start_loc
            p3 = self.parts_list[i].end_loc
            angle_bet = angle_between_3_points(p1, p2, p3)
            if (angle_bet > 180) and not self.is_right:
                self.parts_list[i].angle = self.parts_list[i-1].angle
            elif (angle_bet < 180) and self.is_right:
                self.parts_list[i].angle = self.parts_list[i-1].angle

            self.parts_list[i].update()

        self.start_leg = self.parts_list[0].start_loc  # problem if no parts
        self.paw = self.parts_list[self.part_amount-1].end_loc  # problem if no parts
        self.start_to_end_len = math.dist(self.start_leg, self.paw)

    def leg_follow(self, pos):
        self.parts_list[len(self.parts_list)-1].follow(pos)
        for i in range(len(self.parts_list)-2, -1, -1):
            target = self.parts_list[i + 1].start_loc
            self.parts_list[i].follow(target)
        self.paw_stand_pos = pos  # fix on last standing point


def create_leg(num_of_parts, is_right):
    part_list = []
    loc = FIXED_JOINT
    part_list.append(legPart(loc, LEG_PART_LEN, True))
    for i in range(1, num_of_parts):
        part_list.append(legPart(part_list[i-1], LEG_PART_LEN))
    leg1 = leg(part_list, is_right)
    return leg1


def draw_leg(screen, leg1):
    for i in range(0, len(leg1.parts_list)):
        start_loc = [leg1.parts_list[i].start_loc[0] + SCREEN_CENTER[0], leg1.parts_list[i].start_loc[1]*-1 + SCREEN_CENTER[1]]
        end_loc = [leg1.parts_list[i].end_loc[0] + SCREEN_CENTER[0], leg1.parts_list[i].end_loc[1]*-1 + SCREEN_CENTER[1]]
        pygame.draw.line(screen, RED, start_loc, end_loc, 5)
