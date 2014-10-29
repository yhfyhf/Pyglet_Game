import pyglet
import math
import random

def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt((point_1[0]-point_2[0])**2+(point_1[1]-point_2[1])**2)


def asteroids(num_asteroids, player_position, batch=None):
    asteroids = []
    for i in xrange(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)