# Llama offline game
# Writen by Jack Scrivener
# commented lasted updated on 10/08/2023
# requires the pygame external library

import pygame
import time

pygame.font.init()

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
SKY_YELLOW = (230, 179, 39)
SUN_ORANGE = (230, 147, 39)
SUN_RED = (230, 39, 39)
FLOOR_GREY = (64,64,64)
BLACK = (0,0,0)

#the time it takes for the sun to set after the game / read time
SUN_SET_PERIOD = 2

#The font for the messages 
font = pygame.font.Font("FreeSansBold.ttf", 30)


#______________ Non-Changable Varables & obbjects __________________________________________________________________
#pls leave alone

#sets the start states for the main loop
quit_game = True




#______________ Functions __________________________________________________________________
#This function is called every tick to check for user input and then raise the apporpate flags
def user_input():
    #sets the intial varables to their default state so if no key is pressed then they will return these values
    local_llama_jump = False
    local_llama_duck = False

    local_input_exit = True

    local_y = True
    local_n = True

    for event in pygame.event.get():
        #exits the game if the exit/quit button is pressed
        if event.type == pygame.QUIT:
            local_input_exit = False

        if event.type == pygame.KEYDOWN:
            #raises the jump flag if the up key is pressed
            if event.key == pygame.K_UP:
                local_llama_jump = True

            #raises the jump flag if the space key is pressed
            if event.key == pygame.K_SPACE:
                local_llama_jump = True

            #raises the duck flag if the down key is pressed
            elif event.key == pygame.K_DOWN:
                local_llama_duck = True
            #lowers the y flag if the y key is pressed
            elif event.key == pygame.K_y:
                local_y = False
            #lowers the n flag if the n key is pressed
            elif event.key == pygame.K_n:
                local_n = False

    return(local_llama_jump,local_llama_duck,local_input_exit,local_y,local_n)



#This function is called every frame to update the obsticales being displayed
def  obsticals_update():
    global obsticale_list , obsticale_counter

    #addds obsticales to the list every time period set by the object spawn interval varable 
    if time.time() - round_start_time > OBSTICAL_SPAWN_INTERVAL*obsticale_counter:

        #x_pos , speed , time object spawned, image name , image width, image height
        obsticale_list.append([400,200,time.time(),"test_name.png",20,20])
        obsticale_counter += 1

    
    #removes obsticales from the list if they are off the screen
    if len(obsticale_list) > 0 and obsticale_list[0][0] < -OBSTICAL_WIDTH:
        obsticale_list.pop(0)

    for things in obsticale_list:
        #updates the obsticales x positon based on their speed
        things[0] = INITAL_SCREEN_WIDTH - (time.time() - round_start_time)*0.1* (things[1]*(time.time()-things[2]))

    
      



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

#THis function draws messages to the screen at a disired postion
def message(msg,text_colour, bkgd_colour, x_pos, Y_pos):
    #loads the font 
    txt = font.render(msg, True, text_colour, bkgd_colour)
    #creates a box to write the text to
    text_box = txt.get_rect(center = (x_pos,Y_pos ))
    #maps the text to the box
    screen.blit(txt, text_box)


#This function draws all the things dispalyed on the screen 
def draw(llama_y_pos,sun_colour,sky_colour,sun_y_pos,score):
    global obsticale_list

    #draws the backround
    screen.fill(sky_colour)

    #draws the sun circle
    pygame.draw.circle(screen,sun_colour,[INITAL_SCREEN_WIDTH/2,sun_y_pos],50)
    
    #draws the ground rectangle
    pygame.draw.rect(screen,FLOOR_GREY,[0,Y_POS_REF,400,INITAL_SCREEN_HEIGHT-Y_POS_REF])

    #draws the time/high score
    message("{:.0f}".format(score),FLOOR_GREY,sky_colour,20,20)

    #draws the llamma with its texture
    textrue(LLAMA_X_POS,llama_y_pos,LLAMA_WIDTH,LLAMA_HEIGHT,"Llama3.png")

    #draws the obsticals with their texture
    for things in obsticale_list:
        textrue(things[0],Y_POS_REF-OBSTICAL_HEIGHT,OBSTICAL_WIDTH,OBSTICAL_HEIGHT,"cactus.png")

    
#Smoothly transitons between two colours given the origonal colour, the target colour, the time the transion started and the time the transiton should take/ its period
def colour_transiton(origonal_colour,target_colour,start_time,time_period):
    #convers the origonal colour and target colour tuples into lists as tuples are imutable however lists are not
    origonal_colour_list = list(origonal_colour)
    target_colour_list = list(target_colour)

    #checks to see if the red colour channel needs to decrease to reach the target colour
    if(origonal_colour_list[0] > target_colour_list[0]):
        #if it does then it decreases it by how much is needed over the set time to smoothly change colour
        origonal_colour_list[0] -= (origonal_colour_list[0]-target_colour_list[0])/time_period*(time.time() - start_time) 

    #checks to see if the green colour channel needs to decrease to reach the target colour
    if(origonal_colour_list[1] > target_colour_list[1]):
        #if it does then it decreases it by how much is needed over the set time to smoothly change colour
        origonal_colour_list[1] -= (origonal_colour_list[1]-target_colour_list[1])/time_period*(time.time() - start_time) 

    #checks to see if the blue colour channel needs to decrease to reach the target colour
    if(origonal_colour_list[2] > target_colour_list[2]):
        #if it does then it decreases it by how much is needed over the set time to smoothly change colour
        origonal_colour_list[2] -= (origonal_colour_list[2]-target_colour_list[2])/time_period*(time.time() - start_time) 


    #checks to see if the red colour channel needs to increase to reach the target colour
    if(origonal_colour_list[0] < target_colour_list[0]):
        #if it does then it increases it by how much is needed over the set time to smoothly change colour
        origonal_colour_list[0] += (target_colour_list[0] - origonal_colour_list[0])/time_period*(time.time() - start_time) 

    #checks to see if the green colour channel needs to increase to reach the target colour
    if(origonal_colour_list[1] < target_colour_list[1]):
        #if it does then it increases it by how much is needed over the set time to smoothly change colour
        origonal_colour_list[1] += (target_colour_list[1] - origonal_colour_list[1])/time_period*(time.time() - start_time) 

    #checks to see if the blue colour channel needs to increase to reach the target colour
    if(origonal_colour_list[2] < target_colour_list[2]):
        #if it does then it increases it by how much is needed over the set time to smoothly change colour
        origonal_colour_list[2] += (target_colour_list[2] - origonal_colour_list[2])/time_period*(time.time() - start_time)

    #converts the new edited list back into a tuple
    transitonal_colour = tuple(origonal_colour_list)

    #returns the tuple to be used
    return(transitonal_colour)





#______________ Main Loop __________________________________________________________________

#Creates the screen object with the aformentioned screen height and width and makes it resizable
screen = pygame.display.set_mode((INITAL_SCREEN_WIDTH,INITAL_SCREEN_HEIGHT), pygame.RESIZABLE)

while quit_game:
    #---------------Inital varables----------------------------------------
    quit_round = True

    #creates a list which will be used to store what objects are on screen
    obsticale_list = []

    #these are used for latching if statments in the llama draw function
    currently_jumping = False
    currently_ducking = False

    #these are used to keep track of time since a duck or jump started 
    time_duck_started = 0
    time_jump_started = 0

    #used to calculate the time intervals for object spawning
    obsticale_counter = 1

    #sets the y and n key flags to true by default
    y = True
    n = True



    #---------------Sun Rise Loop----------------------------------------------
    #takes the time of when the sun rise started to be used for animation 
    sun_rising_start_time = time.time()\
    #loops for however long the sun set period should be 
    while time.time() - sun_rising_start_time < SUN_SET_PERIOD:
        #draws the screen using the colour transiton function to change the colour of the sky and sun and the time since the start of the sun rise to calcualte smooth movemoent of the sun
        draw(Y_POS_REF - LLAMA_HEIGHT,colour_transiton(SUN_RED,SUN_ORANGE,sun_rising_start_time,SUN_SET_PERIOD),colour_transiton(SUN_ORANGE,SKY_YELLOW,sun_rising_start_time,SUN_SET_PERIOD),Y_POS_REF + 50 - 75*(time.time() - sun_rising_start_time),0)
        pygame.display.update()


    
    #---------------Game Loop----------------------------------------------
    #takes the time of when the round started to be used for score
    round_start_time = time.time()
    while quit_round:
        #checks for user inputs
        llama_jump,llama_duck,quit_game,y,n = user_input()
    
        #updates the obsticals
        obsticals_update()

        #usses the user inputs to smoothly move the llama through a jump or duck
        currently_jumping,time_jump_started,currently_ducking,time_duck_started,llama_y_pos = llama_update(currently_jumping,time_jump_started,currently_ducking,time_duck_started)
        
        #draws everything on the screen
        draw(llama_y_pos,SUN_ORANGE,SKY_YELLOW,Y_POS_REF - 100,time.time()-round_start_time)

        #kills the llama if the obstical is in contact with its image
        if(Y_POS_REF-llama_y_pos-LLAMA_HEIGHT < OBSTICAL_HEIGHT and len(obsticale_list) > 0 and obsticale_list[0][0] > 19 and obsticale_list[0][0] < 31):
            quit_round = False
    
        pygame.display.update()

    #---------------Sun set Loop----------------------------------------------
    #takes the time of when the sun set started to be used for animation 
    sun_setting_start_time = time.time()
    #loops for however long the sun set period should be 
    while time.time() - sun_setting_start_time < SUN_SET_PERIOD:
        #draws the screen using the colour transiton function to change the colour of the sky and sun and the time since the start of the sun set to calcualte smooth movemoent of the sun
        draw(llama_y_pos,colour_transiton(SUN_ORANGE,SUN_RED,sun_setting_start_time,SUN_SET_PERIOD),colour_transiton(SKY_YELLOW,SUN_ORANGE,sun_setting_start_time,SUN_SET_PERIOD),INITAL_SCREEN_HEIGHT/4 + 76*(time.time() - sun_setting_start_time),0)

        #draws the death message and gives the user their score
        message("ouch you got pricked",SKY_YELLOW,FLOOR_GREY,200,230)
        message("Your Score is : {:.0f}".format(time.time() - round_start_time-(time.time() -sun_setting_start_time)),SKY_YELLOW,FLOOR_GREY,200,270)
        pygame.display.update()

    #Draws over the prevous text to clear the screen 
    pygame.draw.rect(screen,FLOOR_GREY,[0,Y_POS_REF,400,INITAL_SCREEN_HEIGHT-Y_POS_REF])


    #---------------play again Loop----------------------------------------------
    #Draws text prompting the user to ender a y to play again or an n to exit then umpdeates the screen to displa the images
    message("Press y to play again",SKY_YELLOW,FLOOR_GREY,200,230)
    message("Press n to exit",SKY_YELLOW,FLOOR_GREY,200,270)
    pygame.display.update()
    
    #loops until a y or a n is inputed
    while y and n:
        llama_jump,llama_duck,quit_game,y,n = user_input()
        
    #exits the game if the y button is still true which means that the n button was pressed as to exit the prevous loop as one of the two keys must have been pressed
    if y:
        quit_game = False

    




    



