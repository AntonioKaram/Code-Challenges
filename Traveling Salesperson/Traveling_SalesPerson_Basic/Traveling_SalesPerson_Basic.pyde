cities = []
total_cities = 5

recordDistance = 0

bestEver = 0


def setup():
    global cities
    global bestEver
    global recordDistance

    size(500,500)
    
    for i in range(total_cities):
        cities.append(PVector(random(width),random(height)))
        
        
    recordDistance = calcDistance(cities)
    
    x = slice(len(cities))
    bestEver = cities[x]
    
    
def draw():
    global cities
    global bestEver
    global recordDistance
    
    background(0)
    fill(255)
    
    for i in range(len(cities)):
        ellipse(cities[i].x,cities[i].y,10,10)
        
       
    stroke(255)
    strokeWeight(2) 
    noFill()
    
    beginShape()
    
    for i in range(len(cities)):
        vertex(cities[i].x,cities[i].y)
    
    endShape()
    
    stroke(255,0,0)
    strokeWeight(4) 
    beginShape()
    
    for i in range(len(bestEver)):
        vertex(bestEver[i].x,bestEver[i].y)
    
    endShape()
    
    i = floor(random(len(cities)))
    j = floor(random(len(cities)))
    
    swap(cities,i,j)
    
    d = calcDistance(cities)
    
    if d < recordDistance:
        recordDistance = d
        
        x = slice(len(cities))
        bestEver = cities[x]
        print(recordDistance)
    
    
def swap(a,i,j):
     temp = a[i]
     a[i] = a[j]
     a[j] = temp
    
    
def calcDistance(points):
    sum = 0 
    
    for i in range(len(points)-1):
        d = dist(points[i].x,points[i].y,points[i+1].x,points[i+1].y)
        sum+= d
        
    return sum
        
    
    
    
