from tkinter import *
from bird import Bird
import window
from show_text import show_text



def game_over():
    global game_is_running

    if not game_is_running:
        return 0

    game_is_running = False
    bird.v = 0

    level.game_stoped()

    canv.itemconfig(bgnd, fill='#ffa0a0', outline='#ffa0a0')
    bird.col = '#670003'


    if checkpoint_number > unlocked:
        with open('unlocked', 'w') as out:
            print(checkpoint_number, end='', file=out)


    messg = "Press q to exit, r to restart"
    bottom_bar(messg)

    root.bind("q", die)
    root.bind("r", restart)

def die(Event):
    if Event:
        exit(0)

def restart(Event):
    global bckg_bar, text_bar

    if Event:
        level.delete()
        bird.kill()

        canv.delete('ALL')

        bckg_bar = None
        text_bar = None

        # new_game(0)
        start_menu()


def up(event):
    if game_is_running:
        bird.v = bird.v0


def next_level(num=None):
    global level, checkpoint_number

    if num is not None:
        number = num
    else:
        number = level.number + 1

    exec(f'global Level, checkpoint; from level_{number} import Level, checkpoint')
    level = Level(canv, root, fps, bird, Width, Height)
    display_level(number)

    if checkpoint:
        checkpoint_number += 1
        show_text(f'CHECKPOINT {checkpoint_number}', root, canv, Width)
        root.after(int(4000), run_level, 1)

    else:
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
    messg = 'Level ' + str(n)
    bottom_bar(messg)


bckg_bar = None
text_bar = None
def bottom_bar(messg):
    global bckg_bar, text_bar

    if bckg_bar is None:
        bckg_bar = canv.create_rectangle(
            0, Height, Width, Height + 3 * text_size, fill="#afafaf", outline="#afafaf"
        )

    if text_bar is None:
        text_bar = canv.create_text(
            text_size, Height + 3 * text_size // 2,
            fill="black", text=messg, font=str(text_size), anchor=W
        )
    else:
        canv.itemconfig(text_bar, text=messg)




def show_window():
    win_id = window.Window(
        canv, root, fps, level,
        Width, Height
    )

    if game_is_running:
        t = (Width - bird.x) / abs(level.obstacle_v(win_id)) / level.dt * fps
        root.after(int(1000 * t), next_level)


def main():
    global root, Width, Height, text_size, canv, fps

    root = Tk()

    Width = 1200
    Height = 600
    text_size = 9

    canv = Canvas(root, width=Width, height=Height + 3 * text_size, bg='white')
    canv.pack(fill=BOTH, expand=1)

    fps = 1 / 60


    start_menu()

    root.mainloop()

def start_menu(sel_lev=None):
    global unlocked

    if sel_lev is not None:
        global checkpoint_number

        unlocked = 0
        checkpoint_number = 0
        new_game(sel_lev)

        print('Testing mode')
        return 0


    def onclick(event):  # yeah it's function in finction
        global checkpoint_number

        x = event.x
        ind = int((x - Width / 6) // size)

        if ind <= unlocked:
            checkpoint_number = 0 if ind == 0 else ind - 1
            new_game(checkpoints[ind][1])

    canv.delete('all')


    checkpoints = list()
    checkpoints.append((0, 0))

    n = 1
    number = 0
    while True:
        try:
            exec(f'global checkpoint; from level_{number} import checkpoint')
        except ModuleNotFoundError:
            break
        else:

            if checkpoint:
                checkpoints.append((n, number))
                n += 1

            number += 1


    try:
        with open('unlocked') as unlocked:
            unlocked = int(unlocked.read())
    except FileNotFoundError:
        unlocked = 0
    else:
        pass

    amount = len(checkpoints)
    size = Width * 2 / 3 / amount

    for i in range(amount):
        col = '#1ad747' if i <= unlocked else '#777777'

        button = canv.create_rectangle(
            Width / 6 + i * size, Height // 2 - 20,
            Width / 6 + (i + 1) * size, Height // 2 + 20,
            fill=col, outline='white', tag='button'
        )

        label_text = 'start' if i == 0 else str(i)
        canv.create_text(
            Width / 6 + (i + 0.5) * size, Height // 2,
            text=label_text, fill='white', font='20', tag='button'
        )

        canv.tag_bind('button', '<1>', onclick)



def new_game(level_num):
    global game_is_running, bgnd, bird, checkpoint_number

    canv.delete('ALL')


    game_is_running = True
    bgnd = canv.create_rectangle(0, 0, Width, Height, fill='white', outline='white')

    bird = Bird(canv, root, fps, Height, game_over)

    #checkpoint_number = 0
    next_level(level_num)


    root.bind('<Up>', up)


if __name__ == '__main__':
    main()
