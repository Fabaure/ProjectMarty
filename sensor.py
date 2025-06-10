from martypy import Marty, MartyConnectException

def getColor(marty):
    couleur = ""
    # gets the color of the object that Marty is standing on
    color = marty.get_ground_sensor_reading("left") # reads the color
    print("Color : " + str(color))
    if(color < 19):
        couleur = "black"
        return couleur
    elif(color > 19 and color < 24):
        couleur = "blue"
        return couleur
    elif(color > 25 and color < 37):
        couleur = "green"
        return couleur
    elif(color > 38 and color < 59):
        couleur = "cyan"
        return couleur
    elif(color > 60 and color < 80):
        couleur = "red"
        return couleur
    elif(color > 80 and color < 129):
        couleur = "magenta"
        return couleur
    elif(color > 130 and color < 205):
        couleur = "yellow"
        return couleur
    return "gray"




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