import obstacles

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

        self.dt = 0.3
        bird.dt = self.dt

        self.game_is_running = True

    def obstacle_v(self, obstacle):
        if self.game_is_running:
            return -3
        return -3

    def obstacle_size(self, obstacle):
        return 60

    def obstacle_color(self, obstacle):
        return '#777777'

    def update_hole(self, obstacle):
        if obstacle.hole is None:
            obstacle.hole = Hole(
                self.Height / 2 - self.bird.size * 4,
                self.Height / 2 + self.bird.size * 4
            )

    def next_obstacle(self):
        obstacles.Obstacle(
            self.canvas, self.root, self.fps, self.bird, self,
            self.Width, self.Height
        )

        return 1.5 / self.dt

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
