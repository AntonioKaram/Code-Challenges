grid = []
prev = []

dA = 1.0
dB = 0.5
feed = 0.025  # try 0.025
k = 0.062
time_step = 1

def setup():
    global grid
    global prev

    size(300,300,P2D)

    grid = []
    prev = []

    for i in xrange(width):
        grid.append([])
        prev.append([])
        for j in xrange(height):
            a = float(1)
            b = float(0)
            grid[i].append(Cell(a, b))
            prev[i].append(Cell(a, b))

    for n in xrange(10):
        startx = int(random(20, width - 20))
        starty = int(random(20, height - 20))

        for i in xrange(startx, startx + 10):
            for j in xrange(starty, starty + 10):
                a = float(1)
                b = float(1)

                grid[i][j] = Cell(a, b)
                prev[i][j] = Cell(a, b)


class Cell:

    def __init__(self, a_, b_):
        self.a = a_
        self.b = b_


def update():
    global prev
    global grid
    
    for i in xrange(1, width - 1):
        for j in xrange(1, height - 1):
            spot = prev[i][j]
            newspot = grid[i][j]

            a = float(spot.a)  # or does he mean self.a?
            b = float(spot.b)

            laplaceA = float(0)
            laplaceA += a * -1
            laplaceA += prev[i + 1][j].a * 0.2
            laplaceA += prev[i - 1][j].a * 0.2
            laplaceA += prev[i][j + 1].a * 0.2
            laplaceA += prev[i][j - 1].a * 0.2
            laplaceA += prev[i - 1][j - 1].a * 0.05
            laplaceA += prev[i + 1][j - 1].a * 0.05
            laplaceA += prev[i - 1][j + 1].a * 0.05
            laplaceA += prev[i + 1][j + 1].a * 0.05

            laplaceB = float(0)
            laplaceB += b * -1
            laplaceB += prev[i + 1][j].b * 0.2
            laplaceB += prev[i - 1][j].b * 0.2
            laplaceB += prev[i][j + 1].b * 0.2
            laplaceB += prev[i][j - 1].b * 0.2
            laplaceB += prev[i - 1][j - 1].b * 0.05
            laplaceB += prev[i + 1][j - 1].b * 0.05
            laplaceB += prev[i - 1][j + 1].b * 0.05
            laplaceB += prev[i + 1][j + 1].b * 0.05
            
            newspot.a = a + (dA*laplaceA - a*b*b + feed*(1-a))*1;
            newspot.b = b + (dB*laplaceB + a*b*b - (k+feed)*b)*1;

            newspot.a = constrain(newspot.a, 0, 1);
            newspot.b = constrain(newspot.b, 0, 1);

def swap():
    global prev
    global grid
    
    temp = prev
    prev = grid
    grid = temp


def draw():
    #print(frameRate)

    for i in xrange(1):
        update()
        swap()

    loadPixels()
    for i in xrange(width - 1):
        for j in xrange(height-1):
            spot = grid[i][j]
            a = spot.a
            b = spot.b

            pix = i + (j * width)
            pixels[pix] = color((a - b) * 255)

    updatePixels()
