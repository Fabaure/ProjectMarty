def move_forward(marty):
    # function to make marty move forward
    marty.walk(2,'auto',0,25,1500) #walk take in argmument number_of_steps , starting feet, turn degre , distance in mm , time of execution

def move_left(marty):
    # function to make marty move left
    marty.sidestep("left",1,35,1000,) #Take the side of step , the number of steps , degree of steps , time to execute

def move_right(marty):
    # function to make marty move right
    marty.sidestep("right",1,35,1000,)

def move_backward(marty):
    # function to make marty move backwrds
    marty.walk(2,'auto',0,-25,1500) # Walk still work the same way , but negative distance make it walk backward 