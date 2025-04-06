import pygame
import time
pygame.init()
screen = pygame.display.set_mode((640,480))

pos=[100,100]
fighter = pygame.image.load("resources\images\dude.png")
for i in range(1000):
   screen.fill(0)
   screen.blit(fighter,pos)
   pygame.display.flip()
   for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pos[1] -= 10
            if event.key == pygame.K_s:
                pos[1] += 10
            if event.key == pygame.K_a:
                pos[0] -= 10
            if event.key == pygame.K_d:
                pos[0] += 10
   time.sleep(0.1)
