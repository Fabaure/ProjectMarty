from martypy import Marty, MartyConnectException

def getColor(marty):
    # gets the color of the object that Marty is standing on
    color = marty.get_ground_sensor_reading("left") # reads the color
    print("Color : " + str(color))
    if(color < 19):
        return "black"
    elif(color > 19 and color < 27):
        return "blue"
    elif(color > 27 and color < 37):
        return "green"
    elif(color > 38 and color < 57):
        return "cyan"
    elif(color > 64 and color < 90):
        return "red"
    elif(color > 90 and color < 110):
        return "magenta"
    elif(color > 145 and color < 205):
        return "yellow"
    return "no_color"

def getDistance(marty):
    # gets the distance in front of Marty
    distance = marty.get_obstacle_sensor_reading("right") # reads the distance in millimetres
    print("Distance : " + str(distance))
    if(distance != 0):
        print("Obstacle : Yes")
    else:
        print("Obstacle : No")

def getBattery(marty):
    # gets the remaining battery life 
    battery = marty.get_battery_remaining()
    return str(battery)

def getName(marty):
    name = marty.get_marty_name()
    return str(name)