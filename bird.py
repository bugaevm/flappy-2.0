class Bird:
    def __init__(self, canvas, root, fps, max_h, interrupting, x=None, y=None):
        self.size = 20
        self.x = (self.size * 4 if x is None else x)
        #self.y = (Height - self.size) // 2
        self.y = (self.size * 8 if y is None else y)
        self.v0 = -7
        self.v = self.v0
        self.g = 0.25
        self.dt = 1

        self.col = '#e528b8'
        self.objects = None

        self.canvas = canvas
        self.root = root

        self.fps = fps

        self.h = max_h
        self.interrupting = interrupting

        self.draw()
        self.move()


    def draw(self):
        if self.objects is not None:
            self.canvas.delete(self.objects[0])

        r = self.size / 2
        self.objects = [self.canvas.create_oval(
            self.x - r, self.y - r, self.x + r, self.y + r,
            fill=self.col, outline = self.col
        )]

        self.root.after(int(1000 * self.fps), self.draw)

    def move(self):
        dt = self.dt

        if self.y - self.size / 2 > 0 or self.v > 0:
            self.y += self.v * dt + self.g * dt ** 2 / 2

        self.v += self.g * dt

        self.check_falling()

        self.root.after(int(1000 * self.fps), self.move)

    def check_falling(self):
        if self.y + self.size / 2 >= self.h:
            self.interrupting()


if __name__ == '__main__':
    print('This module is not for direct call.')
