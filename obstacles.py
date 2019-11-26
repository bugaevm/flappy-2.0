obstacles_set = set()

class Obstacle:
    def __init__(self, canvas, root, fps, bird, level, Width, Height):
        self.level = level

        # self.size = level.obstacle_size
        # self.hole = level.obstacle_hole
        # self.x = Width
        # self.v = level.obstacle_v
        # self.color = level.obstacle_color

        self.condition = None
        self.objects = set()
        self.bottom = Height

        self.x = Width + 1
        self.hole = None

        self.canvas = canvas
        self.root = root

        self.fps = fps
        self.bird = bird

        obstacles_set.add(self)

        root.after(int(1000 * self.fps), self.update)
        root.after(int(1000 * self.fps), self.draw)

    def draw(self):
        for item in self.objects:
            self.canvas.delete(item)


        rect1 = self.canvas.create_rectangle(
            self.x, 0, self.x + self.size, self.hole.top,
            fill=self.color, outline=self.color
        )

        rect2 = self.canvas.create_rectangle(
            self.x, self.hole.bottom, self.x + self.size, self.bottom,
            fill=self.color, outline=self.color
        )

        self.objects = {rect1, rect2}

        self.root.after(int(1000 * self.fps), self.draw)


    def update(self):
        self.x += self.level.obstacle_v(self) * self.level.dt
        self.size = self.level.obstacle_size(self)

        if self.condition == 'passed':
            self.color = '#1ad747'
        elif self.condition == 'bumped':
            self.color = '#b30b02'
        else:
            self.color = self.level.obstacle_color(self)

        self.level.update_hole(self)

        self.check_passing()

        if self.x >= -2 * self.size:
            self.root.after(int(1000 * self.fps), self.update)
        else:
            self.delete()

    def check_passing(self):
        bird = self.bird
        hole = self.hole

        if (bird.x - bird.size / 2 > self.x + self.size
        and self.condition != 'bumped'):
            self.condition = 'passed'
            return 0

        if (bird.x + bird.size / 2 < self.x
        or hole.top + bird.size / 2 < bird.y < hole.bottom - bird.size / 2):
            return 0

        self.condition = 'bumped'
        bird.interrupting()

        self.check_falling_on_obstacle()

    def check_falling_on_obstacle(self):
        bird = self.bird
        bird_bottom = bird.y + bird.size / 2
        bottom = self.hole.bottom

        if bird.x < self.x and bird.x + bird.size / 2 >= self.x:
            move_obstacles(1)
        if bird.x > self.x + self.size and bird.x - bird.size / 2 <= self.x + self.size:
            move_obstacles(-1)

        if bird_bottom < bottom:
            return 0

        if self.x <= bird.x <= self.x + self.size:
            self.bird.v = 0
            self.bird.y = bottom - bird.size / 2
            return 0



    def delete(self):
        global obstacles_set

        for item in self.objects:
            self.canvas.delete(item)
        obstacles_set -= {self}


def move_obstacles(r):
    for obst in obstacles_set:
        obst.x += r
