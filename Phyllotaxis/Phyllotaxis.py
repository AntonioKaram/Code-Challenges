import pygame
import sys
import math as m

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)


# this code only needs to be ran once
pygame.init()
width = 1000
height = 1000
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
FPS = 1000


n = 0
c = 5

window.fill(black)

while n<10000:
    #allows user to exit the screen
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
   # this code should be ran every frame
    

    a = n * 137.5
    #a = n * 137.3
    #a = n * 137.6
    r = c * m.sqrt(n)

    x = m.floor((r * m.cos(a)) + width/2)
    y = m.floor((r * m.sin(a)) + height/2)

    #color = (r%256,r%256,r%256)
    #color = (r%256,a%256,a%256)

    color = (r%256,n%256,n%256)

    #color = (r%256,a%256,n%256)
    #color = (r%256,n%256,a%256)
    #color = (r%256,r%256,a%256)
    #color = (r%256,a%256,r%256)
    #color = (r%256,r%256,n%256)
    #color = (r%256,n%256,r%256)
    #color = (a%256,a%256,a%256)
    #color = (a%256,r%256,r%256)
    #color = (a%256,n%256,n%256)
    #color = (a%256,r%256,n%256)
    #color = (a%256,n%256,r%256)
    #color = (a%256,a%256,r%256)
    #color = (a%256,r%256,a%256)
    #color = (a%256,n%256,a%256)
    #color = (a%256,a%256,n%256)
    #color = (n%256,n%256,n%256)
    #color = (n%256,n%256,r%256)
    #color = (n%256,r%256,n%256)
    #color = (n%256,n%256,a%256)
    #color = (n%256,a%256,n%256)
    #color = (n%256,a%256,a%256)
    #color = (n%256,r%256,r%256)
    #color = (n%256,r%256,a%256)
    #color = (n%256,a%256,r%256)
    
    
    
    pygame.draw.circle(window,black,(x,y),10)
    pygame.draw.circle(window,color,(x,y),8)

    n+=1
    pygame.display.update()
    clock.tick(FPS)

































