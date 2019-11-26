def rgb2html(r,g,b):
    return "#"+format(r,'02x')+format(g,'02x')+format(b,'02x')
def html2rgb(html):
    return int(html[1:3],base=16),int(html[3:5],base=16),int(html[5:7],base=16)
def grad(colorA,colorB,alpha):
    return colorA[0]*(1-alpha)+colorB[0]*alpha,\
        colorA[1]*(1-alpha)+colorB[1]*alpha,\
        colorA[2]*(1-alpha)+colorB[2]*alpha
