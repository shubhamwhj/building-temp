import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
  
building = pygame.Rect(5,200,30,400)


#create a funtion drawBuilding

#screen.fill((50,150,255))
    
while True:    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #call the drawBuilding function
            
  
   
    pygame.display.update()
    clock.tick(30)
    
    
    
    

