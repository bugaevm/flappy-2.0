from tkinter import *
from bird import Bird
import window


def game_over():
    print('Ooops')

def up(event):
    bird.v = bird.v0

def next_level(first=False):
    global level

    if first:
        number = 0
    else:
        number = level.number + 1

    exec(f'global Level; from level_{number} import Level')
    level = Level(canv, root, fps, bird, Width, Height)

    root.after(int(1000), run_level, 1)

def run_level(period):
    flag = level.next_obstacle()

    if flag is None:
        root.after(int(1000 * period), show_window)

    else:
        root.after(int(1000 * flag), run_level, flag)

def show_window():
    win_id = window.Window(
        canv, root, fps, level,
        Width, Height
    )

    t = (Width - bird.x) / abs(level.obstacle_v(win_id)) / level.dt * fps
    root.after(int(1000 * t), next_level)


def main():
    global root, Width, Height, text_size, canv, fps, bird

    root = Tk()

    Width = 1200
    Height = 600
    text_size = 9

    canv = Canvas(root, width=Width, height=Height + 3 * text_size, bg='white')
    canv.pack(fill=BOTH,expand=1)

    fps = 1 / 60


    bird = Bird(canv, root, fps, Height, game_over)


    next_level(first=True)


    root.bind('<Up>', up)
    root.mainloop()

if __name__ == '__main__':
    main()
