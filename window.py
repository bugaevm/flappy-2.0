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

        self.root.after(int(1000 * self.fps), self.draw)


    def update(self):
        self.x += self.level.obstacle_v(self) * self.level.dt

        self.hole_top = self.bottom * self.x / self.right
        self.hole_bottom = self.bottom - self.hole_top

        if self.x >= -2 * self.size:
            self.root.after(int(1000 * self.fps), self.update)
        else:
            self.delete()


    def delete(self):
        for item in self.objects:
            self.canvas.delete(item)
