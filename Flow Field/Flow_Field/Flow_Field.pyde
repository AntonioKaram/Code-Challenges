inc = 0.1
scl = 15
col = 0
rows = 0
zoff = 0
show = False
particles = []
flowfield = []

class Particle:

    def __init__(self):
        self.pos = PVector(random(width), random(height))
        self.vel = PVector(0,0)
        self.acc = PVector(0, 0)
        self.maxSpeed = 2

    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.maxSpeed)
        self.pos.add(self.vel)
        self.acc.mult(0)

    def applyForce(self, force):
        self.acc.add(force)

    def show(self):
        stroke(0)
        strokeWeight(4)
        point(self.pos.x, self.pos.y)

    def edges(self):
        if self.pos.x > width:
            self.pos.x = 0 
        if self.pos.x < 0:
            self.pos.x = width 
        if self.pos.y > height:
            self.pos.y = 0 
        if self.pos.y < 0:
            self.pos.y = height 
            
    def follow(self,vectors):
        x = floor(self.pos.x /scl)
        y = floor(self.pos.y /scl)
        
        index = constrain(x +(y*(cols)),0,len(vectors)-1)
        force = vectors[index]
        #print(index)
    
        self.applyForce(force)
        


def setup():
    global cols
    global rows
    global particles
    global flowfield

    size(400, 400,P2D)

    cols = floor(width / scl)
    rows = floor(height / scl)
    
    for i in xrange(cols*rows):
        flowfield.append(0)

    for i in xrange(1000):
        particles.append(Particle())

def mousePressed():
    global show
    
    if show == True:
        show = False
    else:
        show = True
    

def draw():
    global zoff
    global flowfield
    global show
    
    background(255)
    yoff = 0
    print(frameRate)

    for y in xrange(rows):
        xoff = 0
        for x in xrange(cols):
            index = x + (y * cols)
            
            angle = noise(xoff, yoff, zoff) * TWO_PI*4
            v = PVector.fromAngle(angle)
            v.setMag(1)
             
        
            flowfield[index] = v
            
            if show == True:
                stroke(0,50)
                strokeWeight(1)
                push()
                translate(x * scl, y * scl)
                rotate(v.heading())
                line(0, 0, scl, 0)
                pop()
        
            

            xoff += inc
        yoff += inc
    zoff += 0.005

    for i in xrange(len(particles)):
        particles[i].follow(flowfield)
        particles[i].update()
        particles[i].show()
        particles[i].edges()
        
    #print(len(flowfield))
       
        
        
