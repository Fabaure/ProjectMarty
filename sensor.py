from martypy import Marty, MartyConnectException

def getColornb(marty):
    # gets the color of the object that Marty is standing on
    color = marty.get_ground_sensor_reading("left") # reads the color
    print("Color : " + str(color))
    return color

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