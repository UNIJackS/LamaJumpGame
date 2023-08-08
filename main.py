# Llama offline game
# Writen by Jack Scrivener
# commented lasted updated on 31/07/2023
# requires pygame external library

import pygame
import time

#______________ Global Varables and Constants __________________________________________________________________


#Sets the inital screen height and width for the screen
INITAL_SCREEN_HEIGHT = 400
INITAL_SCREEN_WIDTH = 400

#sets the intial x of the lama and the refrance point for the y
LLAMA_Y_POS_REF = 200
LLAMA_X_POS = 20

#sets the time between object spawns in seconds
OBJECT_SPAWN_INTERVAL = 2

#how long a jump takes in seconds
llama_jump_period = 2
#how high a jump goes in pixels
llama_jump_height = 40

#how long a duck takes in seconds
llama_duck_period = 2
#how low a duck goes in pixels
llama_duck_depth = 10

#colours for varous objects in rgb values 
LIGHT_BACROUND = (118,30,138)
SNAKE_RED = (245,54,34)
FOOD_BLUE = (127,202,255)


#______________ Non-Changable Varables & obbjects __________________________________________________________________
#pls leave alone

#creates a list which will be used to store what objects are on screen
object_list = []


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
object_counter = 1

#______________ Dictonarys and functions __________________________________________________________________


object_list = []



#This function is called every frame to update the obsticales being displayed
def  object_update():
    global object_list , object_counter

    #print("time.time() - time_since_start {}".format(time.time() - time_since_start))
    #print("OBJECT_SPAWN_INTERVAL*object_counter{}".format(OBJECT_SPAWN_INTERVAL*object_counter))

    if time.time() - time_since_start > OBJECT_SPAWN_INTERVAL*object_counter:
        print("if loop started")

        #x_pos , speed , image name , image width, image height
        object_list.append([400,1,"test_name.png",20,20])
        object_counter += 1
        print(object_list)
        print("number of objects counter: {}".format(object_counter))
        print("number of objects on object list: {}".format(len(object_list)))
    
    #removes objects from the list if they are off the screen
    if len(object_list) > 0 and object_list[0][0] < 0:
        object_list.pop(0)

    #updates the objects x positon based on their speed
    for things in object_list:
        things[0] -= things[1]




def object_draw():
    global object_list
    for things in object_list:
        pygame.draw.rect(screen,SNAKE_RED,[things[0],LLAMA_Y_POS_REF +40,20,20])
        
def user_input():
    llama_jump = False
    llama_duck = False
    
    input_exit = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            input_exit = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                llama_jump = True

            elif event.key == pygame.K_DOWN:
                llama_duck = True

    return(llama_jump,llama_duck,input_exit)


#This function takes two boolen values of weither the user wants to jump or duck. It then checks if they are already
#jumping and if they are not then initating a jump of height or duck of depth and lenth of time determined by the varables 
#at the top of the program 
def llama_draw():
    global currently_jumping,time_jump_started,currently_ducking,time_duck_started
    #sets the lammas positon as the refrance positon
    llama_y_pos = LLAMA_Y_POS_REF

    #checks if the user wants to jump and if they are not already jumping or ducking
    if llama_jump == True and currently_ducking == False and currently_jumping == False:
        #If the user wants to jump and is not currently jumping or ducking then it starts a jump
        currently_jumping = True
        time_jump_started = time.time()

    #checks if the user wants to duck and if they are not already jumping or ducking
    if llama_duck == True and currently_ducking == False and currently_jumping == False:
        #If the user wants to duck and is not currently jumping or ducking then it starts a jump
        currently_ducking = True
        time_duck_started = time.time()

    #checks if the jump has gone on longer than the jump period defined at the top of the program
    if time.time() - time_jump_started > llama_jump_period:
        #stops the jump
        currently_jumping = False
        #sets the y positon to the refrance due to floating points being messey
        llama_y_pos = LLAMA_Y_POS_REF

    #checks if the duck has gone on longer than the duck period defined at the top of the program
    if time.time() - time_duck_started > llama_duck_period:
        #stops the duck
        currently_ducking = False
        #sets the y positon to the refrance due to floating points being messey
        llama_y_pos = LLAMA_Y_POS_REF

    #checks if the llama is currently jumping
    if  currently_jumping == True:
        #calculates where the lama should be based on the time using a parabola
        llama_y_delta = (llama_jump_height)*(time.time() - time_jump_started)*(time.time() - time_jump_started-llama_jump_period)
        #sets the y positon of the lama to the delta calculated plus the y refrance
        llama_y_pos = llama_y_delta +LLAMA_Y_POS_REF

    #checks if the llama is currently jumping
    if  currently_ducking == True:
        #calculates where the lama should be based on the time using a parabola
        llama_y_delta = -((llama_duck_depth)*(time.time() - time_duck_started)*(time.time() - time_duck_started-llama_jump_period))
        #sets the y positon of the lama to the delta calculated plus the y refrance
        llama_y_pos = llama_y_delta +LLAMA_Y_POS_REF

    pygame.draw.rect(screen,SNAKE_RED,[20,llama_y_pos,20,20])

    return()






#______________ Main Loop __________________________________________________________________
    
#Creates the screen object with the aformentioned screen height and width and makes it resizable
screen = pygame.display.set_mode((INITAL_SCREEN_WIDTH,INITAL_SCREEN_HEIGHT), pygame.RESIZABLE)

while quit_game:




    #checks for user inputs
    llama_jump,llama_duck,quit_game = user_input()
    
    object_update()

    
    screen.fill(LIGHT_BACROUND)

    pygame.draw.rect(screen,FOOD_BLUE,[0,LLAMA_Y_POS_REF+20,400,20])

    object_draw()
    #usses the user inputs to smoothly move the llama through a jump or duck

    #this function takes the user input and moves the lama 
    llama_draw()
    

    

    pygame.display.update()