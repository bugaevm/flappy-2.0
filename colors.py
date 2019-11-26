def rgb2html(r,g,b):
    return "#"+format(r,'02x')+format(g,'02x')+format(b,'02x')
def html2rgb(html):
    return int(html[1:3],base=16),int(html[3:5],base=16),int(html[5:7],base=16)
def grad(colorA,colorB,alpha):
    return tuple(colorA[i]*(1-alpha)+colorB[i]*alpha for i in range(3))
