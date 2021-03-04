import pygame, sys, random
from pygame.locals import *

def particle_animation(display, ball, collision, particles, animate):

    #create random r g and b values
    #previous_time = pygame.time.get_ticks()

    if animate:

        # Left paddle
        if collision == -1:
            for i in range(100):
                particles.append([[ball.x, ball.y+15], [random.randint(0, 400) / 10 - 1, random.randint(-20, 20)], random.randint(4, 6), False])
        elif collision == 1: # Right paddle
            for i in range(100):
                particles.append([[ball.x+30, ball.y+15], [random.randint(-400, 0) / 10 - 1, random.randint(-20, 20)], random.randint(4, 6), False])
        else: # Ball
            particles.append([[ball.x+15, ball.y+15], [random.randint(0, 25) / 10 - 1, -2], random.randint(4, 6), True])

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            if particle[3] == False:
                pygame.draw.circle(display, (255,255,255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            else:
                if random.randint(1,5) == 1:
                    r,g,b = 255,255,255
                    pygame.draw.circle(display, (r,g,b), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                else:
                    r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
                    pygame.draw.circle(display, (r,g,b), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))

            if particle[2] <= 0:
                particles.remove(particle)
    else:
        particles.clear()