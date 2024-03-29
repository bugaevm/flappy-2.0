import math

def smooth_tr(x):
    if x < 0:
        return 0
    if x > 1:
        return 1

    return (3 - 2 * x) * x ** 2

class Window:
    def __init__(self, canvas, root, fps, level, Width, Height):
        self.level = level
        self.objects = set()
        self.bottom = Height
        self.right = Width

        self.size = 20

        self.x = Width + 1

        self.canvas = canvas
        self.root = root

        self.fps = fps
        self.color = '#77e1ef'

        self.id = 'window'

        self.alive = True

        self.update()
        self.draw()

    def draw(self):
        for item in self.objects:
            self.canvas.delete(item)


        rect1 = self.canvas.create_rectangle(
            self.x, 0, self.x + self.size, self.hole_top,
            fill=self.color, outline=self.color
        )

        rect2 = self.canvas.create_rectangle(
            self.x, self.hole_bottom, self.x + self.size, self.bottom,
            fill=self.color, outline=self.color
        )

        self.objects = {rect1, rect2}

        if self.alive:
            self.root.after(int(1000 * self.fps), self.draw)


    def update(self):
        Width = self.right
        Height = self.bottom

        self.x += self.level.obstacle_v(self) * self.level.dt

        # if self.x > Width / 2:
        #     self.hole_top = Height // 2 - 1
        # else:
        #     self.hole_top = (Height // 2 - 1) * (1 - math.cos(math.pi * self.x / Width))
        #     self.hole_top = max(self.hole_top, 20)

        init_pos = Height / 2 - 1
        finit_pos = 20
        parametr = -self.x / (Width / 4) + 3

        self.hole_top = init_pos + smooth_tr(parametr) * (finit_pos - init_pos)

        self.hole_bottom = self.bottom - self.hole_top

        if self.x >= -2 * self.size and self.alive:
            self.root.after(int(1000 * self.fps), self.update)
        else:
            self.delete()


    def delete(self):
        for item in self.objects:
            self.canvas.delete(item)

        self.alive = False
