add_library('peasycam')

res = 50 #try 20 with points high strokeWeight and point(x,y,z) #CREATES REALLY COOL EFFECT
r = float(200)

cam = 0

globe = []

def setup():
    global cam
    global globe

    size(600, 600, P3D)
    colorMode(HSB)
    cam = PeasyCam(this, 500)
    
    for i in range(res+1):
        globe.append([])
        for j in range(res+1):
            globe[i].append(0)

def draw():
    global globe
    
    noStroke()
    background(0)
    lights()
    

    for i in range(res+1):
        lat = map(i, 0, res, 0, PI)
        for j in range(res+1):
            lon = map(j, 0, res, 0, TWO_PI)

            x = r * sin(lat) * cos(lon)
            y = r * sin(lat) * sin(lon)
            z = r * cos(lat)

            globe[i][j] = PVector(x,y,z)
            
    for i in range(res):
        hu = map(i,0,res,0,255*6)
        fill(hu%255,255,255)
        
        beginShape(TRIANGLE_STRIP)
        for j in range(res+1):
            v1 = globe[i][j]
            v2 = globe[i+1][j]
            
            vertex(v1.x,v1.y,v1.z)
            vertex(v2.x,v2.y,v2.z)
                     

        endShape()
            
            
