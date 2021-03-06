import os,highscore

########## TO DO ##########
#import other relevant modules(~ 1 line)

########################

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (250,100)

########## TO DO ##########
#Initialize pygame(~ 1 line)

########################

pygame.mixer.init() # initializing mixer separately - necessary for playing sounds

soundpt=pygame.mixer.Sound("assets/sounds/point.wav")
soundlose=pygame.mixer.Sound("assets/sounds/gameover.wav")
soundflap=pygame.mixer.Sound("assets/sounds/swoosh.wav")

########## TO DO ##########
#Initialize colors black and white(~ 2 lines)

########################

grey=(150,150,150)
green=(0,255,100)
blue=(0,0,255)
cyan=(0,255,255)

########## TO DO ##########
#Create game window(1000x700), set a title and fill screen with white color(~ 3 lines)
#Hint : use set_caption() to set a title for the window

########################

#Initializing bird movement settings
bird_vel=0
grav=1
gravsub=1

#Initializing pipe settings
pipe_width=70
pipe_vel=3

#Initializing game loop control settings
app_exit=False
setup=1

########## TO DO ##########
#Initialize clock(~ 1 lines)

########################

def menu(cyan):

    ########## TO DO ##########
    #Load the background image for the menu - "assets/images/Menubackground.png" and fit it to the screen(~ 2 lines)
    #hint: use transform to scale image to the window size

    ########################
    
    display.fill(white)
    display.blit(imag,(0,0))

    ########## TO DO ##########
    #Create a font object of style "Comic Sans" and size 40(~ 1 line)
    #hint: use SysFont()
    #Next creat a label (intuitively named label) using the created font object to render the word "MENU" in cyan

    ########################
    
    label2=fonts.render("CHERRY BLOSSOMS",True,cyan)
    label3=fonts.render("GREENERY",True,cyan)
    label4=fonts.render("INSTRUCTIONS",True,cyan)

    pygame.draw.rect(display,(255,0,0),(350,70,300,60))
    pygame.draw.rect(display,(255,0,0),(350,220,300,60))
    pygame.draw.rect(display,(255,0,0),(350,370,300,60))
    pygame.draw.rect(display,(255,0,0),(350,520,300,60))

    display.blit(label,[500-label.get_width()/ 2,85])
    display.blit(label2,[500-label2.get_width()/ 2,235])
    display.blit(label3,[500-label3.get_width()/ 2,385])
    display.blit(label4,[500-label4.get_width()/ 2,535])
    
    pygame.display.update()

    cond=True

    while cond:

        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos

                if pos[0] in range(335,686) and pos[1] in range(210,291):
                    return 2

                elif pos[0] in range(335,686) and pos[1] in range(360,441):
                    return 1

                elif pos[0] in range(335,686) and pos[1] in range(510,591):
                    instructions(cyan)

            if event.type==pygame.QUIT:
                return 0

def instructions(cyan):

    imag=pygame.image.load("assets/images/Menubackground.png")
    imag=pygame.transform.scale(imag,(1000,700))
    display.fill(white)
    display.blit(imag,(0,0))

    font=pygame.font.SysFont("Copperplate Gothic Bold",50)
    text("Welcome to Flappy bird",50,font)
    text("The objective is to fly through the gaps between the pipes",100,font)
    text("Controls:",170,font)
    text("Click the mouse to fly",220,font)
    text("Press SPACE to pause and unpause",270,font)
    text("There are two backgrounds to choose from",320,font)
    text("So sit back and enjoy",370,font)

    back=pygame.image.load("assets/images/back.png")
    back=pygame.transform.scale(back,(100,50))
    display.blit(back,(0,0))

    pygame.display.update()

    while True:

        for event in pygame.event.get():

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos

                if pos[0] in range(105) and pos[1] in range(55):

                    fonts=pygame.font.SysFont("Comic Sans",40)

                    display.fill(white)
                    display.blit(imag,(0,0))

                    label=fonts.render("MENU",True,cyan)
                    label2=fonts.render("CHERRY BLOSSOMS",True,cyan)
                    label3=fonts.render("GREENERY",True,cyan)
                    label4=fonts.render("INSTRUCTIONS",True,cyan)
                    
                    pygame.draw.rect(display,(255,0,0),(350,70,300,60))
                    pygame.draw.rect(display,(255,0,0),(350,220,300,60))
                    pygame.draw.rect(display,(255,0,0),(350,370,300,60))
                    pygame.draw.rect(display,(255,0,0),(350,520,300,60))

                    display.blit(label,[500-label.get_width()/ 2,85])
                    display.blit(label2,[500-label2.get_width()/ 2,235])
                    display.blit(label3,[500-label3.get_width()/ 2,385])
                    display.blit(label4,[500-label4.get_width()/ 2,535])
                    
                    pygame.display.update()

                    return

def endgame(points):
    highscore.highscore(points)
            
    soundpt.stop()
    soundlose.play()

    pygame.time.wait(500)
    
    imag=pygame.image.load("assets/images/Menubackground.png")
    imag=pygame.transform.scale(imag,(1000,700))
    display.fill(white)
    display.blit(imag,(0,0))

    pygame.draw.rect(display,(255,0,0),(280,140,440,80))

    rendering="Score: "+str(points)
    fonts1=pygame.font.SysFont("Copperplate Gothic Bold",90)
    label6=fonts1.render(rendering,True,cyan)
    display.blit(label6,(500-label6.get_width()/2,150))

    rendering="High Score: "+str(highscore.read())
    fonts2=pygame.font.SysFont("Copperplate Gothic Bold",90)
    pygame.draw.rect(display,(255,0,0),(280,290,440,80))
    label7=fonts2.render(rendering,True,cyan)
    display.blit(label7,(500-label7.get_width()/2,300))

    pygame.draw.rect(display,(255,0,0),(50,450,250,70))
    pygame.draw.rect(display,(255,0,0),(380,450,250,70))
    pygame.draw.rect(display,(255,0,0),(710,450,250,70))
    
    rendering="Menu"
    fonts1=pygame.font.SysFont("Copperplate Gothic Bold",70)
    label6=fonts1.render(rendering,True,cyan)
    display.blit(label6,(175-label6.get_width()/2,460))

    rendering="Retry"
    fonts1=pygame.font.SysFont("Copperplate Gothic Bold",70)
    label6=fonts1.render(rendering,True,cyan)
    display.blit(label6,(505-label6.get_width()/2,460))

    rendering="Quit"
    fonts1=pygame.font.SysFont("Copperplate Gothic Bold",70)
    label6=fonts1.render(rendering,True,cyan)
    display.blit(label6,(825-label6.get_width()/2,460))

    
    pygame.display.update()
    
    condit=True
    app_exit = False
    setup = 0
    
    while condit==True:
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
                app_exit=True
                condit=False

           elif event.type==pygame.MOUSEBUTTONDOWN:
                pos=event.pos

                if pos[0] in range(45,306) and pos[1] in range(445,525):
                    setup=1
                    condit=False

                if pos[0] in range(375,636) and pos[1] in range(445,525):
                    setup=0
                    condit=False

                if pos[0] in range(705,966) and pos[1] in range(445,525):
                    app_exit=True
                    condit=False
                    
    return (app_exit,setup)
        
def text(msg,pos,fonts):
    
    lbl=fonts.render(msg,True,(255,0,0))
    display.blit(lbl,[500-lbl.get_width()/ 2,pos])
             

def pause():
    
    loopvar=True
    while loopvar:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN:
                loopvar=False 

def leap(pts):
    global bird_vel
    if pts<11:
        bird_vel=-5
    else:
        bird_vel=-6

def gravity():
    global grav,gravsub,bird_vel

    if gravsub==6:
        bird_vel+=grav
        gravsub=1
    else:
        gravsub+=1

def pipes():
    pipe_height=random.randint(100,420)
    return pipe_height

def generate_pipes(pipe_x,pipe_height,pipe_down,pipe_up,vel):
    
    if pipe_x[0]==1000:
        pipe_height[0]=pipes()
        pipe1=pygame.image.load("assets/images/Warp Pipe.png")
        pipe1=pygame.transform.scale(pipe1,(pipe_width,pipe_height[0]))
        p1in=pygame.transform.scale(pipe1,(pipe_width,700-(pipe_height[0]+gap)))
        p1in=pygame.transform.rotate(p1in,180)
        pipe_down[0]  = pipe1
        pipe_up[0] = p1in
        
    elif pipe_x[0]==667:
        pipe_height[1]=pipes()
        pipe2=pygame.image.load("assets/images/Warp Pipe.png")
        pipe2=pygame.transform.scale(pipe2,(pipe_width,pipe_height[1]))
        p2in=pygame.transform.scale(pipe2,(pipe_width,700-(pipe_height[1]+gap)))
        p2in=pygame.transform.rotate(p2in,180)
        pipe_down[1]  = pipe2
        pipe_up[1] = p2in
        vel[0]=1
              
    elif pipe_x[0]==334:
        pipe_height[2]=pipes()
        pipe3=pygame.image.load("assets/images/Warp Pipe.png")
        pipe3=pygame.transform.scale(pipe3,(pipe_width,pipe_height[2]))
        p3in=pygame.transform.scale(pipe3,(pipe_width,700-(pipe_height[2]+gap)))
        p3in=pygame.transform.rotate(p3in,180)
        pipe_down[2]  = pipe3
        pipe_up[2] = p3in
        vel[1]=1
     
    elif pipe_x[0]==1:
        pipe_height[3]=pipes()
        pipe4=pygame.image.load("assets/images/Warp Pipe.png")
        pipe4=pygame.transform.scale(pipe4,(pipe_width,pipe_height[3]))
        p4in=pygame.transform.scale(pipe4,(pipe_width,700-(pipe_height[3]+gap)))
        p4in=pygame.transform.rotate(p4in,180)
        pipe_down[3]  = pipe4
        pipe_up[3] = p4in
        vel[2]=1

    return (pipe_height,pipe_up,pipe_down,vel)

def move_pipes(pipe_x,pipe_vel_lock,pipe_vel):

    vel2,vel3,vel4 = tuple(pipe_vel_lock)
    pipe_x[0]-=pipe_vel
    
    if vel2==1:
        pipe_x[1]-=pipe_vel
    if vel3==1:
        pipe_x[2]-=pipe_vel
    if vel4==1:
        pipe_x[3]-=pipe_vel

    if pipe_x[0]<=-335:
      pipe_x[0]=1000
    elif pipe_x[1]<=-335:
      pipe_x[1]=1000
    elif pipe_x[2]<=-335:
      pipe_x[2]=1000
    elif pipe_x[3]<=-335:
      pipe_x[3]=1000

    return pipe_x

def draw(x,h,pipe_down,pipe_up,background):
    p1,p2,p3,p4 = tuple(pipe_down)
    p1in,p2in,p3in,p4in = tuple(pipe_up)
    if p1!=None:
        display.blit(p1,(x[0],700-h[0]))
        display.blit(p1in,(x[0],0))        
        display.blit(background,(x[0]+69,0),(x[0]+69,0,3,700))
    if p2!=None:
        display.blit(p2,(x[1],700-h[1]))
        display.blit(p2in,(x[1],0))
        display.blit(background,(x[1]+69,0),(x[1]+69,0,3,700))
    if p3!=None:
        display.blit(p3,(x[2],700-h[2]))
        display.blit(p3in,(x[2],0))
        display.blit(background,(x[2]+69,0),(x[2]+69,0,3,700))
    if p4!=None:
        display.blit(p4,(x[3],700-h[3]))
        display.blit(p4in,(x[3],0))
        display.blit(background,(x[3]+69,0),(x[3]+69,0,3,700))

def collision(y,x,h):
    for i in range(len(x)):
        if x[i]==346:
            if y <700-25-gap-h[i] or y>660+25-h[i]:# 
                return True
        if x[i] in range(234,346):
            if y in range(684-gap-h[i],694-gap-h[i]) or y in range(666-h[i],674-h[i]):
                return True
            
    if y>700:#651
        return True
                
    return False

def score(pts):
    
    rendering="Score: "+str(pts)
    pygame.draw.rect(display,(255,0,0),(10,10,120,40))
    fonts1=pygame.font.SysFont("Copperplate Gothic Bold",35)
    label5=fonts1.render(rendering,True,cyan)
    display.blit(label5,(15,5+label5.get_height()/ 2))
    
def bird(bird_y,background):

    if  bird_y<651 and bird_y>-1:
        display.blit(background.subsurface(300,bird_y,50,50),(300,bird_y))
    elif bird_y>650:
        display.blit(background.subsurface(300,bird_y,50,700-bird_y),(300,bird_y))
    elif bird_y<0:
        display.blit(background.subsurface(300,0,50,bird_y+50),(300,bird_y))
    
while not app_exit:#loop to control entry and exit from application

    ########## TO DO ##########
    #Initialize internal game loop control variable - game_exit(~ 1 line)

    ########################

    soundlose.stop()
    
    if setup==1:
        back=menu(cyan)

    ########## TO DO ##########
    #Initialize constants for bird(~ 2 lines)
    #Values - 0 , 300 (b_v, b_y)

    ########################

    #variables to control gravity
    grav=1
    gravsub=1
    
    ########## TO DO ##########
    #Initialize constants for pipes(~ 3 lines)
    #Values - 70 , 3, 220 (p_w, p_v,g)

    ########################

    display.fill(white)

    if back==1:
        background=pygame.image.load("assets/images/Birdbackground.png")
        display.blit(background,(0,0))

    elif back==2:
        background=pygame.image.load("assets/images/CherryBlossom.png")
        background=pygame.transform.scale(background,(1000,700))
        display.blit(background,(0,0))

    elif back==0:
        break

    img=pygame.image.load("assets/images/bird2.gif")
    img=pygame.transform.scale(img,(50,50))
    img=img.subsurface(0,3,50,44)
    img=pygame.transform.scale(img,(50,50))

    pipe_x=[1000,1000,1000,1000]
    pipe_height=[0,0,0,0]
    pipe_vel_lock=[0,0,0]

    detervar=0

    pipe_down = [None,None,None,None]
    pipe_up = [None,None,None,None]

    points=0

    pygame.time.wait(500)

    while  not game_exit:

        # Variable to control flying(0 - disabled 1 - enabled) 
        jump=0 # Q - Why is it set to zero at every iteration?

        ########## TO DO ##########
        #Handle user events(~ 8-9 lines)
        #Tasks :
        #1.Enable jump on mouse click(hint: MOUSEBUTTONDOWN)
        #2.Handle game exit caused by clicking on the cross at the top right(hint: event type -> QUIT)
        #3.Pause game functionality when space bar is pressed. (hint: event -> KEYDOWN ; event key -> K_SPACE)
        #   there is pause() method proved
        # Bonus : Can u think of any kind of cheat to add here?
        

        ########################
        
        #Checking for jump     
        if jump==1 and bird_y >= 0:
            soundflap.play()
            leap(points)# This facilitates flapping 

        if app_exit==True:
            break

        #Gravity
        gravity()

        ########## TO DO ##########
        # Handle the scenario when bird tries to fly out and above window(~ 2 lines)
        #Hint: something to do with coordinate(b_y) and velocity(b_v)
        
       
        ########################        

 
        ########## TO DO ##########
        # Generates pipes(~ 1 line)
        #Hint: use method generate_pipes(pipe_x,pipe_height,pipe_down,pipe_up,pipe_vel_lock)
        
        pipe_height,pipe_up,pipe_down,pipe_vel_lock = #Complete
        ########################
        

        #draws bird and pipes
        bird(bird_y,background) 
        draw(pipe_x,pipe_height,pipe_down,pipe_up,background) # <--- Interesting have a look
        display.blit(img,(300,bird_y))

        bird_y+=bird_vel

        if bird_vel<0:# <--- Similarly interesting
            display.blit(background,(300,bird_y+50),(300,bird_y+50,50,int(math.fabs(bird_vel))))
        else:
            display.blit(background,(300,bird_y-bird_vel),(300,bird_y-bird_vel,50,int(math.fabs(bird_vel))))

        #Move pipes across screen
        pipe_x = move_pipes(pipe_x,pipe_vel_lock,pipe_vel)

        ########## TO DO ##########
        # Check if bird colides with pipe(~ 1 line)
        #Hint: use collision(b_y,p_x,p_h)
        #What should it return
        
        
       
        ########################  

        for i in pipe_x:
            ########## TO DO ##########
            #Check if point is earned (~ 3 lines)
            #Hint: increment point when bird passes pipe
            # 226

            ########################
            if i ==244:
                soundpt.play()
            
        score(points)

        ########## TO DO ##########
        #Check and handle endgame (~ 2 lines)
        #Hint: endgame and game_exit are linked
        #Hint: use endgame method --> endgame(points) : returns (app_exit,setup)

        ########################
        
            
        ########## TO DO ##########
        #Update display(~ 1 line)

        ########################

            
        ########## TO DO ##########
        #Enforce specified FPS(100 works fine for this)(~ 1 line)
        #hint: tick-tock

        ########################


pygame.quit()
quit()


