a = 200
b = 100
n = float(2)


def sgn(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    else:
        return 0 


def keyPressed():
    global n
    a = n
    if keyCode == UP:
        a += 0.5
    if keyCode == DOWN:
        a -= 0.5
    if a != 0 :
        n = a
    if a == 0:
        n = n


def setup():
    size(600,600,P2D)
    
    
def draw():
    global a
    global b 
    global n
    
    background(0)
    translate(width/2,height/2)
    stroke(255)
    noFill()
    
    beginShape()
    for angle in range(361):
        angle = radians(angle)
        
        na = 2/n
        x = pow(abs(cos(angle)), na) * a * sgn(cos(angle))
        y = pow(abs(sin(angle)), na) * b * sgn(sin(angle))
        
        vertex(x,y)
        
    endShape(CLOSE)
