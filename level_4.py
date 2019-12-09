import random, math
import obstacles, window


class Hole:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

class Level:
    def __init__(self, canvas, root, fps, bird, Width, Height):
        self.number = 4

        self.canvas = canvas
        self.root = root
        self.fps = fps
        self.bird = bird
        self.Width = Width
        self.Height = Height

        self.dt = 1
        bird.dt = self.dt

        self.obst_number = 35

        self.game_is_running = True

    def obstacle_v(self, obstacle):
        if obstacle.id == 'window':
            return -3

        obstacle.hor_phi += obstacle.hor_w * self.dt
        return -3 * self.game_is_running + 2 * math.cos(obstacle.hor_phi)

    def obstacle_size(self, obstacle):
        return 60

    def obstacle_color(self, obstacle):
        return '#777777'

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

        obst.w = (
            (min(34 - obst.num, 16) - 1) / 40
        ) ** 4 * (-1) ** random.choice(range(2))

        obst.p = random.choice(range(
            -self.Height, self.Height
        )) / self.Height * math.pi

        obst.hor_phi = math.pi * random.choice(range(10)) / 10
        obst.hor_w = 0.05 + 0.25 * (35 - obst.num) / 35

        obst.id = 'obstacle'




        if self.obst_number:
        # if True:
            self.obst_number -= 1
            return 1.5 / self.dt
        else:
            return None

    def game_stoped(self):
        self.game_is_running = False

#     def run(self):
#         global flag
#
#         new_obst_time()
#
#         while True:
#             if flag:
#                 obstacles.Obstacle(
#                     self.canvas, self.root, self.fps, self.bird, self,
#                     self.Width, self.Height
#                 )
#                 print('obst')
#
#                 flag = False
#                 self.root.after(1500, new_obst_time)
#
# flag = False
# def new_obst_time():
#     global flag
#
#     flag = True
#     print(flag)
