import random
import obstacles, window


class Hole:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

class Level:
    def __init__(self, canvas, root, fps, bird, Width, Height):
        self.number = 1

        self.canvas = canvas
        self.root = root
        self.fps = fps
        self.bird = bird
        self.Width = Width
        self.Height = Height

        self.dt = 1
        bird.dt = self.dt

        self.obst_number = 50

        self.game_is_running = True

    def obstacle_v(self, obstacle):
        if self.game_is_running:
            return -3
        return 0

    def obstacle_size(self, obstacle):
        return 60

    def obstacle_color(self, obstacle):
        return '#777777'

    def update_hole(self, obstacle):
        num = obstacle.num
        min_size = self.bird.size * 4

        hole_size = int(min_size + (275 - min_size) / (51 - num) ** (1 / 3) + 0.5)
        t = random.randint(self.bird.size // 2, self.Height - hole_size - self.bird.size // 2)
        if obstacle.hole is None:
            obstacle.hole = Hole(t, t + hole_size)

    def next_obstacle(self):
        obst = obstacles.Obstacle(
            self.canvas, self.root, self.fps, self.bird, self,
            self.Width, self.Height
        )
        obst.num = self.obst_number




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
