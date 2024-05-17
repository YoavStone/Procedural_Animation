import math
import pygame
from py_2d_prototype_leg.settings import *
from py_2d_prototype_leg.legPart import *
from py_2d_prototype_leg.leg import *


class body:
    def __init__(self, init_loc):
        self.body_size = BODY_SIZE
        self.body_loc = init_loc
        self.legs = []
        self.leg_num = 0

    def change_body_loc(self, pos):
        self.body_loc = pos
        for leg in self.legs:
            leg.parts_list[0].start_loc = pos
            leg.update_leg()

    def draw_body(self, screen):
        pygame.draw.circle(screen, RED, self.body_loc, self.body_size)

    def draw_creature(self, screen):
        screen.fill(WHITE)
        self.draw_body(screen)
        for leg in self.legs:
            draw_leg(screen, leg)
            # leg.leg_to_string()
        pygame.display.flip()


def create_creature(leg_num, init_loc):
    b = body(init_loc)
    b.leg_num = leg_num
    for i in range(0, leg_num):
        is_right = False
        if i % 2 == 0:
            is_right = True
        b.legs.append(create_leg(NUM_OF_LEG_PARTS, is_right))
        b.legs[i].leg_to_string()
    return b


def main():

    creature = create_creature(LEG_AMOUNT, FIXED_JOINT)

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
                if pygame.mouse.get_pressed()[0]:  # Left click
                    pos = pygame.mouse.get_pos()
                    creature.legs[0].leg_follow(pos)
                    creature.legs[0].update_leg()
                elif pygame.mouse.get_pressed()[2]:  # Right click
                    pos = pygame.mouse.get_pos()
                    creature.legs[1].leg_follow(pos)
                    creature.legs[1].update_leg()
                elif pygame.mouse.get_pressed()[1]:  # middle click
                    pos = pygame.mouse.get_pos()
                    creature.change_body_loc(pos)

            creature.draw_creature(screen)

            clock.tick(REFRESH_RATE)

    pygame.quit()


if __name__ == "__main__":
    main()
