from tkinter import *
from bird import Bird
import window




def game_over():
    global game_is_running

    if not game_is_running:
        return 0

    game_is_running = False
    bird.v = 0

    level.game_stoped()

    canv.itemconfig(bgnd, fill='#ffa0a0', outline='#ffa0a0')
    bird.col = '#670003'


def up(event):
    if game_is_running:
        bird.v = bird.v0

def next_level(first=False):
    global level

    if first:
        number = 0
    else:
        number = level.number + 1

    exec(f'global Level; from level_{number} import Level')
    level = Level(canv, root, fps, bird, Width, Height)
    display_level(number)

    root.after(int(1000), run_level, 1)

def run_level(period):
    if not game_is_running:
        return 0

    flag = level.next_obstacle()

    if flag is None:
        root.after(int(1000 * period), show_window)

    else:
        root.after(int(1000 * flag), run_level, flag)

def display_level(n):
    messg="LEVEL: "+str(n)
    levelbar=canv.create_rectangle(0,Height,Width,Height+3*text_size,fill="black",outline="black")
    levelabel=canv.create_text(text_size*len(messg)/2,Height+1.5*text_size,fill="yellow",text=messg,font=str(text_size))
        
def show_window():
    win_id = window.Window(
        canv, root, fps, level,
        Width, Height
    )

    if game_is_running:
        t = (Width - bird.x) / abs(level.obstacle_v(win_id)) / level.dt * fps
        root.after(int(1000 * t), next_level)


def main():
    global root, Width, Height, text_size, canv, fps, bird, game_is_running, bgnd

    root = Tk()

    Width = 1200
    Height = 600
    text_size = 9

    canv = Canvas(root, width=Width, height=Height + 3 * text_size, bg='white')
    canv.pack(fill=BOTH,expand=1)

    fps = 1 / 60
    game_is_running = True

    bgnd = canv.create_rectangle(0, 0, Width, Height, fill='white', outline='white')

    levelbar=canv.create_rectangle(0,Height,Width,Height+3*text_size,fill="black",outline="black")
    levelabel=canv.create_text(text_size*len("LEVEL: ")/2,Height+1.5*text_size,fill="yellow",text="LEVEL: ",font=str(text_size))


    bird = Bird(canv, root, fps, Height, game_over)


    next_level(first=True)


    root.bind('<Up>', up)
    root.mainloop()

if __name__ == '__main__':
    main()
