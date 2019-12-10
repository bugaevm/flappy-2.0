import colors

def show_text(txt, rt, cv, w):
    global root, canv, text_object

    root = rt
    canv = cv

    text_object = canv.create_text(w // 2, 100, text=txt, font='150', fill='black')

    change_col(3000)

def change_col(n):
    if n <= 1000:
        col = colors.grad((255, 255, 255), (0, 0, 0), n / 1000)
        col = colors.rgb2html(*col)

        canv.itemconfig(text_object, fill=col)

    if n == 0:
        canv.delete(text_object)
        return 0

    root.after(1, change_col, n - 1)
