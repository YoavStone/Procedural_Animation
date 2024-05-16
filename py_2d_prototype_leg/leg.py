import math
import pygame
from py_2d_prototype_leg.settings import *
from py_2d_prototype_leg.legPart import *


class leg:
    def __init__(self, parts_list):
        self.parts_list = parts_list
        len = 0
        self.part_amount = 0
        for p in parts_list:
            len += p.len
            self.part_amount += 1
        self.max_len = len
        self.start_leg = parts_list[0].start_loc
        self.paw = parts_list[self.part_amount - 1].end_loc  # problem if no parts
        self.start_to_end_len = math.dist(self.start_leg, self.paw)

    def leg_to_string(self):
        for part in self.parts_list:
            print("---")
            part.part_to_string()
        print("------------")
        print("part amount: ", self.part_amount)
        print("max leg len: ", self.max_len)
        print("start leg: ", self.start_leg)
        print("paw: ", self.paw)
        print("start to end len: ", self.start_to_end_len)
        print("#######################")
        print()


def create_leg(num_of_parts):
    part_list = []
    print("start loc: ")
    loc1 = [int(input()), int(input())]
    for i in range(0, num_of_parts):
        print("end loc: ")
        loc2 = [int(input()), int(input())]
        part_list.append(legPart(loc1, loc2))
        loc1 = loc2
    leg1 = leg(part_list)
    return leg1


def main():
    print("how many parts:")
    leg1 = create_leg(int(input()))
    leg1.leg_to_string()

    pygame.init()

    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")
    screen.fill(WHITE)
    pygame.display.flip()
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

    pygame.quit()


if __name__ == "__main__":
    main()
