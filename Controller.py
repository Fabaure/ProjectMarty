import inputs
from martypy import Marty
from Movement import move_forward
from Movement import move_backward
from Movement import move_left
from Movement import move_right

pads = inputs.devices.gamepads

if len(pads) == 0:
    raise Exception("Couldn't find any Gamepads!")

adresse_ip = "192.168.0.100"
marty = Marty("wifi", adresse_ip)

while True:
    events = inputs.get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)
        if event.code == 'BTN_NORTH' and event.state == 1:
            move_forward()
        if event.code == 'BTN_SOUTH' and event.state == 1:
            move_backward()
        if event.code == 'BTN_WEST' and event.state == 1:
            move_left()
        if event.code == 'BTN_EAST' and event.state == 1:
            move_right()