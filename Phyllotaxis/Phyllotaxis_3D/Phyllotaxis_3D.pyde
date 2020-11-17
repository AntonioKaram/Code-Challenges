add_library('peasycam')

n = 0
c = 10


cam = 0
N = 1600
balls = []

class Ball:

    def __init__(self, x, y, z, col):
        self.pos = PVector(x, y, z)
        self.col = col
        
    def show(self):
        pushMatrix()
        fill(self.col)
        noStroke()
        translate(self.pos.x, self.pos.y, self.pos.z)
        sphere(10)
        popMatrix()

def setup():
    global cam
    size(1000, 1000, P3D)  # TRY MAKING IT 3D

    cam = PeasyCam(this, 500)
    
def draw():
    global balls
    global n

    
    background(0)
    translate(-width / 2, -height / 2, 0)
    lights()
    
    if n < N:
        a = n * 137.51
        r = c * sqrt(n)
        x = floor((r * cos(a)) + width / 2)
        y = floor((r * sin(a)) + height / 2)
        z =  r*sin(sin(a))
        col = color(r%256,n%256,n%256)

        balls.append(Ball(x,y,z,col))
    
        for ball in balls:
            ball.show()
            
    
                 
        
    n+=1

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #z = floor((r * cos(a*PI)) + width/2)
    #z = floor((r * cos(a*PI)) + width/2)
    #z = map(sin(a),-1,1,-300,300) 
    #z = map(tan(a),-1,1,-100,100) 
    #z = sqrt(abs(-x*x + y*y + r*r))
    
    
    
    
    
    
    
    
    
    
    
    
    
    # color = (r%256,r%256,r%256)
    # color = (r%256,a%256,a%256
    # color = (r%256,a%256,n%256)
    # color = (r%256,n%256,a%256)
    # color = (r%256,r%256,a%256)
    # color = (r%256,a%256,r%256)
    # color = (r%256,r%256,n%256)
    # color = (r%256,n%256,r%256)
    # color = (a%256,a%256,a%256)
    # color = (a%256,r%256,r%256)
    # color = (a%256,n%256,n%256)
    # color = (a%256,r%256,n%256)
    # color = (a%256,n%256,r%256)
    # color = (a%256,a%256,r%256)
    # color = (a%256,r%256,a%256)
    # color = (a%256,n%256,a%256)
    # color = (a%256,a%256,n%256)
    # color = (n%256,n%256,n%256)
    # color = (n%256,n%256,r%256)
    # color = (n%256,r%256,n%256)
    # color = (n%256,n%256,a%256)
    # color = (n%256,a%256,n%256)
    # color = (n%256,a%256,a%256)
    # color = (n%256,r%256,r%256)
    # color = (n%256,r%256,a%256)
    # color = (n%256,a%256,r%256)
