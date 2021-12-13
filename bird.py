from math import e
from colors import *

def hit_effect(canv, bgnd, root, fps, par):
    a = 1 / fps / 7.5

    if par > a:
        col = '#ffffff'
        canv.itemconfig(bgnd, fill=col, outline=col)
        return 0

    # alpha = min(1, par * (a - par) / (a ** 2 / 4))
    alpha = e ** (-(par - a / 2) ** 2 / 4)
    col = rgb2html(*grad((255, 255, 255), html2rgb('#ffa0a0'), alpha))
    canv.itemconfig(bgnd, fill=col, outline=col)

    root.after(int(1000 * fps), hit_effect, canv, bgnd, root, fps, par + 1)

class Bird:
    def __init__(self, canvas, background, root, fps, max_h, interrupting, x=None, y=None):
        self.size = 20
        self.x = (self.size * 4 if x is None else x)
        #self.y = (Height - self.size) // 2
        self.y = (self.size * 8 if y is None else y)
        self.v0 = -7
        self.v = self.v0
        self.g = 0.25
        self.dt = 1

        # self.col = '#e528b8'
        # self.col0 = '#0087af'
        # self.col0 = '#e528b8'
        # self.col1 = '#5f0000'

        self.colors = ['#5f0000', '#e528b8', '#a028e5', '#282be5', '#0087af']
        self.col = self.colors[-1]
        self.object = None

        self.canvas = canvas
        self.background = background
        self.root = root

        self.fps = fps

        self.h = max_h
        self.interrupting = interrupting

        self.living = 4

        self.draw()
        self.move()


    def draw(self):
        # if not self.living:
        #     return 0

        r = self.size / 2

        if self.object is None:
            self.object = self.canvas.create_oval(
                self.x - r, self.y - r, self.x + r, self.y + r,
                fill=self.col, outline = self.col
            )

            self.canvas.tag_raise(self.object)

        else:
            self.canvas.tag_raise(self.object)

            self.canvas.coords(self.object,
                self.x - r, self.y - r, self.x + r, self.y + r
            )

            self.canvas.itemconfig(self.object,
                fill=self.col, outline = self.col
            )

        # r = self.size / 2
        # self.objects = [self.canvas.create_oval(
        #     self.x - r, self.y - r, self.x + r, self.y + r,
        #     fill=self.col, outline = self.col
        # )]

        self.root.after(int(1000 * self.fps), self.draw)

    def move(self):
        # if not self.living:
        #     return 0

        dt = self.dt

        if self.y - self.size / 2 > 0 or self.v > 0:
            self.y += self.v * dt + self.g * dt ** 2 / 2

        self.v += self.g * dt

        self.check_falling()

        self.root.after(int(1000 * self.fps), self.move)

    def check_falling(self):
        if self.y >= self.h - self.size / 2:
            self.y = self.h - self.size / 2

            if self.living > 1:
                self.v = self.v0
            else:
                self.v *= -0.5
                self.v = max(self.v, self.v0)

            self.hit()

    def hit(self):
        if not self.living:
            return 0

        self.living -= 1
        if self.living:
            hit_effect(self.canvas, self.background, self.root, self.fps, 0)

        # c0 = html2rgb(self.col0)
        # c1 = html2rgb(self.col1)
        # self.col = rgb2html(*grad(c0, c1, 1 - self.living / 4))

        self.col = self.colors[self.living]

        if not self.living:
            self.col = self.colors[0]
            self.interrupting()

    def kill(self):
        self.living = 0


if __name__ == '__main__':
    print('This module is not for direct call.')
