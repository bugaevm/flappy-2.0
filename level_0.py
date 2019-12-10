import random
import obstacles, window

checkpoint = False

class Hole:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

class Level:
    def __init__(self, canvas, root, fps, bird, Width, Height):
        self.number = 0

        self.canvas = canvas
        self.root = root
        self.fps = fps
        self.bird = bird
        self.Width = Width
        self.Height = Height

        self.dt = 1
        bird.dt = self.dt

        self.obst_number = 25

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
        hole_size = 300
        t = random.randint(self.bird.size // 2, self.Height - hole_size - self.bird.size // 2)
        if obstacle.hole is None:
            obstacle.hole = Hole(t, t + hole_size)

    def next_obstacle(self):
        obstacles.Obstacle(
            self.canvas, self.root, self.fps, self.bird, self,
            self.Width, self.Height
        )


        if self.obst_number:
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
