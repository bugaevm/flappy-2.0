import random, math
import obstacles, window

checkpoint = False

class Hole:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

class Level:
    def __init__(self, canvas, root, fps, bird, Width, Height):
        self.number = 3

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

        self.time = 0
        self.running = True
        self.timer()

    def obstacle_v(self, obstacle):
        if self.game_is_running:
            return -3
        return 0

    def obstacle_size(self, obstacle):
        return 60

    def obstacle_color(self, obstacle):
        return '#777777'

    def update_hole(self, obstacle):
        if self.time <= 10:
            obstacle.p += obstacle.step / 10

            top = self.bird.size + obstacle.hole_size // 2
            bottom = self.Height - self.bird.size - obstacle.hole_size // 2

            if obstacle.p > bottom:
                obstacle.p = 2 * bottom - obstacle.p
                obstacle.step *= -1

            if obstacle.p < top:
                obstacle.p = 2 * top - obstacle.p
                obstacle.step *= -1

        p = obstacle.p
        obstacle.hole = Hole(p - obstacle.hole_size / 2, p + obstacle.hole_size / 2)

    def next_obstacle(self):
        obst = obstacles.Obstacle(
            self.canvas, self.root, self.fps, self.bird, self,
            self.Width, self.Height
        )
        obst.num = self.obst_number
        obst.hole_size = self.bird.size * 10


        obst.p = random.choice(range(
            self.bird.size + obst.hole_size // 2,
            self.Height - self.bird.size - obst.hole_size // 2
        ))
        obst.step = random.choice((-1, 1)) * 3 * (40 - obst.num)




        if self.obst_number:
        # if True:
            self.obst_number -= 1
            return 1.5 / self.dt
        else:
            return None

    def game_stoped(self):
        self.game_is_running = False

    def timer(self):
        self.time += 1
        self.time %= 100

        if self.running:
            self.root.after(10, self.timer)

    def delete(self):
        obst_set = set(obstacles.obstacles_set)

        for obst in obst_set:
            obst.delete()

        self.running = False
