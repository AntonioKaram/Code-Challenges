import sys
import pygame
import random
import math as m
from pygame.locals import *

#Colors
white = [255,255,255]
black = [0,0,0]
red = [206, 32, 41]
green = [0,155,0]
yellow = [255, 225, 124]
orange = [255, 102, 75]
brick = [144, 56, 67]
skin = [255, 252, 175]
lime = [0,255,0]
blue = [0,0,204]
pink = [255,0,127]

colors = [red,green,yellow,orange,brick,skin,lime,blue,pink]

# this code only needs to be ran once
pygame.init()
width = 1400
height = 800
window = pygame.display.set_mode((width,height),RESIZABLE)
clock = pygame.time.Clock()
FPS = 240

#Scaling Variables
velocity = random.choice(range(-15,-10))
numP = 100
Gsmall = pygame.math.Vector2(0,0.1)
Gbig = pygame.math.Vector2(0,0.2)

#Environmental Variables
fireworks = []

#Background
Background = pygame.Surface((width,height))                 
Background.fill(black)           
window.blit(Background, (0,0))

class Particle:
    def __init__(self,x,y,col,firework):
        self.pos = pygame.math.Vector2(x,y)
        self.firework = firework
        self.lifespan = 255
        self.a = 1
        self.col = col
        if self.firework:
            self.vel = pygame.math.Vector2(0,velocity)
            self.size = 4
        else:
            self.vel = pygame.math.Vector2(random.uniform(-1,1),random.uniform(-1,1))
            self.vel *= random.choice(range(2,8))
            self.size = 1

        self.acc = pygame.math.Vector2(0,0)

    def applyForce(self,force):
        self.acc += force

    def done(self):
        if self.lifespan < 0:
            return True
        else:
            return False

    def update(self):
        if self.firework != True:
            self.vel *= (0.95)
            self.lifespan -= 4
            self.a += 0.05
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def show(self):
        if self.firework != True:
            if self.lifespan >= 0:
                colorList = self.col
                a = -self.a
                r = m.floor((colorList[1] - (1-a)*255)/a)-255
                g = m.floor((colorList[2] - (1-a)*255)/a)-255
                b = m.floor((colorList[0] - (1-a)*255)/a)-255
                color = (r,g,b)
                if r>=0 and g >= 0 and b>=0:
                    pygame.draw.circle(window,color,(int(self.pos.x),int(self.pos.y)),self.size)

                    
      
        else:
            color = self.col
            pygame.draw.circle(window,color,(int(self.pos.x),int(self.pos.y)),self.size)
            

class Firework:
    def __init__(self):
        self.color = random.choice(colors)
        self.firework = Particle(random.choice(range(width)),height,self.color,True)
        self.exploded = False
        self.particles = []

    def update(self):
        if self.exploded != True :
            self.firework.applyForce(Gbig)
            self.firework.update()

            if self.firework.vel.y > 0:
                self.exploded = True
                self.explode()

        for i in reversed(range(len(self.particles))):
            self.particles[i].applyForce(Gsmall)
            self.particles[i].update()

            if self.particles[i].done():
                self.particles.pop(i)

    def done(self):
        if self.exploded and len(self.particles) ==  0 :
            return True
        else:
            return False
                

    def explode(self):
        for i in range(numP):
            p = Particle(self.firework.pos.x,self.firework.pos.y,self.color, False)
            self.particles.append(p)
            
        

    def show(self):
        if self.exploded != True:
            self.firework.show()

        for i in range(len(self.particles)):
            self.particles[i].show()
        
while True:
    #allows user to exit the screen
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
   # this code should be ran every frame
    Background.set_alpha(25)
    #Background.fill(black)           
    window.blit(Background, (0,0))

    if random.random() < 0.025:
        fireworks.append(Firework())
        
    for i in reversed(range(len(fireworks))):
        fireworks[i].update()
        fireworks[i].show()

        if fireworks[i].done():
            fireworks.pop(i)

        
    pygame.display.update()
    clock.tick(FPS)

































