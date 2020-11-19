order = []
cities = []
total_cities = 10

totalPermutaions = 0


recordDistance = 0

bestEver = 0
count = 0


def setup():
    global order
    global cities
    global bestEver
    global recordDistance
    global totalPermutaions

    size(500, 700)

    for i in range(total_cities):
        cities.append(PVector(random(width), random(height / 2)))
        order.append(i)

    d = calcDistance(cities, order)
    recordDistance = d

    x = slice(len(order))
    bestEver = order[x]
   
    totalPermutaions = factorial(total_cities)
        
    print(totalPermutaions)
    


def draw():
    global count
    global order
    global cities
    global bestEver
    global recordDistance
    

    background(0)
    fill(255)

    #for i in range(len(cities)):
        #ellipse(cities[i].x, cities[i].y, 10, 10)

    stroke(255, 0, 0)
    strokeWeight(4)
    noFill()
    beginShape()

    for i in range(len(order)):
        n = bestEver[i]
        vertex(cities[n].x, cities[n].y)
        ellipse(cities[i].x, cities[i].y, 10, 10)

    endShape()

    translate(0, height / 2)
    stroke(255)
    strokeWeight(1)
    noFill()

    beginShape()

    for i in range(len(order)):
        n = order[i]
        vertex(cities[n].x, cities[n].y)
        ellipse(cities[i].x, cities[i].y, 10, 10)

    endShape()

    d = calcDistance(cities, order)

    if d < recordDistance:
        recordDistance = d
        x = slice(len(order))
        bestEver = order[x]
        
    

    nextOrder()
    fill(255)
    textSize(32)
    percent = 100 * (count/totalPermutaions) 
    #text(str(nf(percent,0,5))+"%",20,height/2-40)


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def calcDistance(points, ord):
    sum = 0

    for i in range(len(order) - 1):
        cityA = points[ord[i]]
        cityB = points[ord[i + 1]]
        d = dist(cityA.x, cityA.y, cityB.x, cityB.y)
        sum += d

    return sum

def nextOrder():
    global count
    global order
    
    count+= 1

    largestI = -1
    largestJ = -1

    for i in range(len(order) - 1):
        if order[i] < order[i + 1]:
            largestI = i

    if largestI == -1:
        print('finished')
        noLoop()

    for j in range(len(order)):
        if order[largestI] < order[j]:
            largestJ = j

    swap(order, largestI, largestJ)

    endArray = order[largestI + 1::]

    order = order[0:largestI + 1]
    endArray = endArray[::-1]
    order.extend(endArray)
    
    
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
