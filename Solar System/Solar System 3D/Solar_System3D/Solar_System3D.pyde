add_library('peasycam')
sun = []

cam = 0
sunTexture = 0
textures = []
class Planet:
    


    
    def __init__(self,r,d,o,img):
        self.v = PVector.random3D()
        self.distance = d
        self.radius = r
        self.angle = random(TWO_PI)
        self.planets = []
        self.orbitSpeed = o
        self.v.mult(self.distance)
        
        noStroke()
        noFill()
        self.globe = createShape(SPHERE,self.radius)
        
        self.globe.setTexture(img)

        
        
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
        index = 0
        for i in range(total):
            r = self.radius/(level*2)
            d = random((self.radius + r),(self.radius+r)*2)
            index = int(random(0,len(textures)))
            self.planets.append(Planet(r,d,o,textures[index]))
            if level <2:
                num = int(random(0,3))
                self.planets[i].spawnMoons(num,level+1)

  
    def show(self):
        pushMatrix()
        noStroke()
        
        v2 = PVector(1,0,1)
        p = PVector((self.v.y*v2.z-self.v.z*v2.y),(self.v.z*v2.x-self.v.x*v2.z),(self.v.x*v2.y-self.v.y*v2.x))                             
        rotate(self.angle,p.x,p.y,p.z)
        translate(self.v.x,self.v.y,self.v.z)
    
        fill(255)
        shape(self.globe)

        print(self.planets)
        
        if self.planets != None:
            for i in range(len(self.planets)):
                self.planets[i].show()
        
        popMatrix()


def setup():
    global sun
    global cam
    global sunTexture
    global textures
    
    size(600,600,P3D)
    cam = PeasyCam(this,500)
    
    sunTexture = loadImage("sun.jpg")
    textures.append(loadImage("earth.jpg"))
    textures.append(loadImage("jupiter.jpg"))
    textures.append(loadImage("neptune.jpg"))
    
    
    sun = Planet(50,0,0,sunTexture)
    sun.spawnMoons(4,1)
    
    
    
    
def draw():
    background(0)
    
    z = 100
    
    for i in range(2):
        z = -z;
        pointLight(200, 200, 200, -100, -100, z);
        pointLight(200, 200, 200, 100, -100, z);
        pointLight(200, 200, 200, 100, 100, z);
        pointLight(200, 200, 200, -100, 100, z);
    
    sun.show()
    sun.orbit()
    
