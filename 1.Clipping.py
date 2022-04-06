'''
Nama  : Himmatuz Zahiroh
NIM   : 20051397070
Kelas : Manajemen Informatika 2020B
CLIPPING COHEN-SUTHERLAND
'''

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8


xMax = 7.0
yMax = 7.0
xMin = 1.0
yMin = 1.0


def getPoint(x,y):
    code = INSIDE
    if x < xMin:
        code |= LEFT
    elif x > xMax:
        code |= RIGHT
    if y < yMin:
        code |= BOTTOM
    elif y > yMax:
        code |= TOP
    
    return code


def display(x1, y1, x2, y2, accept):
    fig, ax = plt.subplots()
    ax.plot([x1,y1], [x2,y2], color="yellow")
    ax.add_patch(Rectangle((1,1), 7, 7, color="black"))
    plt.xlabel('X')
    plt.ylabel('Y')
    if accept:
        subtitle = 'Cohen-Sutherland Algorithm\n' % (x1, y1, x2, y2)
    else:
        subtitle = 'Cohen-Sutherland Algorithm\n'
    plt.show()
    

def clipLine(x1, y1, x2, y2):
    
    codeA = getPoint(x1, y1)
    codeB = getPoint(x2, y2)
    isInside = False
    
    while True:
        
        if codeA == 0 and codeB == 0:
            isInside = True
            break
        
        
        elif (codeA & codeB) != 0:
            break
        
        
        else:
            
            x = 1.0
            y = 1.0
            
            if codeA != 0:
                codeOut = codeA
            else:
                codeOut = codeB
            
            
            if codeOut & TOP:
                
                x = x1 + (x2 - x1) * (yMax - y1) / (y2 - y1)
                y = yMax
            
            elif codeOut & BOTTOM:
                
                x = x1 + (x2 - x1) * (yMin - y1) / (y2 - y1)
                y = yMin
                
            elif codeOut & RIGHT:
                
                y = y1 + (y2 - y1) * (xMax - x1) / (x2 - x1)
                x = xMax
                
            elif codeOut & LEFT:
                
                y = y1 + (y2 - y1) * (xMin - x1) / (x2 - x1)
                x = xMin
                
            
            if codeOut == codeA:
                x1 = x
                y1 = y
                codeA = getPoint(x1, y1)
            else:
                x2 = x
                y2 = y
                codeB = getPoint(x2, y2)
                
    if isInside:
        display(x1, y1, x2, y2, True)
    else:
        display(x1, y1, x2, y2, False)
            

#P(1, 1), Q(10,10)
clipLine(1, 10, 1, 10)



