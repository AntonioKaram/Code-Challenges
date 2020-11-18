# Rain: (138,43,226)
# Background: (230,230,250)

d = []
numP = 2

class Particle:

    def __init__(self, x, y, thick,ln):
        
        self.thick = thick
        self.r = map(ln,10,20,1,2)
        self.pos = PVector(x, height - self.r)
        self.vel = PVector.random2D()
        self.vel.mult(random(2, 6))
        self.acc = PVector()

    def update(self):
        self.acc.add(PVector(0, 0.01))
        self.vel.mult(0.95)
        self.vel.add(self.acc)
        self.pos.add(self.vel)

    def show(self):
        fill(138, 43, 226)
        strokeWeight(self.thick)
        push()
        translate(self.pos.x,self.pos.y)
        rotate(self.vel.heading())
        line(0,0,self.r,self.r)
        #ellipse(0,0,self.r,self.r)
        pop()
    


class Drop:

    def __init__(self):
        self.x = random(width)
        self.y = random(-500, -50)
        self.ln = random(10, 20)
        self.z = random(0, 20)
        self.ln = map(self.z, 0, 20, 10, 20)
        self.yspeed = map(self.z, 0, 20, 1, 20)
        self.thick = map(self.z, 0, 20, 1, 3)
        self.particles = []
        self.times = 0

    def fall(self):
        self.y += self.yspeed
        gravity = map(self.z, 0, 20, 0, 0.1)
        self.yspeed += gravity

        if self.y >= height and self.times <1 :
            self.splash(self.x, self.y)
            self.times += 1
            
        if self.y >= height:
            for i in range(len(self.particles)):
                self.particles[i].update()
                self.particles[i].show()

            if self.y >= height + random(200, 400):
                self.y = random(-200, -100)
                self.yspeed = map(self.z, 0, 20, 2, 6)  # 4,10
                self.particles = []
                self.times = 0

    def show(self):
        strokeWeight(self.thick)
        stroke(138, 43, 226)
        line(self.x, self.y, self.x, self.y + self.ln)

    def splash(self, x, y):
        for i in range(numP):
            self.particles.append(Particle(x, y, self.thick,self.ln))


def setup():
    global d
    size(800, 700)
    for i in range(500):
        d.append(Drop())


def draw():
    background(230, 230, 250)

    for i in range(len(d)):
        d[i].fall()
        d[i].show()
