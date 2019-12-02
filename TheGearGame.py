from vpython import *
#GlowScript 2.7 VPython

#Property of Carlos Guedes
#  & Eloi Leitao
#
#The Gear Game
#TSIW
#FAP 2019

score=0

frames = 0

ang = 0 #Flag to change the vector of rotation of the pointer
vetorRotationPointer = vector(0,0,1)

gears = []
createGears(3)

pointer = []
createPointer() #Arrow for the player to shoot

balls = []

createLine() #Line for the points

createBox() #Box for shoots
enemies = []

scr = label( pos=vec(-15,-15,0), text="Score: " + score )

dt = 0.1 # time step
omega = 0.5 # rotational speed

omegaForArrow = 1

newBall = button(bind = click, text = 'New Ball')

butCreated = False

while (True):
    rate(10)
    
    frames += 1
    
    scr.text = "Score: " + score
    
    if (score >= 500 and (butCreated == False)):
        nextLevel = button(bind = nextLevel, text = 'Next Level')
        butCreated = True
        
    if(frames % 30 == 0): #Create enemies 30 in 30 Frames
        createEnemy()
        
    for k in range(enemies.length): #Update of the enemies
        
        enemies[k].pos = enemies[k].pos + enemies[k].velocity*dt
        
        #print(enemies)
        
        if (enemies[k].pos.z >=20):
            enemies[k].visible = False
            enemies.splice(k,1)                 
            break
       
    for j in range(pointer.length): #Rotation of the pointer
        
        ang+=1
        
        if (ang == 30): 
            ang = 0
            
            vetorRotationPointer = -vetorRotationPointer
            
        pointer[j].rotate(axis=vetorRotationPointer, angle=omegaForArrow*dt)
        
    for i in range(gears.length):#Roll the gears
        
            gears[i].rotate(axis=vector(0,0,1), angle=omega*dt)

             
    for k in range (balls.length): #Interseptions
       
            balls[k].pos = balls[k].pos + balls[k].velocity*dt
            
            for i in range(gears.length):   
                
                #Collision with the Gears
               
                if ((balls[k].pos.x + balls[k].radius >= gears[i].pos.x - 1) and (balls[k].pos.x + balls[k].radius <= gears[i].pos.x + 1) and (balls[k].pos.y + balls[k].radius >= gears[i].pos.y - 1) and (balls[k].pos.y - balls[k].radius <= gears[i].pos.y + 1)):
                    
                    if(score>=50):
                       score-=50 
                       
                    balls[k].visible = False
                    balls.splice(k,1)                 
                    break
                
                if (balls[k].pos.y - balls[k].radius >= 20):
                    balls[k].visible = False
                    balls.splice(k,1) 
                    break
                
                if (balls[k].pos.y + balls[k].radius <= -15):
                    balls[k].visible = False
                    balls.splice(k,1) 
                    break
                
                if(balls[k].pos.x + balls[k].radius>=gears[i].pos.x + 2):
                    score+=100
                    balls[k].visible = False
                    balls.splice(k,1) 
                    break
            
    for l in range(enemies.length):
                    
        #Collision with the enemies
        for k in range(balls.length):
                    
            radSep = balls[k].pos - enemies[l].pos #Radius separation
            touchSep = (balls[k].radius + enemies[l].radius) * radSep.norm() #Compare the radius with the normal vector of both the balls (ball and the enemy)
            
            if (radSep.mag < touchSep.mag): #Collision
                score-=500
                balls[k].visible = False
                balls.splice(k,1) 
                break
                    
               
def nextLevel():
    

    balls = []
        
    gears = []
    createGears(5)
    
    
def createEnemy():
    
    enemy = sphere(pos=vec(-10,3,-20),size=vec(2.3,2.3,2.3))
    enemy.color = color.red
    enemy.velocity = vector(0,0,5)
    
    enemies.push(enemy)
     
def click():
            
    ball = sphere(pos=vec(-20,pointer[0].axis.y,0),size=vec(1,1,1))
    ball.velocity = vector(5,pointer[0].axis.y,0)

    balls.push(ball)
              
def createPointer():
    
    pointer1 = arrow(pos=vec(-25,0,0),axis=vector(0,-5,0), shaftwidth=0.5, color=color.red)
    pointer.push(pointer1)
       
def createLine():
    
    line = arrow(pos=vec(gears[0].pos.x + 2,-15,0),axis=vector(0,30,0), shaftwidth=0.5, color=color.blue)
    
def createBox():
    
    enemyCreater = box(pos=vec(-10,3,-20), size=vec(2,2,2),texture=textures.stucco )

def createGears(n):
    
    y = -4
    
    for j in range(n/2):
        
        g = shapes.gear(n=20,radius=1) #library of gears --> n = teeth
        #radius default = 1
        
        gear_1 = extrusion(path=[vector(0,j * y,0),vector(0,j * y,0.1)], shape=g)#convert to 3d
        
        angleHalfTooth = 0.5*2*pi/20 #tooth/2
        
        gears.push(gear_1)    
    
    for j in range(n/2):
        
        g = shapes.gear(n=20)
        
        gear_1 = extrusion(path=[vector(0,-j * y,0),vector(0,-j * y,0.1)], shape=g)
        
        angleHalfTooth = 0.5*2*pi/20
        
        gears.push(gear_1)