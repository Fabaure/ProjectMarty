import time

def angry(marty):
    if(marty):
        marty.eyes("angry",500) # Eyes take ether a name of preprogramed expression and a time of execution or an angle of rotation and a time of execution
    else:
        print("Marty is sadely not connected") # Print an error when not connected
        return 0
    return 0

def wide_open(marty):
    if(marty):
        marty.eyes("wide",500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def excited(marty):
    if(marty):
        marty.eyes("excited",500)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def wiggle(marty):
    if(marty):
        marty.eyes("wiggle",1000)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def eyes_control(marty,angle,time_in_ms):
    if(marty):
        marty.eyes(angle,time_in_ms)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def color_control(marty,color,pattern,time_set):
    if(marty):
        marty.disco_pattern(int(pattern))
        marty.disco_color(color)
        time.sleep(int(time_set))
    else:
        print("Marty is sadely not connected")
        return 0
    return 0

def feel_control(marty,color,emotion):
    if(marty):
        marty.disco_color(color)
        marty.eyes(emotion,500)
        time.sleep(2)
        marty.disco_color(000000)
    else:
        print("Marty is sadely not connected")
        return 0
    return 0