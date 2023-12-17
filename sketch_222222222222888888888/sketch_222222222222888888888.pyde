x=100
y=100
dirX=10
dirY=10
def setup():
    size(1000,1000)
def draw():
    global x,y,dirY,dirX
    background(34,162,211)
    text(u"NEED FOR SPEED",350,400)
    text(u"StumbleGuys",530,640)
    text(u"AmongUs",690,290)
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
    if y>999:
        dirY=10
    if x<1:
        dirX=-10
    if x>990:
        dirX=10
    rect(200,180,30,20)  
    rect(400,800,30,20)
    rect(700,300,30,20)
    rect(550,650,30,20)
            
    
