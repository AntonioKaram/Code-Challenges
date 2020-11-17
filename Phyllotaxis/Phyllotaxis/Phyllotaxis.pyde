n = 0
c = 5



def setup():
    global cam
    size(1000, 1000, P3D)  # TRY MAKING IT 3D
    background(0)

    
def draw():
    global n
    
    

    a = n * 137.5
    r = c * sqrt(n)
    x = floor((r * cos(a)) + width / 2)
    y = floor((r * sin(a)) + height / 2)
    z = floor((r * cos(a*PI)) + width/2)
    col = color(r%256,n%256,n%256)
    
    fill(col)
    stroke(0)
    ellipse(x,y,10,10)

                 
        
    n+=1
    
    # color = (r%256,r%256,r%256)
    # color = (r%256,a%256,a%256
    # color = (r%256,a%256,n%256)
    # color = (r%256,n%256,a%256)
    # color = (r%256,r%256,a%256)
    # color = (r%256,a%256,r%256)
    # color = (r%256,r%256,n%256)
    # color = (r%256,n%256,r%256)
    # color = (a%256,a%256,a%256)
    # color = (a%256,r%256,r%256)
    # color = (a%256,n%256,n%256)
    # color = (a%256,r%256,n%256)
    # color = (a%256,n%256,r%256)
    # color = (a%256,a%256,r%256)
    # color = (a%256,r%256,a%256)
    # color = (a%256,n%256,a%256)
    # color = (a%256,a%256,n%256)
    # color = (n%256,n%256,n%256)
    # color = (n%256,n%256,r%256)
    # color = (n%256,r%256,n%256)
    # color = (n%256,n%256,a%256)
    # color = (n%256,a%256,n%256)
    # color = (n%256,a%256,a%256)
    # color = (n%256,r%256,r%256)
    # color = (n%256,r%256,a%256)
    # color = (n%256,a%256,r%256)
