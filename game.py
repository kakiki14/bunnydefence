import pygame
import time
pygame.init()
screen = pygame.display.set_mode((640,480))

pos=[100,100]
bullets=[]  
fighter = pygame.image.load("resources\images\dude.png")
grass = pygame.image.load ("resources\images\grass.png")
castle = pygame.image.load("resources\images\castle.png")
bullet=pygame.image.load('resources\images\\bullet.png')
for i in range(1000):
   screen.fill(0)
   for y in range(0,5):
    for x in range(0,8):
     screen.blit(grass,(x*100,y*100))
    for b in bullets:
       screen.blit(bullet,b) 

   screen.blit(castle,(0,50))
   screen.blit(castle,(0,150))
   screen.blit(castle,(0,250))
   screen.blit(castle,(0,350))

   screen.blit(fighter,pos)
   pygame.display.flip()
   for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pos[1] -= 10
            if event.key == pygame.K_DOWN:
                pos[1] += 10
            if event.key == pygame.K_LEFT:
                pos[0] -= 10
            if event.key == pygame.K_RIGHT:
                pos[0] += 10
            if event.key == pygame.K_SPACE:
               bullets.append([pos[0]+30,pos[1]+30]) 
   for b in bullets:
        b[0]+= 3         
   time.sleep(0.1)
