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
        self.start_leg = self.parts_list[0].start_loc  # problem if no parts
        self.paw = self.parts_list[self.part_amount - 1].end_loc  # problem if no parts
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

    def update_leg(self):
        self.parts_list[0].update()
        for i in range(1, len(self.parts_list)):
            self.parts_list[i].start_loc = self.parts_list[i-1].end_loc
            self.parts_list[i].update()
        self.start_leg = self.parts_list[0].start_loc  # problem if no parts
        self.paw = self.parts_list[self.part_amount - 1].end_loc  # problem if no parts
        self.start_to_end_len = math.dist(self.start_leg, self.paw)


def create_leg(num_of_parts):
    part_list = []
    loc = FIXED_JOINT
    part_list.append(legPart(loc, LEG_PART_LEN, True))
    for i in range(1, num_of_parts):
        part_list.append(legPart(part_list[i-1], LEG_PART_LEN))
    leg1 = leg(part_list)
    return leg1


def main():

    leg1 = create_leg(NUM_OF_LEG_PARTS)
    leg1.leg_to_string()
    total = len(leg1.parts_list)

    pygame.init()

    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Game")
    screen.fill(WHITE)
    pygame.display.flip()
    finish = False

    clock = pygame.time.Clock()

    while not finish:  # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = pygame.mouse.get_pos()
                leg1.parts_list[0].start_loc = start_pos

            pos = pygame.mouse.get_pos()
            screen.fill(WHITE)

            leg1.parts_list[total-1].follow(pos)

            for i in range(total-2, -1, -1):
                target = leg1.parts_list[i+1].start_loc
                leg1.parts_list[i].follow(target)

            leg1.update_leg()
            for i in range(0, total):
                pygame.draw.line(screen, RED, leg1.parts_list[i].start_loc, leg1.parts_list[i].end_loc, 5)

            pygame.display.flip()
            leg1.leg_to_string()

            clock.tick(REFRESH_RATE)

    pygame.quit()


if __name__ == "__main__":
    main()
