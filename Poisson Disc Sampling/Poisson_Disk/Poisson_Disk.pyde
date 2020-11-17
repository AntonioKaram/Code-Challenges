r = 6
k = 30

grid = []
active = []
ordered = []

cols = 0
rows = 0

w = r / sqrt(2)  # 2 Being the number of dimentions

def setup():
    global cols
    global rows
    global grid
    global active
    global ordered

    size(750, 750)
    colorMode(HSB)

    # STEP 0
    cols = floor(width / w)
    rows = floor(height / w)

    for i in range(cols * rows):
        grid.append(None)

    # STEP 1
    x = width/2
    y = height/2
    i = floor(x / w)
    j = floor(y / w)

    pos = PVector(x, y)
    grid[i + (j * cols)] = pos
    active.append(pos)


def draw():
    background(0)

    # STEP 2
    for total in range(25):
        if len(active) > 0:
            randIndex = floor(random(len(active)))
            pos = active[randIndex]
            found = False

            for n in range(k):
                sample = PVector.random2D()
                m = random(r, 2 * r)
                sample.setMag(m)
                sample.add(pos)

                col = floor(sample.x / w)
                row = floor(sample.y / w)

                if col < cols and col > 0 and row < rows and row > 0:
                    ok = True
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            index = (col + i) + (row + j) * cols
                            if index < len(grid):
                                neighbor = grid[index]

                                if neighbor != None:
                                    d = PVector.dist(sample, neighbor)
                                    if d < r:
                                        ok = False

                    if ok == True:
                        found = True
                        grid[col + row * cols] = sample
                        active.append(sample)
                        ordered.append(sample)
                        

            if found == False:
                active.pop(randIndex)

    for i in range(len(ordered)):
        if ordered[i] != None:
            #stroke((i/100)%360,255,255)
            stroke((i)%360,255,255)
            strokeWeight(r*0.5)
            point(ordered[i].x, ordered[i].y)

    #for pt in active:
        #stroke(255, 0, 0)
        #strokeWeight(1)
        #point(pt.x, pt.y)
