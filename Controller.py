import inputs
from martypy import Marty
from Movement import move_forward
from Movement import move_backward
from Movement import move_left
from Movement import move_right


def handle_gamepad_event(marty, event):
    if event.ev_type == "Key" and event.state == 1:
        if event.code == 'BTN_NORTH':
            move_forward(marty, 2)
        if event.code == 'BTN_SOUTH':
            move_backward(marty, 2)
        if event.code == 'BTN_WEST':
            move_left(marty, 1)
        if event.code == 'BTN_EAST':
            move_right(marty, 1)