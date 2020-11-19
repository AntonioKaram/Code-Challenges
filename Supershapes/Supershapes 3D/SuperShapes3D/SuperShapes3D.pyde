add_library('peasycam')



res = 50

r = 200

a1a = 1
a2a = 1

b1a = 1
b2a = 1

a1b = 1
a2b = 1

b1b = 1
b2b = 1


m1a = 7
m2a = 7
n1a = 0.2
n2a = 1.7
n3a = 1.7
n4a = 0.2
n5a = 1.7
n6a = 1.7

m1b = 6
m2b = 2
n1b = 60
n2b = 100
n3b = 30
n4b = 10
n5b = 10
n6b = 10


mc =0
offset = 0 

cam = 0

globe = []

def setup():
    global cam
    global globe

    size(600, 600, P3D)
    colorMode(HSB)
    cam = PeasyCam(this, 500)

    for i in range(res + 1):
        globe.append([])
        for j in range(res + 1):
            globe[i].append(0)

def draw():
    global globe
    global offset
    global mc
    global m
    
    
    m1 = map(sin(mc),-1,1,m1a,m1b)
    m2 = map(sin(mc),-1,1,m2a,m2b)
    
    n1 = map(sin(mc),-1,1,n1a,n1b)
    n2 = map(sin(mc),-1,1,n2a,n2b)
    n3 = map(sin(mc),-1,1,n3a,n3b)
    n4 = map(sin(mc),-1,1,n4a,n4b)
    n5 = map(sin(mc),-1,1,n5a,n5b)
    n6 = map(sin(mc),-1,1,n6a,n6b)
    
    a1 = map(sin(mc),-1,1,a1a,a1b)
    a2 = map(sin(mc),-1,1,a2a,a2b)
    
    b1 = map(sin(mc),-1,1,b1a,b1b)
    b2 = map(sin(mc),-1,1,b2a,b2b)
    
    
    
    
    mc += 0.09
    
    noStroke()
    background(0)
    lights()

    for i in range(res + 1):
        lat = map(i, 0, res, -HALF_PI, HALF_PI)
        r2 = float(supershape(lat, m1, n1, n2, n3,a1,b1))
        for j in range(res + 1):
            lon = map(j, 0, res, -PI, PI)

            r1 = float(supershape(lon, m2, n4, n5, n6,a2,b2))

            x = r * r1 * cos(lon) * r2 * cos(lat)
            y = r * r1 * sin(lon) * r2 * cos(lat)
            z = r * r2 * sin(lat)

            globe[i][j] = PVector(x, y, z)

    
    for i in range(res):
        hu = map(i,0,res,0,255*6)
        fill((hu+offset)%255,255,255)

        beginShape(TRIANGLE_STRIP)
        for j in range(res + 1):
            v1 = globe[i][j]
            v2 = globe[i + 1][j]

            vertex(v1.x, v1.y, v1.z)
            vertex(v2.x, v2.y, v2.z)

        endShape()


def supershape(theta, m, n1, n2, n3,a,b):
    m = float(m)
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    theta = float(theta)

    t1 = float(pow(abs((1 / a) * cos(m * theta / 4)), n2))
    t2 = float(pow(abs((1 / b) * sin(m * theta / 4)), n3))

    r = float(pow((t1 + t2), (-1 / n1)))

    return r







#r2 = float(supershape(lat, 2, 10, 10, 10))
#r1 = float(supershape(lon, 8, 60, 100, 30))
# try r = 20 with points heigh strokeWeight and point(x,y,z) CREATES REALLYCOOL EFFECT
#offset += 5
