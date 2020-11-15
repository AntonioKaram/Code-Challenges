bird = 0
pipes = []
score  = 0

def setup():
    global bird
    
    
    size(800,750,P2D)
    
    bird = Bird()
    
    
    
def draw():
    global pipes
    global score
    
    background(0)
    
    if frameCount % 60 == 0:
        pipes.append(Pipe())
    
    for i in range(len(pipes)):
        pipes[-i].update()
        pipes[-i].show()
    
        
        if pipes[i].offscreen == True:
            pipes.pop(i)
            
        if pipes[-i].hits(bird):
            pipes = []
            score = 0
            bird.y = height/2
            bird.x = 164
            break
        
    if frameCount%60 == 0:
        if bird.x > pipes[0].x:
            score +=1

    bird.update()
    bird.show()
    
    textSize(24)
    text(("Score: "+str(score)), 10, 30)
    
    
    
def keyPressed():
    if key == " ":
       bird.up() 
        
        
    
    
class Bird:
    def __init__(self):
        self.y = height/2
        self.x = 164
        self.r = 14
        self.gravity = 1
        self.vel  = 0
        self.lift = -20
        
    def show(self):
        fill(255)
        ellipse(self.x,self.y,self.r,self.r)
        
    def update(self):
        self.vel += self.gravity
        self.vel *= 0.85
        self.y += self.vel
        
        
        if self.y > height:
            self.y = height
            self.vel = 0
            
        if self.y < 0:
            self.y = 0
            self.vel = 0
            
    def up(self):
        self.vel += self.lift
        
        
class Pipe:
    def __init__(self):
        
        
        self.x = width
        self.w = 20
        self.speed = 3
        self.highlight = False
        self.space = random(28,height/2)
        
        if random(1) > 0.5:
            self.top = height/2 - self.space
            self.bottom = height/2 #+ self.space/4
        else:
            self.bottom = height/2 - self.space
            self.top = height/2 #+ self.space/2
        
    def show(self):
        fill(255,0,0)

        rect(self.x,0,self.w,self.top)
        rect(self.x,height-self.bottom,self.w,self.bottom)
        
    def update(self):
        self.x -= self.speed
        
    def offscreen(self):
        if self.x < -self.w:
            return True
        else:
            return False
        
    def hits(self,bird):
        if bird.y < self.top or bird.y  > height-self.bottom:
            if bird.x > self.x and bird.x < self.x +self.w:
                return True
                self.highlight = True
        else:
            return False
            #self.hightlight = False
        
        
    
        
