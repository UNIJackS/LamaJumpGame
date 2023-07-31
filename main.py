# Llama offline game
# Writen by Jack Scrivener
# commented lasted updated on 31/07/2023
# requires pygame external library

from pickle import TRUE
import pygame
import time

#______________ Global Varables and Constants __________________________________________________________________


#Sets the inital screen height and width for the screen
INITAL_SCREEN_HEIGHT = 400
INITAL_SCREEN_WIDTH = 400

#sets the intial x and y positon of the llama the x is constant however the y will change
llama_y_pos = 40
LLAMA_X_POS = 20
#sets the time between object spawns in seconds
OBJECT_SPAWN_INTERVAL = 5

quit_game = True

llama_jump = False
llama_jump_compleate = True
llama_duck = False
llama_duck_compleate = True

llama_jump_period = 3
llama_jump_height = 20

llama_duck_period = 3
llama_duck_depth = 10

jump_start_time = 4
duck_start_time = 4


LIGHT_BACROUND = (118,30,138)
SNAKE_RED = (245,54,34)

object_list = []

time_since_start = time.time()

#______________ Objects and functions __________________________________________________________________


#defines the object class which is used to store info and update the objects which go across the screen
class objects:
    #this function is called when the object is created and defines the objects varous varables
    def __init__(self):
        #defines the inital varables for the object
        self.speed = 1
        self.x_pos = 0
        self.image_name = "test.png"
        self.image_width = 20
        self.image_height = 20



#This function is called every frame to update the obsticales being displayed
def  object_update():
    if time.time() - time_since_start > OBJECT_SPAWN_INTERVAL:
        object_list.append(objects)

    for items in object_list:
        #checks if an object is off the screen and if so delete it 
        if  object_list[items].x_pos < 0:
            object_list.remove[items]
        
        #moves an object to the left by the number of pixels defined by the speed varable
        object_list[items].x_pos += object_list[items].speed


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






#______________ Main Loop __________________________________________________________________
    
#Creates the screen object with the aformentioned screen height and width and makes it resizable
screen = pygame.display.set_mode((INITAL_SCREEN_WIDTH,INITAL_SCREEN_HEIGHT), pygame.RESIZABLE)


currently_jumping = False
time_jump_started = 0

currently_ducking = False
time_duck_started = 0

x = 0
llama_y_delta = 0
while quit_game:
    llama_jump,llama_duck,quit_game = user_input();

    if llama_jump == True and currently_jumping == False and currently_jumping == False:
        currently_jumping = True
        time_jump_started = time.time()

    if llama_duck == True and currently_ducking == False and currently_jumping == False:
        currently_ducking = True
        time_duck_started = time.time()

    if time.time() - time_jump_started > 4:
        currently_jumping = False
        llama_y_delta = 0

    if time.time() - time_duck_started > 4:
        currently_ducking = False

    if time.time() - time_jump_started < 4:
        #llama_y_delta = ((-20)*(time.time() - jump_start_time-1)*(time.time() - jump_start_time-llama_jump_period))
        x = time.time() - time_jump_started
        llama_y_delta = (20)*(x-1)*(x-3)
        llama_y_pos = llama_y_delta +20
    print("currently_jumping :{}".format(currently_jumping))
    print("currently_ducking :{}".format(currently_ducking))
    print("{},{}".format(x,llama_y_delta))
    print("llama_y_pos:{}".format(llama_y_pos))

    print("")
    #time.sleep(1)

    
    screen.fill(LIGHT_BACROUND)
    #llama_y_delta,llama_jump_compleate,llama_duck_compleate,jump_start_time,duck_start_time = llama_draw(llama_jump,llama_duck,llama_jump_compleate,llama_duck_compleate,jump_start_time,duck_start_time)
    pygame.draw.rect(screen,SNAKE_RED,[20,llama_y_pos,20,20])

    pygame.display.update()