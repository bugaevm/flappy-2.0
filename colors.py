def rgb2html(r, g, b):
    res = '#'
    for el in (r, g, b):
        val = ('0' + (hex(el)[2:]))[-2:]
        res += val

    return res

def html2rgb(html):
    return tuple((
        int(html[1:3], base=16), int(html[3:5], base=16), int(html[5:7], base=16)
    ))

def grad(colorA, colorB, alpha):
    return tuple(int(colorA[i] * (1 - alpha) + colorB[i] * alpha + 0.5) for i in range(3))
