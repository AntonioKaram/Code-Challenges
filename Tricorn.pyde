minVal = -2.5
maxVal = 2.5




def setup():
    size(800, 800,P2D)
    pixelDensity(1)


def keyPressed():
    global minVal
    global maxVal
    
    if keyCode == UP:
        minVal += -0.5
        maxVal += 0.5
    if keyCode == DOWN:
        minVal -= -0.5
        maxVal -= 0.5

def draw():
    
    loadPixels()
    maxIterations = 500
    for x in range(width):
        for y in range(height):
            a = map(x, 0, width, minVal, maxVal )
            b = map(y, 0, height, minVal, maxVal)

            zx = a
            zy = b

            n = 0
            
            while zx*zx + zy*zy <4  and n < maxIterations:
                xtemp = zx*zx - zy*zy + a
                zy = -2 * zx*zy + b
                zx = xtemp
                
                n += 1
                if abs(a + b) > 32 :
                    break
                
            
                
            #GrayScale    
            bright = map(n,0,maxIterations,0,1)      
            bright = map(sqrt(bright),0,1,0,255)
            if n == maxIterations :
                 bright = 0

        
                
                
            
            
            

            pix = x + (y * width)
            pixels[pix] = color(bright, 255)

    updatePixels()
