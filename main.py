# Llama offline game
# Writen by Jack Scrivener
# commented lasted updated on 31/07/2023
# requires pygame external library

import pygame
import time

#______________ Changable Global Varables and Constants __________________________________________________________________

#-----llama varables------------------------------------------------
#Sets the inital screen height and width for the screen
INITAL_SCREEN_HEIGHT = 400
INITAL_SCREEN_WIDTH = 400

#sets the intial x of the lama and the refrance point for the y
Y_POS_REF = 200
LLAMA_X_POS = 20

#sets the llamas width and height 
LLAMA_WIDTH = 40
LLAMA_HEIGHT = 40

#how long a jump takes in seconds
LLAMA_JUMP_PERIOD = 1
#how high a jump goes in pixels
LLAMA_JUMP_HEIGHT = 100

#how long a duck takes in seconds
LLAMA_DUCK_PERIOD = 2
#how low a duck goes in pixels
LLAMA_DUCK_DEPTH = 10


#-----obstical varables----------------------------
#sets the time between obsticals spawns in seconds
OBSTICAL_SPAWN_INTERVAL = 2

#sets the width and height of obsticals
OBSTICAL_WIDTH = 20
OBSTICAL_HEIGHT = 20


#-----colours----------------------------
#colours for varous objects in rgb values 
BACROUND_YELLOW = (230, 179, 39)
SUN_ORANGE = (230, 147, 39)
FLOOR_GREY = (64,64,64)


#______________ Non-Changable Varables & obbjects __________________________________________________________________
#pls leave alone

#creates a list which will be used to store what objects are on screen
obsticale_list = []


#takes the time of when the program started to be used for score
time_since_start = time.time()

#these are used for latching if statments in the llama draw function
currently_jumping = False
currently_ducking = False

#these are used to keep track of time since a duck or jump started 
time_duck_started = 0
time_jump_started = 0

#sets the start state for the main loop
quit_game = True

#used to set the time intervals for object spawning
obsticale_counter = 1


#______________ Functions __________________________________________________________________
#This function is called every tick to check for user input and then raise the apporpate flags
def user_input():
    #sets the intial varables to their default state so if no key is pressed then they will return these values
    llama_jump = False
    llama_duck = False

    input_exit = True

    for event in pygame.event.get():
        #exits the game if the exit/quit button is pressed
        if event.type == pygame.QUIT:
            input_exit = False

        if event.type == pygame.KEYDOWN:
            #raises the jump flag if the up key is pressed
            if event.key == pygame.K_UP:
                llama_jump = True
            #raised the duck flag if the down key is pressed
            elif event.key == pygame.K_DOWN:
                llama_duck = True

    return(llama_jump,llama_duck,input_exit)



#This function is called every frame to update the obsticales being displayed
def  object_update():
    global obsticale_list , obsticale_counter

    #addds obsticales to the list every time period set by the object spawn interval varable 
    if time.time() - time_since_start > OBSTICAL_SPAWN_INTERVAL*obsticale_counter:

        #x_pos , speed , time object spawned, image name , image width, image height
        obsticale_list.append([400,200,time.time(),"test_name.png",20,20])
        obsticale_counter += 1
        print(obsticale_list)

    
    #removes obsticales from the list if they are off the screen
    if len(obsticale_list) > 0 and obsticale_list[0][0] < -OBSTICAL_WIDTH:
        obsticale_list.pop(0)

    for things in obsticale_list:
        #updates the obsticales x positon based on their speed
        things[0] = INITAL_SCREEN_WIDTH - (things[1]*(time.time()-things[2]))

    
      



#This function takes two boolen values of weither the user wants to jump or duck. It then checks if they are already
#jumping and if they are not then initating a jump of height or duck of depth and lenth of time determined by the varables 
#at the top of the program 
def llama_update(local_currently_jumping,local_time_jump_started,local_currently_ducking,local_time_duck_started):
    #sets the lammas positon as the refrance positon
    local_llama_y_pos = Y_POS_REF - LLAMA_HEIGHT

    #checks if the user wants to jump and if they are not already jumping or ducking
    if llama_jump == True and local_currently_ducking == False and local_currently_jumping == False:
        #If the user wants to jump and is not currently jumping or ducking then it starts a jump
        local_currently_jumping = True
        local_time_jump_started = time.time()

    #checks if the user wants to duck and if they are not already jumping or ducking
    if llama_duck == True and local_currently_ducking == False and local_currently_jumping == False:
        #If the user wants to duck and is not currently jumping or ducking then it starts a jump
        local_currently_ducking = True
        local_time_duck_started = time.time()

    #checks if the jump has gone on longer than the jump period defined at the top of the program
    if time.time() - local_time_jump_started > LLAMA_JUMP_PERIOD:
        #stops the jump
        local_currently_jumping = False
        #sets the y positon to the refrance due to floating points being messey
        local_llama_y_pos = Y_POS_REF - LLAMA_HEIGHT

    #checks if the duck has gone on longer than the duck period defined at the top of the program
    if time.time() - local_time_duck_started > LLAMA_DUCK_PERIOD:
        #stops the duck
        local_currently_ducking = False
        #sets the y positon to the refrance due to floating points being messey
        local_llama_y_pos = Y_POS_REF - LLAMA_HEIGHT

    #checks if the llama is currently jumping
    if  local_currently_jumping == True:
        #calculates where the lama should be based on the time using a parabola
        llama_y_delta = (LLAMA_JUMP_HEIGHT)*(time.time() - local_time_jump_started)*(time.time() - local_time_jump_started-LLAMA_JUMP_PERIOD)
        #sets the y positon of the lama to the delta calculated plus the y refrance
        local_llama_y_pos = llama_y_delta +Y_POS_REF - LLAMA_HEIGHT

    #checks if the llama is currently jumping
    if  local_currently_ducking == True:
        #calculates where the lama should be based on the time using a parabola
        llama_y_delta = -((LLAMA_DUCK_DEPTH)*(time.time() - local_time_duck_started)*(time.time() - local_time_duck_started-LLAMA_DUCK_PERIOD))
        #sets the y positon of the lama to the delta calculated plus the y refrance
        local_llama_y_pos = llama_y_delta +Y_POS_REF - LLAMA_HEIGHT

    

    return(local_currently_jumping,local_time_jump_started,local_currently_ducking,local_time_duck_started,local_llama_y_pos)

#This function Takes position, width, height and image name and draws an image
def textrue(x_pos,y_pos,local_image_width,local_image_height,local_image_name):
    #draws a rectange the at the images x and y pos the same width and height as it
    location = pygame.Rect(x_pos, y_pos, local_image_width, local_image_height)
    #loads the texture image
    texture = pygame.image.load(local_image_name).convert_alpha()
    #resizes the texture to the image width and height
    resized_texture = pygame.transform.smoothscale(texture, [local_image_width,local_image_height])
    #places the texture over the rectangle
    screen.blit(resized_texture, location)

#This function draws all the things dispalyed on the screen 
def draw(llama_y_pos):
    global obsticale_list

    #draws the backround
    screen.fill(BACROUND_YELLOW)

    #draws the ground rectangle
    pygame.draw.rect(screen,FLOOR_GREY,[0,Y_POS_REF,400,INITAL_SCREEN_HEIGHT-Y_POS_REF])

    #draws the sun circle
    pygame.draw.circle(screen,SUN_ORANGE,[200,100],50)

    #draws the llamma with its texture
    textrue(LLAMA_X_POS,llama_y_pos,LLAMA_WIDTH,LLAMA_HEIGHT,"Llama3.png")

    #draws the obsticals with their texture
    for things in obsticale_list:
        textrue(things[0],Y_POS_REF-OBSTICAL_HEIGHT,OBSTICAL_WIDTH,OBSTICAL_HEIGHT,"cactus.png")

    



#______________ Main Loop __________________________________________________________________
    
#Creates the screen object with the aformentioned screen height and width and makes it resizable
screen = pygame.display.set_mode((INITAL_SCREEN_WIDTH,INITAL_SCREEN_HEIGHT), pygame.RESIZABLE)

while quit_game:

    #checks for user inputs
    llama_jump,llama_duck,quit_game = user_input()
    
    #updates the 
    object_update()

    #usses the user inputs to smoothly move the llama through a jump or duck
    currently_jumping,time_jump_started,currently_ducking,time_duck_started,llama_y_pos = llama_update(currently_jumping,time_jump_started,currently_ducking,time_duck_started)
    #print(llama_y_pos)
    draw(llama_y_pos)

    #if(len(obsticale_list) > 0):
       #print()
    
    print(Y_POS_REF-llama_y_pos-LLAMA_HEIGHT > OBSTICAL_HEIGHT)
    if(Y_POS_REF-llama_y_pos-LLAMA_HEIGHT < OBSTICAL_HEIGHT and len(obsticale_list) > 0 and obsticale_list[0][0] > 19 and obsticale_list[0][0] < 31):
        quit_game = False
    
    pygame.display.update()