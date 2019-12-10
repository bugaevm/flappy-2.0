import random, math
import obstacles, window
from colors import *

checkpoint = False

class Hole:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

class Level:
    def __init__(self, canvas, root, fps, bird, Width, Height):
        self.number = 6

        self.canvas = canvas
        self.root = root
        self.fps = fps
        self.bird = bird
        self.Width = Width
        self.Height = Height

        self.dt = 1
        bird.dt = self.dt

        self.obst_number = 40

        self.game_is_running = True

    def obstacle_v(self, obstacle):
        if self.game_is_running:
            return -3
        return 0

    def obstacle_size(self, obstacle):
        return 60

    def obstacle_color(self, obstacle):
        if not self.game_is_running:
            return '#777777'

        alpha = f(obstacle.x / self.Width, (40 - obstacle.num) / 40)

        col = grad(html2rgb('#777777'), (255, 255, 255), alpha)
        return rgb2html(*col)


    def update_hole(self, obstacle):
        obstacle.p += obstacle.w * self.dt
        centre = self.Height // 2
        ampl = centre - self.bird.size // 2 - obstacle.hole_size // 2

        t = centre + ampl * math.sin(obstacle.p)

        # if obstacle.hole is None:
        obstacle.hole = Hole(t - obstacle.hole_size / 2, t + obstacle.hole_size / 2)

    def next_obstacle(self):
        obst = obstacles.Obstacle(
            self.canvas, self.root, self.fps, self.bird, self,
            self.Width, self.Height
        )
        obst.num = self.obst_number
        obst.hole_size = self.bird.size * 10

        obst.w = 0.005 * (-1) ** random.choice(range(2))

        obst.p = random.choice(range(
            -self.Height, self.Height
        )) / self.Height * math.pi




        if self.obst_number:
        # if True:
            self.obst_number -= 1
            return 1.5 / self.dt
        else:
            return None

    def game_stoped(self):
        self.game_is_running = False


    def delete(self):
        obst_set = set(obstacles.obstacles_set)
        for obst in obst_set:
            obst.delete()


def f(x, n):  # 0 <= x, n <= 1
    point1 = 0.75 + 0.2 * n
    point2 = 0.6
    point3 = 0.5
    point4 = 0.15 + 0.2 * n

    if x > point1:
        return 1 - (x - point1) / (1 - point1)
    elif point3 < x < point2:
        return (x - point3) / (point2 - point3)
    elif point4 < x < point3:
        return 1 - (x - point4) / (point3 - point4)

    return 1
