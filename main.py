import cv2 as cv
import os
import numpy as np

from events import MouseEvent
from widgets import Button

# Define window size
WIDTH, HEIGHT = 720, 480

# Some constants
COLORS = {
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
    "red": (0, 0, 255),
    "yellow": (0, 255, 255),
    "yellow90": (0, 180, 200),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "blue90":(200,0,0),
    "blue-click":(255,50,50),
}
LINE_THICKNESS = 2
CUT_LINE_COLOR = COLORS['red']

BUTTON_COLOR = COLORS['blue']
BUTTON_HOVER_COLOR = COLORS['blue90']
BUTTON_CLICK_COLOR = COLORS["blue-click"]
BUTTON_TEXT_COLOR = COLORS["white"]

key = 0
mouse_events_list = []
last_event = None


def mouse_event_callback(event, xpos, ypos, *args):
    global last_event
    new_event = MouseEvent(event, xpos, ypos)
    if event != last_event:
        mouse_events_list.append(new_event)
    else:
        for i in mouse_events_list:
            if i._id == event:
                i.x = xpos
                i.y = ypos
    last_event = event

cv.namedWindow("Canvas")
cv.setMouseCallback("Canvas", mouse_event_callback)

buttons = []

def demo_callback():
    print("""
    Hello this is testing the 
    callback function weather 
    it will throw an exception or not
    """)

# Create some buttons
for i,text in zip(range(1, 5), ["Save", "Clear", "Next", "Prev"]):
    button = Button(x=i + 1 * 50, y=i * 60,text=text,callback_function=demo_callback)
    buttons.append(button)

while True:
    blank_canvas = np.zeros([HEIGHT, WIDTH, 3], dtype=np.uint8)

    for button in buttons:
        cv.rectangle(blank_canvas, (button.x, button.y), (button.x + button.width, button.y + button.height),
                     BUTTON_COLOR, -1)
        if len(mouse_events_list) > 0:
            current_mouse_event = mouse_events_list[-1]
            if button.is_hover(current_mouse_event.x, current_mouse_event.y):
                # When button is clicked down
                if current_mouse_event._id == cv.EVENT_LBUTTONDOWN:
                    cv.rectangle(blank_canvas, (button.x, button.y),
                                 (button.x + button.width, button.y + button.height),
                                 BUTTON_CLICK_COLOR, -1)
                    if not button.is_down:
                        button.is_down = True
                        if callable(button.callback_function):
                            button.callback_function.__call__()

                # When button is clicked up
                if current_mouse_event._id == cv.EVENT_LBUTTONUP:
                    cv.rectangle(blank_canvas, (button.x, button.y),
                                 (button.x + button.width, button.y + button.height),
                                 BUTTON_COLOR, -1)
                    button.is_down = False

                # When button is hovered
                if current_mouse_event._id == cv.EVENT_MOUSEMOVE:
                    cv.rectangle(blank_canvas, (button.x, button.y),
                                 (button.x + button.width, button.y + button.height),
                                 BUTTON_HOVER_COLOR, -1)

    # Listen for MODES

    #Import Image Mode

    #Draw on Image Mode

    #Save Image Mode

    #Crop Image Mode

    #Rotate Image Mode

    #Blur Image Mode

    #UNDO MODE

    #REDO MODE

    #CUT Image

    #Exit MODE

    #Clear Mode

    key = cv.waitKey(1)
    if key == ord("d"):
        break

    cv.imshow("Canvas", blank_canvas)
