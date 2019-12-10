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
        self.number = 10

        self.canvas = canvas
        self.root = root
        self.fps = fps
        self.bird = bird
        self.Width = Width
        self.Height = Height

        self.dt = 1
        bird.dt = self.dt

        self.obst_number = 10

        self.game_is_running = True

        self.time_flag = True
        self.timer()

    def obstacle_v(self, obstacle):
        if self.game_is_running:
            return -2 / self.dt
        return 0

    def obstacle_size(self, obstacle):
        return 60

    def obstacle_color(self, obstacle):
        if obstacle.num > 5 or obstacle.x > self.Width // 2 or not self.game_is_running:
            return '#777777'

        left = self.bird.x + (self.Width // 2 - self.bird.x) * (1 - obstacle.num / 5)
        alpha = (self.Width // 2 - obstacle.x) / (self.Width // 2 - left)

        if alpha >= 1:
            return 'white'

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

        obst.w = 0.0175 * (-1) ** random.choice(range(2))

        obst.p = random.choice(range(
            -self.Height, self.Height
        )) / self.Height * math.pi




        if self.obst_number:
        # if True:
            self.obst_number -= 1
            return 4 / self.dt
        else:
            return None

    def game_stoped(self):
        self.game_is_running = False

    def timer(self):
        delta = random.choice(range(-4, 6)) / 20

        self.dt = max(0.05, min(self.dt + delta, 1.5))
        self.bird.dt = self.dt

        if self.time_flag:
            self.root.after(600, self.timer)


    def delete(self):
        obst_set = set(obstacles.obstacles_set)
        for obst in obst_set:
            obst.delete()

        self.time_flag = False
