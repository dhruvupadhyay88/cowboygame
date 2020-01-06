import pygame
import random

pygame.init()
#pygame.mixer.pre_init(44100, -16, 1, 512)
#pygame.mixer.init()
win = pygame.display.set_mode((1400,800))
pygame.display.set_caption("Cowboy Game")

#pygame.mixer.music.load('bgmusic.wav')        #loads background music if uncommented
#pygame.mixer.music.play(-1)
 



clock = pygame.time.Clock()

run_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png'),pygame.image.load('R10.png')]
run_left = [pygame.transform.flip(run_right[0],1,0),pygame.transform.flip(run_right[1],1,0),pygame.transform.flip(run_right[2],1,0),pygame.transform.flip(run_right[3],1,0),pygame.transform.flip(run_right[4],1,0),pygame.transform.flip(run_right[5],1,0),pygame.transform.flip(run_right[6],1,0),pygame.transform.flip(run_right[7],1,0),pygame.transform.flip(run_right[8],1,0),pygame.transform.flip(run_right[9],1,0)]
slide_right = [pygame.image.load('S1.png'), pygame.image.load('S2.png'), pygame.image.load('S3.png'), pygame.image.load('S4.png'), pygame.image.load('S5.png'), pygame.image.load('S6.png'), pygame.image.load('S7.png'), pygame.image.load('S8.png'), pygame.image.load('S9.png'),pygame.image.load('S10.png')]
slide_left = [pygame.transform.flip(slide_right[0],1,0),pygame.transform.flip(slide_right[1],1,0),pygame.transform.flip(slide_right[2],1,0),pygame.transform.flip(slide_right[3],1,0),pygame.transform.flip(slide_right[4],1,0),pygame.transform.flip(slide_right[5],1,0),pygame.transform.flip(slide_right[6],1,0),pygame.transform.flip(slide_right[7],1,0),pygame.transform.flip(slide_right[8],1,0),pygame.transform.flip(slide_right[9],1,0)]
idle = [pygame.image.load('I.png'),pygame.transform.flip((pygame.image.load('I.png')),1,0)]

cannonball = pygame.transform.scale(pygame.image.load('cannonball.png'),(100,70))
tumbleweed = pygame.image.load('T1.png')
bomb = pygame.transform.scale(pygame.image.load('B1.png'),(100,100))
explosion = [pygame.image.load('tile000.png'),pygame.image.load('tile001.png'),pygame.image.load('tile002.png'),pygame.image.load('tile003.png'),pygame.image.load('tile004.png'),pygame.image.load('tile005.png'),pygame.image.load('tile006.png'),pygame.image.load('tile007.png'),pygame.image.load('tile008.png'),pygame.image.load('tile009.png'),pygame.image.load('tile010.png'),pygame.image.load('tile011.png'),pygame.image.load('tile012.png'),pygame.image.load('tile013.png'),pygame.image.load('tile014.png'),pygame.image.load('tile015.png'),pygame.image.load('tile016.png'),pygame.image.load('tile017.png'),pygame.image.load('tile018.png'),pygame.image.load('tile019.png')]

bg = pygame.transform.scale(pygame.image.load('bg.jpg'),(1400,800))
heart_pic = pygame.transform.scale(pygame.image.load('heart.png'),(100,100))


for i in range(len(run_right)):
    run_right[i] = pygame.transform.scale(run_right[i],(160,160))
    run_left[i] = pygame.transform.scale(run_left[i],(160,160))
    slide_left[i] = pygame.transform.scale(slide_left[i],(150,90))
    slide_right[i] = pygame.transform.scale(slide_right[i],(150,90))
    try:
        idle[i] = pygame.transform.scale(idle[i],(130,150))
    except:
       continue
    

class Player():           
    
    def __init__(self,x,y,vel):
        self.walkcount = 0
        self.right = False
        self.left = False
        self.slide = False
        self.jump = False
        self.last = 0
        self.jumpCount = 10
        
        self.x = x
        self.y = y
        self.vel = vel
        self.width = 110
        self.height = 140
        self.hitbox = (self.x,self.y,self.width,self.height)
                
    def drawPlayer(self,x,y):
        

        win.blit(bg,(0,0))
        if self.walkcount > 29:
            self.walkcount = 0

        
        if self.left and self.slide:
            win.blit(slide_left[self.walkcount//3],(x,y))
            self.walkcount += 1
            self.width, self.height = 160, 40
            self.hitbox = (self.x,self.y+65,self.width-5,self.height+50)
        elif self.right and self.slide:
            win.blit(slide_right[self.walkcount//3],(x,y))
            self.walkcount += 1
            self.width, self.height = 160, 80
            self.hitbox = (self.x,self.y+65,self.width-5,self.height+10)
        elif self.left:
            win.blit(run_left[self.walkcount//3],(x,y))
            self.walkcount += 1
            self.width, self.height = 110, 140
            self.hitbox = (self.x+20,self.y,self.width-5,self.height+10)
        elif self.right:
            win.blit(run_right[self.walkcount//3],(x,y))
            self.walkcount += 1
            self.width, self.height = 110, 140
            self.hitbox = (self.x+35,self.y,self.width-5,self.height+10)
        else:
            win.blit(idle[man.last],(x,y))
            self.walkcount = 0
            self.width, self.height = 110, 140
            self.hitbox = (self.x+10,self.y,self.width-5,self.height+10)
            
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)            this shows hitboxes if uncommented

    
        

class Cannonball():
    def __init__(self):
        self.x = 1500
        self.y = random.randint(510,550)
        self.vel = random.randint(20,40)
        self.width = 70
        self.height = 70
        self.hitbox = (self.x+15,self.y,self.width,self.height)
        self.visible = False
        self.collide = False
        
    def drawCannonball(self):
        
        win.blit(cannonball,(self.x,self.y))
        self.hitbox = (self.x+15,self.y,self.width,self.height)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        self.x-=self.vel
        
    def reset(self): #reset the position
        self.x = 1500
        self.y = random.randint(510,550)
        self.vel = random.randint(20,40)

    

class Tumbleweed():
    def __init__(self):
        self.x = 1500
        self.vel = random.randint(15,30)
        self.width = random.randint(120,220)
        self.height = self.width
        self.y = (690-self.width)
        self.hitbox = (self.x+0.1*self.width,self.y+15,self.width*0.7,self.height*0.8)
        self.visible = False
        self.collide = False
        self.drawcount = 1
        self.drawing = pygame.transform.scale(tumbleweed,(self.width,self.width))

    def drawTumbleweed(self):
        if self.drawcount > 4:
            self.drawcount = 1

        win.blit(pygame.transform.rotate(self.drawing,90*self.drawcount),(self.x,self.y))
        self.hitbox = (self.x+0.1*self.width,self.y+15,self.width*0.7,self.height*0.8)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        self.x -= self.vel
        self.drawcount+=1

    def reset(self): 
        self.__init__()

class Bomb():
    def __init__(self):
        self.x = random.randint(100,1000)
        self.y = -100
        self.width = 100
        self.height = 100
        self.vel = 10
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.bomb_visible = False
        self.bomb_collide = False
        self.explosion_visible = False
        self.explosion_collide = False
        self.count = 0
        self.bcount = 1

    def drawBomb(self):
        self.vel = self.bcount**2 * 0.05
        win.blit(bomb,(self.x,self.y))
        self.hitbox = (self.x,self.y,self.width-15,self.height)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        self.y+=self.vel
        self.bcount += 1

    def drawExplosion(self):
        global score
        if self.count == 20:
            if not(self.explosion_collide):
                score+=1
            self.reset()
            
        else:
            win.blit(pygame.transform.scale(explosion[self.count],(200,200)),(self.x-65,self.y-80))
            self.hitbox = (self.x-60,self.y-75,190,190)
            #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        self.count+=1

    def reset(self):
        self.__init__()
                   
def gotHit():
    global end
    end-=1
    health[end] = False
    


def healthBar():
    global health
    x = 20
    y = 20
    
    for heart in health:
        if heart:
            win.blit(heart_pic,(x,y))
            x+=120
    if health[0] == False:
        return False
    else:
        return True
           
    

def showScore():
    scoretext = font1.render('Score: '+ str(score),1,(0,0,0))
    win.blit(scoretext,(1100,10))

def showHighScore():
    highscoretext = font2.render('Current High Score: '+ str(highscore),1,(0,0,0))
    win.blit(highscoretext,(600,10))

def updateHighScore():
    global score
    if score > highscore:
        f = open('highscore.txt','w')
        f.write(str(score))
        f.close()


    
    

while True:

    file = open('highscore.txt','r')
    highscore = int(file.read())
    file.close()

    font1 = pygame.font.SysFont('comicsans', 35, True)
    font2 = pygame.font.SysFont('comicsans',20)
    font3 = pygame.font.SysFont('comicsans', 150, True)
    health = [True,True,True]
    end = 0
    score = 0

    man = Player(600,550,15)
    ball = Cannonball()
    tweed = Tumbleweed()
    boom = Bomb()

    
    run = True
    while run:
        
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and man.x>20:
            man.x-= man.vel
            man.left = True
            man.right = False
            man.last = 1
        elif keys[pygame.K_RIGHT] and man.x<1400-150:
            man.x+= man.vel
            man.right = True
            man.left = False
            man.last = 0
        else:
            man.right = False
            man.left = False
            man.walkcount = 0

        man.slide = False
        if keys[pygame.K_DOWN] and (man.left or man.right) and not(man.jump):
            man.slide = True
            

        if keys[pygame.K_UP]:
            man.jump = True
       
        if man.jump:
            if man.jumpCount >= -10:
                man.y-= ((man.jumpCount*abs(man.jumpCount))*0.7)
                man.jumpCount-=1
            else:
                man.jump = False
                man.jumpCount = 10
                
        if man.slide:       
            man.drawPlayer(man.x,man.y+60)
        else:
            man.drawPlayer(man.x,man.y)                     
        
        
        num = random.randint(1,50)  
        if num == 1 and not(ball.visible) :
            ball.visible = True
            ball.collide = False
            
        
        
        elif num == 2 and not(tweed.visible):
            tweed.visible = True
            tweed.collide = False

        elif num == 3 and not(boom.bomb_visible) and not(boom.explosion_visible):
            boom.bomb_visible = True
            boom.bomb_collide = False
            


        if ball.visible == True:
            ball.drawCannonball()
        if not(ball.collide):
            if ( ball.hitbox[0] > man.hitbox[0] and ball.hitbox[0] < man.hitbox[0] + man.hitbox[2] ) or ( ball.hitbox[0] + ball.hitbox[2] > man.hitbox[0] and ball.hitbox[0]+ ball.hitbox[2] < man.hitbox[0] + man.hitbox[2] ):
                if ( ball.hitbox[1] > man.hitbox[1] and ball.hitbox[1] < man.hitbox[1] + man.hitbox[3] ) or ( ball.hitbox[1] + ball.hitbox[3] > man.hitbox[1] and ball.hitbox[1] + ball.hitbox[3] < man.hitbox[1] + man.hitbox[3] ):
                    gotHit()
                    ball.collide = True
                    ball.visible = False
                    ball.reset()
                    
            if ball.hitbox[0] <= -10:
                ball.collide = True
                ball.visible = False
                ball.reset()
                score+=1


        if tweed.visible == True:
            tweed.drawTumbleweed()
        if not(tweed.collide):
            if ( tweed.hitbox[0] > man.hitbox[0] and tweed.hitbox[0] < man.hitbox[0] + man.hitbox[2] ) or ( tweed.hitbox[0] + tweed.hitbox[2] > man.hitbox[0] and tweed.hitbox[0]+ tweed.hitbox[2] < man.hitbox[0] + man.hitbox[2] ):
                if ( tweed.hitbox[1] > man.hitbox[1] and tweed.hitbox[1] < man.hitbox[1] + man.hitbox[3] ) or ( tweed.hitbox[1] + tweed.hitbox[3] > man.hitbox[1] and tweed.hitbox[1] + tweed.hitbox[3] < man.hitbox[1] + man.hitbox[3] ):
                    gotHit()
                    tweed.reset()
                    
            if tweed.hitbox[0] <= -10:
                tweed.reset()
                score+=1

        if boom.bomb_visible == True:
            boom.drawBomb()
        if not(boom.bomb_collide):
            if ( boom.hitbox[0] > man.hitbox[0] and boom.hitbox[0] < man.hitbox[0] + man.hitbox[2] ) or ( boom.hitbox[0] + boom.hitbox[2] > man.hitbox[0] and boom.hitbox[0]+ boom.hitbox[2] < man.hitbox[0] + man.hitbox[2] ):
                if ( boom.hitbox[1] > man.hitbox[1] and boom.hitbox[1] < man.hitbox[1] + man.hitbox[3] ) or ( boom.hitbox[1] + boom.hitbox[3] > man.hitbox[1] and boom.hitbox[1] + boom.hitbox[3] < man.hitbox[1] + man.hitbox[3] ):
                    boom.explosion_visible = True
                    boom.bomb_visible = False
                    
                    
            if boom.hitbox[1] >= 500:
                boom.explosion_visible = True
                boom.bomb_visible = False
                

                
                

        if boom.explosion_visible == True:
            boom.drawExplosion()
        if not(boom.explosion_collide):
            if ( boom.hitbox[0] > man.hitbox[0] and boom.hitbox[0] < man.hitbox[0] + man.hitbox[2] ) or ( boom.hitbox[0] + boom.hitbox[2] > man.hitbox[0] and boom.hitbox[0]+ boom.hitbox[2] < man.hitbox[0] + man.hitbox[2] ):
                if ( boom.hitbox[1] > man.hitbox[1] and boom.hitbox[1] < man.hitbox[1] + man.hitbox[3] ) or ( boom.hitbox[1] + boom.hitbox[3] > man.hitbox[1] and boom.hitbox[1] + boom.hitbox[3] < man.hitbox[1] + man.hitbox[3] ):
                    gotHit()
                    boom.explosion_collide = True
                    
                    

        if not(healthBar()):
            run = False
        showScore()     
        showHighScore()
           
                
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             
    gameover = font3.render('GAME OVER',1,(255,0,0))
    win.blit(gameover,(300,300))
    updateHighScore()
    pygame.display.update()
    pygame.time.delay(3000)
    

    
    



pygame.quit()





    
