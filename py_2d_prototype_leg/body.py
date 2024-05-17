import math
import pygame
from py_2d_prototype_leg.settings import *
from py_2d_prototype_leg.legPart import *
from py_2d_prototype_leg.leg import *


class body:
    def __init__(self, legs_arr):
        self.body_size = BODY_SIZE
        self.legs = legs_arr


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

            leg1.parts_list[total-1].follow(pos)

            for i in range(total-2, -1, -1):
                target = leg1.parts_list[i+1].start_loc
                leg1.parts_list[i].follow(target)

            leg1.update_leg()

            draw_leg(screen, leg1)

            leg1.leg_to_string()

            clock.tick(REFRESH_RATE)

    pygame.quit()


if __name__ == "__main__":
    main()
