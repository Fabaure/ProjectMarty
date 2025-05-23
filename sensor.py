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
    elif(color > 38 and color < 57):
        print("Cyan")
    elif(color > 64 and color < 90):
        print("Red")
    elif(color > 90 and color < 110):
        print("Magenta")
    elif(color > 145 and color < 205):
        print("Yellow")

def getDistance(marty)-> bool:
    # gets the distance in front of Marty
    distance = marty.get_obstacle_sensor_reading("right") # reads the distance in millimetres
    print("Distance : " + str(distance))
    if(distance < 10):
        return True
    else:
        return False

def getBattery(marty):
    # gets the remaining battery life 
    battery = marty.get_battery_remaining()
    print("Battery : " + str(battery) + "%")