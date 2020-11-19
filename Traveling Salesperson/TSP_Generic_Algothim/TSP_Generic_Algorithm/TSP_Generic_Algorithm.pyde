cities = []
fitness = []
population = []

bestEver = 0
currentBest = []
total_cities = 10
populationSize = 400
recordDistance = 100000





def setup():
    global cities
    global population
    
    size(600, 700)

    order = [] 

    
    for i in range(total_cities):
        cities.append(PVector(random(width), random(height / 2)))
        order.append(i)
        
    for i in range(populationSize):
        population.append([])
        for j in range(total_cities):
            population[i].append(j)
            
    shuffle(population)


def draw():
    global Fitness
    global cities
    global bestEver
    global currentBest
    global recordDistance
    

    background(0)
    fill(255)
    
    calcFitness()
    normalizeFitness()
    nextGeneration() 


    stroke(255)
    strokeWeight(4)
    noFill()
    beginShape()

    for i in range(len(bestEver)):
        n = bestEver[i]
        vertex(cities[n].x, cities[n].y)
        ellipse(cities[i].x, cities[i].y, 10, 10)

    endShape()
    
    translate(0,height/2)
    stroke(255,0,0)
    strokeWeight(4)
    noFill()
    beginShape()

    for i in range(len(currentBest)):
        n = currentBest[i]
        vertex(cities[n].x, cities[n].y)
        ellipse(cities[i].x, cities[i].y, 10, 10)

    endShape()
 
    

def calcDistance(points, ord):
    sum = 0

    for i in range(len(ord) - 1):
        cityA = points[ord[i]]
        cityB = points[ord[i + 1]]
        d = dist(cityA.x, cityA.y, cityB.x, cityB.y)
        sum += d

    return sum


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    
    
def calcFitness():
    global Fitness
    global bestEver
    global currentBest
    global recordDistance
    
    for i in range(len(population)-1):
        currentRecord = 10000000
        
        d = calcDistance(cities,population[i])
        if d < recordDistance:
            recordDistance = d
            bestEver = population[i]
            
        if d < currentRecord:
            currentRecord = d
            currentBest = population[i] 
            
              
        fitness.append(1/(d+1))
        
def normalizeFitness():
    global Fitness 
    sum = 0 
    for i in range(len(fitness)-1):
        sum+= fitness[i]
        
    for i in range(len(fitness)-1):
        fitness[i] = fitness[i]/sum
        
def nextGeneration():
    global population
    newPopulation = []
    for i in range(len(population)-1):
        orderA = pickOne(population,fitness)
        orderB = pickOne(population,fitness)
        order = crossover(orderA,orderB)
        mutate(order,0.01)
        newpopulation = newPopulation.append(order)
        
    population = newPopulation
    
    
    
def pickOne(lst,probs):
    index = 0
    r = random(1)
    
    while(r>0 and index<len(lst)):
        r = r- probs[index] 
        index +=1
        
    index -=1

    
    return lst[index]



def mutate(lst,mutationRate):
    for i in range(total_cities):
        if random(1) < mutationRate:
            indexA = floor(random(len(lst)-1))
            indexB = indexA+1
            
            if indexB >= total_cities:
                indexB = 0
    
            tmp = lst[indexA]
            lst[indexA] = lst[indexB]
            lst[indexB] = tmp
    
    
def shuffle(lst):
  for i in range(0,len(lst)-1):
    for j in range(0,len(lst[i])-1):
      k = floor(random((len(lst[i])-1)))
      l = floor(random((len(lst[i])-1)))
      tmp = lst[i][k]
      lst[i][k] = lst[i][l]
      lst[i][l] = tmp
      
      
      
def crossover(orderA,orderB):
    start = floor(random(len(orderA)-1))
    nd = floor(random(start+1,len(orderA)-1))
    
    newOrder =  orderA[start:nd]

    
    for i in range(len(orderB)):
        city = orderB[i]
        
        if city not in newOrder:
            newOrder.append(city)
            
    return newOrder
            

    
