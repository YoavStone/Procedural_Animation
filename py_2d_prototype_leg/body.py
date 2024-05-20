import math
import pygame
import numpy as np
from py_2d_prototype_leg.settings import *
from py_2d_prototype_leg.legPart import *
from py_2d_prototype_leg.leg import *


class body:
    def __init__(self, init_loc):
        self.body_size = BODY_SIZE
        self.body_loc = init_loc
        self.legs = []
        self.leg_num = 0
        self.acc_x = 0  # pixels per sec^2 in direction
        self.acc_y = 0
        self.speed_x = 0  # pixels per sec in direction
        self.speed_y = 0

    def update_body_movement(self):

        self.speed_x += self.acc_x
        self.speed_y += self.acc_y

        if self.speed_x > MAX_SPEED_X:
            self.speed_x = MAX_SPEED_X
        elif self.speed_x < -MAX_SPEED_X:
            self.speed_x = -MAX_SPEED_X
        if self.speed_y < MAX_SPEED_Y:
            self.speed_y = MAX_SPEED_Y

        self.body_loc[0] += self.speed_x
        self.body_loc[1] += self.speed_y

    def update_body_loc(self, inp=""):
        if inp == "":
            if self.speed_x > 0:
                self.acc_x = -FRICTION
            elif self.speed_x < 0:
                self.acc_x = FRICTION
            else:
                self.speed_x = 0
                self.acc_x = 0

            # self.acc_y = GRAVITY # TODO add gravity

        # if inp == "up":
        #     self.acc_y = 10
        elif inp == "left":
            self.acc_x = -MAX_ACC_X
        # elif inp == "down":
        #     self.acceleration = self.acceleration - np.array([0, 0.25])
        elif inp == "right":
            self.acc_x = MAX_ACC_X
        self.update_body_movement()

        for leg in self.legs:
            leg.parts_list[0].start_loc = self.body_loc
            leg.update_leg()

        # avg_height = 0  # TODO add after walk
        # for leg in self.legs:
        #     avg_height = avg_height + leg.paw_stand_pos[1]
        #     if leg.paw_stand_pos[1] <= self.body_loc[1] + 40:  # TODO do something smarter in case of a leg being above the head (transition especially)
        #         avg_height += 100
        #     else:
        #         avg_height -= 100
        # self.body_loc[1] = avg_height/self.leg_num

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
        b.legs.append(create_leg(init_loc, NUM_OF_LEG_PARTS, is_right))
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

            if pygame.mouse.get_pressed()[0]:  # Left click
                pos = pygame.mouse.get_pos()
                pos = list(pos)
                pos[0] -= SCREEN_CENTER[0]
                pos[1] -= SCREEN_CENTER[1]
                pos[1] *= -1
                creature.legs[0].leg_follow(pos)
                creature.legs[0].update_leg()
                if creature.legs[0].paw != pos:
                    opp_pos = rotate(creature.body_loc, creature.legs[0].paw, 180-10)
                    creature.legs[0].leg_follow(opp_pos)
                    creature.legs[0].update_leg()
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
                if creature.legs[1].paw != pos:
                    opp_pos = rotate(creature.body_loc, creature.legs[1].paw, 180+10)
                    creature.legs[1].leg_follow(opp_pos)
                    creature.legs[1].update_leg()
                    creature.legs[1].leg_follow(pos)
                    creature.legs[1].update_leg()

            for i in range(0, LEG_AMOUNT):  # fixed on last point that the leg stood on
                pos = creature.legs[i].paw_stand_pos
                creature.legs[i].leg_follow(pos)
                creature.legs[i].update_leg()
                if creature.legs[i].paw != pos:
                    if creature.legs[i].is_right:
                        opp_pos = rotate(creature.body_loc, creature.legs[i].paw, 180+10)
                    else:
                        opp_pos = rotate(creature.body_loc, creature.legs[i].paw, 180-10)
                    creature.legs[i].leg_follow(opp_pos)
                    creature.legs[i].update_leg()
                    creature.legs[i].leg_follow(pos)
                    creature.legs[i].update_leg()

            keys = pygame.key.get_pressed()  # W A S D
            if keys[pygame.K_w]:  # pressed w
                creature.update_body_loc("up")
            elif keys[pygame.K_a]:  # pressed a
                creature.update_body_loc("left")
            elif keys[pygame.K_s]:  # pressed s
                creature.update_body_loc("down")
            elif keys[pygame.K_d]:  # pressed d
                creature.update_body_loc("right")

        creature.update_body_loc()

        creature.draw_creature(screen)

        clock.tick(REFRESH_RATE)

    pygame.quit()


if __name__ == "__main__":
    main()
