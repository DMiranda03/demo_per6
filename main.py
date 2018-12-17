# Sources:
#https://pythonspot.com/snake-with-pygame/
# https://medium.com/@jodylecompte/code-your-first-game-in-pygame-5585dfcc6388
from pygame.locals import *
from random import randint
import pygame
import time
 
class Fruit:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
#This class is for the fruit that the snake will eat.
 
 
class User:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3

    cCM = 2
    cC = 0


    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.gameend(-100)
           self.y.gameend(-100)
 
       # starting positions
       self.x[1] = 1*44
       self.x[2] = 2*44

 
    def c(self):
 
        self.cC = self.cC + 1
        if self.cC > self.cCM:
 
            # continuous change in length
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # change in head of snake as it gains length
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.cC = 0
 
 
    def mR(self):
        self.direction = 0
 
    def mL(self):
        self.direction = 1
 
    def mU(self):
        self.direction = 2
 
    def mD(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
class Game:
    def Crash(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

#Shows Webpage and display of functions.
class Game:
 
    windowWidth = 800
    windowHeight = 600
    user = 0
    fruit = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._fruit_surf = None
        self.game = Game()
        self.user = User(3) 
        self.fruit = Fruit(5,5)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("box.jpg").convert()
        self._fruit_surf = pygame.image.load("box.jpg").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.user.c()
 
    
        for i in range(0,self.user.length):
            if self.game.Crash(self.fruit.x,self.fruit.y,self.user.x[i], self.user.y[i],44):
                self.fruit.x = randint(2,9) * 44
                self.fruit.y = randint(2,9) * 44
                self.user.length = self.user.length + 1
 
 
        # does snake collide with itself?
        for i in range(2,self.user.length):
            if self.game.Crash(self.user.x[0],self.user.y[0],self.user.x[i], self.user.y[i],40):
                print("You lose!")
                print("x[0] (" + str(self.user.x[0]) + "," + str(self.user.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.user.x[i]) + "," + str(self.user.y[i]) + ")")
                exit(0)
 
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.user.draw(self._display_surf, self._image_surf)
        self.fruit.draw(self._display_surf, self._fruit_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.user.mR()
 
            if (keys[K_LEFT]):
                self.user.mL()
 
            if (keys[K_UP]):
                self.user.mU()
 
            if (keys[K_DOWN]):
                self.user.mD()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
 
            time.sleep (50.0 / 1000.0);
        self.on_cleanup()
 
if __name__ == "__main__" :
    theGame = Game()
    theGame.on_execute()


#Each class is defined and through those definitions, there are changes in the code.
#The class fruit allows for the fruit to be defined. The fruit appears on the screen in random areas.
#The goal of the game is for the snake to eat the fruit and gain length.
#The fruit after being eaten reappears in various areas.
#Therefore, there is the requirement of the creation of a procedure which allows for the fruit to move from place to place.
#As the snake changes gains length, certain issues arise.
#If the snake collides with itself it reduces in length.
#By gaining length, there has to be an update in the postion relative with grid.
#Class Game configures the entire game. It defines all areas of the program dealing with visual profeciency.
#It also allows for the movement of the snake using arrows as well as the delaying of loops yousing time.sleep.