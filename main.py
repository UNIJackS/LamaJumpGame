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
OBJECT_SPAWN_INTERVAL = 5

#how long a jump takes in seconds
llama_jump_period = 2
#how high a jump goes in pixels
llama_jump_height = 20

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
global object_list


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

#______________ Objects and functions __________________________________________________________________


#defines the object class which is used to store info and update the objects which go across the screen
class objects:
    #defines the inital varables for the object
    def __inti__(self):
        self.speed = 1
        self.x_pos = 400
        self.image_name = "test.png"
        self.image_width = 20
        self.image_height = 20

    def dict(self):
        speed_dict = self.speed
        x_pos = self.x_pos
        image_name = self.image_name
        image_width = self.image_width
        image_height = self.image_height
    
        

#This function is called every frame to update the obsticales being displayed
def  object_update(object_counter):
    global object_list, k
    if time.time() - time_since_start > OBJECT_SPAWN_INTERVAL*object_counter:
        print("if loop started")
        #object_list.append(objects)
        object_counter += 1
    
    #print("number of objects :{}".format(len(object_list)))
    
  
    return(object_counter)


def object_draw(object_list):
    for things in object_list:
        pygame.draw.rect(screen,SNAKE_RED,[things.x_pos,LLAMA_Y_POS_REF +20,20,20])
        
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
def llama_draw(currently_jumping,time_jump_started,currently_ducking,time_duck_started):
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

    return(currently_jumping,time_jump_started,currently_ducking,time_duck_started)






#______________ Main Loop __________________________________________________________________
    
#Creates the screen object with the aformentioned screen height and width and makes it resizable
screen = pygame.display.set_mode((INITAL_SCREEN_WIDTH,INITAL_SCREEN_HEIGHT), pygame.RESIZABLE)


object_list = [objects,objects]

k = 0


while quit_game:

   # if object_list[0].dict.x_pos < 0:
    #   print("item deleted")
     #  object_list.pop([0])


    #checks for user inputs
    llama_jump,llama_duck,quit_game = user_input()
    
    #object_counter = object_update(object_counter)

    
    screen.fill(LIGHT_BACROUND)

    #object_list = object_draw(object_list)
    #usses the user inputs to smoothly move the llama through a jump or duck
    #this function usses latching if statments and relative time hence the nesscity to pass so many varables
    currently_jumping,time_jump_started,currently_ducking,time_duck_started = llama_draw(currently_jumping,time_jump_started,currently_ducking,time_duck_started)
    

    pygame.draw.rect(screen,FOOD_BLUE,[0,LLAMA_Y_POS_REF+20,400,20])

    2

    pygame.display.update()