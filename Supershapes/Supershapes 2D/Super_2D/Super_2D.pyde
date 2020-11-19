a = float(1)
b = float(1)
n1 = float(0.3)
n2 = float(0.3)
n3 = float(0.3)
m = float(5)

osc = 0

# a and b are responsible for size/scaling
# all = 1 --> weird circle; all = 1 but m = 0 --> circle
#n1=n2-n3; try 0.3,1

def supershape(theta):
    global a
    global b
    global m
    global n1
    global n2
    global n3

    r = 1

    part1 = pow(abs((1 / a) * cos((m / 4) * theta)), n2)
    part2 = pow(abs((1 / b) * sin((m / 4) * theta)), n3)
    part3 = pow((part1 + part2), 1 / n1)

    if part3 == 0:
        return r

    else:
        r = 1 / part3
        return r


def keyPressed():
    global m
    a = m
    if keyCode == UP:
        a += 0.5
    if keyCode == DOWN:
        a -= 0.5
    if a >= 0:
        m = a
    if a < 0:
        m = m


def setup():
    size(600, 600,P2D)


def draw():
    global m 
    global osc
    
    m = map(sin(osc),-1,1,0,10)
    osc += 0.02
    
    background(0)
    translate(width / 2, height / 2)
    stroke(255)
    noFill()

    radius = 100

    beginShape()
    for angle in range(2*(361)):
        angle = radians(angle)
        r = supershape(angle)
        x = r * cos(angle) * radius
        y = r * sin(angle) * radius

        vertex(x, y)

    endShape(CLOSE)
