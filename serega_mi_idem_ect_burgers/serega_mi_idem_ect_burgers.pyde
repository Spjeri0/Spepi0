x=100
y=100
dirX=10
dirY=10
def setup():
    size(1000,1000)
def draw():
    global x,y,dirY,dirX
    background(232,154,7)

    strokeWeight(10)
    point(x,y)
    if key=='w':
        y=y-dirY
    if key=='s':
        y=y+dirX
    if key=='d':
        x=x+dirX
    if key=='a':
        x=x-dirX
    if y<1:
        dirY=-10
        
    text(u"какать",350,400)
