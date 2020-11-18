popul = 0
count = 0
lifespan = 400
lifeText = 0

target = 0

o1x = 150
o1y = 150
o1w = 10
o1h = 400

o2x = 850
o2y = 150
o2w = 10
o2h = 400

o3x = 300
o3y = 350
o3w = 400
o3h = 10 




maxForce = 0.2

generation = 0




def setup():
    global popul
    global target

    size(1000, 700, P2D)

    popul = Population()
    target = PVector(width / 2, 150)


def draw():
    global popul
    global count
    global generation
    
    background(0)

    popul.run()

    textSize(12)
    text(str(count), 10, 30)
    text(str(generation), 10, 50)
    fill(255)
    
    rect(o1x,o1y,o1w,o1h)
    rect(o2x,o2y,o2w,o2h)
    rect(o3x,o3y,o3w,o3h)
    ellipse(target.x, target.y, 16, 16)
    
    count += 1
    if count == lifespan:
        popul.evaluate()
        popul.selection()
        count = 0
        generation += 1


class Population:

    def __init__(self):
        self.rockets = []
        self.popSize = 75
        self.matingpool = []

        for i in range(self.popSize):
            self.rockets.append(Rocket(None))

    def run(self):
        for rocket in self.rockets:
            rocket.update()
            rocket.sho1w()

    def evaluate(self):
        maxfit = 0

        for rocket in self.rockets:  # TRY MAKING ONE LOOP
            rocket.calcFitness()

            if rocket.fitness > maxfit:
                maxfit = rocket.fitness

            rocket.fitness /= maxfit

        self.matingpool = []

        for rocket in self.rockets:
            n = int(rocket.fitness * 100)
            for j in range(n):
                self.matingpool.append(rocket)
            
            print(rocket.fitness)
                
    def selection(self):
        newRockets = []

        for i in range(len(self.rockets)):
            indexA = int(random(len(self.matingpool)))
            parentA = self.matingpool[indexA].dna

            indexB = int(random(len(self.matingpool)))
            parentB = self.matingpool[indexB].dna

            child = parentA.crossover(parentB)
            child.mutation()

            newRockets.append(Rocket(child))

        self.rockets = newRockets


class Rocket:

    def __init__(self, dna):
        self.pos = PVector(width / 2, height)
        self.vel = PVector()
        self.acc = PVector()
        self.fitness = 0
        self.crashed = False
        self.completed = False
        self.hitEdge = False
        
        if dna != None:
            self.dna = dna
        else:
            self.dna = DNA(None)

    def calcFitness(self):
        d = dist(self.pos.x, self.pos.y, target.x, target.y)

        self.fitness = map(d, 0, width, width, 1)
        
        if self.completed == True:
            self.fitness *= 60
            
        if self.crashed == True:
            self.fitness /=30
        if self.hitEdge == True:
            self.fitness /= 10

    def applyForce(self, force):
        self.acc.add(force)

    def update(self):
        d = dist(self.pos.x,self.pos.y,target.x,target.y)
        
        if d < 10:
            self.completed = True
            self.pos = target.copy()
        
        if self.pos.x >o1x and self.pos.x < o1x+o1w and self.pos.y > o1y and self.pos.y < o1y +o1h:
            self.crashed = True
            
        if self.pos.x >o2x and self.pos.x < o2x+o2w and self.pos.y > o2y and self.pos.y < o2y +o2h:
            self.crashed = True
        
        if self.pos.x >o3x and self.pos.x < o3x+o3w and self.pos.y > o3y and self.pos.y < o3y +o3h:
            self.crashed = True    
        
        if self.pos.x >= width or self.pos.x < 0: 
            self.hitEdge = True
        if self.pos.y > height + 25 or self.pos.y <0:
            self.hitEdge = True
        
        self.applyForce(self.dna.genes[count])
        
        if self.completed != True and self.crashed != True and self.hitEdge != True :
            self.vel.add(self.acc)
            self.pos.add(self.vel)
            self.acc.mult(0)
            self.vel.limit(4)
            

    def sho1w(self):
        push()
        noStroke()
        fill(255, 150)
        translate(self.pos.x, self.pos.y)
        rotate(self.vel.heading())  # VERY IMPORTANT
        rectMode(CENTER)
        rect(0, 0, 25, 5)
        pop()

class DNA:

    def __init__(self, genes):
        if genes != None:
            self.genes = genes
        else:
            self.genes = []

            for i in range(lifespan):
                self.genes.append(PVector.random2D())
                self.genes[i].setMag(maxForce)

    def crossover(self, partner):
        newGenes = []
        midpoint = floor(random(len(self.genes)))

        for i in range(len(self.genes)):
            if i > midpoint:
                newGenes.append(self.genes[i])
            else:
                newGenes.append(partner.genes[i])

        return DNA(newGenes)
    
    def mutation(self):
        for i in range(len(self.genes)):
            if random(1) < 0.01:
                self.genes[i] = PVector.random2D()
                self.genes[i].setMag(maxForce)
                
                
                
    
