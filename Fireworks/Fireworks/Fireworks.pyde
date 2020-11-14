numP = 100
Gsmall = PVector(0, 0.08)
Gbig = PVector(0, 0.2)

fireworks = []
x = 0

class Particle:

    def __init__(self, x, y,hu, firework): 
        self.pos = PVector(x, y)
        self.firework = firework
        self.hu = hu

        self.lifespan = 255
        self.lifespanDelta = random(4, 6)

        if self.firework == True:
            self.vel = PVector(0, random(-15, -10))
        else:
            self.vel = PVector.random2D()
            self.vel.mult(random(1, 4))
        self.acc = PVector(0, 0)

    def applyForce(self, force):
        self.acc.add(force)

    def done(self):
        if self.lifespan < 0:
            return True
        else:
            return False

    def update(self):
        if self.firework != True:
            self.vel.mult(0.95)
            self.lifespan -= self.lifespanDelta

        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)

    def show(self):
        if self.firework == True:
            stroke(self.hu,255,255)
            strokeWeight(6)
        else:
            stroke(self.hu,255,255, self.lifespan)
            strokeWeight(4)
        point(self.pos.x, self.pos.y)

class Firework:

    def __init__(self):
        self.hu = random(255)
        self.firework = Particle(random(width), height,self.hu, True)
        self.particles = []
        self.exploded = False
        

    def done(self):
        if self.exploded == True and len(self.particles) == 0:
            return True
        else:
            return False

    def update(self):

        if self.exploded != True:
            self.firework.applyForce(Gbig)
            self.firework.update()

            if self.firework.vel.y >= 0:
                self.exploded = True
                self.explode()

        for i in reversed(range(len(self.particles))):
            self.particles[i].applyForce(Gsmall)
            self.particles[i].update()

            if self.particles[i].done() == True:
                self.particles.pop(i)

    def show(self):
        if self.exploded != True:
            self.firework.show()

        for i in range(len(self.particles)):
            self.particles[i].show()

    def explode(self):
        for i in range(numP):
            p = Particle(self.firework.pos.x, self.firework.pos.y,self.hu, False)
            self.particles.append(p)


def setup():
    global canvas

    colorMode(HSB)
    #fullScreen(P2D)
    size(1000, 700, P2D)
    

def draw():
    global fireworks
    global x

    noStroke()
    fill( 0, 0, 0, 75)   #Easiest way to make trails
    rect(0, 0, width, height)

    if random(1) < 0.05:
        fireworks.append(Firework())

    for i in reversed(range(len(fireworks))):
        fireworks[i].update()
        fireworks[i].show()

        if fireworks[i].done() == True:
            fireworks.pop(i)


    x += 1
# Create Particles according to sin wave
