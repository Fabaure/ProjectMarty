from martypy import Marty, MartyConnectException

def getColor(marty):
    # gets the color of the object that Marty is standing on
    color = marty.get_ground_sensor_reading("left") # reads the color
    print("Color : " + str(color))
    if(color < 19):
        print("Black")
    elif(color > 19 and color < 27):
        print("Blue")
    elif(color > 27 and color < 37):
        print("Green")
    elif(color > 45 and color < 57):
        print("Cyan")
    elif(color > 75 and color < 90):
        print("Red")
    elif(color > 90 and color < 110):
        print("Magenta")
    elif(color > 180 and color < 205):
        print("Yellow")

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