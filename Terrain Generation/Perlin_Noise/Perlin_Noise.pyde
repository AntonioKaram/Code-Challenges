flying = 0
wMesh = 2000
hMesh = 2000 
cols = None
rows = None
scl = 20

terrain = []

def setup():
    global terrain
    global cols
    global rows
    size(600,600,P3D)
    
    cols = wMesh/scl
    rows = hMesh/scl
    
     
    for x in range(cols):
        terrain.append([])
        for y in range(rows):
            terrain[x].append([])
            
     
        
        
    
    
def draw():
    global flying 
    
    flying -= 0.25
    yoff = flying
    xoff = 0
    for y in range(rows):
        xoff = 0
        for x in range(cols):
            terrain[x][y] = map(noise(xoff,yoff),0,1, -100,100)
            xoff+= 0.2
        yoff += 0.2
    
    
    
    background(0)
    stroke(255)
    noFill()
    
    translate(width/2,height/2+50)
    rotateX(PI/3)
    #rotaleY(PI/6)
    translate(-wMesh/2,-hMesh/2)
    
    
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl,y*scl,terrain[x][y])
            vertex(x*scl,(y+1)*scl,terrain[x][y+1])
        endShape()
