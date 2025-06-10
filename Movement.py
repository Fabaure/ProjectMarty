def move_forward(marty, steps):
    # function to make marty move forward
    marty.walk(steps, 'auto', 0, 25, 1500) #walk takes in the argmuments : number_of_steps , starting feet, turn degre , distance in mm , time of execution

def move_left(marty, steps):
    # function to make marty move left
    marty.sidestep("left", steps, 35, 1000) #sidestep takes in the arguments : the number of steps , degree of steps , time to execute

def move_right(marty, steps):
    # function to make marty move right
    marty.sidestep("right", steps, 35, 1000)

def move_backward(marty, steps):
    # function to make marty move backwrds
    marty.walk(steps, 'auto', 0, -25, 1500) # worksthe same way as walk but negative distance makes it walk backwards