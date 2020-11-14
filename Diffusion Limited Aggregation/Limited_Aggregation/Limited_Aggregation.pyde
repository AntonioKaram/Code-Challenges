r = 4

tree = []
walkers = []


def setup():
    global tree
    global walkers

    size(400, 400,P2D)

    tree.append(Walker(True, width / 2, height / 2))

    for i in xrange(200):
        pt = randomPoint()
        walkers.append(Walker(False, pt[0],pt[1]))


def draw():
    global tree
    global walkers

    background(0)

    for i in xrange(len(tree)):
        tree[i].show()
    
    for i in xrange(len(walkers)):
        walkers[i].show()
        
    
    for i in xrange(10):
        for a in xrange(len(walkers)-1):
            i = -a
            walkers[i].walk()

            if walkers[i].checkStuck(tree) == True:
                tree.append(walkers[i])
                walkers.pop(i)
                #walkers.append(Walker(False, random(width), random(height)))


        

class Walker:

    def __init__(self, stuck, x, y):  # Change variables if dimentions change
        self.pos = PVector(x, y)
        self.stuck = stuck

    def walk(self):
        vel = PVector.random2D()
        vel.mult(5)
        self.pos.add(vel)

        self.pos.x = constrain(self.pos.x, 0, width)
        self.pos.y = constrain(self.pos.y, 0, height)

    def checkStuck(self, others):
        for i in xrange(len(others)):
            d = PVector.dist(self.pos, others[i].pos)
            if d < (r * 2):
                self.stuck = True
                break

        return self.stuck

    def show(self):
        
        if self.stuck == True:
            stroke(255,0,0)
            fill(255,0,0)
        else:
            fill(255)
            stroke(255)
        ellipse(self.pos.x, self.pos.y, r * 2, r * 2)
        
        
        
def randomPoint():
    i =  floor(random(4))
    lst = []
    
    if i == 0:
        lst = [random(width),0]
    elif i == 1:
        lst = [random(width),height]
    elif i == 2:
        lst = [0,random(height)]
    else: 
        lst = [width,random(height)]
        
    return lst
        
    
    
    
    
    
    
    
    
    
        
        
