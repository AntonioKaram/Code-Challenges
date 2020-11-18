sun = []


class Planet:
    def __init__(self,r,d,o):
        self.distance = d
        self.radius = r
        self.angle = random(TWO_PI)
        self.planets = []
        self.orbitSpeed = o
        
    def orbit(self):
        self.angle += self.orbitSpeed
        
        if self.planets != None:
            for i in range(len(self.planets)):
                self.planets[i].orbit() 
    
    def spawnMoons(self,total,level):
        r = 0
        d = 0
        o = random(-0.1,0.1)
        num = 0
        for i in range(total):
            r = self.radius/(level*2)
            d = random((self.radius + r),(self.radius+r)*2)
            
            self.planets.append(Planet(r,d,o))
            if level <2:
                num = int(random(0,3))
                self.planets[i].spawnMoons(num,level+1)

  
    def show(self):
        pushMatrix()
        fill(255,100)
        rotate(self.angle)
        translate(self.distance,0)
        ellipse(0,0,self.radius*2,self.radius*2)
        print(self.planets)
        
        if self.planets != None:
            for i in range(len(self.planets)):
                self.planets[i].show()
        
        popMatrix()


def setup():
    global sun
    size(600,600,P2D)
    
    sun = Planet(50,0,0)
    sun.spawnMoons(5,1)
    
    
def draw():
    background(0)
    translate(width/2, height/2)
    sun.show()
    sun.orbit()
    
