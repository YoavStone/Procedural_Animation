import math
import pygame
import numpy as np
from py_2d_prototype_leg.settings import *
from py_2d_prototype_leg.legPart import *
from py_2d_prototype_leg.leg import *


class body:
    def __init__(self, init_loc):
        self.body_size = BODY_SIZE
        self.body_loc = np.array(init_loc)
        self.legs = []
        self.leg_num = 0
        self.acceleration = np.array([0, 0])  # pixels per sec^2 in direction
        self.speed = np.array([0, 0])  # pixels per sec in direction

    def update_body_movement(self):
        # if self.acceleration[0] > MAX_ACC[0]:
        #     self.acceleration[0] = MAX_ACC[0]
        # elif self.acceleration[0] < -MAX_ACC[0]:
        #     self.acceleration[0] = -MAX_ACC[0]
        # if self.acceleration[1] > MAX_ACC[1]:
        #     self.acceleration[1] = MAX_ACC[1]
        # elif self.acceleration[1] < -MAX_ACC[1]:
        #     self.acceleration[1] = -MAX_ACC[1]

        self.speed = self.speed + self.acceleration

        # if self.speed[0] > MAX_SPEED[0]:
        #     self.speed[0] = MAX_SPEED[0]
        # elif self.speed[0] < -MAX_SPEED[0]:
        #     self.speed[0] = -MAX_SPEED[0]
        # if self.speed[1] > MAX_SPEED[1]:
        #     self.speed[1] = MAX_SPEED[1]
        # elif self.speed[1] < -MAX_SPEED[1]:
        #     self.speed[1] = -MAX_SPEED[1]

        self.body_loc = self.body_loc + self.speed

    def update_body_loc(self, inp=""):
        # if inp == "":
        #     if self.speed[0] > 0:
        #         self.acceleration[0] -= 0.125
        #     elif self.speed[0] < 0:
        #         self.acceleration[0] += 0.125
        #     if self.speed[1] > 0:
        #         self.acceleration[1] -= 0.125
        #     elif self.speed[1] < 0:
        #         self.acceleration[1] += 0.125
        if inp == "up":
            print("inp: ", inp)
            self.acceleration = self.acceleration + np.array([0, 0.25])
        elif inp == "left":
            print("inp: ", inp)
            self.acceleration = self.acceleration - np.array([0.25, 0])
        elif inp == "down":
            print("inp: ", inp)
            self.acceleration = self.acceleration - np.array([0, 0.25])
        elif inp == "right":
            print("inp: ", inp)
            self.acceleration = self.acceleration + np.array([0.25, 0])
        self.update_body_movement()
        print("speed: ", self.speed)
        print("acc: ", self.acceleration)
        for leg in self.legs:
            leg.parts_list[0].start_loc = self.body_loc
            leg.update_leg()

    def draw_body(self, screen):
        loc = [self.body_loc[0] + SCREEN_CENTER[0], self.body_loc[1]*-1 + SCREEN_CENTER[1]]
        pygame.draw.circle(screen, RED, loc, self.body_size)

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
                    pos = list(pos)
                    pos[0] -= SCREEN_CENTER[0]
                    pos[1] -= SCREEN_CENTER[1]
                    pos[1] *= -1
                    creature.legs[0].leg_follow(pos)
                    creature.legs[0].update_leg()
                elif pygame.mouse.get_pressed()[2]:  # Right click
                    pos = pygame.mouse.get_pos()
                    pos = list(pos)
                    pos[0] -= SCREEN_CENTER[0]
                    pos[1] -= SCREEN_CENTER[1]
                    pos[1] *= -1
                    creature.legs[1].leg_follow(pos)
                    creature.legs[1].update_leg()
            if event.type == pygame.KEYDOWN:  # W A S D
                if event.key == pygame.K_w:  # pressed w
                    creature.update_body_loc("up")
                elif event.key == pygame.K_a:  # pressed a
                    creature.update_body_loc("left")
                elif event.key == pygame.K_s:  # pressed s
                    creature.update_body_loc("down")
                elif event.key == pygame.K_d:  # pressed d
                    creature.update_body_loc("right")

        creature.update_body_loc()

        creature.draw_creature(screen)

        clock.tick(REFRESH_RATE)

    pygame.quit()


if __name__ == "__main__":
    main()
