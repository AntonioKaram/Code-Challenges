class Star:
    def __init__(self):
        self.x = random(-width,width)
        self.y = random(-height,height)
        self.z = random(width)
        self.sx = 0
        self.sy = 0
        self.r = 0 
        self.px = self.x
        self.py = self.y
        self.pz = self.z

    
    def update(self):
        self.z -= speed
        
        if self.z < 1:
            self.z = width
            self.x = random(-width,width)
            self.y = random(-height,height)
            self.pz = self.z

    def show(self):
        fill(255)
        noStroke()
        
        self.sx = map(self.x/self.z,0,1,0,width)
        self.sy = map(self.y/self.z,0,1,0,height)
        self.r  = map(self.z, 0, width, 12,0)
        
        ellipse(self.sx,self.sy,self.r,self.r)
            
        self.px = map(self.x/self.pz,0,1,0,width)
        self.py = map(self.y/self.pz,0,1,0,height)
        
        self.pz = self.z
        stroke(255)
        strokeWeight(4)
        line(self.px,self.py,self.sx,self.sy)

stars = []
speed = 0

def setup():
    global stars
    size(800,800,P2D)
    
    for i in range(800):
        stars.append(Star())
    
def draw():
    global speed
    speed = map(mouseX, 0,width, 0, 40)
    
    
    background(0)
    translate(width/2,height/2)
    
    for i in range(len(stars)):
        stars[i].update()
        stars[i].show()
